import datetime
import time
import GeneralPurposeTools as GeneralPurposeTools
from selenium import webdriver
import random
import collections

s_splitString = '*1*!*2*1*!*3*2*1*!'

#Scraper may be used to retreive historical data series from YahooFinance.
def InfiniteScrollScraper(url, \
                            chromeOptions, \
                            promptedAtAccess = False, \
                            maxIterations = 4):
    browser = webdriver.Chrome(chrome_options=chromeOptions)
    browser.get(url)
    time.sleep(1)
    if promptedAtAccess:
        try:
            browser.find_element_by_name('agree').click()
        except:
            pass

    lenOfPageStep = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPageStep=document.body.scrollHeight;return lenOfPageStep;")
    time.sleep(1)

    lenOfPage = 0
    tmpSourceLength = 0
    iterator = 0
    while(True):
            time.sleep(0.25 + random.randint(1,20)/50)
            browser.execute_script("window.scrollBy(0, "+ str(lenOfPage + lenOfPageStep) +");")

            if tmpSourceLength >= len(browser.page_source):
                iterator += 1

            if iterator > maxIterations:
                break

            tmpSourceLength =len(browser.page_source)
            lenOfPage += lenOfPageStep
    return browser.page_source

def ConstructYahooURL(ticker, \
                      function, \
                      yahooFuncType, countryCode=None, \
                      startDate = datetime.datetime.strptime('1980-01-01', '%Y-%m-%d'), \
                      endDate = datetime.datetime.now(), \
                      interval = '1d', \
                      filterInput = 'history'):
    infoPage = 'https://finance.yahoo.com/' + function + '/' + ticker + '/' + yahooFuncType
    if yahooFuncType == 'history':
        infoPage = infoPage + '?period1=' + \
        str(int(startDate.timestamp())) + \
        '&period2=' + str(int(endDate.timestamp())) + \
        '&interval=' + interval + '&filter=' + filterInput + '&frequency=' + \
        interval
    else:
        infoPage = infoPage + '?p=' + ticker
    return infoPage

#All patterns that are not acceptable as inputs.
#Determines if input is NOT acceptable.
def ViaNegativa(queryString, \
                tabooPatterns=[r'\((\d)\)']):
    import re
    if queryString in ['', ' ']:
        return True
    if '(' == queryString[0] and ')' == queryString[-1]:
        return True

    return False

def KeyFinder(queryList):
    keySet = False
    for index, item in enumerate(queryList):
        if ViaNegativa(item) and not keySet:
            continue
        else:
            keySet = True
            return item, queryList[index+1:]

def FindPercentageValue(valueString):
    if '%' in valueString:
        try:
            val = valueString.split('%')[0]
            val = float(val)
            return val/100.0, 'Percentage'
        except:
            pass
    return None, None

def FindSplitValue(valueString):
    splits = ['/', ':']

    splitChar = [char for char in splits if char in valueString]

    if splitChar:
        try:
            val = valueString.split(splitChar[0])
            numerator = float(val[0])
            denominator = float(val[-1])
            return numerator / denominator, 'Split'
        except:
            pass
    return None, None

def FindFloatValue(valueString):
    try:
        val = float(valueString)
        return val, 'Floating Point Number'
    except:
        pass
    return None, None

def FindDateValue(valueString):
    if valueString in ['ttm', 'Current']:
        return valueString, 'Date'
    format = GeneralPurposeTools.DateFormatFromDateString(valueString)
    try:
        if format:
            date = GeneralPurposeTools.StandardDateFromAmericanFormat(valueString, format)
        else:
            date = GeneralPurposeTools.StandardDateFromAmericanFormat(valueString)
        return date, 'Date' 
    except:
        pass
    return None, None

def FindFinancialRowDoubleValue(valueString):
    try:
        if valueString == '-':
            return 0.0, 'Floating Point Number'

        if ',' in valueString:
            value = ''.join(valueString.split(','))
            return FindFloatValue(value)
    except:
        pass
    return None, None 

def FindAbsoluteNumberValue(valueString):
    try:
        lastDigit = valueString[-1]
        magnitudeDict = {'M':1e6, 'B':1e9, 'T':1e12}
        magnitude = magnitudeDict[lastDigit]
    except:
        return None, None
    if not magnitude is None:
        number, t_unused = FindFloatValue(valueString[0:-1])
        try:
            val = number*magnitude
            return val, 'AbsoluteNumber'
        except:
            pass
    return None, None

def FindNaN(valueString):
    if valueString == 'N/A':
        return None, 'NaN'
    return None, None


s_supportedBehaviorsFunctionsDict = collections.OrderedDict()
s_supportedBehaviorsFunctionsDict['DateValue'] =  FindDateValue
s_supportedBehaviorsFunctionsDict['AbsoluteNumber'] = FindAbsoluteNumberValue
s_supportedBehaviorsFunctionsDict['Floating Point Number'] =FindFloatValue
s_supportedBehaviorsFunctionsDict['Date'] = FindDateValue
s_supportedBehaviorsFunctionsDict['Split'] = FindSplitValue
s_supportedBehaviorsFunctionsDict['Percentage'] = FindPercentageValue
s_supportedBehaviorsFunctionsDict['IntegerNumber'] = FindFinancialRowDoubleValue
s_supportedBehaviorsFunctionsDict['NaN'] = FindNaN 

def ConcludeValueAndBehaviorFromKey(key, \
                                    relevantValuesList, \
                                    supportedBehaviorsFunctionsDict, \
                                    keyValueBehaviourDictionary=None ):
    behaviorToValueList = []
    lastBehavior = None
    if keyValueBehaviourDictionary:
        try:
            behaviour = keyValueBehaviourDictionary[key]
            for valueString in relevantValuesList:
                value, behaviorString = behaviour(valueString)
                if value and behaviorString:
                    behaviorToValueList.append((value, behaviorString)) 
        except Exception as e:
            print('Unable to retreive behaviour from dictionary \nError Message: ', e)
            print('Processing behavior matching algorithm')
    else:
        if not relevantValuesList:
                return []
        if behaviorToValueList:
                return behaviorToValueList
        for valueString in relevantValuesList:
            for key, behaviour in supportedBehaviorsFunctionsDict.items():
                value, behaviorString = behaviour(valueString)
                if behaviorString:
                    behaviorToValueList.append((value, behaviorString))
                    lastBehavior = behaviorString
                    break
    if lastBehavior:
        behaviorToValueList = [listItem for listItem in behaviorToValueList if listItem[1] == lastBehavior]
    return behaviorToValueList

def valueStingFromValuesList(valuesList):
    relevantValuesList = []
    for item in valuesList:
        if not ViaNegativa(item):
            relevantValuesList.append(item)

    if relevantValuesList:
        return relevantValuesList
    print('Error in valueStingFromValuesList(valuesList): No acceptable value found')
    return None

def PopulateKeyToValueAndBehaviorDictionary(parsedHtmlFile, behaviorIsincluded=False):
    resultsDictionary = {}
    for i in range(0,len(parsedHtmlFile)):
            indexValue = GeneralPurposeTools.RemoveHTMLTags(str(parsedHtmlFile[i]), s_splitString).split(s_splitString)
            key, valuesList = KeyFinder(indexValue)
            valueString = valueStingFromValuesList(valuesList)
            if valueString:
                valueToBehaviorList = ConcludeValueAndBehaviorFromKey(key, valueString, s_supportedBehaviorsFunctionsDict)
                if valueToBehaviorList:
                    if behaviorIsincluded:
                        #If detailed behavior report is necessary
                        resultsDictionary[key] = valueToBehaviorList
                    else:
                        resultsDictionary[key] = [valueItem[0] for valueItem in valueToBehaviorList]
    return resultsDictionary

def YahooStaticDataURLManufacturer(ticker, \
                                    yahooFunction):
    URL = 'https://finance.yahoo.com/quote/'+ ticker +'/'+ yahooFunction +'?p='+ ticker+ '&.tsrc=fin-srch'
    return URL

def MakeTimeSeriesDateAndClose(headersDataRow, gridDataRows):
    timeSeriesDateAndClose = []
    headers = GeneralPurposeTools.RemoveHTMLTags(str(headersDataRow), s_splitString)
    headers = headers.split(s_splitString)
    headers = GeneralPurposeTools.CleanHeaders(headers)
    for row in gridDataRows:
        tmpString = GeneralPurposeTools.RemoveHTMLTags(str(row), s_splitString)
        tmpStringToList = tmpString.split(s_splitString)
        tmpStringToList = GeneralPurposeTools.ListRemoveUnsupportedDataTypes(tmpStringToList, s_supportedBehaviorsFunctionsDict)
        res = {}
        for idx, rowItem in enumerate(tmpStringToList):
            res[headers[idx]] = rowItem
        timeSeriesDateAndClose.append(res)
    return timeSeriesDateAndClose
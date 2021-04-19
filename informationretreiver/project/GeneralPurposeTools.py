import re
import certifi
from bs4 import BeautifulSoup
import datetime
#-------------------------------------------------#


def RemoveHTMLTags(text, \
                   separator=''):
    """Remove html tags from a string"""
    clean = re.compile('<.*?>')
    return re.sub(clean, separator, text)

def StandardDateFromAmericanFormat(AmericanFormatedDate, \
                                   inputFormat = '%b %d, %Y', \
                                   outPutFormat = '%Y-%m-%d' ):
    return datetime.datetime.strptime(AmericanFormatedDate,inputFormat).strftime(outPutFormat)

def ListRemoveUnsupportedDataTypes(listInput, behaviourFuncs):
    list_ = []
    for listItem in listInput:
        for key_unused, func in behaviourFuncs.items():
            value, behaviorString = func(listItem)
            if behaviorString:
                list_.append(value)
                break
    return list_

#TODO: should be able to find date format from date as string.
def DateFormatFromDateString(dateString):
    format = None
    if dateString.count('/') == 2:
        format = '%m/%d/%Y'
    return format

def CleanHeaders(headers):
    headers_ = []
    for header in headers:
        header = header.replace('*', '')
        subwords = header.split(' ')
        if all(subword.isalpha() for subword in subwords):
            headers_.append(header)
    return headers_

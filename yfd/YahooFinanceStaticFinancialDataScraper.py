from bs4 import BeautifulSoup
import urllib3
import certifi
from yfd.GenericScraper import GenericScraper
import yfd.ScraperSpecificTools as sst

#TODO: Make it possible to dynamically retreive tag codes (div tag code -> 'D(tbr) fi-row Bgc($hoverBgColor):h' etc.)
#TODO: Quarterly data! (selenium?)
#TODO: Expanded data (Expanded lists in Financial statements) (selenium?)
generalYahooTableLineInformation = {'coreData' : ('div', 'D(tbr) fi-row Bgc($hoverBgColor):h'),
                'reportingDates' : ('div', 'D(tbhg)')
                }

s_tagByFunctionDict = {
                    'key-statistics' : {'coreData' : ('tr', True)},
                    'financials' : generalYahooTableLineInformation,
                    'balance-sheet' : generalYahooTableLineInformation,
                    'cash-flow' : generalYahooTableLineInformation
                }

class YahooFinanceStaticFinancialDataScraper(GenericScraper):
    def __init__(self, ticker, yahooFunction):
        #self.ticker = ticker
        self.yahooFunction = yahooFunction
        self.rowTuples = None
        self.pageData = None
        super().__init__(ticker)

    def URLManufacture(self):
        return sst.YahooStaticDataURLManufacturer(self.ticker, self.yahooFunction)

    def Retreive(self):
        URL = self.URLManufacture()
        page = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where()).request('GET',URL)
        soup = BeautifulSoup(page.data, 'html.parser')
        self.pageData = soup
    
    def Scrape(self):
        assert self.pageData, "No Data Retreived"
        rowTuples = []
        for key in s_tagByFunctionDict[self.yahooFunction].keys():
            rowTupleItem = self.pageData.find_all(s_tagByFunctionDict[self.yahooFunction][key][0], class_= s_tagByFunctionDict[self.yahooFunction][key][1])
            assert rowTupleItem, "Error In Scraper for Row Tuple"
            rowTuples.extend(rowTupleItem)
        self.rowTuples = rowTuples

    def ProcessData(self):
        self.result = sst.PopulateKeyToValueAndBehaviorDictionary(self.rowTuples, behaviorIsincluded=False)

    def Display(self):
        for key, value in self.result.items():
            print(key, value)
    
    def Save(self):
        pass
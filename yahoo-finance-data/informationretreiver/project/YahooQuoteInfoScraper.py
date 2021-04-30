from bs4 import BeautifulSoup
import urllib3
import certifi

from GenericScraper import GenericScraper
import ScraperSpecificTools as sst
import GeneralPurposeTools as gpt
"""
General: Extendible quote request, suitable for frequent use (quick).
return:dict with keys: [name, exchange, currency, price]
"""

class YahooQuoteInfoScraper(GenericScraper):
    def __init__(self, ticker, function):
        self.ticker = ticker
        self.yahooFunction = function
        self.data = None
        self.result = {}
        super().__init__()

    def URLManufacture(self):
        return sst.YahooStaticDataURLManufacturer(self.ticker, self.yahooFunction)

    def Retreive(self):
        URL = self.URLManufacture()
        page = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where()).request('GET',URL)
        soup = BeautifulSoup(page.data, 'html.parser')
        self.data = soup
    
    def ScrapeName(self):
        assert self.data
        name_struct = self.data.findAll('h1', attrs={'class': 'D(ib) Fz(18px)'})
        if name_struct:
            name = None 
            for item in name_struct:
                name = gpt.RemoveHTMLTags(str(item)).split('(')[0]
            assert name
            self.result['name'] = name

    def ScrapeExchangeInformation(self):
        assert self.data
        exc_curr_struct = self.data.findAll('div', attrs={'class': 'C($tertiaryColor) Fz(12px)'})
        if exc_curr_struct:
            for item in exc_curr_struct:
                codeString = gpt.RemoveHTMLTags(str(item))
                codeString = codeString.split(' ')

                market = codeString[0]
                currency = codeString[-1]

            assert market
            assert currency
            self.result['exchange'] = market
            self.result['currency'] = currency

    def ScrapePriceInformation(self):
        assert self.data
        price_struct = self.data.findAll('span', attrs={'class': 'Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)'})
        price = None
        if price_struct:
            price = gpt.RemoveHTMLTags(str(price_struct[0]))
            price = float(price)

            self.result['price'] = price

    def Scrape(self):
        self.ScrapeName()
        self.ScrapeExchangeInformation()
        self.ScrapePriceInformation()

    def ProcessData(self):
        pass
    
    def Display(self):
        for key,value in self.result.items():
            print(key, value)

    def Save(self):
        pass
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from GenericScraper import GenericScraper
import ScraperSpecificTools as sst

"""
CHROMEDRIVER is needed for this scraper.
Retreives price and dividend series. (slow)
uses selenium test- framework to interact with webpage.

return : split, div, price
"""

s_tagAndAttributeMatrix = [['tr', 'class', 'C($tertiaryColor) Fz(xs) Ta(end)'], \
                            ['tr', 'class', 'BdT Bdc($seperatorColor) Ta(end) Fz(s) Whs(nw)']]

class YahooFinanceTimeSeriesScraper(GenericScraper):
    def __init__(self, ticker, seriesType, startDate, endDate):
        self.ticker = ticker
        self.startDate = startDate
        self.endDate = endDate
        self.seriesType = seriesType
        self.soupItem = None
        self.timeSeries = None
        super().__init__()

    def URLManufacture(self):
        url = None
        if self.seriesType == "div":
            url = sst.ConstructYahooURL(self.ticker, 'quote', 'history', startDate=self.startDate, endDate=self.endDate, interval = 'div%7Csplit', filterInput = 'div')
        elif self.seriesType == "quote":
            url = sst.ConstructYahooURL(self.ticker, 'quote', 'history', startDate=self.startDate, endDate=self.endDate, interval = '1d')
        elif self.seriesType == "split":
            url =  sst.ConstructYahooURL(self.ticker, 'quote', 'history', startDate=self.startDate, endDate=self.endDate, interval = 'div%7Csplit', filterInput = 'split')
        return url

    def Retreive(self):
        URL = self.URLManufacture()
        chromeOptions = Options()
        chromeOptions.add_argument("--headless")
        soup = BeautifulSoup(sst.InfiniteScrollScraper(URL, chromeOptions, promptedAtAccess=True, maxIterations= 5), features="html.parser")
        self.soupItem = soup

    def Scrape(self):
        pass

    def Display(self):
        for dictionaryItem in self.timeSeries:
            print(dictionaryItem)

    def ProcessData(self):
        dataGridMatrix = []
        for row in s_tagAndAttributeMatrix:
            dataGridMatrix.append(self.soupItem.findAll(row[0], attrs={row[1]: row[2]}))
        headers = dataGridMatrix[0]
        data = dataGridMatrix[1]
        timeSeries = sst.MakeTimeSeriesDateAndClose(headers, data)
        self.timeSeries = timeSeries

    def Save(self):
        pass
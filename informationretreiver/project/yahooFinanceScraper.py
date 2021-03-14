import urllib3
import certifi
from bs4 import BeautifulSoup
import GeneralPurposeTools as GeneralPurposeTools
import ScraperSpecificTools as ScraperSpecificTools
from selenium.webdriver.chrome.options import Options

def YahooHistoricalTimeSeries(ticker, func, yahooFuncType, tagAndAttributeMatrix, \
                              startDate = None, endDate = None, interval = '1d', \
                             browserConditions = "--headless"):
    URL = ScraperSpecificTools.ConstructYahooURL(ticker, func, yahooFuncType, startDate=startDate, endDate=endDate, interval=interval)
    soup = None
    if yahooFuncType == 'history':
        chromeOptions = Options()
        chromeOptions.add_argument(browserConditions)
        soup = BeautifulSoup(ScraperSpecificTools.InfiniteScrollScraper(URL, chromeOptions, promptedAtAccess=True, maxIterations= 5), features="html.parser")
    else:
        soup = GeneralPurposeTools.GetPageHTML('GET', URL, 'html.parser')

    dataGridMatrix = []
    for row in tagAndAttributeMatrix:
        dataGridMatrix.append(soup.findAll(row[0], attrs={row[1]: row[2]}))

    timeSeries, divSeries = ScraperSpecificTools.MakeTimeSeriesDateAndClose(dataGridMatrix[0])
    return timeSeries, divSeries
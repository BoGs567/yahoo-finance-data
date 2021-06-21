from datetime import datetime
import logging
logging.basicConfig(level=logging.DEBUG)

from yfd import YahooQuoteInfoScraper
from yfd import YahooFinanceStaticFinancialDataScraper
from yfd import YahooFinanceTimeSeriesByQueryScraper

ticker = 'AAPL'
startDate = datetime.strptime('2020-01-01', '%Y-%m-%d')
endDate = datetime.strptime('2021-04-01', '%Y-%m-%d')

def LogResult(message, status):
    if status:
        logging.info(message + '-> OK')
    else:
        logging.warning(message + '-> FAILED')
    pass

'''
YahooFinanceTimeSeriesByQueryScraper - test
'''
yahooFunctions = ['quote', 'dividends', 'splits']
for yahooFunction_ in yahooFunctions:
    ysfds = YahooFinanceTimeSeriesByQueryScraper(ticker, yahooFunction_, startTime = startDate, endTime = endDate, frequency = '5d')
    ysfds.GetData()
    status = False
    if ysfds.GetResult():
        status = True
    message = 'YahooFinanceTimeSeriesByQueryScraper:'+yahooFunction_+':'+ticker
    LogResult(message, status)

'''
YahooFinanceStaticFinancialDataScraper - test
'''
yahooFunctions = ['cash-flow', 'balance-sheet', 'financials', 'key-statistics']
for yahooFunction_ in yahooFunctions:
    ysfds = YahooFinanceStaticFinancialDataScraper(ticker = ticker, yahooFunction = yahooFunction_)
    ysfds.GetData()
    status = 'fail'
    if ysfds.GetResult():
        status = 'ok'
    
    message = 'YahooFinanceStaticFinancialDataScraper:'+yahooFunction_+':'+ticker
    LogResult(message, status)

'''
YahooQuoteInfoScraper - test
'''
yqis = YahooQuoteInfoScraper(ticker, 'quote')
yqis.GetData()
status = False
if yqis.GetResult():
    status = True
message = 'YahooQuoteInfoScraper:'+'quote'+':'+ticker
LogResult(message, status)

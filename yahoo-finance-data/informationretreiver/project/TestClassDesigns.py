import datetime
from YahooQuoteInfoScraper import YahooQuoteInfoScraper
from YahooFinanceTimeSeriesScraper import YahooFinanceTimeSeriesScraper
from YahooFinanceStaticFinancialDataScraper import YahooFinanceStaticFinancialDataScraper
from YahooFinanceTimeSeriesByQueryScraper import YahooFinanceTimeSeriesByQueryScraper

#TODO: Make scraper for Options, Bonds.

ticker = 'AAPL'#'AZELIO.ST'#'AAPL'

startDate = datetime.datetime.strptime('2020-01-01', '%Y-%m-%d')
endDate = datetime.datetime.strptime('2021-04-01', '%Y-%m-%d')


yquoteTsScraper = YahooFinanceTimeSeriesByQueryScraper(ticker, 'quote', startTime = startDate, endTime = endDate, frequency = '1d')
yquoteTsScraper.Retreive()
yquoteTsScraper.ProcessData()
yquoteTsScraper.Display()

yquoteTsScraper = YahooFinanceTimeSeriesByQueryScraper(ticker, 'dividends', startTime = startDate, endTime = endDate, frequency = '1d')
yquoteTsScraper.Retreive()
yquoteTsScraper.ProcessData()
yquoteTsScraper.Display()

yquoteTsScraper = YahooFinanceTimeSeriesByQueryScraper(ticker, 'splits', startTime = startDate, endTime = endDate, frequency = '1d')
yquoteTsScraper.Retreive()
yquoteTsScraper.ProcessData()
yquoteTsScraper.Display()

yqis = YahooQuoteInfoScraper(ticker, 'quote')
yqis.Retreive()
yqis.Scrape()
yqis.ProcessData()
yqis.Display()
yqis.Save()
'''
ytss = YahooFinanceTimeSeriesScraper(ticker = ticker, seriesType = "split", startDate = startDate, endDate = endDate)
ytss.Retreive()
ytss.Scrape()
ytss.ProcessData()
ytss.Display()
ytss.Save()

ytss = YahooFinanceTimeSeriesScraper(ticker = ticker, seriesType = "div", startDate = startDate, endDate = endDate)
ytss.Retreive()
ytss.Scrape()
ytss.ProcessData()
ytss.Display()
ytss.Save()

ytss = YahooFinanceTimeSeriesScraper(ticker = ticker, seriesType = "quote", startDate = startDate, endDate = endDate)
ytss.Retreive()
ytss.Scrape()
ytss.ProcessData()
ytss.Display()
ytss.Save()
'''
ysfds = YahooFinanceStaticFinancialDataScraper(ticker = ticker, yahooFunction = 'cash-flow')
ysfds.Retreive()
ysfds.Scrape()
ysfds.ProcessData()
ysfds.Display()
ysfds.Save()

ysfds = YahooFinanceStaticFinancialDataScraper(ticker = ticker, yahooFunction = 'balance-sheet')
ysfds.Retreive()
ysfds.Scrape()
ysfds.ProcessData()
ysfds.Display()
ysfds.Save()

ysfds = YahooFinanceStaticFinancialDataScraper(ticker = ticker, yahooFunction = 'financials')
ysfds.Retreive()
ysfds.Scrape()
ysfds.ProcessData()
ysfds.Display()
ysfds.Save()

#TODO: Fix bug; foot-note number is erroneously included in result. 
ysfds = YahooFinanceStaticFinancialDataScraper(ticker = ticker, yahooFunction = 'key-statistics')
ysfds.Retreive()
ysfds.Scrape()
ysfds.ProcessData()
ysfds.Display()
ysfds.Save()

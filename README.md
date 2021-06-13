# yahoo-finance-data  (Alpha-version)
## _The omnipotent Yahoo-Finance data retreiver_
yahoo-finance-data (yfd) is a package for the retreival of data from Yahoo Finance. It makes use of both scraping and query calls. The yahoo-finance-data package is intended to be simple to use. Its usage is summarized in two steps.
- Create specialized data retreival objects
- Retreive data in a standardized dictionary format

## Features
The asset classes currently supported are: Stocks.
In the future support will be added for Options, Bonds and Crypto.

## Data Types
The following data may be retreived.
- Quote
- Historical (price, dividends, splits)
- Financials 
- Cash-Flow statement
- Balance-Sheet statement
- Key-Statistics

## Installation
```sh
pip install yahoo-finance-data 
```

## Usage
- Retreival of time series data (YahooFinanceTimeSeriesByQueryScraper).
-Availabe function types: ['quote', 'dividends', 'splits']
-Available frequency types: ['1d', '5d', '1mo', '3mo', '6mo', '1y', '2y', '5y', '10y', 'ytd', 'max']
```
from datetime import datetime
from yfd import YahooFinanceTimeSeriesByQueryScraper

ticker = 'AAPL'
startDate = datetime.strptime('2020-01-01', '%Y-%m-%d')
endDate = datetime.strptime('2021-04-01', '%Y-%m-%d')

ysfds = YahooFinanceTimeSeriesByQueryScraper(ticker, function = 'quote', startTime = startDate, endTime = endDate, frequency = '1d')
ysfds.GetData()
resultAsDictionary = ysfds.GetResult()
```
- Quote scraper (YahooQuoteInfoScraper)
-Scrapes quote information: Name, exchange and price.
```
from yfd import YahooQuoteInfoScraper

ticker = 'AAPL'

yqis = YahooQuoteInfoScraper(ticker, function='quote')
yqis.GetData()
resultAsDictionary = yqis.GetResult()
```
- Financials scraper (YahooFinanceStaticFinancialDataScraper)
-Scrapes financial data, the available data retreival types are: ['cash-flow', 'balance-sheet', 'financials', 'key-statistics']
```
from yfd import YahooFinanceStaticFinancialDataScraper

ticker = 'AAPL'

ysfds = YahooFinanceStaticFinancialDataScraper(ticker = ticker, yahooFunction = 'financials')
ysfds.GetData()
resultAsDictionary = ysfds.GetResult()
```

## Dependencies

yahoo-finance-data uses a number of 3rd party projects:
- [certifi] - Validating the trustworthiness of SSL certificates.
- [urllib3] - A powerful, user-friendly HTTP client for Python.
- [beautifulsoup4] - A library which makes it easy to scrape information from web pages.
- [datetime] - Standardize time management.

yahoo-finance-data is itself an open source project with a [public repository][yfd] on GitHub.


## License

MIT

**Free Software*

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)

   [yfd]: <https://github.com/BoGs567/Financial_Data_Base>
   [git-repo-url]: <https://github.com/joemccann/dillinger.git>
   [john gruber]: <http://daringfireball.net>
   [df1]: <http://daringfireball.net/projects/markdown/>
   [markdown-it]: <https://github.com/markdown-it/markdown-it>
   [Ace Editor]: <http://ace.ajax.org>
   [node.js]: <http://nodejs.org>
   [Twitter Bootstrap]: <http://twitter.github.com/bootstrap/>
   [jQuery]: <http://jquery.com>
   [@tjholowaychuk]: <http://twitter.com/tjholowaychuk>
   [express]: <http://expressjs.com>
   [AngularJS]: <http://angularjs.org>
   [Gulp]: <http://gulpjs.com>

   [PlDb]: <https://github.com/joemccann/dillinger/tree/master/plugins/dropbox/README.md>
   [PlGh]: <https://github.com/joemccann/dillinger/tree/master/plugins/github/README.md>
   [PlGd]: <https://github.com/joemccann/dillinger/tree/master/plugins/googledrive/README.md>
   [PlOd]: <https://github.com/joemccann/dillinger/tree/master/plugins/onedrive/README.md>
   [PlMe]: <https://github.com/joemccann/dillinger/tree/master/plugins/medium/README.md>
   [PlGa]: <https://github.com/RahulHP/dillinger/blob/master/plugins/googleanalytics/README.md>

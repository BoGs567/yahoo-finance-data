#https://query1.finance.yahoo.com/v8/finance/chart/AAPL?symbol=AAPL&period1=1587494216&period2=1619030216&interval=1d&includePrePost=true&events=div%7Csplit%7Cearn&lang=en-US&region=US&crumb=t5QZMhgytYZ&corsDomain=finance.yahoo.com

import requests
from GenericScraper import GenericScraper
import ScraperSpecificTools as sst
import GeneralPurposeTools as gpt

from YahooFinanceExceptions import YahooQuoteException #TODO: Make sure YahooQuoteException is implemented correctly!

"""
General: Extendible time period request, suitable for frequent use (quick).
Making use of Yahoo Query1.
return:dict with keys:
"""

class YahooFinanceTimeSeriesByQueryScraper(GenericScraper):
    def __init__(self, ticker, function, startTime, endTime, frequency):
        self.ticker = ticker
        self.function = function #Valid: 'quote', 'dividends', 'splits'
        self.startTime = str(int(startTime.timestamp()))
        self.endTime = str(int(endTime.timestamp()))
        self.frequency = frequency #valid: '1d', '5d', '1mo', '3mo', '6mo', '1y', '2y', '5y', '10y', 'ytd', 'max' (TODO: Make control!)
        self.data = None
        self.result = {}
        super().__init__()

    def URLManufacture(self):
        return (
            'https://query1.finance.yahoo.com/v8/finance/chart/{0}?symbol={0}'
            '&period1={1}&period2={2}&interval={3}&'
            'includePrePost=true&events=div%7Csplit%7Cearn&lang=en-US&'
            'region=US&crumb=t5QZMhgytYZ&corsDomain=finance.yahoo.com'
        ).format(self.ticker, self.startTime, self.endTime, self.frequency) 

    def Retreive(self):
        url = self.URLManufacture()
        response = requests.get(url).json()
        data = response['chart']['result']
        if data:
            self.data = response['chart']['result'][0]
        else:
            self.data = None
            raise YahooQuoteException((response['chart']['error']['description']))
            
    def Scrape(self):
        pass
    
    def ProcessEventTypeData(self, eventData, eventTypeKeys):
        functionTypeData = eventData.get(self.function)
        if functionTypeData:
            for key, item in functionTypeData.items():
                if item.get('date'):
                    if self.result.get('timestamp'):
                        self.result['timestamp'].append(item['date']*1000)
                    else:
                        self.result['timestamp']= [item['date']*1000]
                for key in eventTypeKeys:
                    if item.get(key):
                        if self.result.get(key):
                            self.result[key].append(item[key])
                        else:
                            self.result[key] = [(item[key])]

    def ProcessData(self):
        if self.function == 'quote':
            if self.data.get('timestamp'):
                self.result['timestamp'] = [x * 1000 for x in self.data.get('timestamp')]
            else:
                return
            indicatorDictionary = self.data.get('indicators')
            if indicatorDictionary:
                for key in ['close', 'open', 'low', 'high', 'volume']:
                    res = indicatorDictionary[self.function][0].get(key)
                    if res:
                        self.result[key] = res
                    else:
                        raise YahooQuoteException('key: \"{0}\" is not present in response!'.format(key))
        else:
            events = self.data.get('events')
            if events:
                if self.function == 'dividends':
                    self.ProcessEventTypeData(events, ['amount'])

                elif self.function == 'splits':
                    self.ProcessEventTypeData(events, ['numerator', 'denominator', 'splitRatio' ])
        return

    def Display(self):
        for key,value in self.result.items():
            print(key, value)
        
    def Save(self):
        pass
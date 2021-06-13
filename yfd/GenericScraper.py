'''
Generic scraper class.

'''
import logging

class GenericScraper(object):
    def __init__(self, ticker):
        self.ticker = ticker
        self.data = None
        self.result = {}

    def URLManufacture(self, argsStructure):
        raise NotImplementedError

    '''
    Retreives the data to be processed, 
    if needed this should save temporary files.
    '''
    def Retreive(self):
        raise NotImplementedError

    '''
    Performs the scraping of the input source.
    Both in and main- memory sources should be considered.
    '''
    def Scrape(self):
        raise NotImplementedError

    '''
    Processes some html- file in memory.
    '''
    def ProcessData(self):
        raise NotImplementedError

    '''
    Calls Retreive, Scrape and ProcessData.
    '''
    def GetData(self):
        self.Retreive()
        self.Scrape()
        self.ProcessData()

    def GetResult(self):
        if not self.result:
            logging.warning('No data was retreived for ticker: ' + self.ticker)
            logging.info('Please control that the tcker symbol is valid.')
        return self.result

    def Save(self):
        pass



        
'''
Generic scraper class.

'''

class GenericScraper(object):
    def __init__(self):
        self.data = None
        self.resultGenerator = None
        self.writer = None
        pass

    def URLManufacture(self, argsStructure):
        pass

    '''
    Retreives the data to be processed, 
    if needed this should save temporary files.
    '''
    def Retreive(self):
        pass

    '''
    Performs the scraping of the input source.
    Both in and main- memory sources should be considered.
    '''
    def Scrape(self):
        pass

    '''
    Processes some html- file in memory, connects the resultGenerator to the result.
    '''
    def ProcessData(self):
        pass

    '''
    Uses resultGenerator.
    Add logic for saving processed data.
    '''
    def Save(self):
        pass



        
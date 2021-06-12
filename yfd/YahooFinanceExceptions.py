class YahooQuoteException(Exception):
    def __init__(self, errorMessage):
        self.errorMessage = errorMessage

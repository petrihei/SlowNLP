import solrConnector

class Logic():

    def __init__(self, word):
        self.word = word
        self.results = solrConnector.get_results(self.word)

    def return_result_list(self):
        return self.results

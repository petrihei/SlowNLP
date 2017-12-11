import difflib
class LatinInspector:

    def __init__(self, word, results):
        self.word = word
        self.results = results
        self.percentage = 0.0

    def calculate_percentage(self):
        if len(self.results) != 0:
            for result in self.results:
                self.percentage = difflib.SequenceMatcher(None,self.word,result).ratio()
        return self.percentage

    def __str__(self):
        return str(self.percentage)
import difflib
class LatinInspector:

    def __init__(self, word, results):
        self.word = word
        self.results = results
        self.percentage = 0.0

    # Calculate the similarity ratio between the search word and the search result

    def calculate_percentage_word(self):
        if len(self.results) != 0:
            for result in self.results:
                result = result.lower()
                self.percentage = difflib.SequenceMatcher(None, self.word.lower(), result).ratio()
                return self.percentage
        else:
            self.percentage = 0.0
            return self.percentage

    def __str__(self):
        return str(self.percentage)
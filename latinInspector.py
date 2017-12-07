class LatinInspector:

    def __init__(self, word, results):
        self.word = word
        self.results = results
        self.percentage = 0.0

    def calculate_percentage(self):
        times = 0
        for result in self.results:
            if result == self.word:
                times += 1
        if len(self.results) != 0:
            self.percentage = times / len(self.results)
        return self.percentage

    def __str__(self):
        return str(self.percentage)
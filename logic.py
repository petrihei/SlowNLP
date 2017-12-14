from nltk import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import *

import solrConnector

class Logic():

    def __init__(self, user_input):
        self.user_input = user_input
        self.english_lemma = ""
        self.results = solrConnector.get_results(user_input)
        self.lemmatised_token_list = []

    def get_result_list(self):
        return self.results

    def get_lemmatised_token_list(self):
        stop = set(stopwords.words('english'))
        words = word_tokenize(self.user_input)
        word_list = [i for i in words.lower().split() if i not in stop]

        stemmer = SnowballStemmer("english")
        self.lemmatised_token_list = stemmer.stem(word_list)

        return self.lemmatised_token_list

    def get_word_tuples(self):
        english_words = self.get_lemmatised_token_list(self.user_input)
        word_tuples = []
        for word in english_words:
            word_tuples.append(word, solrConnector.get_results(word))
        return word_tuples

    def get_english_lemma(self):
        english_word = self.user_input
        stemmer = SnowballStemmer("english")
        self.english_lemma = stemmer.stem(english_word)

        return self.english_lemma




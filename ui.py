import logic
import latinInspector
import crawler
from nltk import word_tokenize
from nltk.corpus import stopwords

class Ui:

    def __init__(self):

        self.word = ""
        self.sentence = ""
        print('This highly sophisticated AI finds out whether an English word has Latin roots.')

    def get_user_input(self):
        print("0 - stop the application")
        print("1 - inspect the latin percentage of a single English word")
        print("2 - inspect the latin percentage of a text")
        print("3 - have a chat with latin AI\n")

        user_input = input("Command: ")

        if user_input == "0":
            print("Thank you for your visit. I'm sure this information was very useful to you!")
            exit()
        elif user_input == "1":
            self.word = input("English word: ")
            self.search_word(self.word)
        elif user_input == "2":
            self.sentence = input("English sentence: ")
            self.search_sentence(self.sentence)
        elif user_input == "3":
            self.chat()
        else:
            print("Wrong command. Try again.")
            self.get_user_input()

    def search_word(self, word):
        l = logic.Logic(word)
        latin_word = ''.join(l.get_result_list())
        lat = latinInspector.LatinInspector(word, l.get_result_list())
        percentage = lat.calculate_percentage_word()*100
        if percentage <= 50.0:
            print("This word probably doesn't have Latin roots.")
        else:
            print("The word \"" + word + "\" is " + str(percentage) + " percent latin.")
            print("The closest Latin match is \"" + latin_word + "\".\n")
            self.crawl(latin_word)
        self.get_user_input()

    def search_sentence(self, sentence):
        stop = set(stopwords.words('english'))
        words = word_tokenize(sentence)
        word_list = [i.lower() for i in words if i not in stop]
        total_percentage = 0.0
        index = 0
        for word in word_list:
            l = logic.Logic(word)
            lat = latinInspector.LatinInspector(word, l.get_result_list())
            percentage = lat.calculate_percentage_word() * 100
            total_percentage = total_percentage + percentage
            index += 1
        average_percentage = total_percentage / index
        print("\nEnglish sentence " + "'" + self.sentence + "' is " + str(average_percentage) +
              " percent latin\n")
        self.get_user_input()

    def crawl(self, latin_word):
        print("English definitions for word " + latin_word + " are:")
        for definition in crawler.get_english_definitions(latin_word):
            print(definition)

    def chat(self):
        print('\"finis\" quits the chat')
        user_input = input("Salve! Meum nomen est Latin AI. Ask me anything! ")
        while user_input != "finis":
            print("Nullo intellego! Ask something else")
            user_input = input("")
        self.get_user_input()

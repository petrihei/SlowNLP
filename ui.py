import logic
import latinInspector
import crawler

class Ui:

    def __init__(self):

        self.word = ""
        print('This highly sophisticated program finds out whether an English word has Latin roots.\nTo exit, type "stop".')

    def get_user_input(self):
        self.word = input("English word: ")
        self.search(self.word)

    def search(self, word):
        while word.lower() != "stop":
            l = logic.Logic(word)
            latin_word = ''.join(l.return_result_list())
            lat = latinInspector.LatinInspector(word, l.return_result_list())
            percentage = lat.calculate_percentage()*100
            if percentage <= 50.0:
                print("This word probably doesn't have Latin roots.")
            else:
                print("The word \"" + word + "\" is " + str(percentage) + " percent latin.")
                print("The closest Latin match is \"" + latin_word + "\".\n")
                self.crawl(latin_word)
            word = input("English word: ")
        print("Thank you for your visit. I'm sure this information was very useful to you!")

    def crawl(self, latin_word):
        print("English definitions for word " + latin_word + " are:")
        for definition in crawler.get_english_definitions(latin_word):
            print(definition)

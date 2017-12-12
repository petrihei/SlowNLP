import logic
import latinInspector

class Ui:

    def search(self):
        print('This highly sophisticated program finds out whether an English word has Latin roots.\nTo exit, type "stop".')
        search_word = input("English word: ")
        while search_word.lower() != "stop":
            l = logic.Logic(search_word)
            latin_word = ''.join(l.return_result_list())
            lat = latinInspector.LatinInspector(search_word, l.return_result_list())
            percentage = lat.calculate_percentage()*100
            if percentage <= 50.0:
                print("This word probably doesn't have Latin roots.")
            else:
                print("The word \"" + search_word + "\" is " + str(percentage) + " percent latin.")
                print("The closest Latin match is \"" + latin_word + "\".\n")
            search_word = input("English word: ")
        print("Thank you for your visit. I'm sure this information was very useful to you!")

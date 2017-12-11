import logic
import latinInspector

class Ui:

    def search(self):
        print('"stop" quits the application')
        search_word = ""
        while search_word != "stop":
            search_word = input("English word: ")
            l = logic.Logic(search_word)
            print(l.return_result_list())
            lat = latinInspector.LatinInspector(search_word, l.return_result_list())
            percentage = lat.calculate_percentage()*100
            print("The word " + search_word + " is " + str(percentage) + " percent latin.")

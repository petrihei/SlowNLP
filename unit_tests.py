import unittest
import latinInspector
import logic
import ui

class UiTestCases(unittest.TestCase):
    """Tests for `ui.py`."""

    def test_latin_word_is_100_percent_latin(self):
        """Does it print 100 % for latin words"""
        l = logic.Logic("pax")
        latin_word = ''.join(l.get_result_list())
        lat = latinInspector.LatinInspector("pax", l.get_result_list())
        percentage = lat.calculate_percentage_word() * 100
        self.assertEqual(percentage, 100.0)

    def test_latin_word_is_100_percent_latin2(self):
        """Does it return 100 % for words that are certain latin"""
        l = logic.Logic("imperium")
        latin_word = ''.join(l.get_result_list())
        lat = latinInspector.LatinInspector("imperium", l.get_result_list())
        percentage = lat.calculate_percentage_word() * 100
        self.assertEqual(percentage, 100.0)

    def test_nonlatin_word_is_0_percent_latin(self):
        """Does it return 100 % for words that are certain latin"""
        l = logic.Logic("tamasanaeiolelatinaa")
        latin_word = ''.join(l.get_result_list())
        lat = latinInspector.LatinInspector("imperium", l.get_result_list())
        percentage = lat.calculate_percentage_word() * 100
        self.assertEqual(percentage, 0.0)

    def test_half_latin_sentence_is_50_percent_latin(self):
        """Does it return 50 % for sentence that has one latin and one non-latin word"""
        u = ui.Ui()
        percentage = u.search_sentence("pax tamasanaeiolelatinaa")
        self.assertEqual(percentage, 50.0)

if __name__ == '__main__':
    unittest.main()



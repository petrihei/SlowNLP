from unittest import TestCase
from Hello import Hello


class TestHello(TestCase):
#    def test_huutelu(self):
#        self.fail()

    def test_something(self):
        s = "Hello World!"
        self.assertEqual(s, "Hello World!")



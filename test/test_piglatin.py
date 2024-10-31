import unittest
from piglatin import PigLatin
from error import PigLatinError


class TestPigLatin(unittest.TestCase):

    def test_set_an_input(self):
        translator = PigLatin("hello world")
        phrase = translator.get_phrase()
        self.assertEqual("hello world", phrase)
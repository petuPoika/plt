import unittest
from idlelib.pyparse import trans

from piglatin import PigLatin
from error import PigLatinError


class TestPigLatin(unittest.TestCase):

    def test_set_an_input(self):
        translator = PigLatin("hello world")
        phrase = translator.get_phrase()
        self.assertEqual("hello world", phrase)

    def test_translate_empty_string(self):
        translator = PigLatin("")
        translation = translator.translate()
        self.assertEqual("nil", translation)

    def test_translate_single_word_starts_vowel_ends_y(self):
        translator = PigLatin("any")
        translation = translator.translate()
        self.assertEqual("anynay", translation)
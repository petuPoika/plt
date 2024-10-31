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

    def test_translate_single_word_starts_and_ends_vowel(self):
        translator = PigLatin("apple")
        translation = translator.translate()
        self.assertEqual("appleyay", translation)

    def test_translate_single_word_starts_vowel__ends_consonant(self):
        translator = PigLatin("ask")
        translation = translator.translate()
        self.assertEqual("askay", translation)

    def test_translate_single_word_starts_with_single_consonant(self):
        translator = PigLatin("hello")
        translation = translator.translate()
        self.assertEqual("ellohay", translation)

    def test_translate_single_word_starts_with_more_consonant(self):
        translator = PigLatin("known")
        translation = translator.translate()
        self.assertEqual("ownknay", translation)

    def test_translate_phrase(self):
        translator = PigLatin("hello world")
        translation = translator.translate()
        self.assertEqual("ellohay orldway", translation)
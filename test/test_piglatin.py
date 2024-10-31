import unittest
from piglatin import PigLatin
from error import PigLatinError


class TestPigLatin(unittest.TestCase):

    def test_get_phrase(self):
        piglatin = PigLatin()
        error = PigLatinError()
        piglatin.get_phrase("hello world", "hello world")
        self.assertEqual("hello world", piglatin.get_phrase())

    def test_empty_string(self):
        piglatin = PigLatin()
        with self.assertRaises(PigLatinError) as context:
            piglatin.get_phrase("", "nil")
        self.assertEqual(str(context.exception), "nil")

    def test_translate_wordsStarting_withVowel(self):
        piglatin = PigLatin()
        piglatin.get_phrase("y", "yay")
        self.assertEqual("yay", piglatin.get_phrase("y"))
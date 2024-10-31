import unittest
from piglatin import PigLatin
from error import PigLatinError


class TestPigLatin(unittest.TestCase):

    def test_get_phrase(self):
        piglatin = PigLatin()
        error = PigLatinError()
        piglatin.get_phrase("hello world", "hello world")
        self.assertEqual("hello world", piglatin.get_phrase())

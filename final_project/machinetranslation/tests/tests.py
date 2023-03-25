import unittest
from translator import french_to_english, english_to_french

class TestTranslator(unittest.TestCase):
    def test_frenchToEnglish(self):
        # Check if it returns None when None is passed
        expected = 'Hello'
        self.assertNotEqual(french_to_english(None), expected)
        # Check if it translates French into English properly
        actual = french_to_english('Bonjour')
        self.assertEqual(actual, expected)

    def test_englishToFrench(self):
        # Check if it returns None when None is passed
        expected = 'Bonjour'
        self.assertNotEqual(english_to_french(None), expected)
        # Check if it translates French into English properly
        actual = english_to_french('Hello')
        self.assertEqual(actual, expected)

unittest.main()
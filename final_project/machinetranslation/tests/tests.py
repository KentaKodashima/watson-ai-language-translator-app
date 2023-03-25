import unittest
from translator import french_to_english, english_to_french

class TestTranslator(unittest.TestCase):
    async def test_frenchToEnglish(self):
        # Check if it returns None when None is passed
        self.assertEqual(await french_to_english(None), None)
        # Check if it translates French into English properly
        actual = await french_to_english('Bonjour')
        expected = 'Hello'
        self.assertEqual(actual, expected)

    async def test_englishToFrench(self):
        # Check if it returns None when None is passed
        self.assertEqual(await english_to_french(None), None)
        # Check if it translates French into English properly
        actual = await english_to_french('Hello')
        expected = 'Bonjour'
        self.assertEqual(actual, expected)

unittest.main()
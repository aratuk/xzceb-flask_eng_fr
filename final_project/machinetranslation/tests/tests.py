import unittest
from .translator import english_to_french, french_to_english

#English to French
class test_e2f_translator(unittest.TestCase):
    #Test that Hello = Bonjour
    def test_e2f_hi(self):
        self.assertEqual(english_to_french('Hello')['translations'][0]['translation'], 'Bonjour')
    #Test null
    def test_e2f_null(self):
        self.assertNotEqual(english_to_french(Null), '')
    
#French to English
class test_f2e_translator(unittest.TestCase):
    #Test that Bonjour = Hello
    def test_f2e_hi(self):
        self.assertEqual(french_to_english('Bonjour')['translations'][0]['translation'], 'Hello')
    #Test null
    def test_f2e_null(self):
        self.assertNotEqual(french_to_english(Null), '')


if __name__ == "__main__":
    unittest.main()    

import unittest
from translator import englishToFrench, frenchToEnglish

#English to French
class test_e2f_translator(unittest.TestCase):
    #Test that Hello = Bonjour
    def test_e2f_hi(self):
        self.assertEqual(englishToFrench('Hello')['translations'][0]['translation'], 'Bonjour')
    #Test null
    def test_e2f_null(self):
        self.assertNotEqual(englishToFrench('Null'), '')
    
#French to English
class test_f2e_translator(unittest.TestCase):
    #Test that Bonjour = Hello
    def test_f2e_hi(self):
        self.assertEqual(frenchToEnglish('Bonjour')['translations'][0]['translation'], 'Hello')
    #Test null
    def test_f2e_null(self):
        self.assertNotEqual(frenchToEnglish('Null'), '')


if __name__ == "__main__":
    unittest.main()    
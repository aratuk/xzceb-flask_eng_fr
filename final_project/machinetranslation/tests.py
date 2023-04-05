import unittest
from translator import englishToFrench, frenchToEnglish

class test_translator(unittest.TestCase):
    #def test_e2f_null(self):
    #    self.assertIsNotNone(self,'')
    #def test_f2e_null(self):
    #    self.assertIsNotNone(self,'')
    def test_e2f_hi(self):
        self.assertEqual(englishToFrench('Hello'), 'Bonjour')
    def test_f2e_hi(self):
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello')

if __name__ == "__main__":
    unittest.main()    
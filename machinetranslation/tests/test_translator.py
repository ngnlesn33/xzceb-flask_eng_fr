import sys
import unittest

sys.path.insert(0, 'D:\\Documents\\programming\\python\\course2\\xzceb'
                   '-flask_eng_fr\\machinetranslation')
from translator import englishToFrench, frenchToEnglish


class TestEnglishToFrench(unittest.TestCase):
    def test1(self):
        self.assertEqual(englishToFrench('Hello'.lower()), 'Bonjour'.lower())


class TestFrenchToEnglish(unittest.TestCase):
    def test1(self):
        self.assertEqual(frenchToEnglish('Bonjour'.lower()), 'Hello'.lower())


if __name__ == '__main__':
    unittest.main()

from unittest import TestCase
from main import letters_len, revers_string



class TestLetters(TestCase):
    def test_letter(self):
        self.assertEqual(letters_len('wow1'), 3)


class TestString(TestCase):
    def test_string(self):
        self.assertEqual(revers_string('123'), '321')
        self.assertEqual(revers_string('daun'), 'nuad')


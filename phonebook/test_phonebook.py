import unittest
from phonebook import PhoneBook


class PhoneBookTest(unittest.TestCase):
    def test_lookup_by_name(self):
        phonebook = PhoneBook()
        phonebook.add('Pyl', '123456')
        number = phonebook.lookup('Pyl')
        self.assertEqual(number, '123456')

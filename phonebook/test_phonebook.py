import unittest
from phonebook import PhoneBook


class PhoneBookTest(unittest.TestCase):

    def setUp(self) -> None:
        self.phonebook = PhoneBook()

    def tearDown(self) -> None:
        pass

    def test_lookup_by_name(self):
        self.phonebook.add('Pyl', '123456')
        number = self.phonebook.lookup('Pyl')
        self.assertEqual(number, '123456')

    def test_missing_name(self):
        with self.assertRaises(KeyError):
            self.phonebook.lookup('missing')

    @unittest.skip("WIP")
    def test_empty_phonebook_is_consistent(self):
        self.assertTrue(self.phonebook.is_consistent())
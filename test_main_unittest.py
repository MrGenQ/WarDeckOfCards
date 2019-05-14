import unittest
from unittest import main
from main import compare_cards


class ComparingCards(unittest.TestCase):

    def test_compare_cards(self):
        deck = ['2', '3', '4', '5', '6', '7',
                '8', '9', '10', 'J', 'Q', 'K', 'A']*4
        value = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
        compar = dict(zip(deck, value))
        self.assertEqual(compare_cards('J', 'A', deck, compar), 1)
        self.assertEqual(compare_cards('Q', '10', deck, compar), 0)
        self.assertEqual(compare_cards('K', 'K', deck, compar), -1)


if __name__ == '__main__':
    unittest.main()

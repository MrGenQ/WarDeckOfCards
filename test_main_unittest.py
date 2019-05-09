import unittest
from main import compare_cards

class ComparingCards(unittest.TestCase):

    def test_compare_cards(self):
        self.assertEqual(compare_cards('J', 'A'), 1)
        self.assertEqual(compare_cards('Q', '10'), 0)
        self.assertEqual(compare_cards('K', 'K'), -1)

if __name__ == '__main__':
    unittest.main()
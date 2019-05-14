import unittest
from unittest import main
from main import compare_cards

class ComparingCards(unittest.TestCase):

    def test_compare_cards(self):
        self.assertEqual(compare_cards('2', 'J'), 1)
        self.assertEqual(compare_cards('Q', '10'), 0)
        self.assertEqual(compare_cards('10', '10'), 2)

if __name__ == '__main__':
    
    unittest.main()
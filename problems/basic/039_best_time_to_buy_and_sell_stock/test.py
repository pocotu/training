"""
Test cases for Best Time to Buy and Sell Stock
Problem ID: 039
"""

import unittest
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent))

from solution import max_profit

class TestMaxProfit(unittest.TestCase):

    def test_example_1(self):
        self.assertEqual(max_profit([7,1,5,3,6,4]), 5)

    def test_example_2(self):
        self.assertEqual(max_profit([7,6,4,3,1]), 0)

    def test_single_price(self):
        self.assertEqual(max_profit([1]), 0)

    def test_increasing_prices(self):
        self.assertEqual(max_profit([1,2,3,4,5]), 4)

if __name__ == '__main__':
    unittest.main(verbosity=2)
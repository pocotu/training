"""
Test cases for filter() function
Problem ID: F040
"""

import unittest
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent))

from solution import filter_even_numbers

class TestFilterFunction(unittest.TestCase):

    def test_filter_even_numbers(self):
        self.assertEqual(filter_even_numbers([1, 2, 3, 4, 5]), [2, 4])

if __name__ == '__main__':
    unittest.main(verbosity=2)

"""
Test cases for Lambda Functions
Problem ID: F038
"""

import unittest
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent))

from solution import multiplier

class TestLambdaFunctions(unittest.TestCase):

    def test_multiplier(self):
        self.assertEqual(multiplier(5), 50)

if __name__ == '__main__':
    unittest.main(verbosity=2)

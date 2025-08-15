"""
Test cases for Function with Return Value
Problem ID: F017
"""

import unittest
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent))

from solution import multiply

class TestFunctionWithReturnValue(unittest.TestCase):

    def test_multiply(self):
        self.assertEqual(multiply(5, 3), 15)
        self.assertEqual(multiply(-1, 1), -1)

if __name__ == '__main__':
    unittest.main(verbosity=2)

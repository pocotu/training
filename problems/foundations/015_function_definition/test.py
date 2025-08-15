"""
Test cases for Function Definition
Problem ID: F015
"""

import unittest
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent))

from solution import my_function

class TestFunctionDefinition(unittest.TestCase):

    def test_my_function(self):
        self.assertTrue(my_function())

if __name__ == '__main__':
    unittest.main(verbosity=2)

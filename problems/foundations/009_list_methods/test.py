"""
Test cases for List Methods
Problem ID: F009
"""

import unittest
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent))

from solution import use_list_methods

class TestListMethods(unittest.TestCase):

    def test_use_list_methods(self):
        """Test modifying list according to requirements"""
        result = use_list_methods([1, 2, 3])
        self.assertEqual(result, [1, 3, 4])

if __name__ == '__main__':
    unittest.main(verbosity=2)

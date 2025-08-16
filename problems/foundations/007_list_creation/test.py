"""
Test cases for List Creation
Problem ID: F007
"""

import unittest
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent))

from solution import create_list

class TestListCreation(unittest.TestCase):

    def test_create_list(self):
        """Test that the function returns [1, 2, 3]"""
        result = create_list()
        expected = [1, 2, 3]
        self.assertEqual(result, expected)
        self.assertIsInstance(result, list)

if __name__ == '__main__':
    unittest.main()

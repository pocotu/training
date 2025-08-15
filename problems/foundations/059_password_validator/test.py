"""
Test cases for Password Validator
Problem ID: F059
"""

import unittest
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent))

from solution import is_valid_password

class TestPasswordValidator(unittest.TestCase):

    def test_is_valid_password(self):
        self.assertTrue(is_valid_password("MyPass123!"))
        self.assertFalse(is_valid_password("weakpass"))
        self.assertFalse(is_valid_password("NoSpecial123"))
        self.assertFalse(is_valid_password("SHORT1!"))
        self.assertFalse(is_valid_password("nouppercase123!"))
        self.assertFalse(is_valid_password("NOLOWERCASE123!"))
        self.assertFalse(is_valid_password("NoNumbers!"))

if __name__ == '__main__':
    unittest.main(verbosity=2)
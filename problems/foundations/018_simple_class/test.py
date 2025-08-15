"""
Test cases for Simple Class
Problem ID: F018
"""

import unittest
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent))

from solution import Dog

class TestSimpleClass(unittest.TestCase):

    def test_dog_bark(self):
        my_dog = Dog()
        self.assertEqual(my_dog.bark(), "Woof!")

if __name__ == '__main__':
    unittest.main(verbosity=2)

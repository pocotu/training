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
        """Test that Dog.bark() returns 'Woof!'"""
        my_dog = Dog()
        result = my_dog.bark()
        self.assertEqual(result, "Woof!")
    
    def test_dog_bark_multiple_calls(self):
        """Test multiple calls to bark()"""
        my_dog = Dog()
        self.assertEqual(my_dog.bark(), "Woof!")
        self.assertEqual(my_dog.bark(), "Woof!")
    
    def test_dog_class_instantiation(self):
        """Test that Dog can be instantiated without arguments"""
        my_dog = Dog()
        self.assertIsInstance(my_dog, Dog)

if __name__ == '__main__':
    unittest.main(verbosity=2)

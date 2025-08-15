"""
Test cases for Class Inheritance
Problem ID: F047
"""

import unittest
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent))

from solution import Animal, Dog

class TestClassInheritance(unittest.TestCase):

    def test_animal_sound(self):
        animal = Animal()
        self.assertEqual(animal.make_sound(), "Some generic animal sound")

    def test_dog_sound(self):
        dog = Dog()
        self.assertEqual(dog.make_sound(), "Woof!")

    def test_inheritance(self):
        dog = Dog()
        self.assertIsInstance(dog, Animal)

if __name__ == '__main__':
    unittest.main(verbosity=2)
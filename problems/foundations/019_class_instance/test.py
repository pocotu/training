"""
Test cases for Class Instance
Problem ID: F019
"""

import unittest
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent))

from solution import Person

class TestClassInstance(unittest.TestCase):

    def test_person_instance(self):
        person = Person("John", 25)
        self.assertEqual(person.name, "John")
        self.assertEqual(person.age, 25)
        self.assertIsInstance(person.introduce(), str)

if __name__ == '__main__':
    unittest.main(verbosity=2)

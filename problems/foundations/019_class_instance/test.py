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
        """Test Person constructor with single name argument"""
        person = Person("John")
        self.assertEqual(person.name, "John")
    
    def test_person_multiple_instances(self):
        """Test creating multiple Person instances"""
        person1 = Person("Alice")
        person2 = Person("Bob")
        
        self.assertEqual(person1.name, "Alice")
        self.assertEqual(person2.name, "Bob")
        # Ensure instances are independent
        self.assertNotEqual(person1.name, person2.name)
    
    def test_person_name_attribute_access(self):
        """Test that name attribute is directly accessible"""
        person = Person("Charlie")
        self.assertTrue(hasattr(person, 'name'))
        self.assertEqual(getattr(person, 'name'), "Charlie")

if __name__ == '__main__':
    unittest.main(verbosity=2)

"""
Test cases for String Formatting
Problem ID: F051
"""

import unittest
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent))

from solution import format_person_info

class TestStringFormatting(unittest.TestCase):

    def test_format_person_info(self):
        # Test 1: Caso básico
        result = format_person_info("Alice", 25, "New York")
        expected = "My name is Alice, I am 25 years old, and I live in New York."
        self.assertEqual(result, expected)
        
        # Test 2: Caso básico 2
        result = format_person_info("Bob", 30, "London")
        expected = "My name is Bob, I am 30 years old, and I live in London."
        self.assertEqual(result, expected)
        
        # Test 3: Nombres con espacios
        result = format_person_info("John Doe", 35, "Los Angeles")
        expected = "My name is John Doe, I am 35 years old, and I live in Los Angeles."
        self.assertEqual(result, expected)
        
        # Test 4: Edad cero
        result = format_person_info("Baby", 0, "Hospital")
        expected = "My name is Baby, I am 0 years old, and I live in Hospital."
        self.assertEqual(result, expected)
        
        # Test 5: Ciudad con caracteres especiales
        result = format_person_info("María", 28, "São Paulo")
        expected = "My name is María, I am 28 years old, and I live in São Paulo."
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main(verbosity=2)
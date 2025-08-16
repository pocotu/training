"""
Test cases for List Comprehension Advanced (Problem F071)
"""

import unittest
from solution import filter_and_square, nested_multiplication, conditional_transform

class TestListComprehensionAdvanced(unittest.TestCase):

    def test_filter_and_square(self):
        """Test filtering even numbers and squaring them"""
        self.assertEqual(filter_and_square([1, 2, 3, 4, 5, 6]), [4, 16, 36])
        self.assertEqual(filter_and_square([1, 3, 5]), [])
        self.assertEqual(filter_and_square([2, 4]), [4, 16])
        self.assertEqual(filter_and_square([]), [])

    def test_nested_multiplication(self):
        """Test nested list comprehension"""
        self.assertEqual(nested_multiplication([[1, 2], [3, 4]]), [[2, 4], [6, 8]])
        self.assertEqual(nested_multiplication([[0]]), [[0]])
        self.assertEqual(nested_multiplication([]), [])
        self.assertEqual(nested_multiplication([[1, 2, 3], [4, 5, 6]]), [[2, 4, 6], [8, 10, 12]])

    def test_conditional_transform(self):
        """Test conditional transformation based on word length"""
        self.assertEqual(conditional_transform(["abc", "hello", "hi", "python"]), 
                        ["abc", "hello", "HI", "PYTHON"])
        self.assertEqual(conditional_transform(["a", "ab"]), ["a", "AB"])
        self.assertEqual(conditional_transform([]), [])
        self.assertEqual(conditional_transform(["test"]), ["TEST"])

if __name__ == '__main__':
    unittest.main()

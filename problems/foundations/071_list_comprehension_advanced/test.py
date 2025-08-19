"""
Test cases for List Comprehension Advanced (Problem F071)
"""

import unittest
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent))

from solution import filter_and_square

class TestListComprehensionAdvanced(unittest.TestCase):

    def test_filter_and_square(self):
        # Test 1: Lista mixta
        self.assertEqual(filter_and_square([1, 2, 3, 4, 5, 6]), [4, 16, 36])
        
        # Test 2: Solo números impares
        self.assertEqual(filter_and_square([1, 3, 5]), [])
        
        # Test 3: Solo números pares
        self.assertEqual(filter_and_square([2, 4]), [4, 16])
        
        # Test 4: Lista vacía
        self.assertEqual(filter_and_square([]), [])
        
        # Test 5: Un solo número par
        self.assertEqual(filter_and_square([8]), [64])
        
        # Test 6: Números negativos
        self.assertEqual(filter_and_square([-2, -1, 0, 1, 2]), [4, 0, 4])

if __name__ == '__main__':
    unittest.main(verbosity=2)

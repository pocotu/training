"""
Test cases for Bubble Sort
Problem ID: F044
"""

import unittest
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent))

from solution import bubble_sort

class TestBubbleSort(unittest.TestCase):

    def test_bubble_sort(self):
        # Test 1: Lista normal
        lst1 = [64, 34, 25, 12, 22, 11, 90]
        bubble_sort(lst1)
        self.assertEqual(lst1, [11, 12, 22, 25, 34, 64, 90])
        
        # Test 2: Lista pequeña
        lst2 = [5, 2, 8, 1, 9]
        bubble_sort(lst2)
        self.assertEqual(lst2, [1, 2, 5, 8, 9])
        
        # Test 3: Lista de un elemento
        lst3 = [1]
        bubble_sort(lst3)
        self.assertEqual(lst3, [1])
        
        # Test 4: Lista vacía
        lst4 = []
        bubble_sort(lst4)
        self.assertEqual(lst4, [])
        
        # Test 5: Lista con elementos duplicados
        lst5 = [3, 3, 3, 1, 2]
        bubble_sort(lst5)
        self.assertEqual(lst5, [1, 2, 3, 3, 3])

if __name__ == '__main__':
    unittest.main(verbosity=2)
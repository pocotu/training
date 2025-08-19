"""
Test cases for Simple Calculator
Problem ID: F060
"""

import unittest
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent))

from solution import calculate

class TestSimpleCalculator(unittest.TestCase):

    def test_calculate(self):
        # Operaciones básicas
        self.assertEqual(calculate(10, 5, '+'), 15)
        self.assertEqual(calculate(10, 5, '-'), 5)
        self.assertEqual(calculate(6, 2, '*'), 12)
        self.assertEqual(calculate(10, 2, '/'), 5.0)
        
        # Casos de error
        self.assertEqual(calculate(10, 0, '/'), "Error")
        self.assertEqual(calculate(5, 3, '%'), "Error")
        
        # Casos adicionales con decimales
        self.assertEqual(calculate(1.5, 2.5, '+'), 4.0)
        self.assertEqual(calculate(10, 3, '/'), 10/3)
        
        # Números negativos
        self.assertEqual(calculate(-5, 3, '+'), -2)
        self.assertEqual(calculate(-10, -2, '*'), 20)

if __name__ == '__main__':
    unittest.main(verbosity=2)
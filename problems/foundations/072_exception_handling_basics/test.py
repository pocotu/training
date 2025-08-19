import unittest
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent))

from solution import safe_division

class TestExceptionHandling(unittest.TestCase):
    
    def test_safe_division(self):
        # Test 1: División normal
        self.assertEqual(safe_division(10, 2), 5.0)
        
        # Test 2: División por cero
        self.assertEqual(safe_division(10, 0), "Error: División por cero")
        
        # Test 3: División con decimales
        self.assertEqual(safe_division(7, 2), 3.5)
        
        # Test 4: División de cero
        self.assertEqual(safe_division(0, 5), 0.0)
        
        # Test 5: División por cero de cero
        self.assertEqual(safe_division(0, 0), "Error: División por cero")
        
        # Test 6: Números negativos
        self.assertEqual(safe_division(-10, 2), -5.0)

if __name__ == '__main__':
    unittest.main(verbosity=2)

import unittest
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent))

from solution import calculator

class TestSimpleCalculator(unittest.TestCase):
    
    def test_calculator(self):
        # Test 1: Suma
        self.assertEqual(calculator(5, 3, "add"), 8)
        
        # Test 2: División
        self.assertEqual(calculator(10, 2, "divide"), 5.0)
        
        # Test 3: Multiplicación
        self.assertEqual(calculator(4, 3, "multiply"), 12)
        
        # Test 4: Resta
        self.assertEqual(calculator(10, 4, "subtract"), 6)
        
        # Test 5: División por cero
        self.assertEqual(calculator(10, 0, "divide"), "Error")
        
        # Test 6: Operación inválida
        self.assertEqual(calculator(5, 3, "invalid"), "Error")

if __name__ == '__main__':
    unittest.main(verbosity=2)

if __name__ == '__main__':
    unittest.main()

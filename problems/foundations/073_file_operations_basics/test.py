import unittest
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent))

from solution import count_lines

class TestStringLinesProcessing(unittest.TestCase):
    
    def test_count_lines(self):
        # Test 1: Líneas normales
        self.assertEqual(count_lines("Línea 1\nLínea 2\nLínea 3"), 3)
        
        # Test 2: Con línea vacía
        self.assertEqual(count_lines("Hola\n\nMundo\n"), 2)
        
        # Test 3: String vacío
        self.assertEqual(count_lines(""), 0)
        
        # Test 4: Una sola línea
        self.assertEqual(count_lines("Solo una línea"), 1)
        
        # Test 5: Líneas con espacios
        self.assertEqual(count_lines("Línea 1\n   \nLínea 3"), 2)
        
        # Test 6: Solo espacios y saltos de línea
        self.assertEqual(count_lines("\n   \n\n"), 0)

if __name__ == '__main__':
    unittest.main(verbosity=2)

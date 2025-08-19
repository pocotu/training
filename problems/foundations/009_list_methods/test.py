"""
Test cases for List Methods
Problem ID: F009
"""

import unittest
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent))

from solution import use_list_methods

class TestListMethods(unittest.TestCase):

    def test_use_list_methods(self):
        """Test modifying list according to requirements"""
        original = [1, 2, 3]
        original_copy = original.copy()  # Para comparar después
        result = use_list_methods(original)
        
        # Verificar que el resultado es correcto
        self.assertEqual(result, [1, 3, 4])
        
        # Verificar que la lista original NO fue modificada
        self.assertEqual(original, original_copy)
    
    def test_use_list_methods_different_data(self):
        """Test with different input data"""
        original = [5, 10, 15, 20]
        original_copy = original.copy()
        result = use_list_methods(original)
        
        self.assertEqual(result, [5, 15, 20, 4])
        self.assertEqual(original, original_copy)  # Original unchanged
    
    def test_original_list_unchanged(self):
        """Specific test to ensure original list is not modified"""
        test_list = [100, 200, 300]
        id_before = id(test_list)
        result = use_list_methods(test_list)
        
        # Verificar que la lista original mantiene su contenido
        self.assertEqual(test_list, [100, 200, 300])
        
        # Verificar que el resultado es una lista diferente
        self.assertIsNot(result, test_list)
        self.assertEqual(result, [100, 300, 4])

if __name__ == '__main__':
    unittest.main(verbosity=2)

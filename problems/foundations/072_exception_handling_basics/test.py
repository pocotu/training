import unittest
from solution import safe_division, safe_list_access, safe_int_conversion

class TestExceptionHandling(unittest.TestCase):
    
    def test_safe_division_normal(self):
        """Test división normal"""
        self.assertEqual(safe_division(10, 2), 5.0)
        self.assertEqual(safe_division(15, 3), 5.0)
        self.assertEqual(safe_division(7, 2), 3.5)
    
    def test_safe_division_zero(self):
        """Test división por cero"""
        self.assertEqual(safe_division(10, 0), "Error: División por cero")
        self.assertEqual(safe_division(0, 0), "Error: División por cero")
    
    def test_safe_list_access_normal(self):
        """Test acceso normal a lista"""
        lst = [1, 2, 3, 4, 5]
        self.assertEqual(safe_list_access(lst, 0), 1)
        self.assertEqual(safe_list_access(lst, 2), 3)
        self.assertEqual(safe_list_access(lst, 4), 5)
    
    def test_safe_list_access_index_error(self):
        """Test acceso fuera de rango"""
        lst = [1, 2, 3]
        self.assertEqual(safe_list_access(lst, 5), "Error: Índice fuera de rango")
        self.assertEqual(safe_list_access(lst, -10), "Error: Índice fuera de rango")
        self.assertEqual(safe_list_access([], 0), "Error: Índice fuera de rango")
    
    def test_safe_int_conversion_normal(self):
        """Test conversión normal"""
        self.assertEqual(safe_int_conversion("123"), 123)
        self.assertEqual(safe_int_conversion("0"), 0)
        self.assertEqual(safe_int_conversion("-456"), -456)
    
    def test_safe_int_conversion_error(self):
        """Test conversión con error"""
        self.assertEqual(safe_int_conversion("abc"), "Error: No se puede convertir a entero")
        self.assertEqual(safe_int_conversion("12.34"), "Error: No se puede convertir a entero")
        self.assertEqual(safe_int_conversion(""), "Error: No se puede convertir a entero")

if __name__ == '__main__':
    unittest.main()

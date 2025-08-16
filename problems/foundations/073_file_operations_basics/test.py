import unittest
import os
from solution import write_lines_to_file, read_lines_from_file, count_words_in_file

class TestFileOperations(unittest.TestCase):
    
    def setUp(self):
        """Configuración inicial para tests"""
        self.test_file = "test_file.txt"
        self.test_lines = ["Primera línea", "Segunda línea", "Tercera línea"]
    
    def tearDown(self):
        """Limpieza después de tests"""
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
    
    def test_write_lines_to_file(self):
        """Test escritura de líneas"""
        result = write_lines_to_file(self.test_file, self.test_lines)
        self.assertTrue(result)
        self.assertTrue(os.path.exists(self.test_file))
    
    def test_read_lines_from_file_exists(self):
        """Test lectura de archivo existente"""
        write_lines_to_file(self.test_file, self.test_lines)
        lines = read_lines_from_file(self.test_file)
        self.assertEqual(len(lines), 3)
        self.assertIn("Primera línea", lines[0])
    
    def test_read_lines_from_file_not_exists(self):
        """Test lectura de archivo inexistente"""
        lines = read_lines_from_file("archivo_inexistente.txt")
        self.assertEqual(lines, [])
    
    def test_count_words_in_file_exists(self):
        """Test conteo de palabras en archivo existente"""
        test_content = ["Hola mundo Python", "Es muy genial programar"]
        write_lines_to_file(self.test_file, test_content)
        count = count_words_in_file(self.test_file)
        self.assertEqual(count, 7)  # Total de palabras
    
    def test_count_words_in_file_not_exists(self):
        """Test conteo de palabras en archivo inexistente"""
        count = count_words_in_file("archivo_inexistente.txt")
        self.assertEqual(count, 0)
    
    def test_count_words_empty_file(self):
        """Test conteo en archivo vacío"""
        write_lines_to_file(self.test_file, [])
        count = count_words_in_file(self.test_file)
        self.assertEqual(count, 0)

if __name__ == '__main__':
    unittest.main()

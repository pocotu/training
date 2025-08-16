import unittest
from solution import Student

class TestStudent(unittest.TestCase):
    
    def setUp(self):
        """Configuración inicial para tests"""
        self.student = Student("Ana García", 20)
    
    def test_student_initialization(self):
        """Test inicialización correcta"""
        self.assertEqual(self.student.name, "Ana García")
        self.assertEqual(self.student.age, 20)
        self.assertEqual(self.student.grades, [])
    
    def test_add_grade_single(self):
        """Test añadir una calificación"""
        self.student.add_grade(85)
        self.assertEqual(len(self.student.grades), 1)
        self.assertEqual(self.student.grades[0], 85)
    
    def test_add_grade_multiple(self):
        """Test añadir múltiples calificaciones"""
        grades = [85, 92, 78, 90]
        for grade in grades:
            self.student.add_grade(grade)
        self.assertEqual(len(self.student.grades), 4)
        self.assertEqual(self.student.grades, grades)
    
    def test_get_average_no_grades(self):
        """Test promedio sin calificaciones"""
        average = self.student.get_average()
        self.assertEqual(average, 0.0)
    
    def test_get_average_with_grades(self):
        """Test promedio con calificaciones"""
        self.student.add_grade(80)
        self.student.add_grade(90)
        self.student.add_grade(85)
        average = self.student.get_average()
        self.assertEqual(average, 85.0)
    
    def test_get_average_decimal(self):
        """Test promedio con resultado decimal"""
        self.student.add_grade(85)
        self.student.add_grade(92)
        self.student.add_grade(78)
        average = self.student.get_average()
        self.assertAlmostEqual(average, 85.0, places=1)
    
    def test_get_info_no_grades(self):
        """Test información sin calificaciones"""
        info = self.student.get_info()
        expected = "Ana García (20 años) - Promedio: 0.0"
        self.assertEqual(info, expected)
    
    def test_get_info_with_grades(self):
        """Test información con calificaciones"""
        self.student.add_grade(85)
        self.student.add_grade(95)
        info = self.student.get_info()
        expected = "Ana García (20 años) - Promedio: 90.0"
        self.assertEqual(info, expected)

if __name__ == '__main__':
    unittest.main()

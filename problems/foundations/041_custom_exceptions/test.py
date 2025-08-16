import unittest
from solution import InvalidAgeError, InsufficientFundsError, validate_person

class TestCustomExceptions(unittest.TestCase):
    
    def test_invalid_age_error_creation(self):
        """Test creación de InvalidAgeError"""
        error = InvalidAgeError(-5)
        self.assertIsInstance(error, ValueError)
        self.assertIn("-5", str(error))
    
    def test_insufficient_funds_error_creation(self):
        """Test creación de InsufficientFundsError"""
        error = InsufficientFundsError(100, 150)
        self.assertIsInstance(error, Exception)
        self.assertIn("100", str(error))
        self.assertIn("150", str(error))
    
    def test_validate_person_valid_data(self):
        """Test validación con datos válidos"""
        result = validate_person("Ana", 25, 1000)
        self.assertTrue(result)
    
    def test_validate_person_negative_age(self):
        """Test validación con edad negativa"""
        with self.assertRaises(InvalidAgeError):
            validate_person("Juan", -5, 1000)
    
    def test_validate_person_age_too_high(self):
        """Test validación con edad muy alta"""
        with self.assertRaises(InvalidAgeError):
            validate_person("María", 200, 1000)
    
    def test_validate_person_negative_balance(self):
        """Test validación con balance negativo"""
        with self.assertRaises(InsufficientFundsError):
            validate_person("Pedro", 30, -100)
    
    def test_validate_person_edge_ages(self):
        """Test validación con edades límite"""
        # Edad 0 debe ser válida
        result = validate_person("Bebé", 0, 100)
        self.assertTrue(result)
        
        # Edad 150 debe ser válida
        result = validate_person("Anciano", 150, 100)
        self.assertTrue(result)
    
    def test_exception_inheritance(self):
        """Test herencia correcta de excepciones"""
        self.assertTrue(issubclass(InvalidAgeError, ValueError))
        self.assertTrue(issubclass(InsufficientFundsError, Exception))

if __name__ == '__main__':
    unittest.main()

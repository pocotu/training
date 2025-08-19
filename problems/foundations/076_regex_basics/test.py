import unittest
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent))

from solution import validate_email

class TestRegexBasics(unittest.TestCase):
    
    def test_validate_email(self):
        # Test 1: Email válido básico
        self.assertTrue(validate_email("usuario@dominio.com"))
        
        # Test 2: Sin @
        self.assertFalse(validate_email("email-invalido"))
        
        # Test 3: Email válido alternativo
        self.assertTrue(validate_email("test@gmail.org"))
        
        # Test 4: Sin dominio después de @
        self.assertFalse(validate_email("usuario@"))
        
        # Test 5: Sin usuario antes de @
        self.assertFalse(validate_email("@dominio.com"))
        
        # Test 6: Sin punto en dominio
        self.assertFalse(validate_email("user@domain"))
        
        # Test 7: Multiple @
        self.assertFalse(validate_email("user@domain@com"))

if __name__ == '__main__':
    unittest.main(verbosity=2)

if __name__ == '__main__':
    unittest.main()

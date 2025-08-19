"""
Test cases for Password Validator
Problem ID: F059
"""

import unittest
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent))

from solution import is_valid_password

class TestPasswordValidator(unittest.TestCase):

    def test_is_valid_password(self):
        # Tests válidos
        self.assertTrue(is_valid_password("MyPass123!"))
        self.assertTrue(is_valid_password("SecureP@ss1"))
        
        # Tests inválidos - casos específicos
        self.assertFalse(is_valid_password("weakpass"))  # Sin mayúscula, número, especial
        self.assertFalse(is_valid_password("NoSpecial123"))  # Sin carácter especial
        self.assertFalse(is_valid_password("SHORT1!"))  # Muy corto
        self.assertFalse(is_valid_password("nouppercase123!"))  # Sin mayúscula
        self.assertFalse(is_valid_password("NOLOWERCASE123!"))  # Sin minúscula
        self.assertFalse(is_valid_password("NoNumbers!"))  # Sin números
        
        # Edge cases adicionales
        self.assertFalse(is_valid_password(""))  # String vacío
        self.assertTrue(is_valid_password("Valid1Pass@"))  # Válido adicional

if __name__ == '__main__':
    unittest.main(verbosity=2)
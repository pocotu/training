"""
Solution for Password Validator
Problem ID: F059
"""

def is_valid_password(password):
    """
    Validates a password based on security criteria.
    Args:
        password (str): password to validate
    Returns:
        bool: True if valid, False otherwise
    """
    # Criterios de validación:
    # - Al menos 8 caracteres
    # - Al menos una letra minúscula
    # - Al menos una letra mayúscula
    # - Al menos un dígito
    # - Al menos un carácter especial
    
    if len(password) < 8:
        return False
    
    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(not c.isalnum() for c in password)
    
    return has_lower and has_upper and has_digit and has_special

def main():
    """
    Función principal para 059_password_validator
    """
    # Ejemplos de uso
    test_passwords = [
        "password",
        "Password",
        "Password1",
        "Password1!",
        "Pass1!",
        "VeryStrongPassword123!",
        "weak",
        "NOLOWERCASE123!",
        "nouppercase123!"
    ]
    
    for pwd in test_passwords:
        result = is_valid_password(pwd)
        print(f"'{pwd}' es válida: {result}")
    
    return is_valid_password("Password1!")

if __name__ == "__main__":
    result = main()
    print(f"Resultado: {result}")

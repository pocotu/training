"""
Solution for Palindrome Check
Problem ID: F024
"""

def is_palindrome(s):
    """
    Checks if a string is a palindrome.
    """
    # Convertir a minúsculas y eliminar espacios para comparación más robusta
    clean_s = s.lower().replace(' ', '')
    return clean_s == clean_s[::-1]

def main():
    """
    Función principal para 024_palindrome_check
    """
    # Ejemplo de uso
    test_string = "racecar"
    result = is_palindrome(test_string)
    print(f"¿'{test_string}' es palíndromo?: {result}")
    return result

if __name__ == "__main__":
    result = main()
    print(f"Resultado: {result}")

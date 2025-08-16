"""
Solution for Reverse a String
Problem ID: F023
"""

def reverse_string(s):
    """
    Reverses a string.
    """
    return s[::-1]

def main():
    """
    Función principal para 023_reverse_a_string
    """
    # Ejemplo de uso
    test_string = "hello"
    result = reverse_string(test_string)
    print(f"'{test_string}' al revés: '{result}'")
    return result

if __name__ == "__main__":
    result = main()
    print(f"Resultado: {result}")

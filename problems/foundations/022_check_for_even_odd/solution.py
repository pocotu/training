"""
Solution for Check for Even/Odd
Problem ID: F022
"""

def is_even(num):
    """
    Checks if a number is even.
    """
    return num % 2 == 0

def main():
    """
    Función principal para 022_check_for_even_odd
    """
    # Ejemplo de uso
    test_number = 4
    result = is_even(test_number)
    print(f"¿{test_number} es par?: {result}")
    return result

if __name__ == "__main__":
    result = main()
    print(f"Resultado: {result}")

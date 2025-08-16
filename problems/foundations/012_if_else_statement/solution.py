"""
Solution for If-Else Statement
Problem ID: F012
"""

def check_number(num):
    """
    Checks if a number is positive, negative, or zero.
    """
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"

def main():
    """
    Función principal para 012_if_else_statement
    """
    # Ejemplo de uso
    test_number = 5
    result = check_number(test_number)
    print(f"El número {test_number} es: {result}")
    return result

if __name__ == "__main__":
    result = main()
    print(f"Resultado: {result}")

"""
Solution for Function with Return Value
Problem ID: F017
"""

def multiply(a, b):
    """
    Multiplies two numbers and returns the result.
    """
    return a * b

def main():
    """
    Función principal para 017_function_with_return_value
    """
    # Ejemplo de uso
    result = multiply(4, 6)
    print(f"4 * 6 = {result}")
    return result

if __name__ == "__main__":
    result = main()
    print(f"Resultado: {result}")

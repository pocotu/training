"""
Solution for Arithmetic Operations
Problem ID: F003
"""

def perform_operations(a, b):
    """
    Performs arithmetic operations on two numbers.
    Returns tuple with: (sum, difference, product, quotient)
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    
    sum_result = a + b
    difference = a - b
    product = a * b
    quotient = a / b
    
    return (sum_result, difference, product, quotient)

def main():
    """
    Función principal para 003_arithmetic_operations
    """
    # Ejemplo de uso
    result = perform_operations(10, 5)
    print(f"Operaciones con 10 y 5: {result}")
    return result

if __name__ == "__main__":
    result = main()
    print(f"Resultado: {result}")

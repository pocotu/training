"""
Solution for Factorial Recursive
Problem ID: F042
"""

def factorial(n):
    """
    Calcula el factorial de un número de forma recursiva.
    Args:
        n (int): número para calcular factorial
    Returns:
        int: factorial de n
    """
    if n < 0:
        raise ValueError("Factorial no está definido para números negativos")
    
    # Caso base
    if n == 0 or n == 1:
        return 1
    
    # Caso recursivo
    return n * factorial(n - 1)

def main():
    """
    Función principal para 042_factorial_recursive
    """
    # Ejemplos de uso
    test_cases = [0, 1, 3, 5, 4]
    for num in test_cases:
        result = factorial(num)
        print(f"factorial({num}) = {result}")
    
    return factorial(5)

if __name__ == "__main__":
    result = main()
    print(f"Resultado: {result}")

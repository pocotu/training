"""
Solution for Fibonacci Sequence
Problem ID: F043
"""

def fibonacci(n):
    """
    Calcula el n-ésimo número de Fibonacci.
    Args:
        n (int): posición en la secuencia de Fibonacci
    Returns:
        int: n-ésimo número de Fibonacci
    """
    if n < 0:
        raise ValueError("n debe ser no negativo")
    
    # Casos base
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    # Caso recursivo
    return fibonacci(n - 1) + fibonacci(n - 2)

def main():
    """
    Función principal para 043_fibonacci_sequence
    """
    # Ejemplos de uso
    for i in range(10):
        result = fibonacci(i)
        print(f"fibonacci({i}) = {result}")
    
    return fibonacci(7)

if __name__ == "__main__":
    result = main()
    print(f"Resultado: {result}")

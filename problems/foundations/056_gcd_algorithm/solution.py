"""
Solution for GCD Algorithm
Problem ID: F056
"""

def gcd(a, b):
    """
    Calculates the Greatest Common Divisor using Euclidean algorithm.
    Args:
        a (int): first number
        b (int): second number
    Returns:
        int: greatest common divisor
    """
    # Asegurar que trabajamos con valores absolutos
    a, b = abs(a), abs(b)
    
    # Algoritmo euclidiano
    while b:
        a, b = b, a % b
    
    return a

def main():
    """
    Función principal para 056_gcd_algorithm
    """
    # Ejemplos de uso
    test_cases = [(48, 18), (56, 42), (17, 13), (100, 25), (0, 5)]
    
    for a, b in test_cases:
        result = gcd(a, b)
        print(f"gcd({a}, {b}) = {result}")
    
    return gcd(48, 18)

if __name__ == "__main__":
    result = main()
    print(f"Resultado: {result}")

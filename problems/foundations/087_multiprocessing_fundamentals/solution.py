"""
Solution for Mathematical Functions
Problem ID: F087
"""

def calculate_factorial(n):
    """
    Calculates factorial of n using iteration.
    Returns factorial value (n!).
    """
    # TODO: Implement your solution here
    pass

def calculate_power(base, exponent):
    """
    Calculates base raised to exponent.
    Returns base^exponent.
    """
    # TODO: Implement your solution here
    pass

def calculate_gcd(a, b):
    """
    Calculates greatest common divisor using Euclidean algorithm.
    Returns GCD of a and b.
    """
    # TODO: Implement your solution here
    pass

def main():
    # Ejemplo de uso
    print(f"Factorial de 5: {calculate_factorial(5)}")
    print(f"2^3: {calculate_power(2, 3)}")
    print(f"GCD(48, 18): {calculate_gcd(48, 18)}")
    
    return {
        "factorial_5": calculate_factorial(5),
        "power_2_3": calculate_power(2, 3),
        "gcd_48_18": calculate_gcd(48, 18)
    }

if __name__ == "__main__":
    result = main()
    print(f"Resultado final: {result}")

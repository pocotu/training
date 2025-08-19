"""
Solution for GCD Algorithm
Problem ID: F056
"""

def gcd(a, b):
    # TODO: Implement your solution here
    pass

def main():
    # Ejemplos de uso
    test_cases = [(48, 18), (56, 42), (17, 13), (100, 25), (0, 5)]
    
    for a, b in test_cases:
        result = gcd(a, b)
        print(f"gcd({a}, {b}) = {result}")
    
    return gcd(48, 18)

if __name__ == "__main__":
    result = main()
    print(f"Resultado: {result}")

"""
Solution for Factorial Recursive
Problem ID: F042
"""

def factorial(n):
    # TODO: Implement your solution here
    pass

def main():
    # Ejemplos de uso
    test_cases = [0, 1, 3, 5, 4]
    for num in test_cases:
        result = factorial(num)
        print(f"factorial({num}) = {result}")
    
    return factorial(5)

if __name__ == "__main__":
    result = main()
    print(f"Resultado: {result}")

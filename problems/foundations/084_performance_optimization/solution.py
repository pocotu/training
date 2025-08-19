"""
Solution for Number Comparison Functions
Problem ID: F084
"""

def find_maximum(numbers_list):
    """
    Finds the maximum number in a list without using built-in max().
    Returns None if list is empty.
    """
    # TODO: Implement your solution here
    pass

def find_minimum(numbers_list):
    """
    Finds the minimum number in a list without using built-in min().
    Returns None if list is empty.
    """
    # TODO: Implement your solution here
    pass

def compare_numbers(a, b):
    """
    Compares two numbers and returns appropriate message.
    Returns string with comparison result.
    """
    # TODO: Implement your solution here
    pass

def main():
    # Ejemplo de uso
    numbers = [5, 2, 8, 1, 9, 3]
    
    print(f"Lista: {numbers}")
    print(f"Máximo: {find_maximum(numbers)}")
    print(f"Mínimo: {find_minimum(numbers)}")
    
    print(f"Comparar 5 y 3: {compare_numbers(5, 3)}")
    print(f"Comparar 2 y 7: {compare_numbers(2, 7)}")
    print(f"Comparar 4 y 4: {compare_numbers(4, 4)}")
    
if __name__ == "__main__":
    result = main()
    print(f"Resultado final: {result}")

"""
Solution for Binary Search
Problem ID: F046
"""

def binary_search(arr, target):
    # TODO: Implement your solution here
    pass

def main():
    # Ejemplos de uso (array debe estar ordenado)
    test_arr = [1, 2, 3, 5, 8, 9]
    
    test_cases = [8, 1, 10, 5]
    for target in test_cases:
        result = binary_search(test_arr, target)
        print(f"binary_search({test_arr}, {target}) = {result}")
    
    return binary_search(test_arr, 8)

if __name__ == "__main__":
    result = main()
    print(f"Resultado: {result}")

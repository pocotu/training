"""
Solution for Linear Search
Problem ID: F045
"""

def linear_search(arr, target):
    # TODO: Implement your solution here
    pass

def main():
    # Ejemplos de uso
    test_arr = [5, 2, 8, 1, 9, 3]
    
    test_cases = [8, 1, 10, 5]
    for target in test_cases:
        result = linear_search(test_arr, target)
        print(f"linear_search({test_arr}, {target}) = {result}")
    
    return linear_search(test_arr, 8)

if __name__ == "__main__":
    result = main()
    print(f"Resultado: {result}")

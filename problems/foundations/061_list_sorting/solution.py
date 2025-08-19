"""
Solution for List Sorting
Problem ID: F061
"""

def sort_list(numbers):
    # TODO: Implement your solution here
    pass

def main():
    # Ejemplos de uso
    test_cases = [
        [64, 34, 25, 12, 22, 11, 90],
        [5, 2, 8, 1, 9],
        [],
        [1],
        [3, 1, 4, 1, 5, 9, 2, 6]
    ]
    
    for case in test_cases:
        result = sort_list(case)
        print(f"Original: {case}")
        print(f"Sorted:   {result}\n")
    
    return sort_list([64, 34, 25, 12, 22, 11, 90])

if __name__ == "__main__":
    result = main()
    print(f"Resultado: {result}")

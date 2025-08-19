"""
Solution for Bubble Sort
Problem ID: F044
"""

def bubble_sort(lst):
    """
    Sorts a list in-place using bubble sort algorithm.
    Modifies the original list and returns None.
    """
    # TODO: Implement your solution here
    pass

def main():
    # Ejemplos de uso
    test_cases = [
        [64, 34, 25, 12, 22, 11, 90],
        [5, 2, 8, 1, 9],
        [1],
        [],
        [3, 3, 3]
    ]
    
    for arr in test_cases:
        result = bubble_sort(arr)
        print(f"bubble_sort({arr}) = {result}")
    
    return bubble_sort([64, 34, 25, 12, 22, 11, 90])

if __name__ == "__main__":
    result = main()
    print(f"Resultado: {result}")

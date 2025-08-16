"""
Solution for List Sorting
Problem ID: F061
"""

def sort_list(numbers):
    """
    Sorts a list of numbers using bubble sort algorithm.
    Args:
        numbers (list): list of numbers to sort
    Returns:
        list: sorted list in ascending order
    """
    if not numbers:
        return []
    
    # Create a copy to avoid modifying original list
    result = numbers.copy()
    n = len(result)
    
    # Bubble sort implementation
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]
                swapped = True
        
        # If no swapping occurred, list is already sorted
        if not swapped:
            break
    
    return result

def main():
    """
    Función principal para 061_list_sorting
    """
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

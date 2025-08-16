"""
Solution for Algorithm Implementation - Sorting
Problem ID: F075
"""

def insertion_sort(arr):
    """
    Sorts array using insertion sort algorithm.
    Args:
        arr (list): list to sort
    Returns:
        list: sorted list
    """
    if not arr:
        return []
    
    sorted_arr = arr.copy()
    
    for i in range(1, len(sorted_arr)):
        key = sorted_arr[i]
        j = i - 1
        
        # Move elements greater than key one position ahead
        while j >= 0 and sorted_arr[j] > key:
            sorted_arr[j + 1] = sorted_arr[j]
            j -= 1
        
        sorted_arr[j + 1] = key
    
    return sorted_arr

def selection_sort(arr):
    """
    Sorts array using selection sort algorithm.
    Args:
        arr (list): list to sort
    Returns:
        list: sorted list
    """
    if not arr:
        return []
    
    sorted_arr = arr.copy()
    n = len(sorted_arr)
    
    for i in range(n):
        # Find minimum element in remaining array
        min_idx = i
        for j in range(i + 1, n):
            if sorted_arr[j] < sorted_arr[min_idx]:
                min_idx = j
        
        # Swap the found minimum element with first element
        sorted_arr[i], sorted_arr[min_idx] = sorted_arr[min_idx], sorted_arr[i]
    
    return sorted_arr

def compare_algorithms(arr):
    """
    Compare sorting algorithms performance.
    Args:
        arr (list): list to sort
    Returns:
        dict: comparison results
    """
    import time
    
    # Test insertion sort
    start_time = time.time()
    insertion_result = insertion_sort(arr)
    insertion_time = time.time() - start_time
    
    # Test selection sort
    start_time = time.time()
    selection_result = selection_sort(arr)
    selection_time = time.time() - start_time
    
    return {
        'insertion_sort': {
            'result': insertion_result,
            'time': insertion_time
        },
        'selection_sort': {
            'result': selection_result,
            'time': selection_time
        }
    }

def main():
    """
    Función principal para 075_sorting_algorithms
    """
    # Ejemplo de uso
    print("Sorting Algorithms Example:")
    
    test_array = [64, 34, 25, 12, 22, 11, 90]
    print(f"Original array: {test_array}")
    
    # Test insertion sort
    insertion_result = insertion_sort(test_array)
    print(f"Insertion sort: {insertion_result}")
    
    # Test selection sort
    selection_result = selection_sort(test_array)
    print(f"Selection sort: {selection_result}")
    
    # Compare algorithms
    comparison = compare_algorithms(test_array)
    print(f"Performance comparison available")
    
    return insertion_result

if __name__ == "__main__":
    result = main()
    print(f"Resultado: {result}")

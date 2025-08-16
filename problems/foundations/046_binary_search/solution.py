"""
Solution for Binary Search
Problem ID: F046
"""

def binary_search(arr, target):
    """
    Busca un elemento en una lista ordenada usando búsqueda binaria.
    Args:
        arr (list): lista ordenada donde buscar
        target: elemento a buscar
    Returns:
        int: índice del elemento si se encuentra, -1 si no
    """
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

def main():
    """
    Función principal para 046_binary_search
    """
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

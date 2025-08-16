"""
Solution for Linear Search
Problem ID: F045
"""

def linear_search(arr, target):
    """
    Busca un elemento en una lista usando búsqueda lineal.
    Args:
        arr (list): lista donde buscar
        target: elemento a buscar
    Returns:
        int: índice del elemento si se encuentra, -1 si no
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def main():
    """
    Función principal para 045_linear_search
    """
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

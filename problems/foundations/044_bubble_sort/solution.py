"""
Solution for Bubble Sort
Problem ID: F044
"""

def bubble_sort(arr):
    """
    Ordena una lista usando el algoritmo bubble sort.
    Args:
        arr (list): lista a ordenar
    Returns:
        list: lista ordenada
    """
    if not arr:
        return []
    
    # Crear copia para no modificar el original
    sorted_arr = arr.copy()
    n = len(sorted_arr)
    
    # Bubble sort algorithm
    for i in range(n):
        # Flag para optimización
        swapped = False
        
        for j in range(0, n - i - 1):
            # Comparar elementos adyacentes
            if sorted_arr[j] > sorted_arr[j + 1]:
                # Intercambiar
                sorted_arr[j], sorted_arr[j + 1] = sorted_arr[j + 1], sorted_arr[j]
                swapped = True
        
        # Si no hubo intercambios, la lista ya está ordenada
        if not swapped:
            break
    
    return sorted_arr

def main():
    """
    Función principal para 044_bubble_sort
    """
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

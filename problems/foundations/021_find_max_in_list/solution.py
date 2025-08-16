"""
Solution for Find Max in List
Problem ID: F021
"""

def find_max(lst):
    """
    Finds the maximum element in a list.
    """
    if not lst:
        return None
    return max(lst)

def main():
    """
    Función principal para 021_find_max_in_list
    """
    # Ejemplo de uso
    test_list = [1, 2, 3, 4, 5]
    result = find_max(test_list)
    print(f"Máximo en {test_list}: {result}")
    return result

if __name__ == "__main__":
    result = main()
    print(f"Resultado: {result}")

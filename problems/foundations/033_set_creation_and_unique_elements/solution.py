"""
Solution for Set Creation and Unique Elements
Problem ID: F033
"""

def get_unique_elements(lst):
    """
    Returns unique elements from a list using set.
    """
    return list(set(lst))

def main():
    """
    Función principal para 033_set_creation_and_unique_elements
    """
    # Ejemplo de uso
    test_list = [1, 2, 2, 3, 3, 4, 5]
    result = get_unique_elements(test_list)
    print(f"Elementos únicos de {test_list}: {result}")
    return result

if __name__ == "__main__":
    result = main()
    print(f"Resultado: {result}")

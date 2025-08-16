"""
Solution for List Indexing
Problem ID: F008
"""

def get_list_element(lst, index):
    """
    Returns the element at the given index from the list.
    """
    if 0 <= index < len(lst):
        return lst[index]
    else:
        raise IndexError("Index out of range")

def main():
    """
    Función principal para 008_list_indexing
    """
    # Ejemplo de uso
    test_list = [10, 20, 30, 40, 50]
    result = get_list_element(test_list, 2)
    print(f"Elemento en índice 2 de {test_list}: {result}")
    return result

if __name__ == "__main__":
    result = main()
    print(f"Resultado: {result}")

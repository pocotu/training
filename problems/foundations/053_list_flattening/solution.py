"""
Solution for List Flattening
Problem ID: F053
"""

def flatten_list(nested_list):
    """
    Flattens a nested list into a single list.
    Args:
        nested_list (list): list containing sublists
    Returns:
        list: flattened list
    """
    flattened = []
    for item in nested_list:
        if isinstance(item, list):
            flattened.extend(flatten_list(item))
        else:
            flattened.append(item)
    return flattened

def main():
    """
    Función principal para 053_list_flattening
    """
    # Ejemplo de uso
    test_list = [[1, 2], [3, 4], [5]]
    result = flatten_list(test_list)
    print(f"Lista original: {test_list}")
    print(f"Lista aplanada: {result}")
    
    # Ejemplo más complejo
    complex_list = [[1, [2, 3]], [4, 5], [6, [7, [8]]]]
    complex_result = flatten_list(complex_list)
    print(f"Lista compleja: {complex_list}")
    print(f"Lista aplanada: {complex_result}")
    
    return result

if __name__ == "__main__":
    result = main()
    print(f"Resultado: {result}")

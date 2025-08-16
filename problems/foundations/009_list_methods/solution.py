"""
Solution for List Methods
Problem ID: F009
"""

def use_list_methods(lst):
    """
    Modifies a list by:
    1. Adding 4 to the end
    2. Removing element at index 1
    3. Returning modified list
    """
    # Hacer una copia para no modificar la original
    modified_list = lst.copy()
    
    # Añadir 4 al final
    modified_list.append(4)
    
    # Eliminar elemento en índice 1 (si existe)
    if len(modified_list) > 1:
        modified_list.pop(1)
    
    return modified_list

def main():
    """
    Función principal para 009_list_methods
    """
    # Ejemplo de uso
    test_list = [1, 2, 3]
    result = use_list_methods(test_list)
    print(f"Lista original: {test_list}")
    print(f"Lista modificada: {result}")
    return result

if __name__ == "__main__":
    result = main()
    print(f"Resultado: {result}")

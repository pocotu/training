"""
Solution for Slicing with Steps
Problem ID: F027
"""

def get_every_other_element(lst):
    """
    Returns every other element from a list using slicing with steps.
    """
    return lst[::2]

def main():
    """
    Función principal para 027_slicing_with_steps
    """
    # Ejemplo de uso
    test_list = [1, 2, 3, 4, 5, 6, 7, 8]
    result = get_every_other_element(test_list)
    print(f"Elementos alternos de {test_list}: {result}")
    return result

if __name__ == "__main__":
    result = main()
    print(f"Resultado: {result}")

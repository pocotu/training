"""
Solution for Set Operations (Union)
Problem ID: F034
"""

def get_union(set1, set2):
    """
    Returns the union of two sets.
    """
    return set(set1) | set(set2)

def main():
    """
    Función principal para 034_set_operations_union
    """
    # Ejemplo de uso
    set1 = [1, 2, 3]
    set2 = [3, 4, 5]
    result = get_union(set1, set2)
    print(f"Unión de {set1} y {set2}: {result}")
    return result

if __name__ == "__main__":
    result = main()
    print(f"Resultado: {result}")

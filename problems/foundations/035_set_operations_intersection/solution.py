"""
Solution for Set Operations (Intersection)
Problem ID: F035
"""

def get_intersection(set1, set2):
    """
    Returns the intersection of two sets.
    """
    return set(set1) & set(set2)

def main():
    """
    Función principal para 035_set_operations_intersection
    """
    # Ejemplo de uso
    set1 = [1, 2, 3, 4]
    set2 = [3, 4, 5, 6]
    result = get_intersection(set1, set2)
    print(f"Intersección de {set1} y {set2}: {result}")
    return result

if __name__ == "__main__":
    result = main()
    print(f"Resultado: {result}")

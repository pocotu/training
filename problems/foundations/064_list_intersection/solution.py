"""
Solution for List Intersection
Problem ID: F064
"""

def find_intersection(list1, list2):
    """
    Finds the intersection of two lists (common elements).
    Args:
        list1 (list): first list
        list2 (list): second list
    Returns:
        list: list of common elements (without duplicates)
    """
    # Convert to sets to find intersection, then back to list
    set1 = set(list1)
    set2 = set(list2)
    intersection = set1 & set2
    
    # Return as sorted list for consistency
    return sorted(list(intersection))

def main():
    """
    Función principal para 064_list_intersection
    """
    # Ejemplos de uso
    test_cases = [
        ([1, 2, 3, 4, 5], [3, 4, 5, 6, 7]),
        ([1, 2, 2, 3], [2, 3, 4, 5]),
        ([], [1, 2, 3]),
        ([1, 2, 3], [4, 5, 6]),
        (['a', 'b', 'c'], ['b', 'c', 'd'])
    ]
    
    for list1, list2 in test_cases:
        result = find_intersection(list1, list2)
        print(f"List 1: {list1}")
        print(f"List 2: {list2}")
        print(f"Intersection: {result}\n")
    
    return find_intersection([1, 2, 3, 4, 5], [3, 4, 5, 6, 7])

if __name__ == "__main__":
    result = main()
    print(f"Resultado: {result}")

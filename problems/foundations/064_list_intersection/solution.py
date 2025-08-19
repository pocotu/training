"""
Solution for List Intersection
Problem ID: F064
"""

def find_intersection(list1, list2):
    # TODO: Implement your solution here
    pass

def main():
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

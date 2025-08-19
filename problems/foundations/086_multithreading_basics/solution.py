"""
Solution for List Operations and Processing
Problem ID: F086
"""

def combine_lists(list1, list2):
    """
    Combines two lists by alternating elements.
    Returns combined list with alternated elements.
    """
    # TODO: Implement your solution here
    pass

def group_by_length(words_list):
    """
    Groups words by their length.
    Returns dictionary with length as key and words list as value.
    """
    # TODO: Implement your solution here
    pass

def flatten_nested_list(nested_list):
    """
    Flattens a nested list (one level only).
    Returns flattened list with all elements.
    """
    # TODO: Implement your solution here
    pass

def main():
    # Ejemplo de uso
    list1 = [1, 2, 3]
    list2 = ["a", "b", "c"]
    words = ["casa", "carro", "sol", "luna", "estrella"]
    nested = [[1, 2], [3, 4, 5], [6]]
    
    print(f"Combinar {list1} y {list2}: {combine_lists(list1, list2)}")
    print(f"Agrupar por longitud {words}: {group_by_length(words)}")
    print(f"Aplanar {nested}: {flatten_nested_list(nested)}")
    
    return {
        "combined": combine_lists(list1, list2),
        "grouped": group_by_length(words),
        "flattened": flatten_nested_list(nested)
    }



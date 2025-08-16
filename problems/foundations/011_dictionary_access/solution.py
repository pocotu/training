"""
Solution for Dictionary Access
Problem ID: F011
"""

def get_dictionary_value(dictionary, key):
    """
    Returns the value for the given key from the dictionary.
    """
    if key in dictionary:
        return dictionary[key]
    else:
        return None

def main():
    """
    Función principal para 011_dictionary_access
    """
    # Ejemplo de uso
    test_dict = {'name': 'Alice', 'age': 30, 'city': 'New York'}
    result = get_dictionary_value(test_dict, 'age')
    print(f"Valor para 'age': {result}")
    return result

if __name__ == "__main__":
    result = main()
    print(f"Resultado: {result}")

"""
Solution for Iterating Dictionary Items
Problem ID: F031
"""

def format_dictionary(dictionary):
    """
    Formats a dictionary by iterating over its items.
    Returns a list of formatted strings.
    """
    result = []
    for key, value in dictionary.items():
        result.append(f"{key}: {value}")
    return result

def main():
    """
    Función principal para 031_iterating_dictionary_items
    """
    # Ejemplo de uso
    test_dict = {'name': 'Alice', 'age': 30, 'city': 'New York'}
    result = format_dictionary(test_dict)
    print(f"Diccionario formateado: {result}")
    return result

if __name__ == "__main__":
    result = main()
    print(f"Resultado: {result}")

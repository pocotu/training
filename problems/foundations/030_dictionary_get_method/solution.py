"""
Solution for Dictionary get() method
Problem ID: F030
"""

def get_value_safely(dictionary, key, default="Not Found"):
    """
    Gets a value from a dictionary safely using the get() method.
    """
    return dictionary.get(key, default)

def main():
    """
    Función principal para 030_dictionary_get_method
    """
    # Ejemplo de uso
    test_dict = {'name': 'Alice', 'age': 30}
    result = get_value_safely(test_dict, 'city', 'Unknown')
    print(f"Valor para 'city' con default: {result}")
    return result

if __name__ == "__main__":
    result = main()
    print(f"Resultado: {result}")

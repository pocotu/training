"""
Solution for Dictionary Comprehensions
Problem ID: F032
"""

def create_squared_dict(numbers):
    """
    Creates a dictionary with numbers as keys and their squares as values.
    """
    return {num: num ** 2 for num in numbers}

def main():
    """
    Función principal para 032_dictionary_comprehensions
    """
    # Ejemplo de uso
    test_numbers = [1, 2, 3, 4, 5]
    result = create_squared_dict(test_numbers)
    print(f"Diccionario de cuadrados: {result}")
    return result

if __name__ == "__main__":
    result = main()
    print(f"Resultado: {result}")

"""
Solution for Dictionary Creation
Problem ID: F010
"""

def create_dictionary():
    """
    Creates and returns a dictionary with keys 'name', 'age', and 'city'.
    """
    return {
        'name': 'John',
        'age': 25,
        'city': 'New York'
    }

def main():
    """
    Función principal para 010_dictionary_creation
    """
    result = create_dictionary()
    print(f"Diccionario creado: {result}")
    return result

if __name__ == "__main__":
    result = main()
    print(f"Resultado: {result}")

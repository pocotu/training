"""
Solution for String join() method
Problem ID: F036
"""

def join_strings(strings, separator):
    """
    Joins a list of strings with a separator using the join() method.
    """
    return separator.join(strings)

def main():
    """
    Función principal para 036_string_join_method
    """
    # Ejemplo de uso
    test_strings = ['apple', 'banana', 'cherry']
    result = join_strings(test_strings, ', ')
    print(f"Strings unidas: '{result}'")
    return result

if __name__ == "__main__":
    result = main()
    print(f"Resultado: {result}")

"""
Solution for String Length
Problem ID: F005
"""

def get_string_length(text):
    """
    Returns the length of a string.
    """
    return len(text)

def main():
    """
    Función principal para 005_string_length
    """
    test_string = "Python Programming"
    result = get_string_length(test_string)
    print(f"Longitud de '{test_string}': {result}")
    return result

if __name__ == "__main__":
    result = main()
    print(f"Resultado: {result}")

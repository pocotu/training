"""
Solution for String Slicing
Problem ID: F006
"""

def get_substring(s, start, end):
    """
    Returns a substring from start to end-1.
    """
    return s[start:end]


def main():
    """
    Función principal para 006_string_slicing
    """
    # Ejemplo de uso
    test_string = "Hello, World!"
    result = get_substring(test_string, 7, 12)
    print(f"Substring de '{test_string}' desde 7 hasta 12: '{result}'")
    return result

if __name__ == "__main__":
    result = main()
    print(f"Resultado: {result}")

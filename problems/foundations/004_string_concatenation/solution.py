"""
Solution for String Concatenation
Problem ID: F004
"""

def concatenate_strings(str1, str2):
    """
    Concatenates two strings with a space between them.
    """
    return str1 + " " + str2

def main():
    """
    Función principal para 004_string_concatenation
    """
    result = concatenate_strings("Hello", "World")
    print(f"Strings concatenadas: '{result}'")
    return result

if __name__ == "__main__":
    result = main()
    print(f"Resultado: {result}")

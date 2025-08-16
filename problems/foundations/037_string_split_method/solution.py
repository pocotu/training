"""
Solution for String split() method
Problem ID: F037
"""

def split_string(text, separator):
    """
    Splits a string into a list using the split() method.
    """
    return text.split(separator)

def main():
    """
    Función principal para 037_string_split_method
    """
    # Ejemplo de uso
    test_text = "apple,banana,cherry"
    result = split_string(test_text, ',')
    print(f"String dividida: {result}")
    return result

if __name__ == "__main__":
    result = main()
    print(f"Resultado: {result}")

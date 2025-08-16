"""
Solution for Count Vowels
Problem ID: F025
"""

def count_vowels(s):
    """
    Counts the number of vowels in a string.
    """
    vowels = 'aeiouAEIOU'
    return sum(1 for char in s if char in vowels)

def main():
    """
    Función principal para 025_count_vowels
    """
    # Ejemplo de uso
    test_string = "hello world"
    result = count_vowels(test_string)
    print(f"Vocales en '{test_string}': {result}")
    return result

if __name__ == "__main__":
    result = main()
    print(f"Resultado: {result}")

"""
Solution for Anagram Check
Problem ID: F057
"""

def are_anagrams(str1, str2):
    """
    Checks if two strings are anagrams.
    Args:
        str1 (str): first string
        str2 (str): second string
    Returns:
        bool: True if anagrams, False otherwise
    """
    # Normalizar strings: minúsculas, remover espacios
    str1 = str1.lower().replace(" ", "")
    str2 = str2.lower().replace(" ", "")
    
    # Si tienen diferente longitud, no pueden ser anagramas
    if len(str1) != len(str2):
        return False
    
    # Comparar caracteres ordenados
    return sorted(str1) == sorted(str2)

def main():
    """
    Función principal para 057_anagram_check
    """
    # Ejemplos de uso
    test_cases = [
        ("listen", "silent"),
        ("evil", "vile"),
        ("hello", "bello"),
        ("anagram", "nagaram"),
        ("rat", "car"),
        ("The Eyes", "They See")
    ]
    
    for str1, str2 in test_cases:
        result = are_anagrams(str1, str2)
        print(f"'{str1}' y '{str2}' son anagramas: {result}")
    
    return are_anagrams("listen", "silent")

if __name__ == "__main__":
    result = main()
    print(f"Resultado: {result}")

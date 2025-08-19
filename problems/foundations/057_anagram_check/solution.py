"""
Solution for Anagram Check
Problem ID: F057
"""

def are_anagrams(str1, str2):
    # TODO: Implement your solution here
    pass

def main():
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

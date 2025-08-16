"""
Solution for String Reversal Methods
Problem ID: F062
"""

def reverse_with_slicing(text):
    """
    Reverses a string using slicing.
    Args:
        text (str): string to reverse
    Returns:
        str: reversed string
    """
    return text[::-1]

def reverse_with_loop(text):
    """
    Reverses a string using a loop.
    Args:
        text (str): string to reverse
    Returns:
        str: reversed string
    """
    result = ""
    for char in text:
        result = char + result
    return result

def reverse_with_recursion(text):
    """
    Reverses a string using recursion.
    Args:
        text (str): string to reverse
    Returns:
        str: reversed string
    """
    if len(text) <= 1:
        return text
    return text[-1] + reverse_with_recursion(text[:-1])

def main():
    """
    Función principal para 062_string_reversal_methods
    """
    test_string = "Hello World!"
    
    print(f"Original string: '{test_string}'")
    print(f"Slicing method: '{reverse_with_slicing(test_string)}'")
    print(f"Loop method:    '{reverse_with_loop(test_string)}'")
    print(f"Recursion:      '{reverse_with_recursion(test_string)}'")
    
    return reverse_with_slicing(test_string)

if __name__ == "__main__":
    result = main()
    print(f"Resultado: {result}")

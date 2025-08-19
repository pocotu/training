"""
Solution for Text Processing Functions
Problem ID: F085
"""

def count_characters(text):
    """
    Counts characters in text, excluding spaces.
    Returns integer count of non-space characters.
    """
    # TODO: Implement your solution here
    pass

def reverse_words(sentence):
    """
    Reverses the order of words in a sentence.
    Returns string with words in reverse order.
    """
    # TODO: Implement your solution here
    pass

def capitalize_words(text):
    """
    Capitalizes the first letter of each word.
    Returns string with capitalized words.
    """
    # TODO: Implement your solution here
    pass

def main():
    # Ejemplo de uso
    text1 = "Hola mundo"
    text2 = "Hola mundo Python"
    text3 = "hola mundo python"
    
    print(f"Texto: '{text1}' -> Caracteres: {count_characters(text1)}")
    print(f"Texto: '{text2}' -> Invertido: '{reverse_words(text2)}'")
    print(f"Texto: '{text3}' -> Capitalizado: '{capitalize_words(text3)}'")
    
if __name__ == "__main__":
    result = main()
    print(f"Resultado final: {result}")

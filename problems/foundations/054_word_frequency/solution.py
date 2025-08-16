"""
Solution for Word Frequency
Problem ID: F054
"""

def word_frequency(text):
    """
    Counts the frequency of words in a text.
    Args:
        text (str): input text
    Returns:
        dict: dictionary with word frequencies
    """
    # Limpiar texto: minúsculas, dividir por espacios, remover puntuación
    import re
    words = re.findall(r'\b\w+\b', text.lower())
    
    frequency = {}
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1
    
    return frequency

def main():
    """
    Función principal para 054_word_frequency
    """
    # Ejemplo de uso
    test_text = "hello world hello python world"
    result = word_frequency(test_text)
    print(f"Texto: '{test_text}'")
    print(f"Frecuencias: {result}")
    
    # Ejemplo más complejo
    complex_text = "The quick brown fox jumps over the lazy dog. The dog was really lazy!"
    complex_result = word_frequency(complex_text)
    print(f"\nTexto complejo: '{complex_text}'")
    print(f"Frecuencias: {complex_result}")
    
    return result

if __name__ == "__main__":
    result = main()
    print(f"Resultado: {result}")

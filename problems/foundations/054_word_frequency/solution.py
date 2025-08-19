"""
Solution for Word Frequency
Problem ID: F054
"""

def word_frequency(text):
    # TODO: Implement your solution here
    pass

def main():
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

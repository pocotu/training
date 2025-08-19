"""
Solution for Word Counter
Problem ID: F066
"""

def count_words(text):
    # TODO: Implement your solution here
    pass

def main():
    # Ejemplos de uso
    test_texts = [
        "Hello world hello python world",
        "The quick brown fox jumps over the lazy dog",
        "Python is great Python is fun",
        "",
        "One word"
    ]
    
    for text in test_texts:
        result = count_words(text)
        print(f"Text: '{text}'")
        print(f"Results: {result}\n")
    
    return count_words("Hello world hello python world")

if __name__ == "__main__":
    result = main()
    print(f"Resultado: {result}")

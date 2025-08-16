"""
Solution for Word Counter
Problem ID: F066
"""

def count_words(text):
    """
    Counts words in a text.
    Args:
        text (str): text to analyze
    Returns:
        dict: dictionary with word count statistics
    """
    if not text or not text.strip():
        return {
            'total_words': 0,
            'unique_words': 0,
            'word_frequency': {},
            'average_word_length': 0
        }
    
    # Clean and split text into words
    import re
    words = re.findall(r'\b\w+\b', text.lower())
    
    # Count word frequencies
    word_frequency = {}
    for word in words:
        word_frequency[word] = word_frequency.get(word, 0) + 1
    
    # Calculate statistics
    total_words = len(words)
    unique_words = len(word_frequency)
    average_length = sum(len(word) for word in words) / total_words if words else 0
    
    return {
        'total_words': total_words,
        'unique_words': unique_words,
        'word_frequency': word_frequency,
        'average_word_length': round(average_length, 1)
    }

def main():
    """
    Función principal para 066_word_counter
    """
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

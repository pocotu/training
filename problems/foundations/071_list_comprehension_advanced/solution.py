"""
Solution for List Comprehension Advanced
Problem ID: F071
"""

def filter_and_square(numbers):
    """
    Filters even numbers and squares them using list comprehension.
    Args:
        numbers (list): list of integers
    Returns:
        list: squared even numbers
    """
    return [num ** 2 for num in numbers if num % 2 == 0]

def nested_multiplication(matrix):
    """
    Multiplies all elements in a 2D matrix by 2 using nested comprehension.
    Args:
        matrix (list): 2D matrix (list of lists)
    Returns:
        list: new matrix with all elements multiplied by 2
    """
    return [[element * 2 for element in row] for row in matrix]

def conditional_transform(words):
    """
    Transforms words based on length: uppercase if even length, lowercase if odd.
    Args:
        words (list): list of strings
    Returns:
        list: transformed strings
    """
    return [word.upper() if len(word) % 2 == 0 else word.lower() for word in words]

def main():
    """
    Función principal para 071_list_comprehension_advanced
    """
    # Ejemplos de uso
    print("List Comprehension Advanced Examples:")
    
    numbers = [1, 2, 3, 4, 5, 6, 7, 8]
    filtered = filter_and_square(numbers)
    print(f"Filter and square {numbers}: {filtered}")
    
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    doubled = nested_multiplication(matrix)
    print(f"Matrix doubled: {doubled}")
    
    words = ["hello", "world", "python", "code", "test"]
    transformed = conditional_transform(words)
    print(f"Conditional transform {words}: {transformed}")
    
    return filtered

if __name__ == "__main__":
    result = main()
    print(f"Resultado: {result}")

"""
Solution for List Comprehension Advanced
Problem ID: F071
"""

def filter_and_square(numbers):
    # TODO: Implement your solution here
    pass

def nested_multiplication(matrix):
    # TODO: Implement your solution here
    pass

def conditional_transform(words):
    # TODO: Implement your solution here
    pass

def main():
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

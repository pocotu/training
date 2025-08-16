"""
Solution for List Comprehensions
Problem ID: F026
"""

def square_numbers(numbers):
    """
    Returns a list of squared numbers using list comprehension.
    """
    return [num ** 2 for num in numbers]

def main():
    """
    Función principal para 026_list_comprehensions
    """
    # Ejemplo de uso
    test_list = [1, 2, 3, 4, 5]
    result = square_numbers(test_list)
    print(f"Cuadrados de {test_list}: {result}")
    return result

if __name__ == "__main__":
    result = main()
    print(f"Resultado: {result}")

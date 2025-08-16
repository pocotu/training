"""
Solution for filter() function
Problem ID: F040
"""

def filter_even_numbers(numbers):
    """
    Uses filter() function to get only even numbers from a list.
    """
    return list(filter(lambda x: x % 2 == 0, numbers))

def main():
    """
    Función principal para 040_filter_function
    """
    # Ejemplo de uso
    test_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = filter_even_numbers(test_numbers)
    print(f"Números pares usando filter(): {result}")
    return result

if __name__ == "__main__":
    result = main()
    print(f"Resultado: {result}")

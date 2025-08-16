"""
Solution for map() function
Problem ID: F039
"""

def square_list(numbers):
    """
    Uses map() function to square all numbers in a list.
    """
    return list(map(lambda x: x ** 2, numbers))

def main():
    """
    Función principal para 039_map_function
    """
    # Ejemplo de uso
    test_numbers = [1, 2, 3, 4, 5]
    result = square_list(test_numbers)
    print(f"Cuadrados usando map(): {result}")
    return result

if __name__ == "__main__":
    result = main()
    print(f"Resultado: {result}")

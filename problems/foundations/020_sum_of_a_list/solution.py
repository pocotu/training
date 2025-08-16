"""
Solution for Sum of a List
Problem ID: F020
"""

def sum_list(numbers):
    """
    Returns the sum of all numbers in a list.
    """
    return sum(numbers)

def main():
    """
    Función principal para 020_sum_of_a_list
    """
    # Ejemplo de uso
    test_list = [1, 2, 3, 4, 5]
    result = sum_list(test_list)
    print(f"Suma de {test_list}: {result}")
    return result

if __name__ == "__main__":
    result = main()
    print(f"Resultado: {result}")

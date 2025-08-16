"""
Solution for For Loop
Problem ID: F013
"""

def sum_list(numbers):
    """
    Sums all numbers in a list using a for loop.
    """
    total = 0
    for num in numbers:
        total += num
    return total

def main():
    """
    Función principal para 013_for_loop
    """
    # Ejemplo de uso
    test_list = [1, 2, 3, 4, 5]
    result = sum_list(test_list)
    print(f"Suma de {test_list}: {result}")
    return result

if __name__ == "__main__":
    result = main()
    print(f"Resultado: {result}")

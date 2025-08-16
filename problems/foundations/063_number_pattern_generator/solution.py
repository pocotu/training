"""
Solution for Number Pattern Generator
Problem ID: F063
"""

def generate_pattern(n):
    """
    Generates a number pattern based on the input.
    Creates a triangle pattern like:
    1
    12
    123
    Args:
        n (int): number of rows
    Returns:
        list: list of strings representing the pattern
    """
    pattern = []
    for i in range(1, n + 1):
        row = ""
        for j in range(1, i + 1):
            row += str(j)
        pattern.append(row)
    return pattern

def main():
    """
    Función principal para 063_number_pattern_generator
    """
    # Ejemplo de uso
    n = 5
    result = generate_pattern(n)
    
    print(f"Pattern for n = {n}:")
    for row in result:
        print(row)
    
    return result

if __name__ == "__main__":
    result = main()
    print(f"Resultado: {result}")

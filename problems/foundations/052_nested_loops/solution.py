"""
Solution for Nested Loops
Problem ID: F052
"""

def multiplication_table(n):
    """
    Generates a multiplication table up to n.
    Args:
        n (int): size of the table
    Returns:
        list: list of lists representing the multiplication table
    """
    table = []
    for i in range(1, n + 1):
        row = []
        for j in range(1, n + 1):
            row.append(i * j)
        table.append(row)
    return table

def main():
    """
    Función principal para 052_nested_loops
    """
    # Ejemplo de uso
    result = multiplication_table(3)
    print(f"Tabla de multiplicación 3x3: {result}")
    
    # Mostrar de forma más legible
    for i, row in enumerate(result, 1):
        print(f"Fila {i}: {row}")
    
    return result

if __name__ == "__main__":
    result = main()
    print(f"Resultado: {result}")

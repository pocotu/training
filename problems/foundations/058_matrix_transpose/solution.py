"""
Solution for Matrix Transpose
Problem ID: F058
"""

def transpose_matrix(matrix):
    """
    Transposes a matrix (rows become columns).
    Args:
        matrix (list): list of lists representing a matrix
    Returns:
        list: transposed matrix
    """
    if not matrix or not matrix[0]:
        return []
    
    rows = len(matrix)
    cols = len(matrix[0])
    
    # Crear matriz transpuesta
    transposed = []
    for j in range(cols):
        new_row = []
        for i in range(rows):
            new_row.append(matrix[i][j])
        transposed.append(new_row)
    
    return transposed

def main():
    """
    Función principal para 058_matrix_transpose
    """
    # Ejemplo de uso
    test_matrix = [
        [1, 2, 3],
        [4, 5, 6]
    ]
    
    result = transpose_matrix(test_matrix)
    print(f"Matriz original:")
    for row in test_matrix:
        print(f"  {row}")
    
    print(f"Matriz transpuesta:")
    for row in result:
        print(f"  {row}")
    
    # Ejemplo cuadrada
    square_matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    
    square_result = transpose_matrix(square_matrix)
    print(f"\nMatriz cuadrada original:")
    for row in square_matrix:
        print(f"  {row}")
    
    print(f"Matriz cuadrada transpuesta:")
    for row in square_result:
        print(f"  {row}")
    
    return result

if __name__ == "__main__":
    result = main()
    print(f"Resultado: {result}")

"""
Solution for Matrix Operations
Problem ID: F068
"""

def matrix_add(matrix1, matrix2):
    """
    Adds two matrices.
    Args:
        matrix1 (list): first matrix
        matrix2 (list): second matrix
    Returns:
        list: sum of matrices
    """
    if not matrix1 or not matrix2:
        return []
    
    rows = len(matrix1)
    cols = len(matrix1[0])
    
    # Check if matrices have same dimensions
    if rows != len(matrix2) or cols != len(matrix2[0]):
        return []
    
    result = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)
    
    return result

def matrix_transpose(matrix):
    """
    Transposes a matrix.
    Args:
        matrix (list): matrix to transpose
    Returns:
        list: transposed matrix
    """
    if not matrix or not matrix[0]:
        return []
    
    rows = len(matrix)
    cols = len(matrix[0])
    
    transposed = []
    for j in range(cols):
        row = []
        for i in range(rows):
            row.append(matrix[i][j])
        transposed.append(row)
    
    return transposed

def matrix_diagonal_sum(matrix):
    """
    Calculates the sum of diagonal elements.
    Args:
        matrix (list): square matrix
    Returns:
        int: sum of diagonal elements
    """
    if not matrix or len(matrix) != len(matrix[0]):
        return 0
    
    diagonal_sum = 0
    for i in range(len(matrix)):
        diagonal_sum += matrix[i][i]
    
    return diagonal_sum

def main():
    """
    Función principal para 068_matrix_operations
    """
    # Ejemplos de uso
    matrix_a = [[1, 2, 3], [4, 5, 6]]
    matrix_b = [[7, 8, 9], [10, 11, 12]]
    
    print("Matrix A:")
    for row in matrix_a:
        print(row)
    
    print("\nMatrix B:")
    for row in matrix_b:
        print(row)
    
    # Addition
    sum_result = matrix_add(matrix_a, matrix_b)
    print(f"\nA + B:")
    for row in sum_result:
        print(row)
    
    # Transpose
    transpose_result = matrix_transpose(matrix_a)
    print(f"\nTranspose of A:")
    for row in transpose_result:
        print(row)
    
    # Diagonal sum (for square matrix)
    square_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    diagonal = matrix_diagonal_sum(square_matrix)
    print(f"\nDiagonal sum of square matrix: {diagonal}")
    
    return sum_result

if __name__ == "__main__":
    result = main()
    print(f"Resultado: {result}")

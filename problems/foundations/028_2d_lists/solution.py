"""
Solution for 2D Lists (Matrix Access)
Problem ID: F028
"""

def get_matrix_element(matrix, row, col):
    """
    Gets an element from a 2D list (matrix) at the specified row and column.
    """
    if 0 <= row < len(matrix) and 0 <= col < len(matrix[row]):
        return matrix[row][col]
    else:
        return None

def main():
    """
    Función principal para 028_2d_lists
    """
    # Ejemplo de uso
    test_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    result = get_matrix_element(test_matrix, 1, 2)
    print(f"Elemento en [1][2] de la matriz: {result}")
    return result

if __name__ == "__main__":
    result = main()
    print(f"Resultado: {result}")

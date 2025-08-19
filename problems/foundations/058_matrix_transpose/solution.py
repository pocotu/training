"""
Solution for Matrix Transpose
Problem ID: F058
"""

def transpose_matrix(matrix):
    # TODO: Implement your solution here
    pass

def main():
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

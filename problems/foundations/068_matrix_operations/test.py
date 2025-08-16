"""
Test cases for Matrix Operations (Problem F068)
"""

import pytest
from solution import matrix_add, matrix_transpose, matrix_diagonal_sum

def test_matrix_add():
    """Test matrix addition"""
    matrix1 = [[1, 2], [3, 4]]
    matrix2 = [[5, 6], [7, 8]]
    expected = [[6, 8], [10, 12]]
    assert matrix_add(matrix1, matrix2) == expected

def test_matrix_add_single():
    """Test matrix addition with single element"""
    matrix1 = [[5]]
    matrix2 = [[3]]
    expected = [[8]]
    assert matrix_add(matrix1, matrix2) == expected

def test_matrix_add_3x3():
    """Test matrix addition with 3x3 matrices"""
    matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    matrix2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
    expected = [[10, 10, 10], [10, 10, 10], [10, 10, 10]]
    assert matrix_add(matrix1, matrix2) == expected

def test_matrix_transpose():
    """Test matrix transpose"""
    matrix = [[1, 2, 3], [4, 5, 6]]
    expected = [[1, 4], [2, 5], [3, 6]]
    assert matrix_transpose(matrix) == expected

def test_matrix_transpose_square():
    """Test transpose of square matrix"""
    matrix = [[1, 2], [3, 4]]
    expected = [[1, 3], [2, 4]]
    assert matrix_transpose(matrix) == expected

def test_matrix_transpose_single():
    """Test transpose of single element matrix"""
    matrix = [[5]]
    expected = [[5]]
    assert matrix_transpose(matrix) == expected

def test_matrix_transpose_column():
    """Test transpose of column vector"""
    matrix = [[1], [2], [3]]
    expected = [[1, 2, 3]]
    assert matrix_transpose(matrix) == expected

def test_matrix_diagonal_sum():
    """Test diagonal sum"""
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    expected = 15  # 1 + 5 + 9
    assert matrix_diagonal_sum(matrix) == expected

def test_matrix_diagonal_sum_2x2():
    """Test diagonal sum of 2x2 matrix"""
    matrix = [[1, 2], [3, 4]]
    expected = 5  # 1 + 4
    assert matrix_diagonal_sum(matrix) == expected

def test_matrix_diagonal_sum_single():
    """Test diagonal sum of single element matrix"""
    matrix = [[42]]
    expected = 42
    assert matrix_diagonal_sum(matrix) == expected

def test_matrix_diagonal_sum_identity():
    """Test diagonal sum of identity matrix"""
    matrix = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    expected = 3  # 1 + 1 + 1
    assert matrix_diagonal_sum(matrix) == expected

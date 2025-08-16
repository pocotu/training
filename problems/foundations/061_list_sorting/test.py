"""
Test cases for List Sorting (Problem F061)
"""

import pytest
from solution import sort_list

def test_basic_sorting():
    """Test basic list sorting"""
    numbers = [64, 34, 25, 12, 22, 11, 90]
    expected = [11, 12, 22, 25, 34, 64, 90]
    assert sort_list(numbers) == expected

def test_small_list():
    """Test with small list"""
    numbers = [5, 2, 8, 1, 9]
    expected = [1, 2, 5, 8, 9]
    assert sort_list(numbers) == expected

def test_empty_list():
    """Test with empty list"""
    assert sort_list([]) == []

def test_single_element():
    """Test with single element"""
    assert sort_list([42]) == [42]

def test_already_sorted():
    """Test with already sorted list"""
    numbers = [1, 2, 3, 4, 5]
    expected = [1, 2, 3, 4, 5]
    assert sort_list(numbers) == expected

def test_reverse_sorted():
    """Test with reverse sorted list"""
    numbers = [5, 4, 3, 2, 1]
    expected = [1, 2, 3, 4, 5]
    assert sort_list(numbers) == expected

def test_negative_numbers():
    """Test with negative numbers"""
    numbers = [-3, -1, -5, 0, 2]
    expected = [-5, -3, -1, 0, 2]
    assert sort_list(numbers) == expected

def test_duplicates():
    """Test with duplicate numbers"""
    numbers = [3, 1, 4, 1, 5, 3]
    expected = [1, 1, 3, 3, 4, 5]
    assert sort_list(numbers) == expected

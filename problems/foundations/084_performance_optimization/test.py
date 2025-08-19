"""
Tests for Number Comparison Functions
Problem ID: F084
"""

import pytest
from solution import find_maximum, find_minimum, compare_numbers

def test_find_maximum_normal_list():
    """Test finding maximum in normal list"""
    result = find_maximum([5, 2, 8, 1, 9])
    assert result == 9

def test_find_maximum_single_element():
    """Test finding maximum in single element list"""
    result = find_maximum([42])
    assert result == 42

def test_find_maximum_empty_list():
    """Test finding maximum in empty list"""
    result = find_maximum([])
    assert result is None

def test_find_minimum_normal_list():
    """Test finding minimum in normal list"""
    result = find_minimum([5, 2, 8, 1, 9])
    assert result == 1

def test_find_minimum_single_element():
    """Test finding minimum in single element list"""
    result = find_minimum([42])
    assert result == 42

def test_find_minimum_empty_list():
    """Test finding minimum in empty list"""
    result = find_minimum([])
    assert result is None

def test_compare_numbers_first_greater():
    """Test comparing when first number is greater"""
    result = compare_numbers(5, 3)
    assert result == "5 es mayor que 3"

def test_compare_numbers_first_smaller():
    """Test comparing when first number is smaller"""
    result = compare_numbers(2, 7)
    assert result == "2 es menor que 7"

def test_compare_numbers_equal():
    """Test comparing when both numbers are equal"""
    result = compare_numbers(4, 4)
    assert result == "4 es igual a 4"

def test_find_maximum_with_negatives():
    """Test finding maximum with negative numbers"""
    result = find_maximum([-5, -2, -8, -1, -9])
    assert result == -1

def test_find_minimum_with_negatives():
    """Test finding minimum with negative numbers"""
    result = find_minimum([-5, -2, -8, -1, -9])
    assert result == -9

if __name__ == "__main__":
    pytest.main([__file__])

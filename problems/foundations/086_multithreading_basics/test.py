"""
Tests for List Operations and Processing
Problem ID: F086
"""

import pytest
from solution import combine_lists, group_by_length, flatten_nested_list

def test_combine_lists_equal_length():
    """Test combining lists of equal length"""
    result = combine_lists([1, 2, 3], ["a", "b", "c"])
    assert result == [1, "a", 2, "b", 3, "c"]

def test_combine_lists_first_longer():
    """Test combining when first list is longer"""
    result = combine_lists([1, 2, 3, 4], ["a", "b"])
    assert result == [1, "a", 2, "b", 3, 4]

def test_combine_lists_second_longer():
    """Test combining when second list is longer"""
    result = combine_lists([1, 2], ["a", "b", "c", "d"])
    assert result == [1, "a", 2, "b", "c", "d"]

def test_group_by_length_basic():
    """Test grouping words by length"""
    words = ["casa", "carro", "sol", "luna", "estrella"]
    result = group_by_length(words)
    expected = {3: ["sol"], 4: ["casa", "luna"], 5: ["carro"], 8: ["estrella"]}
    assert result == expected

def test_flatten_nested_list_basic():
    """Test flattening nested list"""
    nested = [[1, 2], [3, 4, 5], [6]]
    result = flatten_nested_list(nested)
    assert result == [1, 2, 3, 4, 5, 6]



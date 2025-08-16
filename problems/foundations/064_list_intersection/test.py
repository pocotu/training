"""
Test cases for List Intersection (Problem F064)
"""

import pytest
from solution import find_intersection

def test_basic_intersection():
    """Test basic intersection of two lists"""
    list1 = [1, 2, 3, 4]
    list2 = [3, 4, 5, 6]
    expected = [3, 4]
    assert find_intersection(list1, list2) == expected

def test_string_intersection():
    """Test intersection with strings"""
    list1 = ['a', 'b', 'c']
    list2 = ['b', 'c', 'd']
    expected = ['b', 'c']
    assert find_intersection(list1, list2) == expected

def test_with_duplicates():
    """Test intersection with duplicates"""
    list1 = [1, 2, 2, 3]
    list2 = [2, 3, 3, 4]
    expected = [2, 3]
    assert find_intersection(list1, list2) == expected

def test_no_intersection():
    """Test with no common elements"""
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    expected = []
    assert find_intersection(list1, list2) == expected

def test_empty_lists():
    """Test with empty lists"""
    assert find_intersection([], [1, 2, 3]) == []
    assert find_intersection([1, 2, 3], []) == []
    assert find_intersection([], []) == []

def test_identical_lists():
    """Test with identical lists"""
    list1 = [1, 2, 3]
    list2 = [1, 2, 3]
    expected = [1, 2, 3]
    assert find_intersection(list1, list2) == expected

def test_order_preservation():
    """Test that order from first list is preserved"""
    list1 = [3, 1, 4, 2]
    list2 = [1, 2, 3, 4]
    expected = [3, 1, 4, 2]
    assert find_intersection(list1, list2) == expected

def test_mixed_types():
    """Test with mixed data types"""
    list1 = [1, 'a', 2, 'b']
    list2 = ['b', 1, 'c', 3]
    expected = [1, 'b']
    assert find_intersection(list1, list2) == expected

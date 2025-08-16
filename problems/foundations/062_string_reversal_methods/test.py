"""
Test cases for String Reversal Methods (Problem F062)
"""

import pytest
from solution import reverse_with_slicing, reverse_with_loop, reverse_with_recursion

def test_basic_string():
    """Test basic string reversal"""
    text = "hello"
    expected = "olleh"
    assert reverse_with_slicing(text) == expected
    assert reverse_with_loop(text) == expected
    assert reverse_with_recursion(text) == expected

def test_python_string():
    """Test with Python string"""
    text = "Python"
    expected = "nohtyP"
    assert reverse_with_slicing(text) == expected
    assert reverse_with_loop(text) == expected
    assert reverse_with_recursion(text) == expected

def test_empty_string():
    """Test with empty string"""
    text = ""
    expected = ""
    assert reverse_with_slicing(text) == expected
    assert reverse_with_loop(text) == expected
    assert reverse_with_recursion(text) == expected

def test_single_character():
    """Test with single character"""
    text = "a"
    expected = "a"
    assert reverse_with_slicing(text) == expected
    assert reverse_with_loop(text) == expected
    assert reverse_with_recursion(text) == expected

def test_palindrome():
    """Test with palindrome"""
    text = "level"
    expected = "level"
    assert reverse_with_slicing(text) == expected
    assert reverse_with_loop(text) == expected
    assert reverse_with_recursion(text) == expected

def test_with_spaces():
    """Test with spaces"""
    text = "hello world"
    expected = "dlrow olleh"
    assert reverse_with_slicing(text) == expected
    assert reverse_with_loop(text) == expected
    assert reverse_with_recursion(text) == expected

def test_with_numbers():
    """Test with numbers"""
    text = "12345"
    expected = "54321"
    assert reverse_with_slicing(text) == expected
    assert reverse_with_loop(text) == expected
    assert reverse_with_recursion(text) == expected

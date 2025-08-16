"""
Test cases for Word Counter (Problem F066)
"""

import pytest
from solution import count_words

def test_basic_counting():
    """Test basic word counting"""
    text = "Hello world! Hello Python world."
    expected = {
        'hello': 2,
        'world': 2,
        'python': 1
    }
    assert count_words(text) == expected

def test_longer_text():
    """Test with longer text"""
    text = "The quick brown fox jumps over the lazy dog."
    expected = {
        'the': 2,
        'quick': 1,
        'brown': 1,
        'fox': 1,
        'jumps': 1,
        'over': 1,
        'lazy': 1,
        'dog': 1
    }
    assert count_words(text) == expected

def test_ignore_single_chars():
    """Test ignoring single character words"""
    text = "a I am happy"
    expected = {
        'am': 1,
        'happy': 1
    }
    assert count_words(text) == expected

def test_empty_string():
    """Test with empty string"""
    assert count_words("") == {}

def test_punctuation_handling():
    """Test handling of punctuation"""
    text = "Hello, world! How are you? I'm fine."
    expected = {
        'hello': 1,
        'world': 1,
        'how': 1,
        'are': 1,
        'you': 1,
        'fine': 1
    }
    assert count_words(text) == expected

def test_numbers_in_words():
    """Test words with numbers"""
    text = "Python3 is great! Version 3.9 rocks."
    expected = {
        'python3': 1,
        'is': 1,
        'great': 1,
        'version': 1,
        'rocks': 1
    }
    assert count_words(text) == expected

def test_case_insensitive():
    """Test case insensitive counting"""
    text = "Python python PYTHON PyThOn"
    expected = {
        'python': 4
    }
    assert count_words(text) == expected

def test_multiple_spaces():
    """Test with multiple spaces"""
    text = "hello    world  python   programming"
    expected = {
        'hello': 1,
        'world': 1,
        'python': 1,
        'programming': 1
    }
    assert count_words(text) == expected

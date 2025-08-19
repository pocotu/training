"""
Tests for Text Processing Functions
Problem ID: F085
"""

import pytest
from solution import count_characters, reverse_words, capitalize_words

def test_count_characters_basic():
    """Test counting characters excluding spaces"""
    result = count_characters("Hola mundo")
    assert result == 9  # H-o-l-a-m-u-n-d-o = 9 characters

def test_count_characters_no_spaces():
    """Test counting characters with no spaces"""
    result = count_characters("Python")
    assert result == 6

def test_count_characters_only_spaces():
    """Test counting characters with only spaces"""
    result = count_characters("   ")
    assert result == 0

def test_count_characters_empty():
    """Test counting characters in empty string"""
    result = count_characters("")
    assert result == 0

def test_reverse_words_basic():
    """Test reversing word order in sentence"""
    result = reverse_words("Hola mundo Python")
    assert result == "Python mundo Hola"

def test_reverse_words_single_word():
    """Test reversing single word"""
    result = reverse_words("Python")
    assert result == "Python"

def test_reverse_words_two_words():
    """Test reversing two words"""
    result = reverse_words("Hola mundo")
    assert result == "mundo Hola"

def test_capitalize_words_basic():
    """Test capitalizing words"""
    result = capitalize_words("hola mundo python")
    assert result == "Hola Mundo Python"

def test_capitalize_words_already_capitalized():
    """Test capitalizing already capitalized words"""
    result = capitalize_words("Hola Mundo Python")
    assert result == "Hola Mundo Python"

def test_capitalize_words_mixed_case():
    """Test capitalizing mixed case words"""
    result = capitalize_words("hOLA mUNDO pYTHON")
    assert result == "HOLA MUNDO PYTHON"

def test_capitalize_words_single_word():
    """Test capitalizing single word"""
    result = capitalize_words("python")
    assert result == "Python"

if __name__ == "__main__":
    pytest.main([__file__])

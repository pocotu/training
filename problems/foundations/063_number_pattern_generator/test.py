"""
Test cases for Number Pattern Generator (Problem F063)
"""

import pytest
from solution import generate_pattern

def test_pattern_n3():
    """Test pattern for n=3"""
    expected = [
        "  1  ",
        " 1 2 ",
        "1 2 3"
    ]
    assert generate_pattern(3) == expected

def test_pattern_n4():
    """Test pattern for n=4"""
    expected = [
        "   1   ",
        "  1 2  ",
        " 1 2 3 ",
        "1 2 3 4"
    ]
    assert generate_pattern(4) == expected

def test_pattern_n1():
    """Test pattern for n=1"""
    expected = ["1"]
    assert generate_pattern(1) == expected

def test_pattern_n2():
    """Test pattern for n=2"""
    expected = [
        " 1 ",
        "1 2"
    ]
    assert generate_pattern(2) == expected

def test_pattern_n5():
    """Test pattern for n=5"""
    expected = [
        "    1    ",
        "   1 2   ",
        "  1 2 3  ",
        " 1 2 3 4 ",
        "1 2 3 4 5"
    ]
    assert generate_pattern(5) == expected

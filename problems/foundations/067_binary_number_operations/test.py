"""
Test cases for Binary Number Operations (Problem F067)
"""

import pytest
from solution import decimal_to_binary, binary_to_decimal, binary_add

def test_decimal_to_binary():
    """Test decimal to binary conversion"""
    assert decimal_to_binary(10) == "1010"
    assert decimal_to_binary(7) == "111"
    assert decimal_to_binary(0) == "0"
    assert decimal_to_binary(1) == "1"
    assert decimal_to_binary(15) == "1111"
    assert decimal_to_binary(8) == "1000"

def test_binary_to_decimal():
    """Test binary to decimal conversion"""
    assert binary_to_decimal("1010") == 10
    assert binary_to_decimal("111") == 7
    assert binary_to_decimal("0") == 0
    assert binary_to_decimal("1") == 1
    assert binary_to_decimal("1111") == 15
    assert binary_to_decimal("1000") == 8

def test_binary_add():
    """Test binary addition"""
    assert binary_add("1010", "111") == "10001"
    assert binary_add("101", "110") == "1011"
    assert binary_add("1", "1") == "10"
    assert binary_add("0", "0") == "0"
    assert binary_add("1111", "1") == "10000"

def test_conversions_consistency():
    """Test that conversions are consistent"""
    test_numbers = [0, 1, 7, 10, 15, 31, 63, 127]
    
    for num in test_numbers:
        binary = decimal_to_binary(num)
        back_to_decimal = binary_to_decimal(binary)
        assert back_to_decimal == num

def test_addition_consistency():
    """Test binary addition consistency with decimal"""
    test_cases = [
        (5, 3),  # 101 + 11 = 1000 (8)
        (12, 7), # 1100 + 111 = 10011 (19)
        (1, 1),  # 1 + 1 = 10 (2)
        (0, 5),  # 0 + 101 = 101 (5)
    ]
    
    for a, b in test_cases:
        bin_a = decimal_to_binary(a)
        bin_b = decimal_to_binary(b)
        bin_result = binary_add(bin_a, bin_b)
        decimal_result = binary_to_decimal(bin_result)
        assert decimal_result == a + b

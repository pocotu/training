"""
Tests for Debug and Error Handling Functions  
Problem ID: F091
"""

import pytest
from solution import debug_print, safe_divide, validate_input
import io
import sys

def test_debug_print_info_level():
    """Test debug print with INFO level"""
    # Capture stdout to test print output
    captured_output = io.StringIO()
    sys.stdout = captured_output
    
    debug_print("Test message", "INFO")
    
    sys.stdout = sys.__stdout__  # Reset stdout
    output = captured_output.getvalue().strip()
    assert output == "[INFO] Test message"

def test_debug_print_error_level():
    """Test debug print with ERROR level"""
    captured_output = io.StringIO()
    sys.stdout = captured_output
    
    debug_print("Error occurred", "ERROR")
    
    sys.stdout = sys.__stdout__
    output = captured_output.getvalue().strip()
    assert output == "[ERROR] Error occurred"

def test_safe_divide_normal():
    """Test normal division"""
    result = safe_divide(10, 2)
    assert result == 5.0

def test_safe_divide_by_zero():
    """Test division by zero"""
    result = safe_divide(10, 0)
    assert result is None

def test_safe_divide_negative():
    """Test division with negative numbers"""
    result = safe_divide(-10, 2)
    assert result == -5.0

def test_validate_input_valid_int():
    """Test validating valid integer string"""
    result = validate_input("123", "int")
    assert result is True

def test_validate_input_invalid_int():
    """Test validating invalid integer string"""
    result = validate_input("abc", "int")
    assert result is False

def test_validate_input_valid_float():
    """Test validating valid float string"""
    result = validate_input("123.45", "float")
    assert result is True

def test_validate_input_valid_str():
    """Test validating string type"""
    result = validate_input("hello", "str")
    assert result is True

if __name__ == "__main__":
    pytest.main([__file__])

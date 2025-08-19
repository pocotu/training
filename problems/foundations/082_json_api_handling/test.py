"""
Tests for Dictionary Data Processing
Problem ID: F082
"""

import pytest
from solution import process_user_data

def test_process_simple_user_data():
    """Test processing user data dictionary with two users"""
    data = {
        "users": [
            {"name": "Ana", "age": 25},
            {"name": "Bob", "age": 30}
        ]
    }
    result = process_user_data(data)
    assert result["total_users"] == 2
    assert result["average_age"] == 27.5
    assert result["names"] == ["Ana", "Bob"]

def test_process_single_user():
    """Test processing single user data"""
    data = {
        "users": [
            {"name": "Carlos", "age": 35}
        ]
    }
    result = process_user_data(data)
    assert result["total_users"] == 1
    assert result["average_age"] == 35.0
    assert result["names"] == ["Carlos"]

def test_process_empty_users():
    """Test processing empty user list"""
    data = {"users": []}
    result = process_user_data(data)
    assert result["total_users"] == 0
    assert result["average_age"] == 0
    assert result["names"] == []

def test_process_multiple_users():
    """Test processing multiple users with different ages"""
    data = {
        "users": [
            {"name": "Diana", "age": 20},
            {"name": "Eva", "age": 30},
            {"name": "Felix", "age": 40}
        ]
    }
    result = process_user_data(data)
    assert result["total_users"] == 3
    assert result["average_age"] == 30.0
    assert result["names"] == ["Diana", "Eva", "Felix"]

def test_process_users_same_age():
    """Test processing users with same age"""
    data = {
        "users": [
            {"name": "Gabriel", "age": 25},
            {"name": "Helena", "age": 25}
        ]
    }
    result = process_user_data(data)
    assert result["total_users"] == 2
    assert result["average_age"] == 25.0
    assert result["names"] == ["Gabriel", "Helena"]

def test_process_users_decimal_average():
    """Test processing users resulting in decimal average"""
    data = {
        "users": [
            {"name": "Ivan", "age": 23},
            {"name": "Julia", "age": 27},
            {"name": "Klaus", "age": 31}
        ]
    }
    result = process_user_data(data)
    assert result["total_users"] == 3
    assert abs(result["average_age"] - 27.0) < 0.01
    assert result["names"] == ["Ivan", "Julia", "Klaus"]

if __name__ == "__main__":
    pytest.main([__file__])

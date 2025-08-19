"""
Tests for Data Storage Using Lists
Problem ID: F083
"""

import pytest
from solution import create_user_list, add_user, get_users_by_age

def test_create_user_list():
    """Test creating empty user list"""
    result = create_user_list()
    assert result == []
    assert isinstance(result, list)

def test_add_single_user():
    """Test adding single user"""
    users = create_user_list()
    result = add_user(users, "Ana García", "ana@email.com", 28)
    
    assert len(result) == 1
    assert result[0]["id"] == 1
    assert result[0]["name"] == "Ana García"
    assert result[0]["email"] == "ana@email.com"
    assert result[0]["age"] == 28

def test_add_multiple_users():
    """Test adding multiple users with auto-incremented IDs"""
    users = create_user_list()
    users = add_user(users, "Ana", "ana@email.com", 28)
    users = add_user(users, "Bob", "bob@email.com", 22)
    users = add_user(users, "Carlos", "carlos@email.com", 35)
    
    assert len(users) == 3
    assert users[0]["id"] == 1
    assert users[1]["id"] == 2
    assert users[2]["id"] == 3

def test_get_users_by_age_filter():
    """Test filtering users by minimum age"""
    users = [
        {"id": 1, "name": "Ana", "email": "ana@email.com", "age": 28},
        {"id": 2, "name": "Bob", "email": "bob@email.com", "age": 22},
        {"id": 3, "name": "Carlos", "email": "carlos@email.com", "age": 35}
    ]
    
    result = get_users_by_age(users, 25)
    assert len(result) == 2
    assert result[0]["name"] == "Ana"
    assert result[1]["name"] == "Carlos"

def test_get_users_by_age_no_match():
    """Test filtering with no matching users"""
    users = [
        {"id": 1, "name": "Ana", "email": "ana@email.com", "age": 20},
        {"id": 2, "name": "Bob", "email": "bob@email.com", "age": 22}
    ]
    
    result = get_users_by_age(users, 30)
    assert result == []

def test_get_users_by_age_all_match():
    """Test filtering where all users match"""
    users = [
        {"id": 1, "name": "Ana", "email": "ana@email.com", "age": 28},
        {"id": 2, "name": "Bob", "email": "bob@email.com", "age": 30}
    ]
    
    result = get_users_by_age(users, 25)
    assert len(result) == 2
    assert result == users

if __name__ == "__main__":
    pytest.main([__file__])

"""
Test cases for Grade Calculator (Problem F065)
"""

import pytest
from solution import calculate_grade

def test_all_high_grades():
    """Test with all high grades"""
    grades = [85, 92, 78, 90, 88]
    result = calculate_grade(grades)
    
    assert result['average'] == 86.6
    assert result['letter_grade'] == 'B'
    assert result['highest'] == 92
    assert result['lowest'] == 78
    assert result['passing'] == 5

def test_mixed_grades():
    """Test with mixed grades"""
    grades = [45, 67, 89, 52]
    result = calculate_grade(grades)
    
    assert result['average'] == 63.25
    assert result['letter_grade'] == 'D'
    assert result['highest'] == 89
    assert result['lowest'] == 45
    assert result['passing'] == 2

def test_all_failing():
    """Test with all failing grades"""
    grades = [45, 32, 58, 41]
    result = calculate_grade(grades)
    
    assert result['average'] == 44.0
    assert result['letter_grade'] == 'F'
    assert result['highest'] == 58
    assert result['lowest'] == 32
    assert result['passing'] == 0

def test_single_grade():
    """Test with single grade"""
    grades = [95]
    result = calculate_grade(grades)
    
    assert result['average'] == 95.0
    assert result['letter_grade'] == 'A'
    assert result['highest'] == 95
    assert result['lowest'] == 95
    assert result['passing'] == 1

def test_boundary_grades():
    """Test with boundary grades"""
    grades = [90, 80, 70, 60, 59]
    result = calculate_grade(grades)
    
    assert result['average'] == 71.8
    assert result['letter_grade'] == 'C'
    assert result['highest'] == 90
    assert result['lowest'] == 59
    assert result['passing'] == 4

def test_perfect_scores():
    """Test with perfect scores"""
    grades = [100, 100, 100]
    result = calculate_grade(grades)
    
    assert result['average'] == 100.0
    assert result['letter_grade'] == 'A'
    assert result['highest'] == 100
    assert result['lowest'] == 100
    assert result['passing'] == 3

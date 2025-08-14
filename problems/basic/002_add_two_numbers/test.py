"""
Test cases for Add Two Numbers problem
Problem ID: 002
"""

import pytest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from solution import ListNode, add_two_numbers, list_to_array, array_to_list

class TestAddTwoNumbers:
    """Test class for Add Two Numbers problem"""
    
    def test_example_1(self):
        """Test example 1 from LeetCode"""
        # l1 = [2,4,3], l2 = [5,6,4] -> [7,0,8]
        l1 = array_to_list([2, 4, 3])
        l2 = array_to_list([5, 6, 4])
        result = add_two_numbers(l1, l2)
        assert list_to_array(result) == [7, 0, 8]
    
    def test_example_2(self):
        """Test example 2 from LeetCode"""
        # l1 = [0], l2 = [0] -> [0]
        l1 = array_to_list([0])
        l2 = array_to_list([0])
        result = add_two_numbers(l1, l2)
        assert list_to_array(result) == [0]
    
    def test_example_3(self):
        """Test example 3 from LeetCode"""
        # l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9] -> [8,9,9,9,0,0,0,1]
        l1 = array_to_list([9, 9, 9, 9, 9, 9, 9])
        l2 = array_to_list([9, 9, 9, 9])
        result = add_two_numbers(l1, l2)
        assert list_to_array(result) == [8, 9, 9, 9, 0, 0, 0, 1]
    
    def test_different_lengths(self):
        """Test lists of different lengths"""
        # l1 = [9,9], l2 = [1] -> [0,0,1]
        l1 = array_to_list([9, 9])
        l2 = array_to_list([1])
        result = add_two_numbers(l1, l2)
        assert list_to_array(result) == [0, 0, 1]
        
        # l1 = [1], l2 = [9,9] -> [0,0,1]
        l1 = array_to_list([1])
        l2 = array_to_list([9, 9])
        result = add_two_numbers(l1, l2)
        assert list_to_array(result) == [0, 0, 1]
    
    def test_single_digits(self):
        """Test single digit addition"""
        # l1 = [5], l2 = [5] -> [0,1]
        l1 = array_to_list([5])
        l2 = array_to_list([5])
        result = add_two_numbers(l1, l2)
        assert list_to_array(result) == [0, 1]
        
        # l1 = [1], l2 = [2] -> [3]
        l1 = array_to_list([1])
        l2 = array_to_list([2])
        result = add_two_numbers(l1, l2)
        assert list_to_array(result) == [3]
    
    def test_carry_propagation(self):
        """Test carry propagation through multiple digits"""
        # l1 = [9,9,9], l2 = [1] -> [0,0,0,1]
        l1 = array_to_list([9, 9, 9])
        l2 = array_to_list([1])
        result = add_two_numbers(l1, l2)
        assert list_to_array(result) == [0, 0, 0, 1]
    
    def test_edge_cases(self):
        """Test edge cases"""
        # Maximum single digit
        l1 = array_to_list([9])
        l2 = array_to_list([9])
        result = add_two_numbers(l1, l2)
        assert list_to_array(result) == [8, 1]
        
        # No carry needed
        l1 = array_to_list([1, 2, 3])
        l2 = array_to_list([4, 5, 6])
        result = add_two_numbers(l1, l2)
        assert list_to_array(result) == [5, 7, 9]

if __name__ == "__main__":
    pytest.main([__file__, "-v"])

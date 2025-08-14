"""
Test cases for Add Two Numbers problem
Problem ID: 102
"""

import pytest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from solution import add_two_numbers, ListNode

class TestAddTwoNumbers:
    """Test class for Add Two Numbers problem"""
    
    def create_linked_list(self, digits):
        """Helper to create linked list from list of digits"""
        if not digits:
            return None
        
        head = ListNode(digits[0])
        current = head
        for digit in digits[1:]:
            current.next = ListNode(digit)
            current = current.next
        return head
    
    def linked_list_to_array(self, head):
        """Helper to convert linked list to array"""
        result = []
        while head:
            result.append(head.val)
            head = head.next
        return result
    
    def test_example_1(self):
        """Test example 1 from LeetCode"""
        # 342 + 465 = 807
        l1 = self.create_linked_list([2, 4, 3])  # represents 342
        l2 = self.create_linked_list([5, 6, 4])  # represents 465
        result = add_two_numbers(l1, l2)
        expected = [7, 0, 8]  # represents 807
        assert self.linked_list_to_array(result) == expected
    
    def test_example_2(self):
        """Test example 2 from LeetCode"""
        # 0 + 0 = 0
        l1 = self.create_linked_list([0])
        l2 = self.create_linked_list([0])
        result = add_two_numbers(l1, l2)
        expected = [0]
        assert self.linked_list_to_array(result) == expected
    
    def test_example_3(self):
        """Test example 3 from LeetCode"""
        # 9999999 + 9999 = 10009998
        l1 = self.create_linked_list([9,9,9,9,9,9,9])
        l2 = self.create_linked_list([9,9,9,9])
        result = add_two_numbers(l1, l2)
        expected = [8,9,9,9,0,0,0,1]
        assert self.linked_list_to_array(result) == expected
    
    def test_different_lengths(self):
        """Test numbers with different lengths"""
        # 99 + 1 = 100
        l1 = self.create_linked_list([9, 9])
        l2 = self.create_linked_list([1])
        result = add_two_numbers(l1, l2)
        expected = [0, 0, 1]
        assert self.linked_list_to_array(result) == expected
    
    def test_carry_propagation(self):
        """Test carry propagation"""
        # 999 + 1 = 1000
        l1 = self.create_linked_list([9, 9, 9])
        l2 = self.create_linked_list([1])
        result = add_two_numbers(l1, l2)
        expected = [0, 0, 0, 1]
        assert self.linked_list_to_array(result) == expected
    
    def test_single_digits(self):
        """Test single digit addition"""
        # 5 + 5 = 10
        l1 = self.create_linked_list([5])
        l2 = self.create_linked_list([5])
        result = add_two_numbers(l1, l2)
        expected = [0, 1]
        assert self.linked_list_to_array(result) == expected

if __name__ == "__main__":
    pytest.main([__file__, "-v"])

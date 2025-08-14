"""
Solution for Add Two Numbers
Problem ID: 102
LeetCode Problem: https://leetcode.com/problems/add-two-numbers/

You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.
"""

class ListNode:
    """Definition for singly-linked list."""
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def add_two_numbers(l1: ListNode, l2: ListNode) -> ListNode:
    """
    Add two numbers represented as linked lists.
    
    Args:
        l1: First number as linked list (reverse order)
        l2: Second number as linked list (reverse order)
        
    Returns:
        Sum as linked list (reverse order)
        
    Time Complexity: O(max(m,n))
    Space Complexity: O(max(m,n))
    """
    dummy_head = ListNode(0)
    current = dummy_head
    carry = 0
    
    while l1 or l2 or carry:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0
        
        total = val1 + val2 + carry
        carry = total // 10
        digit = total % 10
        
        current.next = ListNode(digit)
        current = current.next
        
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next
    
    return dummy_head.next

if __name__ == "__main__":
    # Create test case: 342 + 465 = 807
    # Represented as [2,4,3] + [5,6,4] = [7,0,8]
    
    # Create first number: 342 -> [2,4,3]
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)
    
    # Create second number: 465 -> [5,6,4]
    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)
    
    result = add_two_numbers(l1, l2)
    
    # Print result
    output = []
    while result:
        output.append(result.val)
        result = result.next
    
    print(f"Result: {output}")  # Should be [7,0,8]

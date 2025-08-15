"""
Solution for LeetCode Problem 21 - Merge Two Sorted Lists
Problem ID: 017

Approach: Iterative with dummy node
Time Complexity: O(n + m)
Space Complexity: O(1)
"""

class ListNode:
    """Definition for singly-linked list."""
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_two_lists(list1, list2):
    """
    Merge two sorted linked lists iteratively.
    
    Args:
        list1: ListNode - Head of first sorted linked list
        list2: ListNode - Head of second sorted linked list
        
    Returns:
        ListNode: Head of merged sorted linked list
    """
    # Create a dummy node to simplify the logic
    dummy = ListNode(0)
    current = dummy
    
    # Merge lists while both have nodes
    while list1 and list2:
        if list1.val <= list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next
    
    # Append remaining nodes (at most one list will have remaining nodes)
    current.next = list1 if list1 else list2
    
    return dummy.next

def merge_two_lists_recursive(list1, list2):
    """
    Merge two sorted linked lists recursively.
    
    Args:
        list1: ListNode - Head of first sorted linked list
        list2: ListNode - Head of second sorted linked list
        
    Returns:
        ListNode: Head of merged sorted linked list
    """
    # Base cases
    if not list1:
        return list2
    if not list2:
        return list1
    
    # Recursive case
    if list1.val <= list2.val:
        list1.next = merge_two_lists_recursive(list1.next, list2)
        return list1
    else:
        list2.next = merge_two_lists_recursive(list1, list2.next)
        return list2

# Helper functions for testing
def create_linked_list(values):
    """Create a linked list from a list of values."""
    if not values:
        return None
    
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def linked_list_to_list(head):
    """Convert a linked list to a Python list."""
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

# Alias for the main function
solve = merge_two_lists

# Alternative class-based solution (for LeetCode submission format)
class Solution:
    def solutionMethod(self):
        """
        TODO: Implement solution method with correct name and signature
        """
        pass

if __name__ == "__main__":
    # Test your solution locally
    print("Testing solution...")
    result = solve()
    print(f"Result: {result}")

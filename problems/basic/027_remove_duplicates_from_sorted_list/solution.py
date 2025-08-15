"""
Solution for Remove Duplicates from Sorted List
Problem ID: 027
LeetCode: https://leetcode.com/problems/remove-duplicates-from-sorted-list/
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def delete_duplicates(head):
    """
    Remove duplicates from sorted linked list.
    """
    # TODO: Implement your solution here
    pass

def create_linked_list(values):
    """Helper function to create linked list from array"""
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def linked_list_to_array(head):
    """Helper function to convert linked list to array"""
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result
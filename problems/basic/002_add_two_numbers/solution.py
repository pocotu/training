"""
Add Two Numbers - LeetCode Problem #2
Problem ID: 002

You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.

Time Complexity: O(max(m,n))
Space Complexity: O(max(m,n))
"""

class ListNode:
    """Definition for singly-linked list."""
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __repr__(self):
        """String representation for debugging"""
        values = []
        current = self
        while current:
            values.append(str(current.val))
            current = current.next
        return " -> ".join(values)

def add_two_numbers(l1, l2):
    """
    Add two numbers represented as linked lists in reverse order.
    
    Args:
        l1: ListNode representing first number in reverse order
        l2: ListNode representing second number in reverse order
        
    Returns:
        ListNode representing sum in reverse order
    """
    dummy_head = ListNode(0)
    current = dummy_head
    carry = 0
    
    # Process both lists while either has nodes or there's a carry
    while l1 or l2 or carry:
        # Get values from current nodes (0 if node is None)
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0
        
        # Calculate sum and new carry
        total = val1 + val2 + carry
        carry = total // 10
        digit = total % 10
        
        # Create new node with the digit
        current.next = ListNode(digit)
        current = current.next
        
        # Move to next nodes if they exist
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
    
    return dummy_head.next

def add_two_numbers_recursive(l1, l2, carry=0):
    """
    Recursive solution for Add Two Numbers.
    Alternative implementation for learning purposes.
    
    Args:
        l1: ListNode representing first number
        l2: ListNode representing second number
        carry: Current carry value
        
    Returns:
        ListNode representing sum
    """
    # Base case: if no more nodes and no carry
    if not l1 and not l2 and carry == 0:
        return None
    
    # Get values from current nodes
    val1 = l1.val if l1 else 0
    val2 = l2.val if l2 else 0
    
    # Calculate sum and new carry
    total = val1 + val2 + carry
    new_carry = total // 10
    digit = total % 10
    
    # Create current node
    result = ListNode(digit)
    
    # Get next nodes
    next1 = l1.next if l1 else None
    next2 = l2.next if l2 else None
    
    # Recursively process next nodes
    result.next = add_two_numbers_recursive(next1, next2, new_carry)
    
    return result

# Helper functions for testing
def array_to_list(arr):
    """Convert array to linked list"""
    if not arr:
        return None
    
    head = ListNode(arr[0])
    current = head
    
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    
    return head

def list_to_array(head):
    """Convert linked list to array"""
    result = []
    current = head
    
    while current:
        result.append(current.val)
        current = current.next
    
    return result

def print_addition(l1, l2, result):
    """Pretty print the addition operation"""
    arr1 = list_to_array(l1)
    arr2 = list_to_array(l2)
    arr_result = list_to_array(result)
    
    # Convert to actual numbers (reverse the arrays)
    num1 = int(''.join(map(str, reversed(arr1))))
    num2 = int(''.join(map(str, reversed(arr2))))
    sum_result = int(''.join(map(str, reversed(arr_result))))
    
    print(f"  {arr1} (represents {num1})")
    print(f"+ {arr2} (represents {num2})")
    print(f"= {arr_result} (represents {sum_result})")
    print(f"  Verification: {num1} + {num2} = {sum_result}")

# Example usage and testing
if __name__ == "__main__":
    # Test cases from LeetCode
    test_cases = [
        ([2, 4, 3], [5, 6, 4]),  # 342 + 465 = 807
        ([0], [0]),              # 0 + 0 = 0
        ([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9])  # 9999999 + 9999 = 10009998
    ]
    
    print("Testing Add Two Numbers solutions:")
    print("=" * 50)
    
    for i, (arr1, arr2) in enumerate(test_cases, 1):
        print(f"\nTest Case {i}:")
        
        # Convert arrays to linked lists
        l1 = array_to_list(arr1)
        l2 = array_to_list(arr2)
        
        # Test iterative solution
        result_iter = add_two_numbers(l1, l2)
        print("Iterative Solution:")
        print_addition(l1, l2, result_iter)
        
        # Test recursive solution
        l1 = array_to_list(arr1)  # Recreate lists since they're modified
        l2 = array_to_list(arr2)
        result_rec = add_two_numbers_recursive(l1, l2)
        print("\nRecursive Solution:")
        print_addition(array_to_list(arr1), array_to_list(arr2), result_rec)
        
        # Verify both solutions give same result
        iter_array = list_to_array(result_iter)
        rec_array = list_to_array(result_rec)
        print(f"\nBoth solutions match: {iter_array == rec_array}")
        print("-" * 30)
    
    # Additional edge case testing
    print("\nEdge Case Testing:")
    print("=" * 30)
    
    # Single digit with carry
    l1 = array_to_list([9])
    l2 = array_to_list([9])
    result = add_two_numbers(l1, l2)
    print("Single digit with carry:")
    print_addition(array_to_list([9]), array_to_list([9]), result)
    
    # Different lengths
    l1 = array_to_list([9, 9])
    l2 = array_to_list([1])
    result = add_two_numbers(l1, l2)
    print("\nDifferent lengths:")
    print_addition(array_to_list([9, 9]), array_to_list([1]), result)

"""
Solution for Remove Linked List Elements
Problem ID: 203
LeetCode Problem: https://leetcode.com/problems/remove-linked-list-elements/

Remove all elements from a linked list of integers that have value val.
"""

# Definition for singly-linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __repr__(self):
        """String representation for debugging."""
        result = []
        current = self
        while current and len(result) < 20:  # Prevent infinite loops
            result.append(str(current.val))
            current = current.next
        return " -> ".join(result) + (" -> ..." if current else "")

def remove_elements_iterative(head: ListNode, val: int) -> ListNode:
    """
    Iterative approach with dummy node.
    
    Args:
        head: Head of the linked list
        val: Value to remove
        
    Returns:
        New head of the modified list
        
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    # Create dummy node to handle edge cases
    dummy = ListNode(0)
    dummy.next = head
    
    prev = dummy
    current = head
    
    while current:
        if current.val == val:
            prev.next = current.next
        else:
            prev = current
        current = current.next
    
    return dummy.next

def remove_elements_recursive(head: ListNode, val: int) -> ListNode:
    """
    Recursive approach.
    
    Args:
        head: Head of the linked list
        val: Value to remove
        
    Returns:
        New head of the modified list
        
    Time Complexity: O(n)
    Space Complexity: O(n) - recursion stack
    """
    if not head:
        return None
    
    head.next = remove_elements_recursive(head.next, val)
    
    return head.next if head.val == val else head

def remove_elements_no_dummy(head: ListNode, val: int) -> ListNode:
    """
    Iterative approach without dummy node.
    
    Args:
        head: Head of the linked list
        val: Value to remove
        
    Returns:
        New head of the modified list
        
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    # Remove nodes from the beginning
    while head and head.val == val:
        head = head.next
    
    if not head:
        return None
    
    # Remove nodes from the middle and end
    current = head
    while current.next:
        if current.next.val == val:
            current.next = current.next.next
        else:
            current = current.next
    
    return head

def remove_elements_two_pointers(head: ListNode, val: int) -> ListNode:
    """
    Two pointers approach.
    
    Args:
        head: Head of the linked list
        val: Value to remove
        
    Returns:
        New head of the modified list
        
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if not head:
        return None
    
    # Find first node that doesn't need to be removed
    while head and head.val == val:
        head = head.next
    
    if not head:
        return None
    
    # Use two pointers to remove nodes
    slow = head
    fast = head.next
    
    while fast:
        if fast.val == val:
            slow.next = fast.next
        else:
            slow = fast
        fast = fast.next
    
    return head

def remove_elements_optimized(head: ListNode, val: int) -> ListNode:
    """
    Optimized approach with early termination checks.
    
    Args:
        head: Head of the linked list
        val: Value to remove
        
    Returns:
        New head of the modified list
        
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if not head:
        return None
    
    # Quick check: if list is empty after removing target values from start
    while head and head.val == val:
        head = head.next
    
    if not head:
        return None
    
    # Optimize: if no more target values exist, return early
    current = head
    has_target = False
    temp = current.next
    
    while temp:
        if temp.val == val:
            has_target = True
            break
        temp = temp.next
    
    if not has_target:
        return head
    
    # Remove target values from rest of list
    while current.next:
        if current.next.val == val:
            current.next = current.next.next
        else:
            current = current.next
    
    return head

# Main function for the problem
def removeElements(head: ListNode, val: int) -> ListNode:
    """
    Main solution using iterative approach with dummy node.
    """
    return remove_elements_iterative(head, val)

# Utility functions for testing
def create_linked_list(values: list) -> ListNode:
    """Create a linked list from a list of values."""
    if not values:
        return None
    
    head = ListNode(values[0])
    current = head
    
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    
    return head

def linked_list_to_list(head: ListNode) -> list:
    """Convert linked list to Python list."""
    result = []
    current = head
    
    while current:
        result.append(current.val)
        current = current.next
        
        # Prevent infinite loops
        if len(result) > 1000:
            break
    
    return result

def count_nodes(head: ListNode) -> int:
    """Count nodes in linked list."""
    count = 0
    current = head
    
    while current:
        count += 1
        current = current.next
        
        # Prevent infinite loops
        if count > 1000:
            break
    
    return count

if __name__ == "__main__":
    # Test cases
    test_cases = [
        # Basic cases
        ([1, 2, 6, 3, 4, 5, 6], 6, [1, 2, 3, 4, 5]),
        ([7, 7, 7, 7], 7, []),
        ([1, 2, 3, 4, 5], 6, [1, 2, 3, 4, 5]),
        
        # Edge cases
        ([], 1, []),
        ([1], 1, []),
        ([1], 2, [1]),
        ([1, 1], 1, []),
        ([1, 2], 1, [2]),
        ([1, 2], 2, [1]),
        
        # All same values
        ([5, 5, 5, 5, 5], 5, []),
        ([1, 1, 1, 2, 2, 2], 1, [2, 2, 2]),
        ([1, 1, 1, 2, 2, 2], 2, [1, 1, 1]),
        
        # Remove from beginning
        ([6, 6, 1, 2, 3], 6, [1, 2, 3]),
        
        # Remove from end
        ([1, 2, 3, 6, 6], 6, [1, 2, 3]),
        
        # Remove from middle
        ([1, 2, 6, 6, 3, 4], 6, [1, 2, 3, 4]),
        
        # No removal needed
        ([1, 2, 3, 4, 5], 6, [1, 2, 3, 4, 5]),
        
        # Large values
        ([1000000, 999999, 1000000], 1000000, [999999]),
    ]
    
    print("=" * 60)
    print("REMOVE LINKED LIST ELEMENTS - COMPREHENSIVE TESTING")
    print("=" * 60)
    
    algorithms = [
        ("Iterative with Dummy", remove_elements_iterative),
        ("Recursive", remove_elements_recursive),
        ("No Dummy Node", remove_elements_no_dummy),
        ("Two Pointers", remove_elements_two_pointers),
        ("Optimized", remove_elements_optimized),
    ]
    
    for i, (input_list, val, expected) in enumerate(test_cases):
        print(f"\nTest Case {i + 1}:")
        print(f"  Input: {input_list}")
        print(f"  Remove value: {val}")
        print(f"  Expected: {expected}")
        
        results = []
        for name, func in algorithms:
            try:
                # Create fresh linked list for each algorithm
                head = create_linked_list(input_list)
                
                import time
                start_time = time.time()
                result_head = func(head, val)
                end_time = time.time()
                
                result_list = linked_list_to_list(result_head)
                results.append(result_list)
                
                status = "✓" if result_list == expected else "✗"
                print(f"  {name}: {result_list} {status} ({end_time - start_time:.6f}s)")
                
            except Exception as e:
                print(f"  {name}: ERROR - {e}")
        
        # Check consistency
        if len(set(tuple(r) for r in results)) > 1:
            print(f"  WARNING: Inconsistent results")
    
    # Performance testing
    print("\n" + "=" * 60)
    print("PERFORMANCE TESTING")
    print("=" * 60)
    
    import random
    import time
    
    # Generate test data
    performance_tests = [
        ("Small list", 100),
        ("Medium list", 1000),
        ("Large list", 10000),
        ("Very large list", 50000),
    ]
    
    for test_name, size in performance_tests:
        print(f"\n{test_name} ({size} nodes):")
        
        # Generate random list
        values = [random.randint(1, 10) for _ in range(size)]
        target_val = random.randint(1, 10)
        
        for name, func in algorithms:
            try:
                # Create fresh linked list
                head = create_linked_list(values)
                
                start_time = time.time()
                result_head = func(head, target_val)
                end_time = time.time()
                
                result_count = count_nodes(result_head)
                print(f"  {name}: {result_count} nodes remaining, {end_time - start_time:.6f}s")
                
            except Exception as e:
                print(f"  {name}: ERROR - {e}")
    
    # Memory efficiency testing
    print("\n" + "=" * 60)
    print("MEMORY EFFICIENCY TESTING")
    print("=" * 60)
    
    import sys
    
    def estimate_memory_usage(head):
        """Estimate memory usage of linked list."""
        total_size = 0
        current = head
        count = 0
        
        while current and count < 1000:  # Limit for safety
            total_size += sys.getsizeof(current)
            current = current.next
            count += 1
        
        return total_size, count
    
    # Test memory usage with different removal patterns
    memory_tests = [
        ("Remove none", [1, 2, 3, 4, 5], 6),
        ("Remove all", [3, 3, 3, 3, 3], 3),
        ("Remove half", [1, 3, 1, 3, 1, 3], 3),
        ("Remove first half", [3, 3, 1, 2, 4, 5], 3),
        ("Remove last half", [1, 2, 4, 5, 3, 3], 3),
    ]
    
    for test_name, values, remove_val in memory_tests:
        print(f"\n{test_name}:")
        original_head = create_linked_list(values)
        original_size, original_count = estimate_memory_usage(original_head)
        
        print(f"  Original: {original_count} nodes, ~{original_size} bytes")
        
        # Test iterative method (most commonly used)
        test_head = create_linked_list(values)
        result_head = remove_elements_iterative(test_head, remove_val)
        result_size, result_count = estimate_memory_usage(result_head)
        
        print(f"  After removal: {result_count} nodes, ~{result_size} bytes")
        print(f"  Removed: {original_count - result_count} nodes")
    
    # Edge case stress testing
    print("\n" + "=" * 60)
    print("EDGE CASE STRESS TESTING")
    print("=" * 60)
    
    edge_cases = [
        ("Single node removal", [42], 42),
        ("Single node keep", [42], 43),
        ("All same values", [7] * 1000, 7),
        ("Alternating pattern", [1, 2] * 500, 1),
        ("Remove first element", [1] + [2] * 999, 1),
        ("Remove last element", [2] * 999 + [1], 1),
        ("No target in large list", list(range(1000)), 1001),
    ]
    
    for test_name, values, remove_val in edge_cases:
        print(f"\n{test_name}:")
        
        # Test main algorithms on edge cases
        test_algorithms = [
            ("Iterative", remove_elements_iterative),
            ("Recursive", remove_elements_recursive),
            ("Optimized", remove_elements_optimized),
        ]
        
        for name, func in test_algorithms:
            try:
                head = create_linked_list(values)
                
                start_time = time.time()
                result_head = func(head, remove_val)
                end_time = time.time()
                
                result_count = count_nodes(result_head)
                removed_count = len(values) - result_count
                
                print(f"  {name}: removed {removed_count}, {end_time - start_time:.6f}s")
                
            except Exception as e:
                print(f"  {name}: ERROR - {e}")
    
    # Correctness validation
    print("\n" + "=" * 60)
    print("CORRECTNESS VALIDATION")
    print("=" * 60)
    
    def validate_removal(original_values, remove_val, result_head):
        """Validate that removal was done correctly."""
        result_values = linked_list_to_list(result_head)
        
        # Check that no target values remain
        if remove_val in result_values:
            return False, f"Target value {remove_val} still present"
        
        # Check that all non-target values are preserved in order
        expected = [val for val in original_values if val != remove_val]
        if result_values != expected:
            return False, f"Expected {expected}, got {result_values}"
        
        return True, "Correct"
    
    # Validation test cases
    validation_cases = [
        ([1, 2, 6, 3, 4, 5, 6], 6),
        ([7, 7, 7, 7], 7),
        ([], 1),
        ([1], 1),
        ([1, 1, 2, 2, 3, 3], 2),
        (list(range(100)), 50),
    ]
    
    for values, remove_val in validation_cases:
        print(f"\nValidating removal of {remove_val} from {len(values)} nodes:")
        
        for name, func in algorithms:
            try:
                head = create_linked_list(values)
                result_head = func(head, remove_val)
                
                is_valid, message = validate_removal(values, remove_val, result_head)
                status = "✓" if is_valid else "✗"
                
                print(f"  {name}: {status} {message}")
                
            except Exception as e:
                print(f"  {name}: ERROR - {e}")
    
    # Recursive depth testing
    print("\n" + "=" * 60)
    print("RECURSIVE DEPTH TESTING")
    print("=" * 60)
    
    # Test recursive approach with deep lists
    recursive_tests = [100, 500, 1000]
    
    for depth in recursive_tests:
        print(f"\nTesting recursion with depth {depth}:")
        values = list(range(depth))
        remove_val = depth // 2
        
        try:
            head = create_linked_list(values)
            
            start_time = time.time()
            result_head = remove_elements_recursive(head, remove_val)
            end_time = time.time()
            
            result_count = count_nodes(result_head)
            print(f"  Recursive: {result_count} nodes, {end_time - start_time:.6f}s ✓")
            
        except RecursionError:
            print(f"  Recursive: RecursionError (depth limit exceeded) ✗")
        except Exception as e:
            print(f"  Recursive: ERROR - {e}")

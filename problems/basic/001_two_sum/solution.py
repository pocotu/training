"""
Two Sum - LeetCode Problem #1
Problem ID: 001

Given an array of integers nums and an integer target, return indices 
of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and 
you may not use the same element twice.

Time Complexity: O(n)
Space Complexity: O(n)
"""

def two_sum(nums, target):
    """
    Find two numbers in array that add up to target.
    
    Args:
        nums: List of integers
        target: Target sum
        
    Returns:
        List of two indices whose values sum to target
    """
    # Dictionary to store value and its index
    num_map = {}
    
    for i, num in enumerate(nums):
        complement = target - num
        
        # If complement exists in map, we found our pair
        if complement in num_map:
            return [num_map[complement], i]
        
        # Store current number and its index
        num_map[num] = i
    
    # Should never reach here based on problem constraints
    return []

def two_sum_brute_force(nums, target):
    """
    Brute force solution - O(n^2) time complexity.
    Alternative solution for learning purposes.
    
    Args:
        nums: List of integers
        target: Target sum
        
    Returns:
        List of two indices whose values sum to target
    """
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []

# Example usage and testing
if __name__ == "__main__":
    # Test cases from LeetCode
    test_cases = [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1])
    ]
    
    print("Testing Two Sum solutions:")
    print("=" * 40)
    
    for i, (nums, target, expected) in enumerate(test_cases, 1):
        result = two_sum(nums, target)
        brute_result = two_sum_brute_force(nums, target)
        
        print(f"Test Case {i}:")
        print(f"  Input: nums = {nums}, target = {target}")
        print(f"  Expected: {expected}")
        print(f"  Hash Map Solution: {result}")
        print(f"  Brute Force Solution: {brute_result}")
        print(f"  Hash Map Correct: {result == expected}")
        print(f"  Brute Force Correct: {brute_result == expected}")
        print()
    
    # Performance test with larger array
    import time
    
    large_nums = list(range(10000)) + [5000]
    large_target = 15000
    
    # Test hash map solution
    start_time = time.time()
    hash_result = two_sum(large_nums, large_target)
    hash_time = time.time() - start_time
    
    # Test brute force solution (be careful with large arrays)
    start_time = time.time()
    brute_result = two_sum_brute_force(large_nums, large_target)
    brute_time = time.time() - start_time
    
    print("Performance Test (10,001 elements):")
    print(f"Hash Map Solution: {hash_time:.6f} seconds")
    print(f"Brute Force Solution: {brute_time:.6f} seconds")
    print(f"Hash Map is {brute_time/hash_time:.2f}x faster")

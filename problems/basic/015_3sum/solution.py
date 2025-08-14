"""
3Sum - LeetCode Problem #15
Problem ID: 015

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Time Complexity: O(n^2)
Space Complexity: O(1) - not counting output space
"""

def three_sum(nums):
    """
    Find all unique triplets that sum to zero.
    
    Args:
        nums: List of integers
        
    Returns:
        List of unique triplets that sum to zero
    """
    nums.sort()  # Sort the array
    result = []
    n = len(nums)
    
    for i in range(n - 2):
        # Skip duplicate values for the first element
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
        left = i + 1
        right = n - 1
        
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            
            if current_sum == 0:
                result.append([nums[i], nums[left], nums[right]])
                
                # Skip duplicates for left pointer
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                # Skip duplicates for right pointer
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                
                left += 1
                right -= 1
            elif current_sum < 0:
                left += 1
            else:
                right -= 1
    
    return result

def three_sum_brute_force(nums):
    """
    Brute force solution for comparison - O(n^3) time complexity.
    
    Args:
        nums: List of integers
        
    Returns:
        List of unique triplets that sum to zero
    """
    result = set()
    n = len(nums)
    
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if nums[i] + nums[j] + nums[k] == 0:
                    triplet = tuple(sorted([nums[i], nums[j], nums[k]]))
                    result.add(triplet)
    
    return [list(triplet) for triplet in sorted(result)]

# Example usage and testing
if __name__ == "__main__":
    test_cases = [
        [-1, 0, 1, 2, -1, -4],
        [0, 1, 1],
        [0, 0, 0],
        [-2, 0, 1, 1, 2],
        [-1, 0, 1, 0]
    ]
    
    print("Testing 3Sum:")
    print("=" * 40)
    
    for i, nums in enumerate(test_cases, 1):
        print(f"Test {i}: {nums}")
        
        nums_copy1 = nums.copy()
        nums_copy2 = nums.copy()
        
        result1 = three_sum(nums_copy1)
        result2 = three_sum_brute_force(nums_copy2)
        
        print(f"  Optimized: {result1}")
        print(f"  Brute Force: {result2}")
        print(f"  Match: {sorted(result1) == sorted(result2)}")
        print()

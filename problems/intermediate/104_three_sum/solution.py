"""
Solution for 3Sum
Problem ID: 104
LeetCode Problem: https://leetcode.com/problems/3sum/

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
"""

def three_sum(nums: list[int]) -> list[list[int]]:
    """
    Find all unique triplets that sum to zero.
    
    Args:
        nums: Array of integers
        
    Returns:
        List of triplets that sum to zero
        
    Time Complexity: O(n²)
    Space Complexity: O(1) excluding output space
    """
    if len(nums) < 3:
        return []
    
    nums.sort()
    result = []
    
    for i in range(len(nums) - 2):
        # Skip duplicates for first element
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
        left = i + 1
        right = len(nums) - 1
        
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            
            if current_sum == 0:
                result.append([nums[i], nums[left], nums[right]])
                
                # Skip duplicates
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                
                left += 1
                right -= 1
            elif current_sum < 0:
                left += 1
            else:
                right -= 1
    
    return result

if __name__ == "__main__":
    # Test cases
    test_cases = [
        [-1,0,1,2,-1,-4],  # Expected: [[-1,-1,2],[-1,0,1]]
        [0,1,1],           # Expected: []
        [0,0,0],           # Expected: [[0,0,0]]
    ]
    
    for nums in test_cases:
        result = three_sum(nums)
        print(f"Input: {nums} -> Output: {result}")

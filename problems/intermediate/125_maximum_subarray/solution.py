"""
Solution for LeetCode Problem 53 - Maximum Subarray
Problem ID: 125

Approach: Kadane's Algorithm
Time Complexity: O(n)
Space Complexity: O(1)
"""

def max_sub_array(nums):
    """
    Find the contiguous subarray with the largest sum.
    
    Args:
        nums: List[int] - Array of integers
        
    Returns:
        int: Maximum sum of contiguous subarray
    """
    max_sum = current_sum = nums[0]
    
    for num in nums[1:]:
        # Either extend existing subarray or start new one
        current_sum = max(num, current_sum + num)
        # Update global maximum
        max_sum = max(max_sum, current_sum)
    
    return max_sum

def max_sub_array_dp(nums):
    """
    Dynamic Programming approach (equivalent to Kadane's)
    
    Args:
        nums: List[int] - Array of integers
        
    Returns:
        int: Maximum sum of contiguous subarray
    """
    n = len(nums)
    dp = [0] * n
    dp[0] = nums[0]
    max_sum = nums[0]
    
    for i in range(1, n):
        dp[i] = max(nums[i], dp[i-1] + nums[i])
        max_sum = max(max_sum, dp[i])
    
    return max_sum

def max_sub_array_divide_conquer(nums):
    """
    Divide and conquer approach
    Time: O(n log n), Space: O(log n)
    """
    def max_crossing_sum(nums, left, mid, right):
        left_sum = float('-inf')
        sum_val = 0
        for i in range(mid, left - 1, -1):
            sum_val += nums[i]
            left_sum = max(left_sum, sum_val)
        
        right_sum = float('-inf')
        sum_val = 0
        for i in range(mid + 1, right + 1):
            sum_val += nums[i]
            right_sum = max(right_sum, sum_val)
        
        return left_sum + right_sum
    
    def max_subarray_rec(nums, left, right):
        if left == right:
            return nums[left]
        
        mid = (left + right) // 2
        
        left_max = max_subarray_rec(nums, left, mid)
        right_max = max_subarray_rec(nums, mid + 1, right)
        cross_max = max_crossing_sum(nums, left, mid, right)
        
        return max(left_max, right_max, cross_max)
    
    return max_subarray_rec(nums, 0, len(nums) - 1)

# Alias for main function
solve = max_sub_array

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

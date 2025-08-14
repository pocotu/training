"""
Solution for Container With Most Water
Problem ID: 103
LeetCode Problem: https://leetcode.com/problems/container-with-most-water/

You are given an integer array height of length n. There are n vertical lines drawn such that
the two endpoints of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container that contains the most water.
"""

def max_area(height: list[int]) -> int:
    """
    Find the maximum area of water that can be contained.
    
    Args:
        height: Array of heights
        
    Returns:
        Maximum area
        
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    left = 0
    right = len(height) - 1
    max_water = 0
    
    while left < right:
        # Calculate current area
        width = right - left
        current_height = min(height[left], height[right])
        current_area = width * current_height
        
        max_water = max(max_water, current_area)
        
        # Move the pointer with smaller height
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    
    return max_water

if __name__ == "__main__":
    # Test cases
    test_cases = [
        [1,8,6,2,5,4,8,3,7],  # Expected: 49
        [1,1],                 # Expected: 1
    ]
    
    for heights in test_cases:
        result = max_area(heights)
        print(f"Input: {heights} -> Output: {result}")

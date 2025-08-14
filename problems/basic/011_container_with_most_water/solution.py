"""
Container With Most Water - LeetCode Problem #11
Problem ID: 011

You are given an integer array height of length n. Find two lines that together 
with the x-axis form a container that can hold the most water.

Time Complexity: O(n)
Space Complexity: O(1)
"""

def max_area(height):
    """
    Find maximum water area using two pointers approach.
    
    Args:
        height: List of integers representing heights
        
    Returns:
        Maximum area of water that can be contained
    """
    left = 0
    right = len(height) - 1
    max_water = 0
    
    while left < right:
        # Calculate current area
        width = right - left
        current_height = min(height[left], height[right])
        current_area = width * current_height
        
        # Update maximum area
        max_water = max(max_water, current_area)
        
        # Move pointer with smaller height
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    
    return max_water

def max_area_brute_force(height):
    """
    Brute force solution for comparison - O(n^2) time complexity.
    
    Args:
        height: List of integers representing heights
        
    Returns:
        Maximum area of water that can be contained
    """
    max_water = 0
    n = len(height)
    
    for i in range(n):
        for j in range(i + 1, n):
            width = j - i
            current_height = min(height[i], height[j])
            current_area = width * current_height
            max_water = max(max_water, current_area)
    
    return max_water

# Example usage and testing
if __name__ == "__main__":
    test_cases = [
        [1, 8, 6, 2, 5, 4, 8, 3, 7],  # Expected: 49
        [1, 1],                       # Expected: 1
        [4, 3, 2, 1, 4],             # Expected: 16
        [1, 2, 1]                     # Expected: 2
    ]
    
    print("Testing Container With Most Water:")
    print("=" * 40)
    
    for i, heights in enumerate(test_cases, 1):
        result1 = max_area(heights)
        result2 = max_area_brute_force(heights)
        print(f"Test {i}: {heights}")
        print(f"  Two Pointers: {result1}")
        print(f"  Brute Force: {result2}")
        print(f"  Match: {result1 == result2}")
        print()

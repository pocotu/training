"""
Solution for Trapping Rain Water
Problem ID: 205
LeetCode Problem: https://leetcode.com/problems/trapping-rain-water/

Given n non-negative integers representing an elevation map where the width of each bar is 1,
compute how much water it can trap after raining.
"""

def trap_two_pointers(height: list[int]) -> int:
    """
    Two pointers approach - most optimal.
    
    Args:
        height: Array representing elevation map
        
    Returns:
        Amount of water that can be trapped
        
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if not height or len(height) < 3:
        return 0
    
    left, right = 0, len(height) - 1
    left_max = right_max = 0
    water = 0
    
    while left < right:
        if height[left] < height[right]:
            if height[left] >= left_max:
                left_max = height[left]
            else:
                water += left_max - height[left]
            left += 1
        else:
            if height[right] >= right_max:
                right_max = height[right]
            else:
                water += right_max - height[right]
            right -= 1
    
    return water

def trap_dp_precompute(height: list[int]) -> int:
    """
    Dynamic Programming with precomputation.
    
    Args:
        height: Array representing elevation map
        
    Returns:
        Amount of water that can be trapped
        
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    if not height or len(height) < 3:
        return 0
    
    n = len(height)
    
    # Precompute left_max for each position
    left_max = [0] * n
    left_max[0] = height[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i - 1], height[i])
    
    # Precompute right_max for each position
    right_max = [0] * n
    right_max[n - 1] = height[n - 1]
    for i in range(n - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], height[i])
    
    # Calculate trapped water
    water = 0
    for i in range(n):
        water_level = min(left_max[i], right_max[i])
        if water_level > height[i]:
            water += water_level - height[i]
    
    return water

def trap_stack(height: list[int]) -> int:
    """
    Monotonic stack approach.
    
    Args:
        height: Array representing elevation map
        
    Returns:
        Amount of water that can be trapped
        
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    if not height or len(height) < 3:
        return 0
    
    stack = []
    water = 0
    
    for i, h in enumerate(height):
        while stack and height[stack[-1]] < h:
            bottom = stack.pop()
            
            if not stack:
                break
            
            # Calculate trapped water between stack[-1] and i
            width = i - stack[-1] - 1
            bounded_height = min(height[stack[-1]], h) - height[bottom]
            water += width * bounded_height
        
        stack.append(i)
    
    return water

# Main function for the problem
def trap(height: list[int]) -> int:
    """
    Main solution function using the most optimal approach.
    """
    return trap_two_pointers(height)

if __name__ == "__main__":
    # Test cases
    test_cases = [
        ([0,1,0,2,1,0,1,3,2,1,2,1], 6),
        ([4,2,0,3,2,5], 9),
        ([3,0,2,0,4], 7),
        ([1,2,3,4,5], 0),  # No water can be trapped
        ([5,4,3,2,1], 0),  # No water can be trapped
        ([2,0,2], 2),      # Simple case
        ([3,2,0,4], 5),    # Valley pattern
        ([1], 0),          # Single element
        ([], 0),           # Empty array
    ]
    
    print("=" * 60)
    print("TRAPPING RAIN WATER - COMPREHENSIVE TESTING")
    print("=" * 60)
    
    algorithms = [
        ("Two Pointers", trap_two_pointers),
        ("DP Precompute", trap_dp_precompute),
        ("Monotonic Stack", trap_stack),
    ]
    
    for i, (heights, expected) in enumerate(test_cases, 1):
        print(f"\nTest Case {i}: {heights}")
        print(f"Expected: {expected}")
        
        for name, func in algorithms:
            try:
                result = func(heights)
                status = "✓" if result == expected else "✗"
                print(f"  {name}: {result} {status}")
            except Exception as e:
                print(f"  {name}: ERROR - {e}")
    
    # Performance comparison
    print("\n" + "=" * 60)
    print("PERFORMANCE COMPARISON")
    print("=" * 60)
    
    import time
    import random
    
    # Generate large test case
    random.seed(42)
    large_height = [random.randint(0, 20) for _ in range(10000)]
    
    print(f"Large test: array length = {len(large_height)}")
    
    for name, func in algorithms:
        start_time = time.time()
        result = func(large_height)
        end_time = time.time()
        print(f"{name}: result={result}, time={end_time - start_time:.6f}s")
    
    # Visualization helper for small cases
    def visualize_trap(height):
        """Helper function to visualize water trapping."""
        if not height:
            return
        
        water_trapped = trap_two_pointers(height)
        max_height = max(height)
        
        print(f"\nVisualization (water trapped: {water_trapped}):")
        for level in range(max_height, 0, -1):
            line = ""
            for h in height:
                if h >= level:
                    line += "█"
                else:
                    # Check if water can be trapped at this position
                    left_max = max(height[:height.index(h)] + [0])
                    right_max = max(height[height.index(h)+1:] + [0])
                    water_level = min(left_max, right_max)
                    if water_level >= level:
                        line += "~"
                    else:
                        line += " "
            print(line)
    
    # Visualize a few small cases
    print("\n" + "=" * 60)
    print("VISUALIZATIONS")
    print("=" * 60)
    
    small_cases = [
        [0,1,0,2,1,0,1,3,2,1,2,1],
        [4,2,0,3,2,5],
        [3,0,2,0,4],
    ]
    
    for heights in small_cases:
        print(f"\nHeight array: {heights}")
        # Simple text representation
        trapped = trap_two_pointers(heights)
        print(f"Water trapped: {trapped}")
        
        # Show height distribution
        for i, h in enumerate(heights):
            print(f"Position {i}: height {h}")
            if i > 0 and i < len(heights) - 1:
                left_max = max(heights[:i])
                right_max = max(heights[i+1:])
                water_level = min(left_max, right_max)
                if water_level > h:
                    print(f"  -> Water level: {water_level}, trapped: {water_level - h}")
                else:
                    print(f"  -> No water trapped")
        print("-" * 30)

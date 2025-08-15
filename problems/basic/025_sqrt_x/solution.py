"""
Solution for LeetCode Problem 69 - Sqrt(x)
Problem ID: 025

Approach: Binary Search
Time Complexity: O(log n)
Space Complexity: O(1)
"""

def my_sqrt(x):
    """
    Compute and return the square root of x (integer part only).
    
    Args:
        x: int - Non-negative integer
        
    Returns:
        int: Integer part of sqrt(x)
    """
    if x < 2:
        return x
    
    left, right = 1, x // 2
    
    while left <= right:
        mid = (left + right) // 2
        square = mid * mid
        
        if square == x:
            return mid
        elif square < x:
            left = mid + 1
        else:
            right = mid - 1
    
    return right  # right will be the largest integer whose square is <= x

def my_sqrt_newton(x):
    """
    Newton's method for finding square root (faster convergence)
    
    Args:
        x: int - Non-negative integer
        
    Returns:
        int: Integer part of sqrt(x)
    """
    if x < 2:
        return x
    
    # Start with initial guess
    guess = x
    while guess * guess > x:
        guess = (guess + x // guess) // 2
    
    return guess

# Alias for main function
solve = my_sqrt

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

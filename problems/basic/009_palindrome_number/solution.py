"""
Palindrome Number - LeetCode Problem #9
Problem ID: 009

Given an integer x, return true if x is palindrome integer.

Time Complexity: O(log n)
Space Complexity: O(1)
"""

def is_palindrome(x):
    """
    Check if integer is palindrome without converting to string.
    
    Args:
        x: Integer to check
        
    Returns:
        True if x is palindrome, False otherwise
    """
    # Negative numbers and numbers ending in 0 (except 0) are not palindromes
    if x < 0 or (x % 10 == 0 and x != 0):
        return False
    
    # Reverse half of the number
    reversed_half = 0
    while x > reversed_half:
        reversed_half = reversed_half * 10 + x % 10
        x //= 10
    
    # For odd number of digits, we need to get rid of the middle digit
    # by dividing reversed_half by 10
    return x == reversed_half or x == reversed_half // 10

def is_palindrome_string(x):
    """
    Alternative solution using string conversion.
    
    Args:
        x: Integer to check
        
    Returns:
        True if x is palindrome, False otherwise
    """
    s = str(x)
    return s == s[::-1]

# Example usage and testing
if __name__ == "__main__":
    test_cases = [121, -121, 10, 0, 12321, 12345, 1, 11, 1001]
    
    print("Testing Palindrome Number:")
    print("=" * 40)
    
    for num in test_cases:
        result1 = is_palindrome(num)
        result2 = is_palindrome_string(num)
        print(f"{num:6} -> Math: {result1}, String: {result2}, Match: {result1 == result2}")

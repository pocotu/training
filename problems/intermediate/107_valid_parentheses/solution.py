"""
Solution for Valid Parentheses
Problem ID: 107
LeetCode Problem: https://leetcode.com/problems/valid-parentheses/

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.
"""

def is_valid(s: str) -> bool:
    """
    Check if parentheses are valid.
    
    Args:
        s: String containing parentheses
        
    Returns:
        True if valid, False otherwise
        
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in mapping:
            # Closing bracket
            if not stack or stack.pop() != mapping[char]:
                return False
        else:
            # Opening bracket
            stack.append(char)
    
    return len(stack) == 0

if __name__ == "__main__":
    # Test cases
    test_cases = [
        "()",       # Expected: True
        "()[]{}", # Expected: True
        "(]",       # Expected: False
        "([)]",     # Expected: False
        "{[]}",     # Expected: True
    ]
    
    for s in test_cases:
        result = is_valid(s)
        print(f"Input: '{s}' -> Output: {result}")

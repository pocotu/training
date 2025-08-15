"""
Solution for LeetCode Problem 20 - Valid Parentheses
Problem ID: 016

Approach: Stack-based solution
Time Complexity: O(n)
Space Complexity: O(n)
"""

def is_valid(s: str) -> bool:
    """
    Determine if the input string is valid parentheses.
    
    Args:
        s: String containing just the characters '(', ')', '{', '}', '[' and ']'
        
    Returns:
        bool: True if string is valid, False otherwise
    """
    # Stack to keep track of opening brackets
    stack = []
    
    # Mapping of closing to opening brackets
    mapping = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in mapping:  # Closing bracket
            if not stack or stack.pop() != mapping[char]:
                return False
        else:  # Opening bracket
            stack.append(char)
    
    # Valid if no unmatched opening brackets remain
    return len(stack) == 0


def is_valid_alternative(s: str) -> bool:
    """
    Alternative solution using while loop and string replacement.
    Less efficient but more intuitive.
    
    Args:
        s: String containing parentheses
        
    Returns:
        bool: True if valid, False otherwise
    """
    while '()' in s or '[]' in s or '{}' in s:
        s = s.replace('()', '').replace('[]', '').replace('{}', '')
    
    return s == ""


# Alias for the main function (common pattern in competitive programming)
solve = is_valid

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

"""
Solution for Longest Palindromic Substring
Problem ID: 106
LeetCode Problem: https://leetcode.com/problems/longest-palindromic-substring/

Given a string s, return the longest palindromic substring in s.
"""

def longest_palindrome(s: str) -> str:
    """
    Find the longest palindromic substring.
    
    Args:
        s: Input string
        
    Returns:
        Longest palindromic substring
        
    Time Complexity: O(n²)
    Space Complexity: O(1)
    """
    if not s:
        return ""
    
    start = 0
    max_len = 1
    
    def expand_around_center(left: int, right: int) -> int:
        """Expand around center and return length of palindrome."""
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1
    
    for i in range(len(s)):
        # Check for odd length palindromes (center at i)
        len1 = expand_around_center(i, i)
        
        # Check for even length palindromes (center between i and i+1)
        len2 = expand_around_center(i, i + 1)
        
        current_max = max(len1, len2)
        
        if current_max > max_len:
            max_len = current_max
            start = i - (current_max - 1) // 2
    
    return s[start:start + max_len]

if __name__ == "__main__":
    # Test cases
    test_cases = [
        "babad",    # Expected: "bab" or "aba"
        "cbbd",     # Expected: "bb"
        "a",        # Expected: "a"
        "racecar",  # Expected: "racecar"
    ]
    
    for s in test_cases:
        result = longest_palindrome(s)
        print(f"Input: '{s}' -> Output: '{result}'")

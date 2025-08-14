"""
Solution for Longest Substring Without Repeating Characters
Problem ID: 101
LeetCode Problem: https://leetcode.com/problems/longest-substring-without-repeating-characters/

Given a string s, find the length of the longest substring without repeating characters.
"""

def length_of_longest_substring(s: str) -> int:
    """
    Find the length of the longest substring without repeating characters.
    
    Args:
        s: Input string
        
    Returns:
        Length of longest substring without repeating characters
        
    Time Complexity: O(n)
    Space Complexity: O(min(m,n)) where m is charset size
    """
    if not s:
        return 0
    
    char_index = {}
    max_length = 0
    start = 0
    
    for end, char in enumerate(s):
        if char in char_index and char_index[char] >= start:
            start = char_index[char] + 1
        
        char_index[char] = end
        max_length = max(max_length, end - start + 1)
    
    return max_length

if __name__ == "__main__":
    # Test cases
    test_cases = [
        "abcabcbb",  # Expected: 3
        "bbbbb",     # Expected: 1
        "pwwkew",    # Expected: 3
        "",          # Expected: 0
        "a",         # Expected: 1
    ]
    
    for s in test_cases:
        result = length_of_longest_substring(s)
        print(f"Input: '{s}' -> Output: {result}")

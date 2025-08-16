"""
Palindrome Partitioning - LeetCode Problem #131
Problem ID: 130

Given a string s, partition s such that every substring of the partition 
is a palindrome. Return all possible palindrome partitioning of s.

Time Complexity: O(n * 2^n) where n is length of string
Space Complexity: O(n) for recursion depth
"""

def partition(s):
    """
    Find all possible palindrome partitions of string s.
    
    Args:
        s: str - input string
        
    Returns:
        List[List[str]]: all palindrome partitions
    """
    def is_palindrome(string):
        """Check if string is palindrome"""
        return string == string[::-1]
    
    def backtrack(start, path):
        """Backtrack to find all valid partitions"""
        # If we've reached the end, add current path to result
        if start == len(s):
            result.append(path[:])  # Make a copy
            return
        
        # Try all possible substrings starting from 'start'
        for end in range(start + 1, len(s) + 1):
            substring = s[start:end]
            if is_palindrome(substring):
                path.append(substring)
                backtrack(end, path)
                path.pop()  # Backtrack
    
    result = []
    backtrack(0, [])
    return result

# Optimized version with DP for palindrome checking
def partition_optimized(s):
    """
    Optimized version using DP to precompute palindromes.
    """
    n = len(s)
    
    # Precompute palindrome table
    dp = [[False] * n for _ in range(n)]
    
    # Every single character is palindrome
    for i in range(n):
        dp[i][i] = True
    
    # Check for palindromes of length 2
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
    
    # Check for palindromes of length 3 and more
    for length in range(3, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j] and dp[i + 1][j - 1]:
                dp[i][j] = True
    
    def backtrack(start, path):
        if start == n:
            result.append(path[:])
            return
        
        for end in range(start, n):
            if dp[start][end]:  # Use precomputed palindrome check
                path.append(s[start:end + 1])
                backtrack(end + 1, path)
                path.pop()
    
    result = []
    backtrack(0, [])
    return result

# Alternative approach using expand around center for palindrome check
def partition_expand_center(s):
    """
    Version using expand around center for palindrome detection.
    """
    def expand_palindromes(s):
        """Find all palindromic substrings using expand around center"""
        palindromes = set()
        n = len(s)
        
        def expand_around_center(left, right):
            while left >= 0 and right < n and s[left] == s[right]:
                palindromes.add((left, right))
                left -= 1
                right += 1
        
        for i in range(n):
            # Odd length palindromes
            expand_around_center(i, i)
            # Even length palindromes
            expand_around_center(i, i + 1)
        
        return palindromes
    
    palindrome_set = expand_palindromes(s)
    
    def backtrack(start, path):
        if start == len(s):
            result.append(path[:])
            return
        
        for end in range(start, len(s)):
            if (start, end) in palindrome_set:
                path.append(s[start:end + 1])
                backtrack(end + 1, path)
                path.pop()
    
    result = []
    backtrack(0, [])
    return result

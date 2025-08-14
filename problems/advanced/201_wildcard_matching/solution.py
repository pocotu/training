"""
Solution for Wildcard Matching
Problem ID: 201
LeetCode Problem: https://leetcode.com/problems/wildcard-matching/

Given an input string (s) and a pattern (p), implement wildcard pattern matching
with support for '?' and '*' where:
- '?' Matches any single character.
- '*' Matches any sequence of characters (including the empty sequence).
"""

def is_match_dp(s: str, p: str) -> bool:
    """
    Dynamic Programming approach (2D table).
    
    Args:
        s: Input string
        p: Pattern string with wildcards
        
    Returns:
        True if pattern matches string, False otherwise
        
    Time Complexity: O(m*n)
    Space Complexity: O(m*n)
    """
    m, n = len(s), len(p)
    
    # dp[i][j] represents whether s[0:i] matches p[0:j]
    dp = [[False] * (n + 1) for _ in range(m + 1)]
    
    # Empty pattern matches empty string
    dp[0][0] = True
    
    # Handle patterns like a* or *a* which can match empty string
    for j in range(1, n + 1):
        if p[j - 1] == '*':
            dp[0][j] = dp[0][j - 1]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if p[j - 1] == '*':
                # '*' can match empty string or any character
                dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
            elif p[j - 1] == '?' or s[i - 1] == p[j - 1]:
                # '?' matches any character, or exact character match
                dp[i][j] = dp[i - 1][j - 1]
    
    return dp[m][n]

def is_match_dp_optimized(s: str, p: str) -> bool:
    """
    Space-optimized DP approach (1D array).
    
    Args:
        s: Input string
        p: Pattern string with wildcards
        
    Returns:
        True if pattern matches string, False otherwise
        
    Time Complexity: O(m*n)
    Space Complexity: O(n)
    """
    m, n = len(s), len(p)
    
    # Use two arrays for current and previous row
    prev = [False] * (n + 1)
    curr = [False] * (n + 1)
    
    # Empty pattern matches empty string
    prev[0] = True
    
    # Handle patterns that can match empty string
    for j in range(1, n + 1):
        if p[j - 1] == '*':
            prev[j] = prev[j - 1]
    
    for i in range(1, m + 1):
        curr[0] = False  # Non-empty string can't match empty pattern
        
        for j in range(1, n + 1):
            if p[j - 1] == '*':
                curr[j] = prev[j] or curr[j - 1]
            elif p[j - 1] == '?' or s[i - 1] == p[j - 1]:
                curr[j] = prev[j - 1]
            else:
                curr[j] = False
        
        prev, curr = curr, prev
    
    return prev[n]

def is_match_recursive(s: str, p: str) -> bool:
    """
    Recursive approach with memoization.
    
    Args:
        s: Input string
        p: Pattern string with wildcards
        
    Returns:
        True if pattern matches string, False otherwise
        
    Time Complexity: O(m*n)
    Space Complexity: O(m*n)
    """
    memo = {}
    
    def helper(i: int, j: int) -> bool:
        if (i, j) in memo:
            return memo[(i, j)]
        
        # Base cases
        if j == len(p):
            result = i == len(s)
        elif i == len(s):
            # Pattern must be all '*' to match empty string
            result = all(c == '*' for c in p[j:])
        elif p[j] == '*':
            # '*' can match empty string or one or more characters
            result = helper(i, j + 1) or helper(i + 1, j)
        elif p[j] == '?' or s[i] == p[j]:
            result = helper(i + 1, j + 1)
        else:
            result = False
        
        memo[(i, j)] = result
        return result
    
    return helper(0, 0)

def is_match_greedy(s: str, p: str) -> bool:
    """
    Greedy approach with two pointers.
    Most space-efficient but complex logic.
    
    Args:
        s: Input string
        p: Pattern string with wildcards
        
    Returns:
        True if pattern matches string, False otherwise
        
    Time Complexity: O(m*n) worst case, O(m+n) average
    Space Complexity: O(1)
    """
    s_idx = p_idx = 0
    star_p = star_s = -1
    
    while s_idx < len(s):
        # Current characters match or pattern has '?'
        if p_idx < len(p) and (p[p_idx] == '?' or s[s_idx] == p[p_idx]):
            s_idx += 1
            p_idx += 1
        # Pattern has '*'
        elif p_idx < len(p) and p[p_idx] == '*':
            star_p = p_idx
            star_s = s_idx
            p_idx += 1
        # No match, but we have seen '*' before
        elif star_p != -1:
            p_idx = star_p + 1
            star_s += 1
            s_idx = star_s
        # No match and no '*' to fall back
        else:
            return False
    
    # Skip remaining '*' in pattern
    while p_idx < len(p) and p[p_idx] == '*':
        p_idx += 1
    
    return p_idx == len(p)

# Main function for the problem
def isMatch(s: str, p: str) -> bool:
    """
    Main solution function using the most efficient approach.
    """
    return is_match_greedy(s, p)

if __name__ == "__main__":
    # Test cases
    test_cases = [
        ("aa", "a", False),
        ("aa", "*", True),
        ("cb", "?a", False),
        ("adceb", "*a*b*", True),
        ("acdcb", "a*c?b", False),
        ("", "*", True),
        ("", "?", False),
        ("abc", "abc", True),
        ("abc", "a*c", True),
        ("abc", "a*b*c", True),
    ]
    
    print("=" * 60)
    print("WILDCARD MATCHING - COMPREHENSIVE TESTING")
    print("=" * 60)
    
    algorithms = [
        ("2D DP", is_match_dp),
        ("1D DP Optimized", is_match_dp_optimized),
        ("Recursive + Memo", is_match_recursive),
        ("Greedy Two Pointers", is_match_greedy),
    ]
    
    for i, (s, p, expected) in enumerate(test_cases, 1):
        print(f"\nTest Case {i}: s='{s}', p='{p}'")
        print(f"Expected: {expected}")
        
        for name, func in algorithms:
            try:
                result = func(s, p)
                status = "✓" if result == expected else "✗"
                print(f"  {name}: {result} {status}")
            except Exception as e:
                print(f"  {name}: ERROR - {e}")
    
    # Performance comparison
    print("\n" + "=" * 60)
    print("PERFORMANCE COMPARISON")
    print("=" * 60)
    
    import time
    
    # Large test case
    large_s = "a" * 1000 + "b"
    large_p = "*" + "a" * 500 + "*b"
    
    print(f"Large test: s length={len(large_s)}, p length={len(large_p)}")
    
    for name, func in algorithms:
        start_time = time.time()
        try:
            result = func(large_s, large_p)
            end_time = time.time()
            print(f"{name}: {result} in {end_time - start_time:.6f}s")
        except Exception as e:
            print(f"{name}: ERROR - {e}")
    
    # Edge cases
    print("\n" + "=" * 60)
    print("EDGE CASES")
    print("=" * 60)
    
    edge_cases = [
        ("", "", True),
        ("a", "", False),
        ("", "*", True),
        ("", "?", False),
        ("*", "*", True),
        ("?", "?", True),
    ]
    
    for s, p, expected in edge_cases:
        result = isMatch(s, p)
        status = "✓" if result == expected else "✗"
        print(f"s='{s}', p='{p}' -> {result} {status} (expected {expected})")

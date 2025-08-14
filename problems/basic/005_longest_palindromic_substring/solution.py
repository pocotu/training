"""
Longest Palindromic Substring - LeetCode Problem #5
Problem ID: 005

Given a string s, return the longest palindromic substring in s.

Time Complexity: O(n^2) for expand around centers approach
Space Complexity: O(1) for expand around centers approach
"""

def longest_palindrome(s):
    """
    Find longest palindromic substring using expand around centers approach.
    
    Args:
        s: Input string
        
    Returns:
        Longest palindromic substring
    """
    if not s:
        return ""
    
    start = 0
    max_len = 1
    
    for i in range(len(s)):
        # Check for odd-length palindromes (center is at i)
        len1 = expand_around_center(s, i, i)
        # Check for even-length palindromes (center is between i and i+1)
        len2 = expand_around_center(s, i, i + 1)
        
        # Get the maximum length palindrome centered at i
        current_max = max(len1, len2)
        
        # Update result if we found a longer palindrome
        if current_max > max_len:
            max_len = current_max
            # Calculate starting position
            start = i - (current_max - 1) // 2
    
    return s[start:start + max_len]

def expand_around_center(s, left, right):
    """
    Helper function to expand around center and find palindrome length.
    
    Args:
        s: Input string
        left: Left boundary
        right: Right boundary
        
    Returns:
        Length of palindrome centered between left and right
    """
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    
    # Return length of palindrome
    return right - left - 1

def longest_palindrome_dp(s):
    """
    Find longest palindromic substring using dynamic programming.
    
    Args:
        s: Input string
        
    Returns:
        Longest palindromic substring
    """
    if not s:
        return ""
    
    n = len(s)
    # dp[i][j] represents whether substring s[i:j+1] is palindrome
    dp = [[False] * n for _ in range(n)]
    
    start = 0
    max_len = 1
    
    # Every single character is a palindrome
    for i in range(n):
        dp[i][i] = True
    
    # Check for two-character palindromes
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            start = i
            max_len = 2
    
    # Check for palindromes of length 3 and more
    for length in range(3, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            
            # Check if s[i:j+1] is palindrome
            if s[i] == s[j] and dp[i + 1][j - 1]:
                dp[i][j] = True
                start = i
                max_len = length
    
    return s[start:start + max_len]

def longest_palindrome_manacher(s):
    """
    Find longest palindromic substring using Manacher's algorithm.
    Time Complexity: O(n), Space Complexity: O(n)
    
    Args:
        s: Input string
        
    Returns:
        Longest palindromic substring
    """
    if not s:
        return ""
    
    # Preprocess string: insert '#' between characters
    # "abc" becomes "#a#b#c#"
    processed = '#'.join('^{}$'.format(s))
    n = len(processed)
    
    # Array to store radius of palindrome at each position
    radius = [0] * n
    center = 0  # Center of rightmost palindrome
    right = 0   # Right boundary of rightmost palindrome
    
    max_len = 0
    center_index = 0
    
    for i in range(1, n - 1):
        # Mirror of i with respect to center
        mirror = 2 * center - i
        
        # If i is within right boundary, use previously computed values
        if i < right:
            radius[i] = min(right - i, radius[mirror])
        
        # Try to expand palindrome centered at i
        try:
            while processed[i + radius[i] + 1] == processed[i - radius[i] - 1]:
                radius[i] += 1
        except IndexError:
            pass
        
        # If palindrome centered at i extends past right, update center and right
        if i + radius[i] > right:
            center = i
            right = i + radius[i]
        
        # Update maximum length palindrome
        if radius[i] > max_len:
            max_len = radius[i]
            center_index = i
    
    # Extract the longest palindrome from original string
    start = (center_index - max_len) // 2
    return s[start:start + max_len]

def longest_palindrome_brute_force(s):
    """
    Brute force solution for comparison - O(n^3) time complexity.
    
    Args:
        s: Input string
        
    Returns:
        Longest palindromic substring
    """
    if not s:
        return ""
    
    def is_palindrome(substring):
        """Check if string is palindrome"""
        return substring == substring[::-1]
    
    max_len = 0
    result = ""
    
    # Check all possible substrings
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            substring = s[i:j]
            if is_palindrome(substring) and len(substring) > max_len:
                max_len = len(substring)
                result = substring
    
    return result

def find_all_palindromes(s):
    """
    Find all palindromic substrings in the string.
    
    Args:
        s: Input string
        
    Returns:
        List of all palindromic substrings
    """
    if not s:
        return []
    
    palindromes = set()
    
    for i in range(len(s)):
        # Find odd-length palindromes
        left, right = i, i
        while left >= 0 and right < len(s) and s[left] == s[right]:
            palindromes.add(s[left:right + 1])
            left -= 1
            right += 1
        
        # Find even-length palindromes
        left, right = i, i + 1
        while left >= 0 and right < len(s) and s[left] == s[right]:
            palindromes.add(s[left:right + 1])
            left -= 1
            right += 1
    
    return sorted(list(palindromes), key=len, reverse=True)

def count_palindromic_substrings(s):
    """
    Count total number of palindromic substrings.
    
    Args:
        s: Input string
        
    Returns:
        Number of palindromic substrings
    """
    if not s:
        return 0
    
    count = 0
    
    for i in range(len(s)):
        # Count odd-length palindromes
        count += expand_and_count(s, i, i)
        # Count even-length palindromes
        count += expand_and_count(s, i, i + 1)
    
    return count

def expand_and_count(s, left, right):
    """Helper function to expand and count palindromes"""
    count = 0
    while left >= 0 and right < len(s) and s[left] == s[right]:
        count += 1
        left -= 1
        right += 1
    return count

# Example usage and testing
if __name__ == "__main__":
    # Test cases from LeetCode
    test_cases = [
        "babad",      # Expected: "bab" or "aba"
        "cbbd",       # Expected: "bb"
        "a",          # Expected: "a"
        "ac",         # Expected: "a" or "c"
        "racecar",    # Expected: "racecar"
        "abcdef",     # Expected: any single character
        "aaaaaa",     # Expected: "aaaaaa"
        ""            # Expected: ""
    ]
    
    print("Testing Longest Palindromic Substring:")
    print("=" * 50)
    
    for i, s in enumerate(test_cases, 1):
        print(f"\nTest Case {i}: '{s}'")
        
        # Test all approaches
        result_expand = longest_palindrome(s)
        result_dp = longest_palindrome_dp(s)
        result_manacher = longest_palindrome_manacher(s)
        result_brute = longest_palindrome_brute_force(s)
        
        print(f"  Expand Around Centers: '{result_expand}' (length: {len(result_expand)})")
        print(f"  Dynamic Programming: '{result_dp}' (length: {len(result_dp)})")
        print(f"  Manacher's Algorithm: '{result_manacher}' (length: {len(result_manacher)})")
        print(f"  Brute Force: '{result_brute}' (length: {len(result_brute)})")
        
        # Verify all results have same length (different palindromes of same length are valid)
        lengths = [len(result_expand), len(result_dp), len(result_manacher), len(result_brute)]
        print(f"  All methods find same length: {len(set(lengths)) == 1}")
        
        # Find all palindromes for comparison
        all_palindromes = find_all_palindromes(s)
        if all_palindromes:
            print(f"  All palindromes: {all_palindromes[:5]}...")  # Show first 5
        
        # Count palindromic substrings
        count = count_palindromic_substrings(s)
        print(f"  Total palindromic substrings: {count}")
    
    # Performance comparison
    print("\n" + "=" * 50)
    print("Performance Test:")
    
    import time
    
    # Create a test string with known palindromes
    test_string = "abcdefghijklmnopqrstuvwxyzzyxwvutsrqponmlkjihgfedcba"
    
    algorithms = [
        ("Expand Around Centers", longest_palindrome),
        ("Dynamic Programming", longest_palindrome_dp),
        ("Manacher's Algorithm", longest_palindrome_manacher),
        ("Brute Force", longest_palindrome_brute_force)
    ]
    
    print(f"Test string length: {len(test_string)}")
    
    for name, func in algorithms:
        start_time = time.time()
        result = func(test_string)
        end_time = time.time()
        
        print(f"{name}: '{result[:10]}...' (length: {len(result)}) in {end_time - start_time:.6f} seconds")
    
    # Additional test cases
    print("\n" + "=" * 50)
    print("Additional Test Cases:")
    
    special_cases = [
        "abacabad",        # Multiple palindromes
        "forgeeksskeegfor", # Longer palindrome
        "AAAAAA",          # All same characters
        "ABCBA",           # Simple palindrome
        "ABCDCBA"          # Another palindrome
    ]
    
    for case in special_cases:
        result = longest_palindrome(case)
        all_palindromes = find_all_palindromes(case)
        longest_ones = [p for p in all_palindromes if len(p) == len(result)]
        
        print(f"'{case}' -> '{result}' (length: {len(result)})")
        if len(longest_ones) > 1:
            print(f"  Other longest palindromes: {longest_ones[1:]}")
        print(f"  Total palindromes: {count_palindromic_substrings(case)}")

"""
Longest Substring Without Repeating Characters - LeetCode Problem #3
Problem ID: 003

Given a string s, find the length of the longest substring without repeating characters.

Time Complexity: O(n)
Space Complexity: O(min(m,n)) where m is size of charset
"""

def length_of_longest_substring(s):
    """
    Find length of longest substring without repeating characters.
    Uses sliding window with hash map approach.
    
    Args:
        s: Input string
        
    Returns:
        Length of longest substring without repeating characters
    """
    if not s:
        return 0
    
    char_map = {}  # Character -> index mapping
    left = 0  # Left pointer of sliding window
    max_length = 0
    
    for right, char in enumerate(s):
        # If character is already in current window
        if char in char_map and char_map[char] >= left:
            # Move left pointer to position after the duplicate
            left = char_map[char] + 1
        
        # Update character position
        char_map[char] = right
        
        # Update max length
        max_length = max(max_length, right - left + 1)
    
    return max_length

def length_of_longest_substring_set(s):
    """
    Alternative solution using sliding window with set.
    
    Args:
        s: Input string
        
    Returns:
        Length of longest substring without repeating characters
    """
    if not s:
        return 0
    
    char_set = set()
    left = 0
    max_length = 0
    
    for right, char in enumerate(s):
        # Remove characters from left until no duplicate
        while char in char_set:
            char_set.remove(s[left])
            left += 1
        
        # Add current character
        char_set.add(char)
        
        # Update max length
        max_length = max(max_length, right - left + 1)
    
    return max_length

def length_of_longest_substring_optimized(s):
    """
    Optimized solution with better handling of character positions.
    
    Args:
        s: Input string
        
    Returns:
        Length of longest substring without repeating characters
    """
    if not s:
        return 0
    
    # Use dictionary to store last seen index of each character
    last_seen = {}
    start = 0
    max_length = 0
    
    for end, char in enumerate(s):
        # If character was seen before and is in current window
        if char in last_seen:
            # Move start to max of current start or position after last occurrence
            start = max(start, last_seen[char] + 1)
        
        # Update last seen position
        last_seen[char] = end
        
        # Update max length
        max_length = max(max_length, end - start + 1)
    
    return max_length

def length_of_longest_substring_brute_force(s):
    """
    Brute force solution for comparison - O(n^3) time complexity.
    
    Args:
        s: Input string
        
    Returns:
        Length of longest substring without repeating characters
    """
    if not s:
        return 0
    
    def has_unique_chars(substring):
        """Check if substring has all unique characters"""
        return len(substring) == len(set(substring))
    
    max_length = 0
    n = len(s)
    
    # Check all possible substrings
    for i in range(n):
        for j in range(i + 1, n + 1):
            substring = s[i:j]
            if has_unique_chars(substring):
                max_length = max(max_length, len(substring))
    
    return max_length

def find_longest_substring(s):
    """
    Returns the actual longest substring (not just length).
    
    Args:
        s: Input string
        
    Returns:
        Tuple of (length, substring)
    """
    if not s:
        return (0, "")
    
    char_map = {}
    left = 0
    max_length = 0
    start_pos = 0
    
    for right, char in enumerate(s):
        if char in char_map and char_map[char] >= left:
            left = char_map[char] + 1
        
        char_map[char] = right
        
        current_length = right - left + 1
        if current_length > max_length:
            max_length = current_length
            start_pos = left
    
    return (max_length, s[start_pos:start_pos + max_length])

# Example usage and testing
if __name__ == "__main__":
    # Test cases from LeetCode
    test_cases = [
        "abcabcbb",    # Expected: 3 ("abc")
        "bbbbb",       # Expected: 1 ("b")
        "pwwkew",      # Expected: 3 ("wke")
        "",            # Expected: 0
        "a",           # Expected: 1
        "abcdef",      # Expected: 6
        "dvdf"         # Expected: 3 ("vdf")
    ]
    
    print("Testing Longest Substring Without Repeating Characters:")
    print("=" * 60)
    
    for i, s in enumerate(test_cases, 1):
        print(f"\nTest Case {i}: '{s}'")
        
        # Test all three approaches
        result1 = length_of_longest_substring(s)
        result2 = length_of_longest_substring_set(s)
        result3 = length_of_longest_substring_optimized(s)
        result4 = length_of_longest_substring_brute_force(s)
        
        length, substring = find_longest_substring(s)
        
        print(f"  Hash Map Approach: {result1}")
        print(f"  Set Approach: {result2}")
        print(f"  Optimized Approach: {result3}")
        print(f"  Brute Force: {result4}")
        print(f"  Actual Substring: '{substring}' (length: {length})")
        print(f"  All methods agree: {result1 == result2 == result3 == result4}")
    
    # Performance comparison
    print("\n" + "=" * 60)
    print("Performance Test:")
    
    import time
    
    # Create a longer test string
    test_string = "abcdefghijklmnopqrstuvwxyz" * 100  # 2600 characters
    
    # Test optimized approach
    start_time = time.time()
    result_opt = length_of_longest_substring_optimized(test_string)
    opt_time = time.time() - start_time
    
    # Test set approach
    start_time = time.time()
    result_set = length_of_longest_substring_set(test_string)
    set_time = time.time() - start_time
    
    print(f"String length: {len(test_string)}")
    print(f"Optimized approach: {result_opt} in {opt_time:.6f} seconds")
    print(f"Set approach: {result_set} in {set_time:.6f} seconds")
    print(f"Results match: {result_opt == result_set}")
    
    # Additional test cases
    print("\n" + "=" * 60)
    print("Additional Test Cases:")
    
    special_cases = [
        "abba",           # Expected: 2 ("ab" or "ba")
        " ",              # Expected: 1 (space character)
        "au",             # Expected: 2
        "aab",            # Expected: 2 ("ab")
        "tmmzuxt"         # Expected: 5 ("mzuxt")
    ]
    
    for case in special_cases:
        length, substring = find_longest_substring(case)
        print(f"'{case}' -> Length: {length}, Substring: '{substring}'")

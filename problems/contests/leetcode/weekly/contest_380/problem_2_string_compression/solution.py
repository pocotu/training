"""
Solution for String Compression II - LeetCode Weekly Contest 380 Problem 2
Contest: Weekly Contest 380
Problem: 2
Difficulty: Medium
"""

from typing import List

def compress_two_pointers(chars: List[str]) -> int:
    """
    Two pointers approach for in-place string compression.
    
    Args:
        chars: List of characters to compress
        
    Returns:
        New length after compression
        
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if not chars:
        return 0
    
    write = 0  # Write pointer
    read = 0   # Read pointer
    
    while read < len(chars):
        current_char = chars[read]
        count = 0
        
        # Count consecutive occurrences
        while read < len(chars) and chars[read] == current_char:
            count += 1
            read += 1
        
        # Write the character
        chars[write] = current_char
        write += 1
        
        # Write the count if > 1
        if count > 1:
            count_str = str(count)
            for digit in count_str:
                chars[write] = digit
                write += 1
    
    return write

def compress_optimized(chars: List[str]) -> int:
    """
    Optimized version with better handling of large counts.
    
    Args:
        chars: List of characters to compress
        
    Returns:
        New length after compression
        
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    n = len(chars)
    if n <= 1:
        return n
    
    write_idx = 0
    i = 0
    
    while i < n:
        current_char = chars[i]
        count = 1
        
        # Count consecutive characters
        while i + count < n and chars[i + count] == current_char:
            count += 1
        
        # Write character
        chars[write_idx] = current_char
        write_idx += 1
        
        # Write count if more than 1
        if count > 1:
            # Convert count to string and write each digit
            for digit in str(count):
                chars[write_idx] = digit
                write_idx += 1
        
        i += count
    
    return write_idx

def compress_iterative(chars: List[str]) -> int:
    """
    Iterative approach with explicit state tracking.
    
    Args:
        chars: List of characters to compress
        
    Returns:
        New length after compression
        
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if not chars:
        return 0
    
    result_length = 0
    i = 0
    
    while i < len(chars):
        current_char = chars[i]
        count = 1
        
        # Find end of current group
        j = i + 1
        while j < len(chars) and chars[j] == current_char:
            count += 1
            j += 1
        
        # Place character at result position
        chars[result_length] = current_char
        result_length += 1
        
        # Place count digits if count > 1
        if count > 1:
            count_digits = str(count)
            for digit in count_digits:
                chars[result_length] = digit
                result_length += 1
        
        i = j  # Move to next group
    
    return result_length

def compress_single_pass(chars: List[str]) -> int:
    """
    Single pass solution with minimal operations.
    
    Args:
        chars: List of characters to compress
        
    Returns:
        New length after compression
        
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if len(chars) <= 1:
        return len(chars)
    
    anchor = write = 0
    
    for read in range(len(chars) + 1):
        # Process group when we reach end or find different character
        if read == len(chars) or chars[read] != chars[anchor]:
            # Write the character
            chars[write] = chars[anchor]
            write += 1
            
            # Write count if group size > 1
            group_size = read - anchor
            if group_size > 1:
                for c in str(group_size):
                    chars[write] = c
                    write += 1
            
            anchor = read
    
    return write

# Main function for the contest problem
def compress(chars: List[str]) -> int:
    """
    Main solution for contest submission.
    """
    return compress_optimized(chars)

if __name__ == "__main__":
    # Test cases from the problem
    test_cases = [
        # Basic examples
        (["a","a","b","b","c","c","c"], 6, ["a","2","b","2","c","3"]),
        (["a"], 1, ["a"]),
        (["a","b","b","b","b","b","b","b","b","b","b","b","b"], 4, ["a","b","1","2"]),
        
        # Edge cases
        (["a","a"], 2, ["a","2"]),
        (["a","a","a","a","a","a","a","a","a","a"], 3, ["a","1","0"]),
        (["a","b","c"], 3, ["a","b","c"]),
        (["a","a","a","b","b","a","a"], 6, ["a","3","b","2","a","2"]),
        
        # Large counts
        (["a"] * 100, 4, ["a","1","0","0"]),
        (["a"] * 12 + ["b"] * 3, 6, ["a","1","2","b","3"]),
        
        # Mixed patterns
        (["a","b","b","c","c","c","d"], 7, ["a","b","2","c","3","d"]),
    ]
    
    print("=" * 60)
    print("STRING COMPRESSION II - CONTEST TESTING")
    print("=" * 60)
    
    algorithms = [
        ("Two Pointers", compress_two_pointers),
        ("Optimized", compress_optimized),
        ("Iterative", compress_iterative),
        ("Single Pass", compress_single_pass),
    ]
    
    for i, (chars_input, expected_length, expected_result) in enumerate(test_cases):
        print(f"\nTest Case {i + 1}:")
        print(f"  Input: {chars_input}")
        print(f"  Expected Length: {expected_length}")
        print(f"  Expected Result: {expected_result}")
        
        for name, func in algorithms:
            try:
                # Make a copy for testing
                chars_copy = chars_input.copy()
                
                import time
                start_time = time.time()
                result_length = func(chars_copy)
                end_time = time.time()
                
                # Check result
                result_array = chars_copy[:result_length]
                length_correct = result_length == expected_length
                array_correct = result_array == expected_result
                
                status = "✓" if (length_correct and array_correct) else "✗"
                print(f"  {name}: length={result_length}, result={result_array} {status} ({end_time - start_time:.6f}s)")
                
                if not length_correct:
                    print(f"    Expected length {expected_length}, got {result_length}")
                if not array_correct:
                    print(f"    Expected {expected_result}, got {result_array}")
                
            except Exception as e:
                print(f"  {name}: ERROR - {e}")
    
    # Performance testing
    print("\n" + "=" * 60)
    print("PERFORMANCE TESTING")
    print("=" * 60)
    
    import random
    import time
    
    def generate_test_chars(size, pattern="random"):
        """Generate test character arrays with different patterns."""
        if pattern == "random":
            chars = ['a', 'b', 'c', 'd', 'e']
            return [random.choice(chars) for _ in range(size)]
        elif pattern == "repetitive":
            # Mostly repeated characters
            return ['a'] * (size // 2) + ['b'] * (size // 4) + ['c'] * (size // 4)
        elif pattern == "alternating":
            return ['a' if i % 2 == 0 else 'b' for i in range(size)]
        elif pattern == "no_compression":
            # Each character appears only once
            chars = []
            for i in range(size):
                chars.append(chr(ord('a') + (i % 26)))
            return chars
    
    performance_tests = [
        ("Small Random", 100, "random"),
        ("Medium Random", 500, "random"),
        ("Large Random", 1000, "random"),
        ("Repetitive Pattern", 1000, "repetitive"),
        ("Alternating Pattern", 1000, "alternating"),
        ("No Compression", 1000, "no_compression"),
    ]
    
    for test_name, size, pattern in performance_tests:
        print(f"\n{test_name} (size {size}):")
        
        test_chars = generate_test_chars(size, pattern)
        
        for name, func in algorithms:
            try:
                chars_copy = test_chars.copy()
                
                start_time = time.time()
                result_length = func(chars_copy)
                end_time = time.time()
                
                compression_ratio = result_length / size * 100
                print(f"  {name}: length={result_length} ({compression_ratio:.1f}%), time={end_time - start_time:.6f}s")
                
            except Exception as e:
                print(f"  {name}: ERROR - {e}")
    
    # Contest simulation
    print("\n" + "=" * 60)
    print("CONTEST SIMULATION")
    print("=" * 60)
    
    print("Contest Problem 2: String Compression II")
    print("Difficulty: Medium (4 points)")
    print("Expected Time: 12-18 minutes")
    print("\nKey Insights:")
    print("  • Use two pointers: one for reading, one for writing")
    print("  • Count consecutive characters in groups")
    print("  • Handle count > 1 by converting to string digits")
    print("  • In-place modification requires careful index management")
    
    print("\nContest Strategy:")
    print("  1. Understand in-place requirement (2 mins)")
    print("  2. Design two-pointer approach (3 mins)")
    print("  3. Handle count conversion carefully (5 mins)")
    print("  4. Test with examples, especially large counts (3-5 mins)")
    print("  5. Debug edge cases (2-3 mins)")
    
    print("\nCommon Mistakes to Avoid:")
    print("  • Forgetting to handle counts >= 10 (multi-digit)")
    print("  • Incorrect index management in two-pointer approach")
    print("  • Not handling single characters (count = 1) correctly")
    print("  • Off-by-one errors in group counting")
    print("  • Modifying array while reading from same positions")

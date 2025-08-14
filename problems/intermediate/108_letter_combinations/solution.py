"""
Letter Combinations of a Phone Number - LeetCode Problem #17
Problem ID: 108

Given a string containing digits from 2-9 inclusive, return all possible letter 
combinations that the number could represent.

Time Complexity: O(3^m * 4^n) where m is number of digits with 3 letters, n is number with 4
Space Complexity: O(3^m * 4^n) for the output
"""

def letter_combinations(digits):
    """
    Generate all letter combinations using backtracking.
    
    Args:
        digits: String of digits 2-9
        
    Returns:
        List of all possible letter combinations
    """
    if not digits:
        return []
    
    # Mapping of digits to letters
    phone_map = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
    result = []
    
    def backtrack(index, path):
        # Base case: we've processed all digits
        if index == len(digits):
            result.append(path)
            return
        
        # Get letters for current digit
        current_digit = digits[index]
        letters = phone_map[current_digit]
        
        # Try each letter for current digit
        for letter in letters:
            backtrack(index + 1, path + letter)
    
    backtrack(0, "")
    return result

def letter_combinations_iterative(digits):
    """
    Iterative solution using queue/list.
    
    Args:
        digits: String of digits 2-9
        
    Returns:
        List of all possible letter combinations
    """
    if not digits:
        return []
    
    phone_map = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
    result = [""]
    
    for digit in digits:
        letters = phone_map[digit]
        result = [prefix + letter for prefix in result for letter in letters]
    
    return result

def letter_combinations_bfs(digits):
    """
    BFS approach using queue.
    
    Args:
        digits: String of digits 2-9
        
    Returns:
        List of all possible letter combinations
    """
    if not digits:
        return []
    
    from collections import deque
    
    phone_map = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
    queue = deque([""])
    
    for digit in digits:
        letters = phone_map[digit]
        for _ in range(len(queue)):
            prefix = queue.popleft()
            for letter in letters:
                queue.append(prefix + letter)
    
    return list(queue)

# Example usage and testing
if __name__ == "__main__":
    test_cases = [
        "23",     # Expected: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
        "",       # Expected: []
        "2",      # Expected: ["a","b","c"]
        "234",    # Expected: 27 combinations
        "7"       # Expected: ["p","q","r","s"]
    ]
    
    print("Testing Letter Combinations of Phone Number:")
    print("=" * 50)
    
    for i, digits in enumerate(test_cases, 1):
        print(f"\nTest Case {i}: digits = '{digits}'")
        
        # Test all approaches
        result1 = letter_combinations(digits)
        result2 = letter_combinations_iterative(digits)
        result3 = letter_combinations_bfs(digits)
        
        print(f"  Backtracking: {result1[:10]}{'...' if len(result1) > 10 else ''}")
        print(f"  Iterative: {result2[:10]}{'...' if len(result2) > 10 else ''}")
        print(f"  BFS: {result3[:10]}{'...' if len(result3) > 10 else ''}")
        print(f"  Count: {len(result1)}")
        print(f"  All methods agree: {result1 == result2 == result3}")
    
    # Performance test
    print("\n" + "=" * 50)
    print("Performance Test:")
    
    import time
    
    test_digits = "2345"  # Should generate 3*3*3*3 = 81 combinations
    
    algorithms = [
        ("Backtracking", letter_combinations),
        ("Iterative", letter_combinations_iterative),
        ("BFS", letter_combinations_bfs)
    ]
    
    for name, func in algorithms:
        start_time = time.time()
        result = func(test_digits)
        end_time = time.time()
        
        print(f"{name}: {len(result)} combinations in {end_time - start_time:.6f} seconds")
    
    # Edge cases
    print("\n" + "=" * 50)
    print("Edge Cases:")
    
    edge_cases = ["9", "22", "999"]
    
    for case in edge_cases:
        result = letter_combinations(case)
        print(f"'{case}' -> {len(result)} combinations: {result[:5]}{'...' if len(result) > 5 else ''}")

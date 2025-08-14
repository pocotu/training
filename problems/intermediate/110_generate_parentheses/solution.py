"""
Generate Parentheses - LeetCode Problem #22
Problem ID: 110

Given n pairs of parentheses, write a function to generate all combinations 
of well-formed parentheses.

Time Complexity: O(4^n / sqrt(n)) - Catalan number
Space Complexity: O(4^n / sqrt(n)) for the output
"""

def generate_parenthesis(n):
    """
    Generate all valid parentheses combinations using backtracking.
    
    Args:
        n: Number of pairs of parentheses
        
    Returns:
        List of all valid parentheses combinations
    """
    result = []
    
    def backtrack(current, open_count, close_count):
        # Base case: we've used all n pairs
        if len(current) == 2 * n:
            result.append(current)
            return
        
        # Add opening parenthesis if we haven't used all n
        if open_count < n:
            backtrack(current + "(", open_count + 1, close_count)
        
        # Add closing parenthesis if it won't exceed opening ones
        if close_count < open_count:
            backtrack(current + ")", open_count, close_count + 1)
    
    backtrack("", 0, 0)
    return result

def generate_parenthesis_dp(n):
    """
    Dynamic programming solution.
    
    Args:
        n: Number of pairs of parentheses
        
    Returns:
        List of all valid parentheses combinations
    """
    if n == 0:
        return [""]
    
    result = []
    
    # For each way to split n pairs into left and right parts
    for i in range(n):
        # i pairs inside first parentheses, n-1-i pairs after
        left_combos = generate_parenthesis_dp(i)
        right_combos = generate_parenthesis_dp(n - 1 - i)
        
        for left in left_combos:
            for right in right_combos:
                result.append(f"({left}){right}")
    
    return result

def generate_parenthesis_iterative(n):
    """
    Iterative solution using BFS approach.
    
    Args:
        n: Number of pairs of parentheses
        
    Returns:
        List of all valid parentheses combinations
    """
    from collections import deque
    
    # Queue stores (current_string, open_count, close_count)
    queue = deque([("", 0, 0)])
    result = []
    
    while queue:
        current, open_count, close_count = queue.popleft()
        
        # If we've used all pairs, add to result
        if len(current) == 2 * n:
            result.append(current)
            continue
        
        # Add opening parenthesis if possible
        if open_count < n:
            queue.append((current + "(", open_count + 1, close_count))
        
        # Add closing parenthesis if possible
        if close_count < open_count:
            queue.append((current + ")", open_count, close_count + 1))
    
    return result

def is_valid_parentheses(s):
    """
    Helper function to validate parentheses string.
    
    Args:
        s: String to validate
        
    Returns:
        True if valid, False otherwise
    """
    count = 0
    for char in s:
        if char == '(':
            count += 1
        elif char == ')':
            count -= 1
            if count < 0:
                return False
    return count == 0

def count_valid_parentheses(n):
    """
    Count total number of valid parentheses combinations (Catalan number).
    
    Args:
        n: Number of pairs
        
    Returns:
        Count of valid combinations
    """
    if n <= 1:
        return 1
    
    # Catalan number formula: C(n) = (2n)! / ((n+1)! * n!)
    # Or recursive: C(n) = sum(C(i) * C(n-1-i)) for i in range(n)
    
    catalan = [0] * (n + 1)
    catalan[0] = catalan[1] = 1
    
    for i in range(2, n + 1):
        for j in range(i):
            catalan[i] += catalan[j] * catalan[i - 1 - j]
    
    return catalan[n]

# Example usage and testing
if __name__ == "__main__":
    test_cases = [1, 2, 3, 4]
    
    print("Testing Generate Parentheses:")
    print("=" * 40)
    
    for n in test_cases:
        print(f"\nTest Case n = {n}:")
        
        # Test all approaches
        result1 = generate_parenthesis(n)
        result2 = generate_parenthesis_dp(n)
        result3 = generate_parenthesis_iterative(n)
        
        print(f"  Backtracking: {result1}")
        print(f"  Dynamic Programming: {result2}")
        print(f"  Iterative: {result3}")
        print(f"  Count: {len(result1)}")
        print(f"  Expected (Catalan): {count_valid_parentheses(n)}")
        print(f"  All methods agree: {sorted(result1) == sorted(result2) == sorted(result3)}")
        
        # Validate all results
        all_valid = all(is_valid_parentheses(s) for s in result1)
        print(f"  All results valid: {all_valid}")
    
    # Performance comparison
    print("\n" + "=" * 40)
    print("Performance Test (n=6):")
    
    import time
    
    algorithms = [
        ("Backtracking", generate_parenthesis),
        ("Dynamic Programming", generate_parenthesis_dp),
        ("Iterative", generate_parenthesis_iterative)
    ]
    
    n = 6
    for name, func in algorithms:
        start_time = time.time()
        result = func(n)
        end_time = time.time()
        
        print(f"{name}: {len(result)} combinations in {end_time - start_time:.6f} seconds")
    
    # Catalan numbers
    print("\n" + "=" * 40)
    print("Catalan Numbers (Valid Parentheses Count):")
    
    for i in range(1, 8):
        count = count_valid_parentheses(i)
        actual = len(generate_parenthesis(i))
        print(f"n={i}: Catalan={count}, Actual={actual}, Match={count == actual}")
    
    # Edge cases
    print("\n" + "=" * 40)
    print("Edge Cases:")
    
    # n = 0 case
    result_0 = generate_parenthesis(0) if 0 >= 0 else []
    print(f"n=0: {result_0}")
    
    # Large n warning
    print(f"Note: For n=8, there are {count_valid_parentheses(8)} combinations")
    print(f"Note: For n=10, there are {count_valid_parentheses(10)} combinations")

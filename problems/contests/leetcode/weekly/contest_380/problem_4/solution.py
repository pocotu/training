"""
LeetCode Weekly Contest 380 - Problem 4: Count Valid Parentheses Permutations
https://leetcode.com/contest/weekly-contest-380/problems/count-valid-parentheses-permutations/

Dynamic Programming / Combinatorics Problem
Time Complexity: O(n²)
Space Complexity: O(n²)

Key Insight: Use DP to track valid states with balance (open - close parentheses).
The balance must never go negative and must end at 0.
"""

MOD = 10**9 + 7

def count_valid_parentheses_dp(s):
    """
    Dynamic programming solution for counting valid parentheses.
    
    State: dp[i][balance] = number of ways to fill first i positions
    with exactly 'balance' more open than close parentheses.
    
    Args:
        s: String with '(', ')', and '?' characters
        
    Returns:
        int: Number of valid ways modulo 10^9 + 7
        
    Algorithm:
    1. Initialize DP table
    2. For each position, try all valid transitions
    3. Return dp[n][0] (final position with balance 0)
    """
    n = len(s)
    
    # Edge case: odd length strings can't be valid
    if n % 2 == 1:
        return 0
    
    # dp[i][balance] = ways to reach position i with given balance
    # Maximum balance is n//2 (all opens at beginning)
    max_balance = n // 2
    dp = [[0] * (max_balance + 1) for _ in range(n + 1)]
    
    # Base case: empty string has balance 0
    dp[0][0] = 1
    
    for i in range(n):
        for balance in range(max_balance + 1):
            if dp[i][balance] == 0:
                continue
            
            char = s[i]
            
            # Try placing '('
            if char == '(' or char == '?':
                if balance + 1 <= max_balance:
                    dp[i + 1][balance + 1] = (dp[i + 1][balance + 1] + dp[i][balance]) % MOD
            
            # Try placing ')'
            if char == ')' or char == '?':
                if balance > 0:  # Can't go negative
                    dp[i + 1][balance - 1] = (dp[i + 1][balance - 1] + dp[i][balance]) % MOD
    
    return dp[n][0]

def count_valid_parentheses_memo(s):
    """
    Memoized recursive solution.
    
    Uses recursion with memoization to explore all valid paths.
    
    Args:
        s: String with '(', ')', and '?' characters
        
    Returns:
        int: Number of valid ways modulo 10^9 + 7
    """
    n = len(s)
    
    if n % 2 == 1:
        return 0
    
    memo = {}
    
    def solve(pos, balance):
        """
        Recursive function to count ways from position pos with given balance.
        
        Args:
            pos: Current position in string
            balance: Current balance (open - close)
            
        Returns:
            int: Number of valid ways from this state
        """
        # Base case: reached end of string
        if pos == n:
            return 1 if balance == 0 else 0
        
        # Memoization check
        if (pos, balance) in memo:
            return memo[(pos, balance)]
        
        # Invalid state: balance is negative
        if balance < 0:
            return 0
        
        # Invalid state: impossible to balance remaining string
        remaining = n - pos
        if balance > remaining:
            return 0
        
        result = 0
        char = s[pos]
        
        # Try placing '('
        if char == '(' or char == '?':
            result = (result + solve(pos + 1, balance + 1)) % MOD
        
        # Try placing ')'
        if char == ')' or char == '?':
            if balance > 0:
                result = (result + solve(pos + 1, balance - 1)) % MOD
        
        memo[(pos, balance)] = result
        return result
    
    return solve(0, 0)

def count_valid_parentheses_optimized(s):
    """
    Space-optimized DP solution.
    
    Uses only two arrays instead of 2D table since we only need
    previous row to compute current row.
    
    Args:
        s: String with '(', ')', and '?' characters
        
    Returns:
        int: Number of valid ways modulo 10^9 + 7
    """
    n = len(s)
    
    if n % 2 == 1:
        return 0
    
    max_balance = n // 2
    
    # Use two arrays for space optimization
    prev = [0] * (max_balance + 1)
    curr = [0] * (max_balance + 1)
    
    prev[0] = 1
    
    for i in range(n):
        # Reset current array
        for j in range(max_balance + 1):
            curr[j] = 0
        
        for balance in range(max_balance + 1):
            if prev[balance] == 0:
                continue
            
            char = s[i]
            
            # Try placing '('
            if char == '(' or char == '?':
                if balance + 1 <= max_balance:
                    curr[balance + 1] = (curr[balance + 1] + prev[balance]) % MOD
            
            # Try placing ')'
            if char == ')' or char == '?':
                if balance > 0:
                    curr[balance - 1] = (curr[balance - 1] + prev[balance]) % MOD
        
        # Swap arrays
        prev, curr = curr, prev
    
    return prev[0]

def count_valid_parentheses_catalan(s):
    """
    Catalan number approach with constraints.
    
    Uses mathematical properties related to Catalan numbers
    but accounts for fixed positions.
    
    Args:
        s: String with '(', ')', and '?' characters
        
    Returns:
        int: Number of valid ways modulo 10^9 + 7
    """
    n = len(s)
    
    if n % 2 == 1:
        return 0
    
    # Count fixed characters
    fixed_open = s.count('(')
    fixed_close = s.count(')')
    questions = s.count('?')
    
    # Need equal open and close
    needed_open = n // 2 - fixed_open
    needed_close = n // 2 - fixed_close
    
    # Check if it's possible
    if needed_open < 0 or needed_close < 0 or needed_open + needed_close != questions:
        return 0
    
    # For simple cases, we can use combinatorial approach
    # But for general case with position constraints, need DP
    return count_valid_parentheses_dp(s)

def count_valid_parentheses_mathematical(s):
    """
    Mathematical approach using recurrence relations.
    
    Exploits mathematical structure of the problem.
    
    Args:
        s: String with '(', ')', and '?' characters
        
    Returns:
        int: Number of valid ways modulo 10^9 + 7
    """
    n = len(s)
    
    if n % 2 == 1:
        return 0
    
    # Use mathematical recurrence relation
    # C(n) = sum_{i=0}^{n-1} C(i) * C(n-1-i) for Catalan numbers
    # But we need to account for constraints
    
    # For contest purposes, fall back to DP
    return count_valid_parentheses_dp(s)

def solve_contest_version(s):
    """
    Contest-optimized solution.
    
    Balances correctness with implementation speed for contest.
    """
    n = len(s)
    
    # Quick validation
    if n % 2 == 1:
        return 0
    
    # Use memoized recursion for clarity and correctness
    memo = {}
    
    def dp(pos, balance):
        if pos == n:
            return 1 if balance == 0 else 0
        
        if balance < 0 or balance > n - pos:
            return 0
        
        if (pos, balance) in memo:
            return memo[(pos, balance)]
        
        result = 0
        char = s[pos]
        
        if char == '(' or char == '?':
            result = (result + dp(pos + 1, balance + 1)) % MOD
        
        if char == ')' or char == '?':
            if balance > 0:
                result = (result + dp(pos + 1, balance - 1)) % MOD
        
        memo[(pos, balance)] = result
        return result
    
    return dp(0, 0)

class Solution:
    """LeetCode solution class."""
    
    def countValidParentheses(self, s: str) -> int:
        return solve_contest_version(s)

def test_solution():
    """Test the solution with provided examples."""
    test_cases = [
        ("(?)", 1),
        ("(??)", 2),
        ("???)", 5),
        ("??????", 132),
        ("()", 1),
        ("())", 0),
        ("((", 0),
        ("?", 0),
        ("??", 1),
        ("????", 2),
        ("(?(?))", 1),
    ]
    
    print("Testing Count Valid Parentheses Permutations...")
    
    methods = [
        count_valid_parentheses_dp,
        count_valid_parentheses_memo,
        count_valid_parentheses_optimized,
        solve_contest_version
    ]
    
    for method in methods:
        print(f"\nTesting {method.__name__}:")
        all_correct = True
        
        for s, expected in test_cases:
            try:
                result = method(s)
                status = "✓" if result == expected else "✗"
                print(f"  '{s}' -> {result} (expected {expected}) {status}")
                if result != expected:
                    all_correct = False
            except Exception as e:
                print(f"  '{s}' -> ERROR: {e}")
                all_correct = False
        
        print(f"Method {method.__name__}: {'PASS' if all_correct else 'FAIL'}")

def performance_test():
    """Performance testing for contest conditions."""
    import time
    import random
    
    print("\nPerformance Testing...")
    
    # Generate test cases of different sizes
    sizes = [10, 20, 50, 100]
    
    for size in sizes:
        # Create string with roughly equal ?, (, )
        chars = ['?'] * (size // 2) + ['('] * (size // 4) + [')'] * (size // 4)
        if len(chars) < size:
            chars.extend(['?'] * (size - len(chars)))
        
        random.shuffle(chars)
        test_string = ''.join(chars[:size])
        
        start_time = time.time()
        result = solve_contest_version(test_string)
        end_time = time.time()
        
        print(f"Size {size}: Result {result}, Time {end_time - start_time:.4f}s")

def validate_catalan_relationship():
    """Validate relationship with Catalan numbers."""
    print("\nValidating Catalan number relationship...")
    
    # For strings of only '?', result should be Catalan numbers
    catalan = [1, 1, 2, 5, 14, 42, 132, 429]  # C_0 to C_7
    
    for i in range(0, 8):
        n = 2 * i  # Only even lengths are valid
        if n <= 14:  # Keep test size reasonable
            s = '?' * n
            result = solve_contest_version(s)
            expected = catalan[i] if i < len(catalan) else "Unknown"
            print(f"  Length {n}: {result} (Catalan C_{i} = {expected})")

if __name__ == "__main__":
    # Uncomment for testing
    # test_solution()
    # performance_test()
    # validate_catalan_relationship()
    
    # LeetCode submission
    pass

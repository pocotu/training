"""
Codeforces Round #915 (Div. 2) - Problem A: Number Game
https://codeforces.com/contest/1915/problem/A

Game Theory / Mathematics Problem
Time Complexity: O(1)
Space Complexity: O(1)

Key Insight: This is a pattern-based game theory problem.
The winner depends on the mathematical properties of n.
"""

def solve_number_game(n):
    """
    Determine winner of the number game with optimal play.
    
    Game Rules:
    - Players alternate turns, Alice goes first
    - Each turn: subtract any positive divisor of current number
    - Cannot subtract the number itself if it makes result 0 (unless winning move)
    - Player who cannot move loses
    
    Args:
        n: Starting positive integer
        
    Returns:
        str: "Alice" or "Bob" indicating the winner
        
    Pattern Analysis:
    - n = 1: Alice wins (subtracts 1, game ends)
    - n = 2: Alice wins (subtracts 2, game ends)
    - n = 3: Alice wins (subtracts 3, game ends)
    - n = 4: Bob wins (Alice forced into losing position)
    
    Mathematical Pattern:
    - If n is odd: Alice wins (subtract 1, leave even for Bob)
    - If n is even: depends on whether n/2 is odd or even
    - If n = 2^k for k > 1: Bob wins
    - If n = 2 * odd: Alice wins
    """
    # Pattern Recognition Approach
    if n % 2 == 1:
        # Odd numbers: Alice always wins
        return "Alice"
    else:
        # Even numbers: check if power of 2
        temp = n
        while temp % 2 == 0:
            temp //= 2
        
        if temp == 1:
            # n is a power of 2
            return "Bob"
        else:
            # n = 2 * odd number
            return "Alice"

def solve_optimized(n):
    """
    Optimized solution using direct mathematical analysis.
    
    Key insight: Alice wins except when n is a power of 2 greater than 2.
    
    Args:
        n: Starting positive integer
        
    Returns:
        str: Winner of the game
    """
    if n == 1 or n == 2:
        return "Alice"
    
    # Check if n is a power of 2 and greater than 2
    if n > 2 and (n & (n - 1)) == 0:
        return "Bob"
    
    return "Alice"

def solve_game_theory(n):
    """
    Complete game theory analysis for educational purposes.
    
    This approach demonstrates the full game theory reasoning
    but is not necessary for contest efficiency.
    """
    # Memoization for smaller values (educational)
    memo = {}
    
    def is_losing_position(num):
        if num in memo:
            return memo[num]
        
        if num == 0:
            memo[num] = True
            return True
        
        # Try all possible moves
        for divisor in get_divisors(num):
            if divisor == num:
                # Can only subtract n if it's a winning move
                if num - divisor == 0:
                    memo[num] = False
                    return False
            else:
                # Regular move
                if is_losing_position(num - divisor):
                    memo[num] = False
                    return False
        
        memo[num] = True
        return True
    
    # For large n, use pattern recognition
    if n <= 100:
        return "Bob" if is_losing_position(n) else "Alice"
    else:
        return solve_optimized(n)

def get_divisors(n):
    """Get all positive divisors of n."""
    divisors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    return sorted(divisors)

def solve_pattern_analysis(n):
    """
    Solution using complete pattern analysis.
    
    Pattern Discovery:
    n=1: Alice (A wins)
    n=2: Alice (A wins)  
    n=3: Alice (A wins)
    n=4: Bob (B wins)
    n=5: Alice (A wins)
    n=6: Alice (A wins)
    n=7: Alice (A wins)
    n=8: Bob (B wins)
    ...
    
    Pattern: Bob wins only when n is a power of 2 greater than 2
    """
    # Direct pattern implementation
    if n <= 2:
        return "Alice"
    
    # Check if n is power of 2
    power_of_2 = True
    temp = n
    while temp > 1:
        if temp % 2 != 0:
            power_of_2 = False
            break
        temp //= 2
    
    return "Bob" if power_of_2 else "Alice"

def main():
    """Main function for contest submission."""
    t = int(input())
    for _ in range(t):
        n = int(input())
        print(solve_optimized(n))

def test_solution():
    """Comprehensive test suite for validation."""
    test_cases = [
        # Basic test cases
        (1, "Alice"),
        (2, "Alice"), 
        (3, "Alice"),
        (4, "Bob"),
        (5, "Alice"),
        (6, "Alice"),
        (7, "Alice"),
        (8, "Bob"),
        (9, "Alice"),
        (10, "Alice"),
        
        # Powers of 2
        (16, "Bob"),
        (32, "Bob"),
        (64, "Bob"),
        (128, "Bob"),
        (256, "Bob"),
        
        # Large odd numbers
        (999999999, "Alice"),
        (999999997, "Alice"),
        
        # Large even non-powers of 2
        (999999998, "Alice"),
        (999999996, "Alice"),
        
        # Edge cases
        (1000000000, "Alice"),  # 2^9 * 5^9 * something
    ]
    
    print("Testing Number Game Solution...")
    all_methods = [solve_number_game, solve_optimized, solve_pattern_analysis]
    
    for method in all_methods:
        print(f"\nTesting {method.__name__}:")
        all_correct = True
        
        for n, expected in test_cases:
            result = method(n)
            status = "✓" if result == expected else "✗"
            print(f"  n={n}: {result} {status}")
            if result != expected:
                all_correct = False
                print(f"    Expected: {expected}, Got: {result}")
        
        print(f"Method {method.__name__}: {'PASS' if all_correct else 'FAIL'}")

def performance_test():
    """Performance testing for contest conditions."""
    import time
    import random
    
    print("\nPerformance Testing...")
    
    # Test with large inputs
    test_inputs = []
    for _ in range(1000):
        test_inputs.append(random.randint(1, 10**9))
    
    start_time = time.time()
    for n in test_inputs:
        solve_optimized(n)
    end_time = time.time()
    
    print(f"Processed 1000 large inputs in {end_time - start_time:.4f} seconds")
    print(f"Average time per test case: {(end_time - start_time) / 1000:.6f} seconds")

if __name__ == "__main__":
    # Uncomment for testing
    # test_solution()
    # performance_test()
    
    # Contest submission
    main()

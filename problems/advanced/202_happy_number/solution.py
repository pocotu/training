"""
Solution for Happy Number
Problem ID: 202
LeetCode Problem: https://leetcode.com/problems/happy-number/

Write an algorithm to determine if a number n is happy.
A happy number is defined by the following process:
- Start with any positive integer, replace with sum of squares of digits
- Repeat until number equals 1 (happy) or loops endlessly (not happy)
"""

def is_happy_set(n: int) -> bool:
    """
    Hash set approach to detect cycles.
    
    Args:
        n: Input number to check
        
    Returns:
        True if number is happy, False otherwise
        
    Time Complexity: O(log n) - digits in number
    Space Complexity: O(log n) - for cycle detection set
    """
    def get_sum_of_squares(num):
        """Calculate sum of squares of digits."""
        total = 0
        while num > 0:
            digit = num % 10
            total += digit * digit
            num //= 10
        return total
    
    seen = set()
    
    while n != 1 and n not in seen:
        seen.add(n)
        n = get_sum_of_squares(n)
    
    return n == 1

def is_happy_floyd(n: int) -> bool:
    """
    Floyd's Cycle Detection (Tortoise and Hare) approach.
    
    Args:
        n: Input number to check
        
    Returns:
        True if number is happy, False otherwise
        
    Time Complexity: O(log n)
    Space Complexity: O(1) - constant space
    """
    def get_sum_of_squares(num):
        """Calculate sum of squares of digits."""
        total = 0
        while num > 0:
            digit = num % 10
            total += digit * digit
            num //= 10
        return total
    
    slow = n
    fast = n
    
    # Move pointers until they meet or reach 1
    while True:
        slow = get_sum_of_squares(slow)           # Move one step
        fast = get_sum_of_squares(get_sum_of_squares(fast))  # Move two steps
        
        if slow == 1 or fast == 1:
            return True
        
        if slow == fast:  # Cycle detected
            return False

def is_happy_hardcoded(n: int) -> bool:
    """
    Optimized approach using mathematical property.
    All numbers either reach 1 or enter the cycle: 4 → 16 → 37 → 58 → 89 → 145 → 42 → 20 → 4
    
    Args:
        n: Input number to check
        
    Returns:
        True if number is happy, False otherwise
        
    Time Complexity: O(log n)
    Space Complexity: O(1)
    """
    def get_sum_of_squares(num):
        """Calculate sum of squares of digits."""
        total = 0
        while num > 0:
            digit = num % 10
            total += digit * digit
            num //= 10
        return total
    
    # Known cycle values that indicate unhappy numbers
    cycle_members = {4, 16, 37, 58, 89, 145, 42, 20}
    
    while n != 1 and n not in cycle_members:
        n = get_sum_of_squares(n)
    
    return n == 1

def is_happy_optimized_math(n: int) -> bool:
    """
    Mathematical optimization using digit sum properties.
    
    Args:
        n: Input number to check
        
    Returns:
        True if number is happy, False otherwise
        
    Time Complexity: O(log n)
    Space Complexity: O(1)
    """
    def get_sum_of_squares_optimized(num):
        """Optimized calculation of sum of squares."""
        total = 0
        while num:
            num, digit = divmod(num, 10)
            total += digit * digit
        return total
    
    # Use mathematical insight: if we reach any single digit other than 1 or 7,
    # we know it's not happy (except 1 and 7, all single digits lead to cycles)
    while n >= 10:
        n = get_sum_of_squares_optimized(n)
    
    # Single digit check: only 1 and 7 lead to happiness
    return n == 1 or n == 7

def is_happy_recursive(n: int, memo=None) -> bool:
    """
    Recursive approach with memoization.
    
    Args:
        n: Input number to check
        memo: Memoization dictionary
        
    Returns:
        True if number is happy, False otherwise
        
    Time Complexity: O(log n)
    Space Complexity: O(log n)
    """
    if memo is None:
        memo = {}
    
    if n in memo:
        return memo[n]
    
    if n == 1:
        return True
    
    if n in {4, 16, 37, 58, 89, 145, 42, 20}:  # Known cycle
        memo[n] = False
        return False
    
    def get_sum_of_squares(num):
        """Calculate sum of squares of digits."""
        total = 0
        while num > 0:
            digit = num % 10
            total += digit * digit
            num //= 10
        return total
    
    next_n = get_sum_of_squares(n)
    result = is_happy_recursive(next_n, memo)
    memo[n] = result
    return result

# Main function for the problem
def isHappy(n: int) -> bool:
    """
    Main solution using Floyd's cycle detection for optimal space.
    """
    return is_happy_floyd(n)

if __name__ == "__main__":
    # Test cases
    test_cases = [
        # Basic happy numbers
        (1, True),
        (7, True),
        (10, True),
        (13, True),
        (19, True),
        (23, True),
        (28, True),
        (68, True),
        (82, True),
        (86, True),
        (91, True),
        (94, True),
        (97, True),
        
        # Basic unhappy numbers
        (2, False),
        (3, False),
        (4, False),
        (5, False),
        (6, False),
        (8, False),
        (9, False),
        (11, False),
        (12, False),
        (14, False),
        (15, False),
        (16, False),
        (17, False),
        (18, False),
        (20, False),
        
        # Larger numbers
        (100, True),
        (999, False),
        (1111, False),
        (9999, False),
        
        # Edge cases
        (2147483647, False),  # Max 32-bit integer
    ]
    
    print("=" * 60)
    print("HAPPY NUMBER - COMPREHENSIVE TESTING")
    print("=" * 60)
    
    algorithms = [
        ("Set-based Detection", is_happy_set),
        ("Floyd's Cycle Detection", is_happy_floyd),
        ("Hardcoded Cycle", is_happy_hardcoded),
        ("Optimized Math", is_happy_optimized_math),
        ("Recursive Memoization", is_happy_recursive),
    ]
    
    # Test all algorithms
    for i, (n, expected) in enumerate(test_cases):
        print(f"\nTest Case {i + 1}: n = {n}, expected = {expected}")
        
        results = []
        for name, func in algorithms:
            try:
                import time
                start_time = time.time()
                result = func(n)
                end_time = time.time()
                
                results.append(result)
                status = "✓" if result == expected else "✗"
                print(f"  {name}: {result} {status} ({end_time - start_time:.6f}s)")
                
            except Exception as e:
                print(f"  {name}: ERROR - {e}")
        
        # Check consistency
        if len(set(results)) > 1:
            print(f"  WARNING: Inconsistent results: {results}")
    
    # Performance testing
    print("\n" + "=" * 60)
    print("PERFORMANCE TESTING")
    print("=" * 60)
    
    import time
    import random
    
    # Test with various number sizes
    performance_tests = [
        ("Small numbers", [random.randint(1, 100) for _ in range(1000)]),
        ("Medium numbers", [random.randint(100, 10000) for _ in range(1000)]),
        ("Large numbers", [random.randint(10000, 1000000) for _ in range(1000)]),
        ("Very large numbers", [random.randint(1000000, 2147483647) for _ in range(100)]),
    ]
    
    for test_name, test_numbers in performance_tests:
        print(f"\n{test_name} ({len(test_numbers)} numbers):")
        
        for name, func in algorithms:
            try:
                start_time = time.time()
                happy_count = 0
                for num in test_numbers:
                    if func(num):
                        happy_count += 1
                end_time = time.time()
                
                print(f"  {name}: {happy_count} happy numbers, {end_time - start_time:.6f}s")
                
            except Exception as e:
                print(f"  {name}: ERROR - {e}")
    
    # Mathematical analysis
    print("\n" + "=" * 60)
    print("MATHEMATICAL ANALYSIS")
    print("=" * 60)
    
    def analyze_sequence(n, max_steps=20):
        """Analyze the sequence of a number."""
        def get_sum_of_squares(num):
            total = 0
            while num > 0:
                digit = num % 10
                total += digit * digit
                num //= 10
            return total
        
        sequence = [n]
        current = n
        
        for _ in range(max_steps):
            current = get_sum_of_squares(current)
            sequence.append(current)
            
            if current == 1:
                return sequence, "HAPPY"
            
            if current in sequence[:-1]:  # Cycle detected
                cycle_start = sequence.index(current)
                cycle = sequence[cycle_start:-1]
                return sequence, f"CYCLE: {cycle}"
        
        return sequence, "TRUNCATED"
    
    # Analyze some interesting numbers
    analysis_numbers = [1, 2, 4, 7, 10, 13, 19, 23, 44, 82, 97]
    
    for num in analysis_numbers:
        sequence, result = analyze_sequence(num)
        is_happy = is_happy_floyd(num)
        print(f"n = {num}: {' → '.join(map(str, sequence[:10]))}{'...' if len(sequence) > 10 else ''}")
        print(f"  Result: {result}, Happy: {is_happy}")
    
    # Cycle detection validation
    print("\n" + "=" * 60)
    print("CYCLE DETECTION VALIDATION")
    print("=" * 60)
    
    # Known cycle: 4 → 16 → 37 → 58 → 89 → 145 → 42 → 20 → 4
    known_cycle = [4, 16, 37, 58, 89, 145, 42, 20]
    
    print("Known unhappy cycle:")
    print(" → ".join(map(str, known_cycle + [known_cycle[0]])))
    
    # Verify all numbers in cycle are detected as unhappy
    for num in known_cycle:
        result = is_happy_floyd(num)
        print(f"  {num}: {'✗' if not result else '✓'} ({'unhappy' if not result else 'happy'})")
    
    # Test cycle convergence
    print("\nTesting cycle convergence:")
    test_unhappy = [2, 3, 5, 6, 8, 9, 11, 12, 14, 15]
    
    for num in test_unhappy:
        sequence, result = analyze_sequence(num, 15)
        converges_to_cycle = any(x in known_cycle for x in sequence)
        print(f"  {num}: converges to known cycle = {converges_to_cycle}")
    
    # Happy number statistics
    print("\n" + "=" * 60)
    print("HAPPY NUMBER STATISTICS")
    print("=" * 60)
    
    # Count happy numbers in ranges
    ranges = [(1, 100), (1, 1000), (1, 10000)]
    
    for start, end in ranges:
        happy_count = 0
        total_count = end - start + 1
        
        for i in range(start, end + 1):
            if is_happy_floyd(i):
                happy_count += 1
        
        percentage = (happy_count / total_count) * 100
        print(f"Range {start}-{end}: {happy_count}/{total_count} happy numbers ({percentage:.2f}%)")
    
    # Distribution by number of digits
    print("\nHappy number distribution by digit count:")
    
    for digits in range(1, 6):
        start = 10 ** (digits - 1) if digits > 1 else 1
        end = 10 ** digits - 1
        
        # Sample for larger ranges
        if end - start > 10000:
            sample_size = 1000
            sample_numbers = random.sample(range(start, end + 1), sample_size)
            happy_count = sum(1 for n in sample_numbers if is_happy_floyd(n))
            percentage = (happy_count / sample_size) * 100
            print(f"  {digits} digits (sample): {happy_count}/{sample_size} happy ({percentage:.1f}%)")
        else:
            happy_count = sum(1 for n in range(start, end + 1) if is_happy_floyd(n))
            total = end - start + 1
            percentage = (happy_count / total) * 100
            print(f"  {digits} digits: {happy_count}/{total} happy ({percentage:.1f}%)")

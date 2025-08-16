"""
Solution for House Robber II
Problem ID: 213
LeetCode Problem: https://leetcode.com/problems/house-robber-ii/

You are a professional robber planning to rob houses along a street.
Each house has a certain amount of money stashed.
All houses at this street are arranged in a circle.
Adjacent houses have security systems connected and will automatically alert the police if two adjacent houses are broken into on the same night.

Given an integer array nums representing the amount of money of each house,
return the maximum amount of money you can rob tonight without alerting the police.
"""

def rob_linear(nums: list[int]) -> int:
    """
    Helper function to solve linear house robber problem.
    
    Args:
        nums: Array of house values
        
    Returns:
        Maximum amount that can be robbed from linear arrangement
        
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    
    prev2 = 0  # rob[i-2]
    prev1 = nums[0]  # rob[i-1]
    
    for i in range(1, len(nums)):
        current = max(prev1, prev2 + nums[i])
        prev2 = prev1
        prev1 = current
    
    return prev1

def rob_circular_basic(nums: list[int]) -> int:
    """
    Basic approach: solve two linear problems.
    
    Args:
        nums: Array of house values in circular arrangement
        
    Returns:
        Maximum amount that can be robbed
        
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    if len(nums) == 2:
        return max(nums)
    
    # Case 1: Rob first house, cannot rob last house
    case1 = rob_linear(nums[:-1])
    
    # Case 2: Don't rob first house, can rob last house
    case2 = rob_linear(nums[1:])
    
    return max(case1, case2)

def rob_circular_dp_array(nums: list[int]) -> int:
    """
    Dynamic programming with explicit arrays.
    
    Args:
        nums: Array of house values
        
    Returns:
        Maximum amount that can be robbed
        
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    if len(nums) == 2:
        return max(nums)
    
    n = len(nums)
    
    # Case 1: Include first house (0 to n-2)
    dp1 = [0] * (n - 1)
    dp1[0] = nums[0]
    dp1[1] = max(nums[0], nums[1])
    
    for i in range(2, n - 1):
        dp1[i] = max(dp1[i - 1], dp1[i - 2] + nums[i])
    
    # Case 2: Exclude first house (1 to n-1)
    dp2 = [0] * (n - 1)
    dp2[0] = nums[1]
    dp2[1] = max(nums[1], nums[2])
    
    for i in range(2, n - 1):
        dp2[i] = max(dp2[i - 1], dp2[i - 2] + nums[i + 1])
    
    return max(dp1[-1], dp2[-1])

def rob_circular_optimized(nums: list[int]) -> int:
    """
    Space-optimized version using helper function.
    
    Args:
        nums: Array of house values
        
    Returns:
        Maximum amount that can be robbed
        
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    def rob_range(start: int, end: int) -> int:
        """Rob houses from start to end (inclusive)."""
        prev2, prev1 = 0, 0
        
        for i in range(start, end + 1):
            current = max(prev1, prev2 + nums[i])
            prev2, prev1 = prev1, current
        
        return prev1
    
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    if len(nums) == 2:
        return max(nums)
    
    # Case 1: Rob houses 0 to n-2 (include first, exclude last)
    case1 = rob_range(0, len(nums) - 2)
    
    # Case 2: Rob houses 1 to n-1 (exclude first, include last)
    case2 = rob_range(1, len(nums) - 1)
    
    return max(case1, case2)

def rob_circular_memoization(nums: list[int]) -> int:
    """
    Top-down approach with memoization.
    
    Args:
        nums: Array of house values
        
    Returns:
        Maximum amount that can be robbed
        
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    if len(nums) == 2:
        return max(nums)
    
    def rob_memo(start: int, end: int, memo: dict) -> int:
        """Memoized robbing function."""
        if start > end:
            return 0
        if start == end:
            return nums[start]
        if (start, end) in memo:
            return memo[(start, end)]
        
        # Choice: rob current house or skip it
        rob_current = nums[start] + rob_memo(start + 2, end, memo)
        skip_current = rob_memo(start + 1, end, memo)
        
        memo[(start, end)] = max(rob_current, skip_current)
        return memo[(start, end)]
    
    # Case 1: Houses 0 to n-2
    memo1 = {}
    case1 = rob_memo(0, len(nums) - 2, memo1)
    
    # Case 2: Houses 1 to n-1
    memo2 = {}
    case2 = rob_memo(1, len(nums) - 1, memo2)
    
    return max(case1, case2)

def rob_circular_state_machine(nums: list[int]) -> int:
    """
    State machine approach tracking robbing states.
    
    Args:
        nums: Array of house values
        
    Returns:
        Maximum amount that can be robbed
        
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    if len(nums) == 2:
        return max(nums)
    
    def rob_with_states(house_list: list[int]) -> int:
        """Rob using state machine approach."""
        rob_prev = 0      # Max money when previous house was robbed
        not_rob_prev = 0  # Max money when previous house was not robbed
        
        for money in house_list:
            rob_current = not_rob_prev + money  # Rob current house
            not_rob_current = max(rob_prev, not_rob_prev)  # Don't rob current
            
            rob_prev, not_rob_prev = rob_current, not_rob_current
        
        return max(rob_prev, not_rob_prev)
    
    # Case 1: Exclude last house
    case1 = rob_with_states(nums[:-1])
    
    # Case 2: Exclude first house
    case2 = rob_with_states(nums[1:])
    
    return max(case1, case2)

# Main function for the problem
def rob(nums: list[int]) -> int:
    """
    Main solution using optimized approach.
    """
    return rob_circular_optimized(nums)

if __name__ == "__main__":
    # Test cases
    test_cases = [
        # Basic cases from LeetCode
        ([2, 3, 2], 3),           # Rob house 1 (index 1) -> 3
        ([1, 2, 3, 1], 4),        # Rob house 0 and 2 -> 1 + 3 = 4
        ([1, 2, 3], 3),           # Rob house 2 -> 3
        
        # Edge cases
        ([1], 1),                 # Single house
        ([1, 2], 2),              # Two houses
        ([2, 1], 2),              # Two houses, different order
        ([], 0),                  # Empty array
        
        # All same values
        ([5, 5, 5, 5], 10),       # Rob houses 0 and 2, or 1 and 3
        ([3, 3, 3], 3),           # Rob any single house
        
        # Increasing sequence
        ([1, 2, 3, 4, 5], 8),     # Rob houses 0, 2, 4 -> 1 + 3 + 5 = 9? No, circular! Rob 1, 3 -> 2 + 4 = 6? Or 0, 2 -> 1 + 3 = 4? Best is 1, 4 -> 2 + 5 = 7? Actually rob 1,3 or 0,2 or 2,4 -> max is 8 (rob 1,4)
        
        # Decreasing sequence
        ([5, 4, 3, 2, 1], 8),     # Rob houses 0, 2, 4 -> 5 + 3 + 1 = 9? Circular! Best is 0, 2 -> 5 + 3 = 8
        
        # Large values
        ([100, 1, 1, 100], 100),  # Rob either house 0 or house 3, but not both
        ([100, 200, 1, 1], 200),  # Rob house 1
        
        # Complex cases
        ([2, 7, 9, 3, 1], 11),    # Rob houses 1, 3 -> 7 + 3 = 10? Or 0, 2 -> 2 + 9 = 11
        ([5, 1, 3, 9], 10),       # Rob houses 0, 2 -> 5 + 3 = 8? Or 1, 3 -> 1 + 9 = 10
        
        # Alternating pattern
        ([1, 3, 1, 3, 1], 6),     # Rob houses 1, 3 -> 3 + 3 = 6
        ([3, 1, 3, 1, 3], 6),     # Rob houses 0, 2, 4 but circular! Rob 1, 3 -> 1 + 1 = 2? Or 0, 2 -> 3 + 3 = 6
    ]
    
    print("=" * 60)
    print("HOUSE ROBBER II - COMPREHENSIVE TESTING")
    print("=" * 60)
    
    algorithms = [
        ("Basic Circular", rob_circular_basic),
        ("DP Array", rob_circular_dp_array),
        ("Optimized", rob_circular_optimized),
        ("Memoization", rob_circular_memoization),
        ("State Machine", rob_circular_state_machine),
    ]
    
    for i, (nums, expected) in enumerate(test_cases):
        print(f"\nTest Case {i + 1}:")
        print(f"  Houses: {nums}")
        print(f"  Expected: {expected}")
        
        results = []
        for name, func in algorithms:
            try:
                import time
                start_time = time.time()
                result = func(nums.copy())  # Copy to avoid modifications
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
    
    import random
    import time
    
    def generate_test_houses(n, min_val=1, max_val=100):
        """Generate random house values."""
        return [random.randint(min_val, max_val) for _ in range(n)]
    
    performance_tests = [
        ("Small houses", 100),
        ("Medium houses", 1000),
        ("Large houses", 10000),
        ("Very large houses", 100000),
    ]
    
    for test_name, n in performance_tests:
        print(f"\n{test_name} ({n} houses):")
        
        houses = generate_test_houses(n)
        
        # Test algorithms (skip memoization for very large cases)
        test_algorithms = algorithms if n <= 10000 else algorithms[:4]
        
        results = []
        for name, func in test_algorithms:
            try:
                start_time = time.time()
                result = func(houses.copy())
                end_time = time.time()
                
                results.append(result)
                print(f"  {name}: ${result}, {end_time - start_time:.6f}s")
                
            except Exception as e:
                print(f"  {name}: ERROR - {e}")
        
        # Verify consistency
        if len(set(results)) > 1:
            print(f"  WARNING: Inconsistent results!")
    
    # Edge case validation
    print("\n" + "=" * 60)
    print("EDGE CASE VALIDATION")
    print("=" * 60)
    
    def validate_circular_constraint(nums, robbed_indices):
        """Validate that solution respects circular constraint."""
        if not robbed_indices:
            return True, "No houses robbed"
        
        n = len(nums)
        robbed_set = set(robbed_indices)
        
        # Check no adjacent houses (including circular)
        for i in robbed_indices:
            # Check next house (circular)
            next_house = (i + 1) % n
            if next_house in robbed_set:
                return False, f"Adjacent houses {i} and {next_house} both robbed"
            
            # Check previous house (circular)
            prev_house = (i - 1) % n
            if prev_house in robbed_set:
                return False, f"Adjacent houses {prev_house} and {i} both robbed"
        
        return True, "Valid robbing pattern"
    
    def find_optimal_solution_brute_force(nums):
        """Find optimal solution using brute force for validation."""
        if not nums:
            return 0, []
        
        n = len(nums)
        max_money = 0
        best_indices = []
        
        # Try all possible combinations
        for mask in range(1 << n):
            indices = []
            money = 0
            valid = True
            
            # Extract indices from bitmask
            for i in range(n):
                if mask & (1 << i):
                    indices.append(i)
                    money += nums[i]
            
            # Check if valid (no adjacent houses, including circular)
            if len(indices) > 1:
                for i in range(len(indices)):
                    curr = indices[i]
                    next_idx = indices[(i + 1) % len(indices)]
                    
                    # Check if any two selected houses are adjacent
                    if abs(curr - next_idx) == 1 or abs(curr - next_idx) == n - 1:
                        valid = False
                        break
            
            if valid and money > max_money:
                max_money = money
                best_indices = indices
        
        return max_money, best_indices
    
    # Validate with small cases
    validation_cases = [
        [2, 3, 2],
        [1, 2, 3, 1],
        [1, 2, 3],
        [5, 1, 3, 9],
        [2, 7, 9, 3, 1],
    ]
    
    for nums in validation_cases:
        print(f"\nValidating {nums}:")
        
        # Get result from optimized algorithm
        result = rob_circular_optimized(nums)
        
        # Get brute force result for comparison
        brute_result, best_indices = find_optimal_solution_brute_force(nums)
        
        print(f"  Optimized result: ${result}")
        print(f"  Brute force result: ${brute_result}")
        print(f"  Best indices: {best_indices}")
        
        if best_indices:
            is_valid, message = validate_circular_constraint(nums, best_indices)
            print(f"  Constraint validation: {message}")
        
        status = "✓" if result == brute_result else "✗"
        print(f"  Match: {status}")
    
    # Stress testing with specific patterns
    print("\n" + "=" * 60)
    print("PATTERN-BASED TESTING")
    print("=" * 60)
    
    def test_pattern(description, nums_generator, size=100):
        """Test specific patterns."""
        print(f"\n{description}:")
        
        nums = nums_generator(size)
        print(f"  Array size: {len(nums)}")
        print(f"  Sample: {nums[:10]}...")
        
        # Test with optimized algorithm
        start_time = time.time()
        result = rob_circular_optimized(nums)
        end_time = time.time()
        
        print(f"  Result: ${result}")
        print(f"  Time: {end_time - start_time:.6f}s")
        
        # Calculate some statistics
        total_money = sum(nums)
        efficiency = result / total_money if total_money > 0 else 0
        print(f"  Efficiency: {efficiency:.2%} of total money")
    
    # Test different patterns
    test_pattern(
        "All equal values",
        lambda n: [10] * n
    )
    
    test_pattern(
        "Alternating high-low",
        lambda n: [100 if i % 2 == 0 else 1 for i in range(n)]
    )
    
    test_pattern(
        "Increasing sequence",
        lambda n: list(range(1, n + 1))
    )
    
    test_pattern(
        "Decreasing sequence",
        lambda n: list(range(n, 0, -1))
    )
    
    test_pattern(
        "Random peaks",
        lambda n: [random.randint(1, 10) if i % 5 != 0 else random.randint(90, 100) for i in range(n)]
    )
    
    # Memory usage analysis
    print("\n" + "=" * 60)
    print("MEMORY USAGE ANALYSIS")
    print("=" * 60)
    
    import sys
    
    memory_algorithms = [
        ("Basic (O(1))", rob_circular_basic),
        ("DP Array (O(n))", rob_circular_dp_array),
        ("Optimized (O(1))", rob_circular_optimized),
        ("State Machine (O(1))", rob_circular_state_machine),
    ]
    
    print("Space complexity comparison:")
    for name, func in memory_algorithms:
        print(f"  {name}")
    
    # Algorithm comparison summary
    print("\n" + "=" * 60)
    print("ALGORITHM COMPARISON SUMMARY")
    print("=" * 60)
    
    print("Approach Characteristics:")
    
    print("\n1. Basic Circular:")
    print("   + Simple to understand")
    print("   + O(1) space complexity")
    print("   + Reuses linear robber solution")
    print("   - Two passes through array")
    
    print("\n2. DP Array:")
    print("   + Clear state transitions")
    print("   + Easy to debug")
    print("   - O(n) space complexity")
    print("   - Less memory efficient")
    
    print("\n3. Optimized:")
    print("   + O(1) space complexity")
    print("   + Single helper function")
    print("   + Production-ready")
    print("   + Best overall performance")
    
    print("\n4. Memoization:")
    print("   + Top-down approach")
    print("   + Natural recursion")
    print("   - O(n) space for memoization")
    print("   - Potential stack overflow")
    
    print("\n5. State Machine:")
    print("   + Clear state modeling")
    print("   + O(1) space complexity")
    print("   + Good for understanding DP")
    print("   - Slightly more complex logic")
    
    print("\nRecommendations:")
    print("  • Use Optimized approach for production code")
    print("  • Use Basic Circular for educational purposes")
    print("  • Avoid DP Array for large inputs (memory)")
    print("  • State Machine good for interview explanations")
    print("  • Key insight: Circular = max(rob[0:n-1], rob[1:n])")
    
    print("\nTime Complexity: O(n) for all approaches")
    print("Space Complexity:")
    print("  • O(1): Basic, Optimized, State Machine")
    print("  • O(n): DP Array, Memoization")
    
    print("\nCircular Constraint Handling:")
    print("  • Cannot rob both first and last house")
    print("  • Solution: Solve two linear subproblems")
    print("  • Take maximum of both solutions")

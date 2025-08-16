"""
Solution for Minimum Size Subarray Sum
Problem ID: 209
LeetCode Problem: https://leetcode.com/problems/minimum-size-subarray-sum/

Given an array of positive integers nums and a positive integer target,
return the minimal length of a contiguous subarray whose sum is greater than or equal to target.
If there is no such subarray, return 0.
"""

def min_subarray_len_brute_force(target: int, nums: list[int]) -> int:
    """
    Brute force approach checking all subarrays.
    
    Args:
        target: Target sum
        nums: Array of positive integers
        
    Returns:
        Minimum length of subarray with sum >= target
        
    Time Complexity: O(n²)
    Space Complexity: O(1)
    """
    n = len(nums)
    min_len = float('inf')
    
    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += nums[j]
            if current_sum >= target:
                min_len = min(min_len, j - i + 1)
                break  # No need to extend further
    
    return min_len if min_len != float('inf') else 0

def min_subarray_len_sliding_window(target: int, nums: list[int]) -> int:
    """
    Sliding window (two pointers) approach.
    
    Args:
        target: Target sum
        nums: Array of positive integers
        
    Returns:
        Minimum length of subarray with sum >= target
        
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    n = len(nums)
    left = 0
    current_sum = 0
    min_len = float('inf')
    
    for right in range(n):
        current_sum += nums[right]
        
        # Shrink window while sum >= target
        while current_sum >= target:
            min_len = min(min_len, right - left + 1)
            current_sum -= nums[left]
            left += 1
    
    return min_len if min_len != float('inf') else 0

def min_subarray_len_binary_search(target: int, nums: list[int]) -> int:
    """
    Binary search on answer length with prefix sums.
    
    Args:
        target: Target sum
        nums: Array of positive integers
        
    Returns:
        Minimum length of subarray with sum >= target
        
    Time Complexity: O(n log n)
    Space Complexity: O(n)
    """
    n = len(nums)
    
    # Build prefix sum array
    prefix_sums = [0] * (n + 1)
    for i in range(n):
        prefix_sums[i + 1] = prefix_sums[i] + nums[i]
    
    def can_achieve_length(length):
        """Check if there's a subarray of given length with sum >= target."""
        for i in range(n - length + 1):
            subarray_sum = prefix_sums[i + length] - prefix_sums[i]
            if subarray_sum >= target:
                return True
        return False
    
    # Binary search on length
    left, right = 1, n
    result = 0
    
    while left <= right:
        mid = (left + right) // 2
        if can_achieve_length(mid):
            result = mid
            right = mid - 1
        else:
            left = mid + 1
    
    return result

def min_subarray_len_optimized_binary_search(target: int, nums: list[int]) -> int:
    """
    Optimized binary search using binary search on prefix sums.
    
    Args:
        target: Target sum
        nums: Array of positive integers
        
    Returns:
        Minimum length of subarray with sum >= target
        
    Time Complexity: O(n log n)
    Space Complexity: O(n)
    """
    import bisect
    
    n = len(nums)
    prefix_sums = [0]
    
    for num in nums:
        prefix_sums.append(prefix_sums[-1] + num)
    
    min_len = float('inf')
    
    for i in range(1, n + 1):
        # Find the smallest j such that prefix_sums[j] - prefix_sums[i-1] >= target
        # This is equivalent to finding prefix_sums[j] >= prefix_sums[i-1] + target
        target_sum = prefix_sums[i - 1] + target
        
        # Binary search for the leftmost position >= target_sum
        j = bisect.bisect_left(prefix_sums, target_sum, i)
        
        if j <= n:
            min_len = min(min_len, j - i + 1)
    
    return min_len if min_len != float('inf') else 0

def min_subarray_len_deque_optimization(target: int, nums: list[int]) -> int:
    """
    Deque-based optimization for special cases.
    
    Args:
        target: Target sum
        nums: Array of positive integers
        
    Returns:
        Minimum length of subarray with sum >= target
        
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    from collections import deque
    
    n = len(nums)
    
    # If any single element >= target, return 1
    if any(num >= target for num in nums):
        return 1
    
    # Use deque to maintain increasing prefix sums
    dq = deque([(0, -1)])  # (prefix_sum, index)
    prefix_sum = 0
    min_len = float('inf')
    
    for i in range(n):
        prefix_sum += nums[i]
        
        # Remove elements from front while we can achieve target
        while dq and prefix_sum - dq[0][0] >= target:
            min_len = min(min_len, i - dq[0][1])
            dq.popleft()
        
        # Maintain monotonic increasing property
        while dq and dq[-1][0] >= prefix_sum:
            dq.pop()
        
        dq.append((prefix_sum, i))
    
    return min_len if min_len != float('inf') else 0

# Main function for the problem
def minSubArrayLen(target: int, nums: list[int]) -> int:
    """
    Main solution using sliding window for optimal performance.
    """
    return min_subarray_len_sliding_window(target, nums)

if __name__ == "__main__":
    # Test cases
    test_cases = [
        # Basic cases from LeetCode
        (7, [2, 3, 1, 2, 4, 3], 2),  # [4, 3] has sum 7
        (4, [1, 4, 4], 1),           # [4] has sum 4
        (11, [1, 1, 1, 1, 1, 1, 1, 1], 0),  # No subarray sums to 11
        
        # Edge cases
        (1, [1], 1),                 # Single element equal to target
        (2, [1], 0),                 # Single element less than target
        (1, [2], 1),                 # Single element greater than target
        (15, [1, 2, 3, 4, 5], 5),    # Entire array needed
        (5, [1, 2, 3, 4, 5], 1),     # Single element (5) is enough
        
        # All same elements
        (6, [2, 2, 2, 2], 3),        # Need 3 elements: [2, 2, 2]
        (10, [5, 5, 5, 5], 2),       # Need 2 elements: [5, 5]
        
        # Large values
        (100, [1, 2, 100], 1),       # Single large element
        (50, [10, 20, 30, 40], 2),   # [20, 30] or [10, 40]
        
        # Increasing sequence
        (10, [1, 2, 3, 4, 5, 6], 4), # [1, 2, 3, 4]
        
        # Decreasing sequence
        (10, [6, 5, 4, 3, 2, 1], 2), # [6, 5]
        
        # Random order
        (8, [3, 1, 7, 2, 4], 2),     # [7, 2] or [3, 1, 7] but shorter is [7, 2]
    ]
    
    print("=" * 70)
    print("MINIMUM SIZE SUBARRAY SUM - COMPREHENSIVE TESTING")
    print("=" * 70)
    
    algorithms = [
        ("Brute Force", min_subarray_len_brute_force),
        ("Sliding Window", min_subarray_len_sliding_window),
        ("Binary Search", min_subarray_len_binary_search),
        ("Optimized Binary Search", min_subarray_len_optimized_binary_search),
        ("Deque Optimization", min_subarray_len_deque_optimization),
    ]
    
    for i, (target, nums, expected) in enumerate(test_cases):
        print(f"\nTest Case {i + 1}:")
        print(f"  Target: {target}")
        print(f"  Array: {nums}")
        print(f"  Expected: {expected}")
        
        results = []
        for name, func in algorithms:
            try:
                import time
                start_time = time.time()
                result = func(target, nums)
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
    print("\n" + "=" * 70)
    print("PERFORMANCE TESTING")
    print("=" * 70)
    
    import random
    import time
    
    performance_tests = [
        ("Small array", 100, lambda: random.randint(1, 10)),
        ("Medium array", 1000, lambda: random.randint(1, 100)),
        ("Large array", 10000, lambda: random.randint(1, 1000)),
        ("Very large array", 100000, lambda: random.randint(1, 10000)),
    ]
    
    for test_name, size, value_gen in performance_tests:
        print(f"\n{test_name} ({size} elements):")
        
        # Generate test data
        nums = [value_gen() for _ in range(size)]
        target = sum(nums) // 4  # Target is 1/4 of total sum
        
        # Test algorithms (skip brute force for large arrays)
        test_algorithms = algorithms if size <= 1000 else algorithms[1:]
        
        results = []
        for name, func in test_algorithms:
            try:
                start_time = time.time()
                result = func(target, nums)
                end_time = time.time()
                
                results.append(result)
                print(f"  {name}: length {result}, {end_time - start_time:.6f}s")
                
            except Exception as e:
                print(f"  {name}: ERROR - {e}")
        
        # Verify consistency
        if len(set(results)) > 1:
            print(f"  WARNING: Inconsistent results!")
    
    # Edge case stress testing
    print("\n" + "=" * 70)
    print("EDGE CASE STRESS TESTING")
    print("=" * 70)
    
    edge_cases = [
        ("All ones, target 1", [1] * 1000, 1),
        ("All ones, target 100", [1] * 1000, 100),
        ("All ones, target 1001", [1] * 1000, 1001),  # Impossible
        ("Increasing sequence", list(range(1, 1001)), 500),
        ("Decreasing sequence", list(range(1000, 0, -1)), 500),
        ("Single large element", [1] * 999 + [1000000], 1000000),
        ("Two large elements", [500000, 500000] + [1] * 998, 1000000),
        ("Alternating small/large", [1, 1000] * 500, 1000),
    ]
    
    for description, nums, target in edge_cases:
        print(f"\n{description}:")
        print(f"  Array size: {len(nums)}")
        print(f"  Target: {target}")
        
        # Test main algorithms
        test_algorithms = [
            ("Sliding Window", min_subarray_len_sliding_window),
            ("Binary Search", min_subarray_len_binary_search),
        ]
        
        results = []
        for name, func in test_algorithms:
            try:
                start_time = time.time()
                result = func(target, nums)
                end_time = time.time()
                
                results.append(result)
                print(f"  {name}: {result}, {end_time - start_time:.6f}s")
                
            except Exception as e:
                print(f"  {name}: ERROR - {e}")
        
        # Verify consistency
        if len(set(results)) > 1:
            print(f"  WARNING: Inconsistent results!")
    
    # Correctness validation
    print("\n" + "=" * 70)
    print("CORRECTNESS VALIDATION")
    print("=" * 70)
    
    def validate_result(target, nums, result):
        """Validate that the result is correct."""
        if result == 0:
            # Check that no subarray sums to target
            n = len(nums)
            for i in range(n):
                current_sum = 0
                for j in range(i, n):
                    current_sum += nums[j]
                    if current_sum >= target:
                        return False, f"Found subarray [{i}:{j+1}] with sum {current_sum}"
            return True, "Correctly identified no valid subarray"
        
        # Check that there exists a subarray of length 'result' with sum >= target
        n = len(nums)
        found_valid = False
        
        for i in range(n - result + 1):
            subarray_sum = sum(nums[i:i + result])
            if subarray_sum >= target:
                found_valid = True
                break
        
        if not found_valid:
            return False, f"No subarray of length {result} has sum >= {target}"
        
        # Check that no shorter subarray works
        if result > 1:
            for length in range(1, result):
                for i in range(n - length + 1):
                    subarray_sum = sum(nums[i:i + length])
                    if subarray_sum >= target:
                        return False, f"Found shorter subarray of length {length} at position {i}"
        
        return True, f"Correctly found minimum length {result}"
    
    validation_cases = [
        (7, [2, 3, 1, 2, 4, 3]),
        (4, [1, 4, 4]),
        (11, [1, 1, 1, 1, 1, 1, 1, 1]),
        (15, [1, 2, 3, 4, 5]),
        (6, [2, 2, 2, 2]),
    ]
    
    for target, nums in validation_cases:
        print(f"\nValidating target={target}, nums={nums}:")
        
        # Test sliding window result
        result = min_subarray_len_sliding_window(target, nums)
        is_valid, message = validate_result(target, nums, result)
        status = "✓" if is_valid else "✗"
        
        print(f"  Result: {result}")
        print(f"  Validation: {status} {message}")
    
    # Special pattern testing
    print("\n" + "=" * 70)
    print("SPECIAL PATTERN TESTING")
    print("=" * 70)
    
    def test_pattern(description, nums_gen, target_gen, size=1000):
        """Test specific patterns."""
        print(f"\n{description}:")
        
        nums = nums_gen(size)
        target = target_gen(nums)
        
        print(f"  Array size: {len(nums)}")
        print(f"  Target: {target}")
        print(f"  Array preview: {nums[:10]}...")
        
        # Test sliding window
        start_time = time.time()
        result = min_subarray_len_sliding_window(target, nums)
        end_time = time.time()
        
        print(f"  Result: {result}")
        print(f"  Time: {end_time - start_time:.6f}s")
        
        # Validate
        is_valid, message = validate_result(target, nums, result)
        print(f"  Validation: {'✓' if is_valid else '✗'} {message}")
    
    # Test different patterns
    test_pattern(
        "Fibonacci-like sequence",
        lambda n: [1, 1] + [sum([1, 1][max(0, i-2):i]) for i in range(2, n)],
        lambda nums: sum(nums) // 10
    )
    
    test_pattern(
        "Powers of 2",
        lambda n: [2**i for i in range(min(n, 20))] + [1] * max(0, n - 20),
        lambda nums: sum(nums) // 5
    )
    
    test_pattern(
        "Random walk",
        lambda n: [max(1, 100 + sum(random.choice([-1, 1]) for _ in range(i))) 
                  for i in range(n)],
        lambda nums: sum(nums) // 8
    )
    
    # Algorithm comparison summary
    print("\n" + "=" * 70)
    print("ALGORITHM COMPARISON SUMMARY")
    print("=" * 70)
    
    print("Time Complexity Comparison:")
    print("  Brute Force:              O(n²)")
    print("  Sliding Window:           O(n)       ← OPTIMAL")
    print("  Binary Search:            O(n log n)")
    print("  Optimized Binary Search:  O(n log n)")
    print("  Deque Optimization:       O(n)")
    
    print("\nSpace Complexity Comparison:")
    print("  Brute Force:              O(1)       ← OPTIMAL")
    print("  Sliding Window:           O(1)       ← OPTIMAL")
    print("  Binary Search:            O(n)")
    print("  Optimized Binary Search:  O(n)")
    print("  Deque Optimization:       O(n)")
    
    print("\nRecommendations:")
    print("  • Use Sliding Window for optimal O(n) time and O(1) space")
    print("  • Use Binary Search when array has special properties")
    print("  • Brute Force only for very small arrays or educational purposes")
    print("  • All positive numbers guarantee sliding window optimality")

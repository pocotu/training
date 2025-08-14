"""
Solution for Maximum Frequency - LeetCode Weekly Contest 380 Problem 1
Contest: Weekly Contest 380
Problem: 1
Difficulty: Easy
"""

from collections import Counter, defaultdict
from typing import List

def max_frequency_hash_table(nums: List[int]) -> int:
    """
    Hash table approach for counting frequencies.
    
    Args:
        nums: List of integers
        
    Returns:
        Maximum frequency of any element
        
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    frequency = {}
    max_freq = 0
    
    for num in nums:
        frequency[num] = frequency.get(num, 0) + 1
        max_freq = max(max_freq, frequency[num])
    
    return max_freq

def max_frequency_counter(nums: List[int]) -> int:
    """
    Using collections.Counter for frequency counting.
    
    Args:
        nums: List of integers
        
    Returns:
        Maximum frequency of any element
        
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    counter = Counter(nums)
    return counter.most_common(1)[0][1]

def max_frequency_defaultdict(nums: List[int]) -> int:
    """
    Using defaultdict for cleaner code.
    
    Args:
        nums: List of integers
        
    Returns:
        Maximum frequency of any element
        
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    frequency = defaultdict(int)
    max_freq = 0
    
    for num in nums:
        frequency[num] += 1
        max_freq = max(max_freq, frequency[num])
    
    return max_freq

def max_frequency_optimized(nums: List[int]) -> int:
    """
    Optimized single-pass solution with early termination potential.
    
    Args:
        nums: List of integers
        
    Returns:
        Maximum frequency of any element
        
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    if not nums:
        return 0
    
    frequency = {}
    max_freq = 1
    
    for num in nums:
        frequency[num] = frequency.get(num, 0) + 1
        if frequency[num] > max_freq:
            max_freq = frequency[num]
    
    return max_freq

# Main function for the contest problem
def maxFrequency(nums: List[int]) -> int:
    """
    Main solution for contest submission.
    """
    return max_frequency_optimized(nums)

if __name__ == "__main__":
    # Test cases from the problem
    test_cases = [
        # Basic examples
        ([1,2,2,3,1,4], 2),
        ([1,1,1,2,2,3], 3),
        ([1], 1),
        
        # Edge cases
        ([1,1,1,1,1], 5),  # All same elements
        ([1,2,3,4,5], 1),  # All different elements
        ([2,2,1,1,3,3], 2),  # Multiple elements with same max frequency
        
        # Larger cases
        ([1]*1000 + [2]*500 + [3]*1500, 1500),  # Large array
        (list(range(100)), 1),  # Sequential numbers
        ([42]*10000, 10000),  # Single element repeated
    ]
    
    print("=" * 60)
    print("MAXIMUM FREQUENCY - CONTEST TESTING")
    print("=" * 60)
    
    algorithms = [
        ("Hash Table", max_frequency_hash_table),
        ("Counter", max_frequency_counter),
        ("DefaultDict", max_frequency_defaultdict),
        ("Optimized", max_frequency_optimized),
    ]
    
    for i, (nums, expected) in enumerate(test_cases):
        print(f"\nTest Case {i + 1}:")
        print(f"  Input: {nums if len(nums) <= 10 else f'{nums[:5]}...{nums[-5:]} (length {len(nums)})'}")
        print(f"  Expected: {expected}")
        
        for name, func in algorithms:
            try:
                import time
                start_time = time.time()
                result = func(nums)
                end_time = time.time()
                
                status = "✓" if result == expected else "✗"
                print(f"  {name}: {result} {status} ({end_time - start_time:.6f}s)")
                
            except Exception as e:
                print(f"  {name}: ERROR - {e}")
    
    # Performance testing
    print("\n" + "=" * 60)
    print("PERFORMANCE TESTING")
    print("=" * 60)
    
    import random
    import time
    
    def generate_test_array(size, pattern="random"):
        """Generate test arrays with different patterns."""
        if pattern == "random":
            return [random.randint(1, 1000) for _ in range(size)]
        elif pattern == "uniform":
            return [1] * size
        elif pattern == "sequential":
            return list(range(1, size + 1))
        elif pattern == "biased":
            # 80% of elements are the same, 20% are different
            common_element = 42
            result = [common_element] * int(size * 0.8)
            result.extend([random.randint(1, 1000) for _ in range(size - len(result))])
            random.shuffle(result)
            return result
    
    performance_tests = [
        ("Small Random", 1000, "random"),
        ("Medium Random", 10000, "random"),
        ("Large Random", 100000, "random"),
        ("Uniform Array", 50000, "uniform"),
        ("Sequential", 50000, "sequential"),
        ("Biased Distribution", 50000, "biased"),
    ]
    
    for test_name, size, pattern in performance_tests:
        print(f"\n{test_name} (size {size}):")
        
        test_array = generate_test_array(size, pattern)
        
        for name, func in algorithms:
            try:
                start_time = time.time()
                result = func(test_array)
                end_time = time.time()
                
                print(f"  {name}: result={result}, time={end_time - start_time:.6f}s")
                
            except Exception as e:
                print(f"  {name}: ERROR - {e}")
    
    # Contest simulation
    print("\n" + "=" * 60)
    print("CONTEST SIMULATION")
    print("=" * 60)
    
    print("Contest Problem 1: Maximum Frequency")
    print("Difficulty: Easy (3 points)")
    print("Expected Time: 5-8 minutes")
    print("\nKey Insights:")
    print("  • Use hash table for O(n) frequency counting")
    print("  • Track maximum frequency during iteration")
    print("  • Handle edge cases: empty array, single element")
    print("  • Python Counter.most_common() is convenient but slightly slower")
    
    print("\nContest Strategy:")
    print("  1. Read problem carefully (1 min)")
    print("  2. Identify it as frequency counting (30 sec)")
    print("  3. Implement hash table solution (3-4 mins)")
    print("  4. Test with examples (1-2 mins)")
    print("  5. Submit and move to next problem")
    
    print("\nCommon Mistakes to Avoid:")
    print("  • Forgetting to handle empty arrays")
    print("  • Using inefficient O(n²) nested loop approach")
    print("  • Not updating max frequency during counting")
    print("  • Off-by-one errors in frequency tracking")

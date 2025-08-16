"""
Solution for Count Primes
Problem ID: 204
LeetCode Problem: https://leetcode.com/problems/count-primes/

Count the number of prime numbers less than a non-negative integer, n.
"""

import math

def count_primes_basic(n: int) -> int:
    """
    Basic trial division approach.
    
    Args:
        n: Upper bound (exclusive)
        
    Returns:
        Count of prime numbers less than n
        
    Time Complexity: O(n^1.5)
    Space Complexity: O(1)
    """
    if n <= 2:
        return 0
    
    def is_prime(num):
        """Check if a number is prime using trial division."""
        if num < 2:
            return False
        if num == 2:
            return True
        if num % 2 == 0:
            return False
        
        for i in range(3, int(math.sqrt(num)) + 1, 2):
            if num % i == 0:
                return False
        return True
    
    count = 0
    for i in range(2, n):
        if is_prime(i):
            count += 1
    
    return count

def count_primes_sieve(n: int) -> int:
    """
    Sieve of Eratosthenes approach.
    
    Args:
        n: Upper bound (exclusive)
        
    Returns:
        Count of prime numbers less than n
        
    Time Complexity: O(n log log n)
    Space Complexity: O(n)
    """
    if n <= 2:
        return 0
    
    # Initialize sieve array
    is_prime = [True] * n
    is_prime[0] = is_prime[1] = False
    
    # Sieve of Eratosthenes
    for i in range(2, int(math.sqrt(n)) + 1):
        if is_prime[i]:
            # Mark all multiples of i as composite
            for j in range(i * i, n, i):
                is_prime[j] = False
    
    # Count primes
    return sum(is_prime)

def count_primes_optimized_sieve(n: int) -> int:
    """
    Optimized Sieve of Eratosthenes.
    Only considers odd numbers and optimizes memory access.
    
    Args:
        n: Upper bound (exclusive)
        
    Returns:
        Count of prime numbers less than n
        
    Time Complexity: O(n log log n)
    Space Complexity: O(n/2)
    """
    if n <= 2:
        return 0
    if n == 3:
        return 1
    
    # Handle 2 separately, then work with odd numbers only
    # is_prime[i] represents whether (2*i + 3) is prime
    size = (n - 3) // 2 + 1
    is_prime = [True] * size
    
    limit = int(math.sqrt(n))
    for i in range(3, limit + 1, 2):
        if i >= n:
            break
        
        # Check if i is prime (convert to index)
        idx = (i - 3) // 2
        if idx < len(is_prime) and is_prime[idx]:
            # Mark multiples of i starting from i*i
            start = i * i
            if start < n:
                start_idx = (start - 3) // 2
                for j in range(start_idx, size, i):
                    is_prime[j] = False
    
    # Count primes: 2 + odd primes
    return 1 + sum(is_prime)

def count_primes_segmented_sieve(n: int) -> int:
    """
    Segmented Sieve approach for better cache efficiency.
    
    Args:
        n: Upper bound (exclusive)
        
    Returns:
        Count of prime numbers less than n
        
    Time Complexity: O(n log log n)
    Space Complexity: O(sqrt(n))
    """
    if n <= 2:
        return 0
    
    limit = int(math.sqrt(n)) + 1
    
    # First, find all primes up to sqrt(n) using simple sieve
    is_prime_small = [True] * limit
    is_prime_small[0] = is_prime_small[1] = False
    
    for i in range(2, int(math.sqrt(limit)) + 1):
        if is_prime_small[i]:
            for j in range(i * i, limit, i):
                is_prime_small[j] = False
    
    primes = [i for i in range(2, limit) if is_prime_small[i]]
    
    count = 0
    segment_size = max(int(math.sqrt(n)), 32768)  # Use cache-friendly size
    
    # Process segments
    for low in range(0, n, segment_size):
        high = min(low + segment_size, n)
        segment = [True] * (high - low)
        
        # Mark composites in current segment
        for prime in primes:
            if prime * prime >= high:
                break
            
            # Find first multiple of prime in segment
            start = max(prime * prime, (low + prime - 1) // prime * prime)
            
            for j in range(start, high, prime):
                segment[j - low] = False
        
        # Count primes in segment
        for i in range(len(segment)):
            num = low + i
            if num >= 2 and segment[i]:
                count += 1
    
    return count

def count_primes_wheel_factorization(n: int) -> int:
    """
    Wheel factorization optimization (2, 3, 5 wheel).
    
    Args:
        n: Upper bound (exclusive)
        
    Returns:
        Count of prime numbers less than n
        
    Time Complexity: O(n log log n) with better constant
    Space Complexity: O(n)
    """
    if n <= 2:
        return 0
    if n <= 3:
        return 1
    if n <= 5:
        return 2
    if n <= 7:
        return 3
    
    # Wheel increments for 2*3*5 = 30 wheel
    # Numbers coprime to 30: [1,7,11,13,17,19,23,29]
    wheel = [4, 6, 10, 12, 16, 18, 22, 24]  # Differences between consecutive coprimes
    
    # Start with base primes
    primes = [2, 3, 5]
    count = 3
    
    # Generate candidates using wheel
    candidate = 7
    wheel_index = 1
    
    while candidate < n:
        is_prime = True
        sqrt_candidate = int(math.sqrt(candidate)) + 1
        
        # Check divisibility by known primes
        for prime in primes:
            if prime >= sqrt_candidate:
                break
            if candidate % prime == 0:
                is_prime = False
                break
        
        if is_prime:
            primes.append(candidate)
            count += 1
        
        # Move to next wheel candidate
        candidate += wheel[wheel_index]
        wheel_index = (wheel_index + 1) % len(wheel)
    
    return count

def count_primes_bit_sieve(n: int) -> int:
    """
    Bit-packed sieve for memory efficiency.
    
    Args:
        n: Upper bound (exclusive)
        
    Returns:
        Count of prime numbers less than n
        
    Time Complexity: O(n log log n)
    Space Complexity: O(n/8) - bit packing
    """
    if n <= 2:
        return 0
    
    # Bit array for odd numbers only (even numbers except 2 are not prime)
    # Bit i represents number 2*i + 3
    size = (n - 3) // 2 + 1
    
    # Use bytearray for bit manipulation
    sieve = bytearray((size + 7) // 8)
    
    def set_bit(index):
        """Set bit at index (mark as composite)."""
        byte_index = index // 8
        bit_index = index % 8
        if byte_index < len(sieve):
            sieve[byte_index] |= (1 << bit_index)
    
    def get_bit(index):
        """Get bit at index (check if composite)."""
        byte_index = index // 8
        bit_index = index % 8
        if byte_index >= len(sieve):
            return False
        return bool(sieve[byte_index] & (1 << bit_index))
    
    # Sieve odd numbers
    limit = int(math.sqrt(n))
    for i in range(3, limit + 1, 2):
        idx = (i - 3) // 2
        if not get_bit(idx):  # i is prime
            # Mark multiples of i
            for j in range(i * i, n, 2 * i):  # Only odd multiples
                if j % 2 == 1:  # Ensure odd
                    mark_idx = (j - 3) // 2
                    set_bit(mark_idx)
    
    # Count primes: 2 + odd primes
    count = 1  # Count 2
    for i in range(size):
        if not get_bit(i):
            count += 1
    
    return count

# Main function for the problem
def countPrimes(n: int) -> int:
    """
    Main solution using optimized sieve for best performance.
    """
    return count_primes_optimized_sieve(n)

if __name__ == "__main__":
    # Test cases
    test_cases = [
        (0, 0),
        (1, 0),
        (2, 0),
        (3, 1),   # primes: [2]
        (4, 2),   # primes: [2, 3]
        (5, 2),   # primes: [2, 3]
        (10, 4),  # primes: [2, 3, 5, 7]
        (20, 8),  # primes: [2, 3, 5, 7, 11, 13, 17, 19]
        (30, 10), # primes: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        (100, 25),
        (1000, 168),
        (10000, 1229),
    ]
    
    print("=" * 60)
    print("COUNT PRIMES - COMPREHENSIVE TESTING")
    print("=" * 60)
    
    algorithms = [
        ("Basic Trial Division", count_primes_basic),
        ("Sieve of Eratosthenes", count_primes_sieve),
        ("Optimized Sieve", count_primes_optimized_sieve),
        ("Segmented Sieve", count_primes_segmented_sieve),
        ("Wheel Factorization", count_primes_wheel_factorization),
        ("Bit-packed Sieve", count_primes_bit_sieve),
    ]
    
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
    
    # Performance comparison
    print("\n" + "=" * 60)
    print("PERFORMANCE COMPARISON")
    print("=" * 60)
    
    performance_test_sizes = [10000, 50000, 100000, 500000]
    
    # For large tests, skip slower algorithms
    fast_algorithms = [
        ("Sieve of Eratosthenes", count_primes_sieve),
        ("Optimized Sieve", count_primes_optimized_sieve),
        ("Segmented Sieve", count_primes_segmented_sieve),
        ("Bit-packed Sieve", count_primes_bit_sieve),
    ]
    
    for n in performance_test_sizes:
        print(f"\nPerformance test for n = {n}:")
        
        # Use basic algorithm only for smaller sizes
        test_algorithms = algorithms if n <= 10000 else fast_algorithms
        
        results = []
        for name, func in test_algorithms:
            try:
                import time
                start_time = time.time()
                result = func(n)
                end_time = time.time()
                
                results.append(result)
                print(f"  {name}: {result} primes in {end_time - start_time:.6f}s")
                
            except Exception as e:
                print(f"  {name}: ERROR - {e}")
        
        # Verify consistency
        if len(set(results)) > 1:
            print(f"  WARNING: Inconsistent results!")
    
    # Memory usage analysis
    print("\n" + "=" * 60)
    print("MEMORY USAGE ANALYSIS")
    print("=" * 60)
    
    import sys
    
    def estimate_memory_usage(n, func):
        """Estimate memory usage for different algorithms."""
        if func == count_primes_basic:
            return 8, "O(1)"  # Minimal memory
        elif func == count_primes_sieve:
            return n, "O(n)"  # Boolean array
        elif func == count_primes_optimized_sieve:
            return n // 2, "O(n/2)"  # Odd numbers only
        elif func == count_primes_segmented_sieve:
            return int(math.sqrt(n)), "O(sqrt(n))"  # Segment size
        elif func == count_primes_bit_sieve:
            return n // 16, "O(n/16)"  # Bit packing
        else:
            return n, "O(n)"  # Default estimate
    
    memory_test_sizes = [1000, 10000, 100000, 1000000]
    
    for n in memory_test_sizes:
        print(f"\nMemory usage estimates for n = {n}:")
        
        for name, func in algorithms:
            estimated_bytes, complexity = estimate_memory_usage(n, func)
            estimated_mb = estimated_bytes / (1024 * 1024)
            print(f"  {name}: ~{estimated_mb:.2f} MB ({complexity})")
    
    # Prime distribution analysis
    print("\n" + "=" * 60)
    print("PRIME DISTRIBUTION ANALYSIS")
    print("=" * 60)
    
    def prime_density(n, prime_count):
        """Calculate prime density."""
        if n <= 0:
            return 0
        return prime_count / n
    
    def theoretical_density(n):
        """Theoretical prime density using prime number theorem."""
        if n <= 1:
            return 0
        return 1 / math.log(n)
    
    analysis_sizes = [100, 1000, 10000, 100000]
    
    for n in analysis_sizes:
        prime_count = count_primes_optimized_sieve(n)
        actual_density = prime_density(n, prime_count)
        theoretical = theoretical_density(n)
        
        print(f"n = {n:6d}: {prime_count:5d} primes")
        print(f"  Actual density: {actual_density:.6f}")
        print(f"  Theoretical:   {theoretical:.6f}")
        print(f"  Ratio:         {actual_density/theoretical if theoretical > 0 else 0:.3f}")
        print()
    
    # Correctness verification with known prime sequences
    print("\n" + "=" * 60)
    print("CORRECTNESS VERIFICATION")
    print("=" * 60)
    
    def get_primes_list(n):
        """Get actual list of primes less than n for verification."""
        if n <= 2:
            return []
        
        is_prime = [True] * n
        is_prime[0] = is_prime[1] = False
        
        for i in range(2, int(math.sqrt(n)) + 1):
            if is_prime[i]:
                for j in range(i * i, n, i):
                    is_prime[j] = False
        
        return [i for i in range(2, n) if is_prime[i]]
    
    # Verify against known prime sequences
    verification_cases = [
        (30, [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]),
        (50, [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]),
    ]
    
    for n, expected_primes in verification_cases:
        actual_primes = get_primes_list(n)
        print(f"Primes less than {n}:")
        print(f"  Expected: {expected_primes}")
        print(f"  Actual:   {actual_primes}")
        print(f"  Match: {'✓' if actual_primes == expected_primes else '✗'}")
        
        # Test all algorithms
        for name, func in algorithms:
            try:
                count = func(n)
                expected_count = len(expected_primes)
                status = "✓" if count == expected_count else "✗"
                print(f"  {name}: {count} {status}")
            except:
                print(f"  {name}: ERROR")
        print()
    
    # Edge case testing
    print("\n" + "=" * 60)
    print("EDGE CASE TESTING")
    print("=" * 60)
    
    edge_cases = [
        (0, "Zero"),
        (1, "One"),
        (2, "Two (first prime)"),
        (3, "Three (second prime)"),
        (4, "Four (first composite)"),
        (2**16, "Large power of 2"),
        (999983, "Large prime - 1"),
        (1000000, "One million"),
    ]
    
    for n, description in edge_cases:
        print(f"\n{description} (n = {n}):")
        
        # Test fast algorithms only for large numbers
        test_algorithms = fast_algorithms if n > 100000 else algorithms
        
        results = []
        for name, func in test_algorithms:
            try:
                import time
                start_time = time.time()
                result = func(n)
                end_time = time.time()
                
                results.append(result)
                print(f"  {name}: {result} ({end_time - start_time:.6f}s)")
                
            except Exception as e:
                print(f"  {name}: ERROR - {e}")
        
        # Check consistency
        if len(set(results)) > 1:
            print(f"  WARNING: Inconsistent results!")
        
        if results:
            density = prime_density(n, results[0])
            print(f"  Prime density: {density:.6f}")
    
    # Twin primes analysis
    print("\n" + "=" * 60)
    print("TWIN PRIMES ANALYSIS")
    print("=" * 60)
    
    def count_twin_primes(n):
        """Count twin prime pairs less than n."""
        primes = get_primes_list(n)
        twin_pairs = []
        
        for i in range(len(primes) - 1):
            if primes[i + 1] - primes[i] == 2:
                twin_pairs.append((primes[i], primes[i + 1]))
        
        return len(twin_pairs), twin_pairs
    
    for n in [100, 1000, 10000]:
        twin_count, twin_pairs = count_twin_primes(n)
        total_primes = count_primes_optimized_sieve(n)
        
        print(f"n = {n}: {twin_count} twin prime pairs out of {total_primes} primes")
        if n <= 100:
            print(f"  Twin pairs: {twin_pairs}")
        print(f"  Twin ratio: {twin_count / total_primes if total_primes > 0 else 0:.4f}")

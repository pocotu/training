"""
Median of Two Sorted Arrays - LeetCode Problem #4
Problem ID: 004

Given two sorted arrays nums1 and nums2 of size m and n respectively,
return the median of the two sorted arrays.

Time Complexity: O(log(min(m,n)))
Space Complexity: O(1)
"""

def find_median_sorted_arrays(nums1, nums2):
    """
    Find median of two sorted arrays using binary search.
    
    Args:
        nums1: First sorted array
        nums2: Second sorted array
        
    Returns:
        Median of the combined arrays as float
    """
    # Ensure nums1 is the smaller array for optimization
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1
    
    m, n = len(nums1), len(nums2)
    
    # Binary search on the smaller array
    left, right = 0, m
    
    while left <= right:
        # Partition nums1
        partition_x = (left + right) // 2
        # Partition nums2 to ensure left side has half elements
        partition_y = (m + n + 1) // 2 - partition_x
        
        # Find max elements on left side of partitions
        max_left_x = float('-inf') if partition_x == 0 else nums1[partition_x - 1]
        max_left_y = float('-inf') if partition_y == 0 else nums2[partition_y - 1]
        
        # Find min elements on right side of partitions
        min_right_x = float('inf') if partition_x == m else nums1[partition_x]
        min_right_y = float('inf') if partition_y == n else nums2[partition_y]
        
        # Check if we found the correct partition
        if max_left_x <= min_right_y and max_left_y <= min_right_x:
            # We found the correct partition
            # Calculate median based on total length
            if (m + n) % 2 == 0:
                # Even total length - average of two middle elements
                return (max(max_left_x, max_left_y) + min(min_right_x, min_right_y)) / 2.0
            else:
                # Odd total length - the max of left side
                return float(max(max_left_x, max_left_y))
        
        elif max_left_x > min_right_y:
            # We have gone too far on right side for partition_x
            # Go to left side
            right = partition_x - 1
        else:
            # We have gone too far on left side for partition_x
            # Go to right side
            left = partition_x + 1
    
    # Should never reach here for valid input
    raise ValueError("Input arrays are not sorted or invalid")

def find_median_merge(nums1, nums2):
    """
    Alternative solution by merging arrays - O(m+n) time complexity.
    Used for verification and learning purposes.
    
    Args:
        nums1: First sorted array
        nums2: Second sorted array
        
    Returns:
        Median of the combined arrays as float
    """
    # Merge the arrays
    merged = []
    i, j = 0, 0
    
    while i < len(nums1) and j < len(nums2):
        if nums1[i] <= nums2[j]:
            merged.append(nums1[i])
            i += 1
        else:
            merged.append(nums2[j])
            j += 1
    
    # Add remaining elements
    while i < len(nums1):
        merged.append(nums1[i])
        i += 1
    
    while j < len(nums2):
        merged.append(nums2[j])
        j += 1
    
    # Calculate median
    n = len(merged)
    if n % 2 == 0:
        return (merged[n // 2 - 1] + merged[n // 2]) / 2.0
    else:
        return float(merged[n // 2])

def find_median_optimized_merge(nums1, nums2):
    """
    Optimized merge approach that only finds necessary elements.
    Time: O(m+n), Space: O(1)
    
    Args:
        nums1: First sorted array
        nums2: Second sorted array
        
    Returns:
        Median of the combined arrays as float
    """
    total_length = len(nums1) + len(nums2)
    is_even = total_length % 2 == 0
    
    # We need to find element(s) at position(s):
    if is_even:
        target_indices = [total_length // 2 - 1, total_length // 2]
    else:
        target_indices = [total_length // 2]
    
    i, j = 0, 0
    current_index = 0
    median_elements = []
    
    while current_index <= max(target_indices) and (i < len(nums1) or j < len(nums2)):
        # Determine which element to take next
        if i >= len(nums1):
            current_val = nums2[j]
            j += 1
        elif j >= len(nums2):
            current_val = nums1[i]
            i += 1
        elif nums1[i] <= nums2[j]:
            current_val = nums1[i]
            i += 1
        else:
            current_val = nums2[j]
            j += 1
        
        # Check if this is one of our target indices
        if current_index in target_indices:
            median_elements.append(current_val)
        
        current_index += 1
    
    # Calculate median
    if is_even:
        return sum(median_elements) / 2.0
    else:
        return float(median_elements[0])

def find_kth_element(nums1, nums2, k):
    """
    Helper function to find kth smallest element in two sorted arrays.
    Can be used to find median by calling with appropriate k values.
    
    Args:
        nums1: First sorted array
        nums2: Second sorted array
        k: Position of element to find (1-indexed)
        
    Returns:
        The kth smallest element
    """
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1
    
    m, n = len(nums1), len(nums2)
    
    if k > m + n or k < 1:
        return None
    
    if m == 0:
        return nums2[k - 1]
    
    if k == 1:
        return min(nums1[0], nums2[0])
    
    # Binary search approach
    left, right = max(0, k - n), min(k, m)
    
    while left <= right:
        cut1 = (left + right) // 2
        cut2 = k - cut1
        
        left1 = float('-inf') if cut1 == 0 else nums1[cut1 - 1]
        left2 = float('-inf') if cut2 == 0 else nums2[cut2 - 1]
        
        right1 = float('inf') if cut1 == m else nums1[cut1]
        right2 = float('inf') if cut2 == n else nums2[cut2]
        
        if left1 <= right2 and left2 <= right1:
            return max(left1, left2)
        elif left1 > right2:
            right = cut1 - 1
        else:
            left = cut1 + 1
    
    return None

# Example usage and testing
if __name__ == "__main__":
    # Test cases from LeetCode
    test_cases = [
        ([1, 3], [2], 2.0),           # Example 1
        ([1, 2], [3, 4], 2.5),        # Example 2
        ([], [1], 1.0),               # Empty array
        ([2], [], 2.0),               # Empty array reverse
        ([1, 2, 3], [4, 5, 6], 3.5),  # Equal length
        ([1], [2, 3, 4], 2.5),        # Different lengths
        ([-1, 0], [1, 2, 3], 1.0),    # Negative numbers
    ]
    
    print("Testing Median of Two Sorted Arrays:")
    print("=" * 50)
    
    for i, (nums1, nums2, expected) in enumerate(test_cases, 1):
        print(f"\nTest Case {i}:")
        print(f"  nums1 = {nums1}")
        print(f"  nums2 = {nums2}")
        print(f"  Expected: {expected}")
        
        # Test binary search solution
        result_binary = find_median_sorted_arrays(nums1, nums2)
        print(f"  Binary Search: {result_binary}")
        
        # Test merge solution
        result_merge = find_median_merge(nums1, nums2)
        print(f"  Merge Solution: {result_merge}")
        
        # Test optimized merge
        result_opt_merge = find_median_optimized_merge(nums1, nums2)
        print(f"  Optimized Merge: {result_opt_merge}")
        
        # Verify all solutions match
        print(f"  All methods agree: {abs(result_binary - expected) < 1e-9 and abs(result_merge - expected) < 1e-9 and abs(result_opt_merge - expected) < 1e-9}")
        
        # Test kth element approach
        total_len = len(nums1) + len(nums2)
        if total_len % 2 == 1:
            k = total_len // 2 + 1
            kth_result = find_kth_element(nums1, nums2, k)
            print(f"  Kth element (k={k}): {kth_result}")
        else:
            k1, k2 = total_len // 2, total_len // 2 + 1
            kth1 = find_kth_element(nums1, nums2, k1)
            kth2 = find_kth_element(nums1, nums2, k2)
            kth_median = (kth1 + kth2) / 2.0
            print(f"  Kth elements (k={k1},{k2}): {kth1}, {kth2} -> {kth_median}")
    
    # Performance comparison
    print("\n" + "=" * 50)
    print("Performance Test:")
    
    import time
    
    # Create larger test arrays
    large_nums1 = list(range(0, 1000, 2))   # [0, 2, 4, ..., 998]
    large_nums2 = list(range(1, 1001, 2))   # [1, 3, 5, ..., 999]
    
    # Test binary search approach
    start_time = time.time()
    result_binary = find_median_sorted_arrays(large_nums1, large_nums2)
    binary_time = time.time() - start_time
    
    # Test merge approach
    start_time = time.time()
    result_merge = find_median_merge(large_nums1, large_nums2)
    merge_time = time.time() - start_time
    
    print(f"Array sizes: {len(large_nums1)}, {len(large_nums2)}")
    print(f"Binary Search: {result_binary} in {binary_time:.6f} seconds")
    print(f"Merge approach: {result_merge} in {merge_time:.6f} seconds")
    print(f"Binary search is {merge_time/binary_time:.2f}x faster")
    print(f"Results match: {abs(result_binary - result_merge) < 1e-9}")
    
    # Edge case testing
    print("\n" + "=" * 50)
    print("Edge Case Testing:")
    
    edge_cases = [
        ([100], [1, 2, 3, 4, 5]),
        ([1, 1, 1, 1], [1, 1, 1, 1]),
        ([-5, -3, -1], [2, 4, 6]),
        ([0], [0]),
    ]
    
    for nums1, nums2 in edge_cases:
        result = find_median_sorted_arrays(nums1, nums2)
        print(f"{nums1} + {nums2} -> {result}")

"""
Solution for Top K Frequent Elements
Problem ID: 109
LeetCode Problem: https://leetcode.com/problems/top-k-frequent-elements/

Given an integer array nums and an integer k, return the k most frequent elements.
You may return the answer in any order.
"""

import heapq
from collections import Counter

def top_k_frequent(nums: list[int], k: int) -> list[int]:
    """
    Find the k most frequent elements.
    
    Args:
        nums: List of integers
        k: Number of most frequent elements to return
        
    Returns:
        List of k most frequent elements
        
    Time Complexity: O(n log k)
    Space Complexity: O(n)
    """
    # Count frequencies
    count = Counter(nums)
    
    # Use min heap to keep track of k most frequent elements
    heap = []
    
    for num, freq in count.items():
        heapq.heappush(heap, (freq, num))
        
        if len(heap) > k:
            heapq.heappop(heap)
    
    # Extract elements from heap
    result = []
    while heap:
        freq, num = heapq.heappop(heap)
        result.append(num)
    
    return result[::-1]  # Reverse to get most frequent first

def top_k_frequent_bucket_sort(nums: list[int], k: int) -> list[int]:
    """
    Alternative solution using bucket sort.
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    count = Counter(nums)
    
    # Create buckets where index represents frequency
    buckets = [[] for _ in range(len(nums) + 1)]
    
    for num, freq in count.items():
        buckets[freq].append(num)
    
    # Collect k most frequent elements
    result = []
    for i in range(len(buckets) - 1, -1, -1):
        for num in buckets[i]:
            result.append(num)
            if len(result) == k:
                return result
    
    return result

if __name__ == "__main__":
    # Test cases
    test_cases = [
        ([1,1,1,2,2,3], 2),  # Expected: [1,2]
        ([1], 1),            # Expected: [1]
    ]
    
    for nums, k in test_cases:
        result1 = top_k_frequent(nums, k)
        result2 = top_k_frequent_bucket_sort(nums, k)
        print(f"Input: {nums}, k={k}")
        print(f"Heap solution: {result1}")
        print(f"Bucket sort: {result2}")
        print()

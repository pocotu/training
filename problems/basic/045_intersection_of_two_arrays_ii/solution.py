"""
Solution for Intersection of Two Arrays II
Problem ID: 045
LeetCode: https://leetcode.com/problems/intersection-of-two-arrays-ii/

Time Complexity: O(m + n)
Space Complexity: O(min(m,n))
"""

def intersect(nums1, nums2):
    """
    Find intersection of two arrays with duplicates.
    
    Args:
        nums1: First array of integers
        nums2: Second array of integers
        
    Returns:
        Array containing intersection with duplicates
    """
    # TODO: Implement your solution here
    pass

def intersect_sorted(nums1, nums2):
    """
    Alternative solution using two pointers (assumes sorted arrays).
    """
    # TODO: Implement two-pointer solution
    pass

def intersect_optimized(nums1, nums2):
    """
    Space-optimized solution.
    """
    # TODO: Implement space-optimized solution
    pass

if __name__ == "__main__":
    # Test cases
    test_cases = [
        ([1,2,2,1], [2,2]),
        ([4,9,5], [9,4,9,8,4]),
        ([1,2,3], [4,5,6]),
        ([1,1,1], [1,1])
    ]
    
    for nums1, nums2 in test_cases:
        result = intersect(nums1, nums2)
        print(f"intersect({nums1}, {nums2}) = {result}")
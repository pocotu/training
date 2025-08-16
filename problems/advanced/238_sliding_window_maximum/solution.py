"""
Sliding Window Maximum - LeetCode Problem #239
Problem ID: 238

You are given an array of integers nums, there is a sliding window of size k 
which is moving from the very left of the array to the very right. You can 
only see the k numbers in the window. Each time the sliding window moves 
right by one position.

Return the max sliding window.

Time Complexity: O(n)
Space Complexity: O(k)
"""

from collections import deque

def max_sliding_window(nums, k):
    """
    Find maximum in each sliding window of size k using monotonic deque.
    
    Args:
        nums: List[int] - array of integers
        k: int - window size
        
    Returns:
        List[int]: maximum value in each window
    """
    if not nums or k == 0:
        return []
    
    dq = deque()  # Store indices
    result = []
    
    for i in range(len(nums)):
        # Remove indices outside current window
        while dq and dq[0] < i - k + 1:
            dq.popleft()
        
        # Remove indices whose values are smaller than current
        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()
        
        dq.append(i)
        
        # Add to result if window is complete
        if i >= k - 1:
            result.append(nums[dq[0]])
    
    return result

# Alternative approach using segment tree (more complex but instructive)
class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)
        self.arr = arr
        self.build(1, 0, self.n - 1)
    
    def build(self, node, start, end):
        if start == end:
            self.tree[node] = self.arr[start]
        else:
            mid = (start + end) // 2
            self.build(2 * node, start, mid)
            self.build(2 * node + 1, mid + 1, end)
            self.tree[node] = max(self.tree[2 * node], self.tree[2 * node + 1])
    
    def query(self, node, start, end, l, r):
        if r < start or end < l:
            return float('-inf')
        if l <= start and end <= r:
            return self.tree[node]
        
        mid = (start + end) // 2
        return max(self.query(2 * node, start, mid, l, r),
                  self.query(2 * node + 1, mid + 1, end, l, r))
    
    def range_max(self, l, r):
        return self.query(1, 0, self.n - 1, l, r)

def max_sliding_window_segment_tree(nums, k):
    """Alternative solution using segment tree"""
    if not nums or k == 0:
        return []
    
    st = SegmentTree(nums)
    result = []
    
    for i in range(len(nums) - k + 1):
        result.append(st.range_max(i, i + k - 1))
    
    return result

# Brute force solution for comparison (O(nk))
def max_sliding_window_brute_force(nums, k):
    """Brute force solution for small inputs or verification"""
    if not nums or k == 0:
        return []
    
    result = []
    for i in range(len(nums) - k + 1):
        window_max = max(nums[i:i+k])
        result.append(window_max)
    
    return result

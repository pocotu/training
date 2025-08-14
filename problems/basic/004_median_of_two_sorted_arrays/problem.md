# Median of Two Sorted Arrays

## Problem Description

Given two sorted arrays `nums1` and `nums2` of size `m` and `n` respectively, return **the median** of the two sorted arrays.

The overall run time complexity should be `O(log (m+n))`.

## Examples

### Example 1:
```
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
```

### Example 2:
```
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
```

## Constraints

- `nums1.length == m`
- `nums2.length == n`
- `0 <= m <= 1000`
- `0 <= n <= 1000`
- `1 <= m + n <= 2000`
- `-10^6 <= nums1[i], nums2[i] <= 10^6`

## Key Insights

1. **Median Definition**: For an array of length n:
   - If n is odd: median is the middle element
   - If n is even: median is the average of two middle elements

2. **Binary Search Approach**: 
   - We need to find the correct partition of both arrays
   - Left partition should contain half of all elements
   - All elements in left partition ≤ all elements in right partition

3. **Partition Properties**:
   - `leftMaxX ≤ rightMinY` and `leftMaxY ≤ rightMinX`
   - Where X and Y are the two arrays after partitioning

## Algorithm

1. Ensure `nums1` is the smaller array (for optimization)
2. Use binary search on the smaller array
3. For each partition of `nums1`, calculate corresponding partition of `nums2`
4. Check if partition is valid
5. Adjust search range based on partition validity
6. Calculate median when valid partition is found

## Related Topics

- Array
- Binary Search
- Divide and Conquer

## Companies

- Google
- Microsoft
- Amazon
- Facebook
- Adobe
- Apple

## Follow Up

Can you solve this problem in O(log(min(m,n))) time complexity?

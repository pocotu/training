# Maximum Frequency

## Problem Statement

Given an integer array `nums`, return the maximum frequency of any element in the array.

The frequency of an element is the number of times it appears in the array.

## Examples

### Example 1:
```
Input: nums = [1,2,2,3,1,4]
Output: 2
Explanation: The elements 1 and 2 both appear 2 times, which is the maximum frequency.
```

### Example 2:
```
Input: nums = [1,1,1,2,2,3]
Output: 3
Explanation: The element 1 appears 3 times, which is the maximum frequency.
```

### Example 3:
```
Input: nums = [1]
Output: 1
Explanation: The element 1 appears 1 time, which is the maximum frequency.
```

## Constraints

- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^5`

## Notes

- This is a straightforward frequency counting problem
- Hash table/dictionary is the most efficient approach
- Consider edge cases with single elements and duplicate maximums

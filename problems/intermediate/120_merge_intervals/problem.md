# Merge Intervals

## Problem Description

Given an array of `intervals` where `intervals[i] = [starti, endi]`, merge all overlapping intervals, and return *an array of the non-overlapping intervals that cover all the intervals in the input*.

## Examples

### Example 1:
```
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
```

### Example 2:
```
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
```

## Constraints

- `1 <= intervals.length <= 10^4`
- `intervals[i].length == 2`
- `0 <= starti <= endi <= 10^4`

## Hints

1. Sort intervals by start time.
2. Iterate through sorted intervals.
3. If current interval overlaps with the last merged interval, merge them.
4. Otherwise, add current interval to result.

## Related Topics

- Array
- Sorting

## Companies

- Facebook
- Microsoft
- Amazon
- Google
- LinkedIn

## Algorithm

1. **Sort**: Sort intervals by start time
2. **Iterate**: Go through each interval
3. **Merge**: If overlap with last merged interval, merge them
4. **Add**: Otherwise, add to result

### Overlap Condition
Two intervals [a,b] and [c,d] overlap if: `b >= c` (assuming a <= c after sorting)

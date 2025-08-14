---
problem_id: "LC_W380_P3"
contest_id: "weekly_380"
platform: "leetcode"
contest_type: "weekly"
problem_number: 3
title: "Maximum Binary Array After Change"
difficulty: "Medium"
points: 5
time_limit: "2 seconds"
memory_limit: "256 MB"
tags: ["array", "greedy", "bit-manipulation", "dynamic-programming"]
contest_stats:
  total_submissions: 3421
  successful_submissions: 1847
  success_rate: 54.0%
  average_attempts: 1.9
approach_hints:
  - "Consider greedy approach for bit optimization"
  - "Think about state transition between 0s and 1s"
  - "Analyze the effect of each operation"
editorial_complexity:
  time: "O(n)"
  space: "O(1)"
contest_context:
  typical_solve_time: "25-40 minutes"
  difficulty_progression: "Third problem in contest - medium difficulty"
  key_insight: "Greedy choice at each position leads to optimal solution"
---

# 3. Maximum Binary Array After Change

**Difficulty:** Medium  
**Points:** 5  
**Time Limit:** 2 seconds  
**Memory Limit:** 256 MB

## Problem Statement

You are given a binary array `nums` of length `n`. You can perform the following operation any number of times:

- Choose an index `i` (0 ≤ i < n) and flip the bit at position `i` (0 becomes 1, 1 becomes 0).
- After flipping, if there exists an index `j` (0 ≤ j < n, j ≠ i) such that `nums[j] == nums[i]`, you must flip the bit at position `j` as well.

Your goal is to maximize the number of 1s in the final array. Return the maximum number of 1s you can achieve.

## Examples

### Example 1:
```
Input: nums = [1,0,1,0]
Output: 4
Explanation:
- Initially: [1,0,1,0]
- Flip index 1: [1,1,1,0], then must flip index 0 (both were 0): [0,1,1,0]
- Flip index 0: [1,1,1,0], then must flip index 3 (both were 0): [1,1,1,1]
- Result: 4 ones
```

### Example 2:
```
Input: nums = [0,0,0,0]
Output: 0
Explanation:
- Any flip operation will create two 1s, but then we must flip them back to 0s.
- Result: 0 ones
```

### Example 3:
```
Input: nums = [1,1,0,0,1]
Output: 5
Explanation:
- Initially: [1,1,0,0,1] already has optimal distribution
- We can achieve all 1s through strategic flipping
- Result: 5 ones
```

## Constraints

- 1 ≤ nums.length ≤ 10^5
- nums[i] is either 0 or 1

## Hints

1. Think about the parity of 0s and 1s after operations
2. Consider what happens when you flip a bit and its consequences
3. The key insight involves analyzing connected components of same bits
4. Greedy approach might work if you consider the global effect of each operation

## Strategy Notes

This problem requires understanding the cascading effect of operations:
- When you flip a bit, you might trigger additional flips
- The final state depends on the parity of operations
- Consider graph theory approach where same-value positions are connected

**Contest Strategy:**
- Start with small examples to understand the pattern
- Look for mathematical properties of the operations
- Consider dynamic programming if greedy doesn't work
- Pay attention to edge cases (all 0s, all 1s, alternating pattern)

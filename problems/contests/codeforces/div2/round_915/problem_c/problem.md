---
problem_id: "915C"
contest_id: "div2_915"
platform: "codeforces"
problem_letter: "C"
title: "Permutation Operations"
difficulty: 1200
points: 1500
time_limit: "2 seconds"
memory_limit: "256 MB"
tags: ["constructive", "permutations", "greedy", "implementation"]
contest_stats:
  total_submissions: 8742
  successful_submissions: 4186
  success_rate: 47.9%
  average_attempts: 2.1
approach_hints:
  - "Think about constructive algorithms"
  - "Consider greedy placement strategies"
  - "Analyze permutation properties"
editorial_complexity:
  time: "O(n log n)"
  space: "O(n)"
---

# C. Permutation Operations

**Time limit:** 2 seconds  
**Memory limit:** 256 MB

## Problem Statement

You are given a positive integer `n`. You need to construct a permutation `p` of length `n` such that the following operation can be performed exactly `k` times:

**Operation:** Choose an index `i` (1 ≤ i ≤ n) such that `p[i] > i`, and replace `p[i]` with `p[i] - 1`.

Your task is to find any valid permutation `p`, or determine that no such permutation exists.

## Input

The first line contains a single integer `t` (1 ≤ t ≤ 1000) — the number of test cases.

Each of the next `t` lines contains two integers `n` and `k` (1 ≤ n ≤ 2000, 0 ≤ k ≤ 10^6) — the length of the permutation and the required number of operations.

## Output

For each test case:
- If no valid permutation exists, print `-1`.
- Otherwise, print `n` integers representing a valid permutation.

## Examples

### Example 1
```
Input:
4
3 2
4 5
2 0
5 10

Output:
3 2 1
4 3 2 1
1 2
-1
```

### Example 2
```
Input:
3
3 1
4 6
6 15

Output:
2 3 1
4 3 2 1
6 5 4 3 2 1
```

## Notes

**Example 1 Explanation:**

For `n=3, k=2` with permutation `[3, 2, 1]`:
- Initial: `[3, 2, 1]`
- Operation 1: Choose i=1 (p[1]=3 > 1), get `[2, 2, 1]` (invalid, not a permutation)

Let's trace `[3, 1, 2]`:
- Initial: `[3, 1, 2]`
- Operation 1: Choose i=1 (p[1]=3 > 1), get `[2, 1, 2]` (invalid)

Actually, let's trace `[2, 3, 1]`:
- Initial: `[2, 3, 1]`
- Operation 1: Choose i=1 (p[1]=2 > 1), get `[1, 3, 1]` (invalid)
- Operation 1: Choose i=2 (p[2]=3 > 2), get `[2, 2, 1]` (invalid)

The operation needs to maintain permutation property at each step.

## Constraints

- 1 ≤ t ≤ 1000
- 1 ≤ n ≤ 2000
- 0 ≤ k ≤ 10^6
- Sum of all n across test cases ≤ 2000

## Strategy Notes

This is a constructive algorithm problem requiring:

1. **Understanding the operation:** We can only decrease elements that are greater than their position
2. **Permutation constraint:** After each operation, we must still have a valid permutation
3. **Counting operations:** We need exactly `k` operations to be possible

**Key insights:**
- Maximum possible operations for permutation of length n
- How to construct permutations that allow specific number of operations
- Greedy vs. optimal construction strategies

## Contest Context

- **Typical solve time:** 20-45 minutes
- **Common mistakes:** Not ensuring permutation remains valid, incorrect operation counting
- **Key insight:** Mathematical relationship between permutation structure and operation count

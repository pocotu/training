---
problem_id: "915A"
contest_id: "div2_915"
platform: "codeforces"
problem_letter: "A"
title: "Number Game"
difficulty: 800
points: 500
time_limit: "1 second"
memory_limit: "256 MB"
tags: ["math", "implementation", "number theory"]
contest_stats:
  total_submissions: 15248
  successful_submissions: 12186
  success_rate: 79.9%
  average_attempts: 1.2
approach_hints:
  - "Look for mathematical patterns"
  - "Consider remainder operations"
  - "Think about game theory basics"
editorial_complexity:
  time: "O(1)"
  space: "O(1)"
---

# A. Number Game

**Time limit:** 1 second  
**Memory limit:** 256 MB

## Problem Statement

Alice and Bob are playing a number game. They start with a positive integer `n`. In each turn, a player can subtract from `n` any positive divisor of the current number (including 1 and the number itself), except they cannot subtract the number itself if it would make the result zero and it's not their winning move.

Alice goes first. The player who cannot make a move loses. Determine who wins with optimal play.

## Input

The first line contains a single integer `t` (1 ≤ t ≤ 1000) — the number of test cases.

Each of the next `t` lines contains a single integer `n` (1 ≤ n ≤ 10^9) — the starting number.

## Output

For each test case, print "Alice" if Alice wins, or "Bob" if Bob wins.

## Examples

### Example 1
```
Input:
4
1
2
3
4

Output:
Alice
Bob
Alice
Bob
```

### Example 2
```
Input:
3
5
6
10

Output:
Alice
Bob
Bob
```

## Notes

**Example 1 Explanation:**
- n = 1: Alice can subtract 1, leaving 0 for Bob. Alice wins.
- n = 2: Alice can subtract 1 (leaving 1) or 2 (leaving 0). If Alice subtracts 2, she wins immediately. Alice wins.
- n = 3: Alice can subtract 1 or 3. If she subtracts 3, she wins. Alice wins.
- n = 4: Alice's options are subtract 1, 2, or 4. All lead to Bob having winning positions. Bob wins.

## Constraints

- 1 ≤ t ≤ 1000
- 1 ≤ n ≤ 10^9

## Strategy Notes

This is a classic game theory problem. The key insight is recognizing the pattern based on number properties:
- Odd numbers: Alice can always subtract 1, leaving an even number for Bob
- Even numbers: More complex analysis needed based on prime factorization
- Powers of 2: Special case requiring careful analysis

## Contest Context

- **Typical solve time:** 5-15 minutes for experienced contestants
- **Common mistakes:** Not considering all edge cases, overthinking the game theory
- **Key insight:** Pattern recognition rather than complex game theory analysis

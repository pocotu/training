# Wildcard Matching

**Difficulty:** Hard  
**LeetCode Problem:** #44  
**Platform:** LeetCode

## Problem Statement

Given an input string (`s`) and a pattern (`p`), implement wildcard pattern matching with support for `'?'` and `'*'` where:

- `'?'` Matches any single character.
- `'*'` Matches any sequence of characters (including the empty sequence).

The matching should cover the **entire** input string (not partial).

## Examples

### Example 1:
```
Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
```

### Example 2:
```
Input: s = "aa", p = "*"
Output: true
Explanation: '*' matches any sequence.
```

### Example 3:
```
Input: s = "cb", p = "?a"
Output: false
Explanation: '?' matches 'c', but the second letter is 'b', which does not match 'a'.
```

## Constraints

- `0 <= s.length, p.length <= 2000`
- `s` contains only lowercase English letters.
- `p` contains only lowercase English letters, `'?'` or `'*'`.

## Algorithm Approaches

### 1. Dynamic Programming (2D)
- **Time Complexity:** O(m × n)
- **Space Complexity:** O(m × n)
- Classic DP table approach

### 2. Dynamic Programming (1D Optimized)
- **Time Complexity:** O(m × n)
- **Space Complexity:** O(n)
- Space-optimized version

### 3. Recursive with Memoization
- **Time Complexity:** O(m × n)
- **Space Complexity:** O(m × n)
- Top-down approach

### 4. Greedy with Two Pointers
- **Time Complexity:** O(m × n) worst case, O(m + n) average
- **Space Complexity:** O(1)
- Most space-efficient approach

## Key Insights

1. **'*' Handling:** The star can match zero or more characters, leading to multiple possibilities
2. **State Transitions:** For each position, consider all possible matches
3. **Edge Cases:** Empty string and pattern combinations
4. **Optimization:** Greedy approach can be more efficient in practice

## Companies

- Google
- Facebook
- Microsoft
- Amazon

# Word Break II

## Problem Description
Given a string `s` and a dictionary of strings `wordDict`, add spaces in `s` to construct a sentence where each word is a valid dictionary word. Return all such possible sentences in any order.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

## Examples

### Example 1
```
Input: s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]
Output: ["cats and dog","cat sand dog"]
```

### Example 2
```
Input: s = "pineapplepenapple", wordDict = ["apple","pen","applepen","pine","pineapple"]
Output: ["pine apple pen apple","pineapple pen apple","pine applepen apple"]
```

### Example 3
```
Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: []
```

## Constraints
- 1 <= s.length <= 20
- 1 <= wordDict.length <= 1000
- 1 <= wordDict[i].length <= 10
- s and wordDict[i] consist of only lowercase English letters
- All the strings of wordDict are unique

## Solution Approach
This is an extension of Word Break I problem. We need to find all possible ways to break the string, not just whether it's possible.

### Approaches:
1. **Backtracking with Memoization**: Use DFS with memoization to avoid recomputing
2. **Dynamic Programming**: Build solutions bottom-up
3. **Trie + Backtracking**: Optimize word lookup using Trie structure

### Key Insights:
- First check if word break is possible (optimization)
- Use memoization to cache results for substrings
- Handle combinatorial explosion carefully
- Consider early pruning strategies

## Time Complexity
- Time: O(2^n) in worst case, but memoization helps
- Space: O(n * 2^n) for storing all possible solutions

## Learning Objectives
- Master advanced dynamic programming with backtracking
- Handle string segmentation with multiple solutions
- Implement effective memoization strategies
- Optimize recursive solutions with early termination

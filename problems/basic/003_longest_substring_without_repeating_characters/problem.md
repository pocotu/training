# Longest Substring Without Repeating Characters

## Problem Description

Given a string `s`, find the length of the **longest substring** without repeating characters.

## Examples

### Example 1:
```
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
```

### Example 2:
```
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
```

### Example 3:
```
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
```

## Constraints

- `0 <= s.length <= 5 * 10^4`
- `s` consists of English letters, digits, symbols and spaces.

## Hints

1. Use the sliding window technique.
2. Keep track of characters you've seen and their positions.
3. When you encounter a repeated character, move the start of your window.
4. Use a hash map to store the most recent index of each character.

## Related Topics

- Hash Table
- String
- Sliding Window

## Companies

- Amazon
- Microsoft
- Facebook
- Google
- Apple
- Adobe

## Algorithm Approaches

### Approach 1: Sliding Window with Hash Map
- Use two pointers to maintain a sliding window
- Use hash map to store character positions
- Move left pointer when duplicate found

### Approach 2: Sliding Window with Set
- Use a set to track characters in current window
- Expand window by moving right pointer
- Shrink window by moving left pointer when duplicate found

### Approach 3: Optimized Sliding Window
- Use hash map to jump directly to position after duplicate
- More efficient than gradually moving left pointer

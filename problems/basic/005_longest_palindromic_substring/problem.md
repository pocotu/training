# Longest Palindromic Substring

## Problem Description

Given a string `s`, return the **longest palindromic substring** in `s`.

A **palindrome** is a string that reads the same forward and backward.

## Examples

### Example 1:
```
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
```

### Example 2:
```
Input: s = "cbbd"
Output: "bb"
```

## Constraints

- `1 <= s.length <= 1000`
- `s` consist of only digits and English letters.

## Approach Overview

### Approach 1: Expand Around Centers
- **Time Complexity**: O(n²)
- **Space Complexity**: O(1)
- For each character, expand around it to find palindromes
- Consider both odd-length (center is a character) and even-length (center is between characters) palindromes

### Approach 2: Dynamic Programming
- **Time Complexity**: O(n²)
- **Space Complexity**: O(n²)
- Build a table dp[i][j] indicating if substring from i to j is palindrome
- Fill table bottom-up using previously computed values

### Approach 3: Manacher's Algorithm
- **Time Complexity**: O(n)
- **Space Complexity**: O(n)
- Advanced algorithm that can find all palindromes in linear time
- Uses preprocessing and takes advantage of palindrome symmetry

## Key Insights

1. **Palindrome Properties**:
   - A palindrome reads the same forwards and backwards
   - If s[i] == s[j] and s[i+1:j] is palindrome, then s[i:j+1] is palindrome

2. **Center Expansion**:
   - Every palindrome has a center
   - Center can be a character (odd length) or between characters (even length)
   - Expand from center while characters match

3. **Edge Cases**:
   - Single character (always palindrome)
   - Two identical characters
   - No palindrome longer than 1 character

## Related Topics

- String
- Dynamic Programming
- Expand Around Centers

## Companies

- Amazon
- Microsoft
- Facebook
- Google
- Adobe
- Apple

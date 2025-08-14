# Generate Parentheses

## Problem Description

Given `n` pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

## Examples

### Example 1:
```
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
```

### Example 2:
```
Input: n = 1
Output: ["()"]
```

## Constraints

- `1 <= n <= 8`

## Hints

1. Use backtracking to generate all valid combinations.
2. Keep track of the number of open and close parentheses used.
3. Add an open parenthesis if we haven't used all n open parentheses.
4. Add a close parenthesis if it wouldn't exceed the number of open parentheses.

## Related Topics

- String
- Dynamic Programming
- Backtracking

## Companies

- Amazon
- Microsoft
- Facebook
- Google
- Uber

## Algorithm Approaches

### Approach 1: Backtracking
- Build the string character by character
- At each step, decide whether to add '(' or ')'
- Ensure validity by tracking open/close counts

### Approach 2: Dynamic Programming
- Build solutions for smaller n values
- Use memoization to avoid repeated calculations

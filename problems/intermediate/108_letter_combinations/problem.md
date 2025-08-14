# Letter Combinations of a Phone Number

## Problem Description

Given a string containing digits from `2-9` inclusive, return all possible letter combinations that the number could represent. Return the answer in **any order**.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

![Phone Keypad](https://upload.wikimedia.org/wikipedia/commons/thumb/7/73/Telephone-keypad2.svg/200px-Telephone-keypad2.svg.png)

- 2: ABC
- 3: DEF
- 4: GHI
- 5: JKL
- 6: MNO
- 7: PQRS
- 8: TUV
- 9: WXYZ

## Examples

### Example 1:
```
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
```

### Example 2:
```
Input: digits = ""
Output: []
```

### Example 3:
```
Input: digits = "2"
Output: ["a","b","c"]
```

## Constraints

- `0 <= digits.length <= 4`
- `digits[i]` is a digit in the range `['2', '9']`.

## Hints

1. Use backtracking to generate all combinations.
2. Build the result incrementally, one digit at a time.
3. For each digit, try all possible letters and recurse.
4. Use a mapping from digits to letters.

## Related Topics

- Hash Table
- String
- Backtracking

## Companies

- Amazon
- Microsoft
- Facebook
- Google
- Apple

# String Compression II

## Problem Statement

Given an array of characters `chars`, compress it using the following algorithm:

Begin with an empty string `s`. For each group of consecutive repeating characters in `chars`:
- If the group's length is 1, append the character to `s`.
- Otherwise, append the character followed by the group's length.

The compressed string `s` should not be returned separately, but instead, be stored in the input character array `chars`. 

Note that group lengths that are 10 or longer will be split into multiple characters in `chars`.

Return the new length of the array after compression.

You must write an algorithm that uses only constant extra space.

## Examples

### Example 1:
```
Input: chars = ["a","a","b","b","c","c","c"]
Output: 6
Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".
After compression: chars = ["a","2","b","2","c","3"]
```

### Example 2:
```
Input: chars = ["a"]
Output: 1
Explanation: The only group is "a", which remains uncompressed since it's a single character.
After compression: chars = ["a"]
```

### Example 3:
```
Input: chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
Output: 4
Explanation: The groups are "a" and "bbbbbbbbbbbb". This compresses to "ab12".
After compression: chars = ["a","b","1","2"]
```

## Constraints

- `1 <= chars.length <= 1000`
- `chars[i]` is a lowercase English letter, uppercase English letter, or digit
- The algorithm must use only constant extra space

## Notes

- Groups with length 1 don't include the count
- Groups with length >= 10 split the digits
- Must modify the array in-place
- Two-pointer technique is recommended

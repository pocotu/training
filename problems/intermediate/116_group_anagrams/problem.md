# Group Anagrams

## Problem Description

Given an array of strings `strs`, group the anagrams together. You can return the answer in **any order**.

An **Anagram** is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

## Examples

### Example 1:
```
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
```

### Example 2:
```
Input: strs = [""]
Output: [[""]]
```

### Example 3:
```
Input: strs = ["a"]
Output: [["a"]]
```

## Constraints

- `1 <= strs.length <= 10^4`
- `0 <= strs[i].length <= 100`
- `strs[i]` consists of lowercase English letters only.

## Hints

1. Two strings are anagrams if they have the same character count.
2. Sorting the characters of each string gives a canonical form.
3. Use a hash map to group strings with the same canonical form.
4. Alternative: Use character frequency as the key.

## Related Topics

- Array
- Hash Table
- String
- Sorting

## Companies

- Amazon
- Facebook
- Microsoft
- Google
- Uber

## Algorithm Approaches

### Approach 1: Sorting
- Sort each string to get canonical form
- Use sorted string as hash map key

### Approach 2: Character Count
- Count frequency of each character
- Use frequency tuple as hash map key

"""
Solution for Group Anagrams
Problem ID: 105
LeetCode Problem: https://leetcode.com/problems/group-anagrams/

Given an array of strings strs, group the anagrams together.
You can return the answer in any order.
"""

def group_anagrams(strs: list[str]) -> list[list[str]]:
    """
    Group anagrams together.
    
    Args:
        strs: List of strings
        
    Returns:
        List of groups where each group contains anagrams
        
    Time Complexity: O(n * k log k) where n is number of strings, k is max length
    Space Complexity: O(n * k)
    """
    anagram_groups = {}
    
    for string in strs:
        # Use sorted string as key
        key = ''.join(sorted(string))
        
        if key not in anagram_groups:
            anagram_groups[key] = []
        
        anagram_groups[key].append(string)
    
    return list(anagram_groups.values())

if __name__ == "__main__":
    # Test cases
    test_cases = [
        ["eat","tea","tan","ate","nat","bat"],
        [""],
        ["a"],
    ]
    
    for strs in test_cases:
        result = group_anagrams(strs)
        print(f"Input: {strs} -> Output: {result}")

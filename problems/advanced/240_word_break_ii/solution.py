"""
Word Break II - LeetCode Problem #140
Problem ID: 240

Given a string s and a dictionary of strings wordDict, add spaces in s 
to construct a sentence where each word is a valid dictionary word. 
Return all such possible sentences in any order.

Time Complexity: O(2^n) worst case
Space Complexity: O(n * 2^n) for storing solutions
"""

from functools import lru_cache
from typing import List

def word_break(s: str, wordDict: List[str]) -> List[str]:
    """
    Find all possible word break combinations using backtracking with memoization.
    
    Args:
        s: input string
        wordDict: list of valid words
        
    Returns:
        List[str]: all possible sentences
    """
    word_set = set(wordDict)
    memo = {}
    
    def backtrack(start: int) -> List[str]:
        if start in memo:
            return memo[start]
        
        if start == len(s):
            return [""]
        
        result = []
        for end in range(start + 1, len(s) + 1):
            word = s[start:end]
            if word in word_set:
                suffix_sentences = backtrack(end)
                for suffix in suffix_sentences:
                    if suffix:
                        result.append(word + " " + suffix)
                    else:
                        result.append(word)
        
        memo[start] = result
        return result
    
    return backtrack(0)

# Alternative approach with early pruning
def word_break_optimized(s: str, wordDict: List[str]) -> List[str]:
    """
    Optimized version with early pruning.
    First check if word break is possible.
    """
    word_set = set(wordDict)
    
    # First check if word break is possible using DP
    def can_break(s: str) -> bool:
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        
        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break
        
        return dp[n]
    
    if not can_break(s):
        return []
    
    # Now find all combinations
    memo = {}
    
    def dfs(start: int) -> List[str]:
        if start in memo:
            return memo[start]
        
        if start == len(s):
            return [""]
        
        result = []
        for end in range(start + 1, len(s) + 1):
            word = s[start:end]
            if word in word_set:
                # Check if remaining string can be broken
                remaining = s[end:]
                if not remaining or can_break(remaining):
                    suffix_sentences = dfs(end)
                    for suffix in suffix_sentences:
                        if suffix:
                            result.append(word + " " + suffix)
                        else:
                            result.append(word)
        
        memo[start] = result
        return result
    
    return dfs(0)

# Trie-based approach for faster word lookup
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word: str):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_word = True

def word_break_trie(s: str, wordDict: List[str]) -> List[str]:
    """
    Trie-based solution for efficient word lookup.
    """
    if not wordDict:
        return []
    
    if not s:
        return [""]
    
    # Build trie
    trie = Trie()
    for word in wordDict:
        trie.insert(word)
    
    memo = {}
    
    def dfs(start: int) -> List[str]:
        if start in memo:
            return memo[start]
        
        if start == len(s):
            return [""]
        
        result = []
        node = trie.root
        
        for end in range(start, len(s)):
            char = s[end]
            if char not in node.children:
                break
            
            node = node.children[char]
            if node.is_word:
                word = s[start:end + 1]
                suffix_sentences = dfs(end + 1)
                for suffix in suffix_sentences:
                    if suffix:
                        result.append(word + " " + suffix)
                    else:
                        result.append(word)
        
        memo[start] = result
        return result
    
    return dfs(0)

# Bottom-up DP approach
def word_break_dp(s: str, wordDict: List[str]) -> List[str]:
    """
    Bottom-up dynamic programming approach.
    """
    word_set = set(wordDict)
    n = len(s)
    
    # dp[i] contains all possible sentences ending at position i
    dp = [[] for _ in range(n + 1)]
    dp[0] = [""]
    
    for i in range(1, n + 1):
        for j in range(i):
            word = s[j:i]
            if word in word_set and dp[j]:
                for sentence in dp[j]:
                    if sentence:
                        dp[i].append(sentence + " " + word)
                    else:
                        dp[i].append(word)
    
    return dp[n]

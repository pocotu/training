"""
Solution for Length of Last Word
Problem ID: 022
LeetCode Problem: 58
"""

def length_of_last_word(s):
    return len(s.strip().split()[-1])

# Alias for main function
solve = length_of_last_word

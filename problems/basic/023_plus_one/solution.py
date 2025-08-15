"""
Solution for Plus One
Problem ID: 023
LeetCode Problem: 66
"""

def plus_one(digits):
    for i in range(len(digits) - 1, -1, -1):
        if digits[i] == 9:
            digits[i] = 0
        else:
            digits[i] += 1
            return digits
    return [1] + digits

# Alias for main function
solve = plus_one

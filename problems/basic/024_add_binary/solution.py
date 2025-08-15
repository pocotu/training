"""
Solution for Add Binary
Problem ID: 024
LeetCode Problem: 67
"""

def add_binary(a, b):
    return bin(int(a, 2) + int(b, 2))[2:]

# Alias for main function
solve = add_binary

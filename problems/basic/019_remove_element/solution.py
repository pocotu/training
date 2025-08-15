"""
Solution for Remove Element
Problem ID: 019
LeetCode Problem: 27
"""

def remove_element(nums, val):
    i = 0
    for j in range(len(nums)):
        if nums[j] != val:
            nums[i] = nums[j]
            i += 1
    return i

# Alias for main function
solve = remove_element

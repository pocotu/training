"""
Sum Root to Leaf Numbers - LeetCode Problem #129
Problem ID: 128

Given a binary tree containing digits from 0-9 only, each root-to-leaf path 
could represent a number. An example is the root-to-leaf path 1->2->3 which 
represents the number 123. Find the total sum of all root-to-leaf numbers.

Time Complexity: O(n)
Space Complexity: O(h) where h is height of tree
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sum_numbers(root):
    """
    Calculate sum of all root-to-leaf numbers.
    
    Args:
        root: TreeNode - root of binary tree
        
    Returns:
        int: sum of all root-to-leaf numbers
    """
    def dfs(node, current_num):
        if not node:
            return 0
        
        # Build current number by appending digit
        current_num = current_num * 10 + node.val
        
        # If leaf node, return the complete number
        if not node.left and not node.right:
            return current_num
        
        # Recursively process left and right subtrees
        return dfs(node.left, current_num) + dfs(node.right, current_num)
    
    return dfs(root, 0)

# Alternative iterative solution using stack
def sum_numbers_iterative(root):
    """Iterative solution using stack with (node, current_number) pairs"""
    if not root:
        return 0
    
    total_sum = 0
    stack = [(root, root.val)]
    
    while stack:
        node, current_num = stack.pop()
        
        # If leaf node, add to total sum
        if not node.left and not node.right:
            total_sum += current_num
        
        # Add children to stack with updated numbers
        if node.right:
            stack.append((node.right, current_num * 10 + node.right.val))
        if node.left:
            stack.append((node.left, current_num * 10 + node.left.val))
    
    return total_sum

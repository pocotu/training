"""
Test cases for Convert Sorted Array to Binary Search Tree
Problem ID: 033
"""

import unittest
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent))

from solution import sorted_array_to_bst, TreeNode

class TestSortedArrayToBST(unittest.TestCase):

    def is_valid_bst(self, root, min_val=float('-inf'), max_val=float('inf')):
        """Helper to validate BST property"""
        if not root:
            return True
        if root.val <= min_val or root.val >= max_val:
            return False
        return (self.is_valid_bst(root.left, min_val, root.val) and
                self.is_valid_bst(root.right, root.val, max_val))

    def get_height(self, root):
        """Helper to calculate tree height"""
        if not root:
            return 0
        return 1 + max(self.get_height(root.left), self.get_height(root.right))

    def is_balanced(self, root):
        """Helper to check if tree is balanced"""
        if not root:
            return True
        left_height = self.get_height(root.left)
        right_height = self.get_height(root.right)
        return (abs(left_height - right_height) <= 1 and
                self.is_balanced(root.left) and
                self.is_balanced(root.right))

    def test_example_1(self):
        nums = [-10, -3, 0, 5, 9]
        root = sorted_array_to_bst(nums)
        self.assertTrue(self.is_valid_bst(root))
        self.assertTrue(self.is_balanced(root))

    def test_example_2(self):
        nums = [1, 3]
        root = sorted_array_to_bst(nums)
        self.assertTrue(self.is_valid_bst(root))
        self.assertTrue(self.is_balanced(root))

if __name__ == '__main__':
    unittest.main(verbosity=2)
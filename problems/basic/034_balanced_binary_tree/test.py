"""
Test cases for Balanced Binary Tree
Problem ID: 034
"""

import unittest
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent))

from solution import is_balanced, TreeNode

class TestBalancedBinaryTree(unittest.TestCase):

    def test_example_1(self):
        # Tree: [3,9,20,null,null,15,7]
        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20, TreeNode(15), TreeNode(7))
        self.assertTrue(is_balanced(root))

    def test_example_2(self):
        # Tree: [1,2,2,3,3,null,null,4,4]
        root = TreeNode(1)
        root.left = TreeNode(2, TreeNode(3, TreeNode(4), TreeNode(4)), TreeNode(3))
        root.right = TreeNode(2)
        self.assertFalse(is_balanced(root))

    def test_empty_tree(self):
        self.assertTrue(is_balanced(None))

if __name__ == '__main__':
    unittest.main(verbosity=2)
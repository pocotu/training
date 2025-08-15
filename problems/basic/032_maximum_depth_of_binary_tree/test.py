"""
Test cases for Maximum Depth of Binary Tree
Problem ID: 032
"""

import unittest
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent))

from solution import max_depth, TreeNode

class TestMaxDepth(unittest.TestCase):

    def test_example_1(self):
        # Tree: [3,9,20,null,null,15,7]
        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20, TreeNode(15), TreeNode(7))
        self.assertEqual(max_depth(root), 3)

    def test_example_2(self):
        # Tree: [1,null,2]
        root = TreeNode(1, None, TreeNode(2))
        self.assertEqual(max_depth(root), 2)

    def test_empty_tree(self):
        self.assertEqual(max_depth(None), 0)

    def test_single_node(self):
        root = TreeNode(1)
        self.assertEqual(max_depth(root), 1)

if __name__ == '__main__':
    unittest.main(verbosity=2)
"""
Test cases for Minimum Depth of Binary Tree
Problem ID: 035
"""

import unittest
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent))

from solution import min_depth, TreeNode

class TestMinDepth(unittest.TestCase):

    def test_example_1(self):
        # Tree: [3,9,20,null,null,15,7]
        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20, TreeNode(15), TreeNode(7))
        self.assertEqual(min_depth(root), 2)

    def test_example_2(self):
        # Tree: [2,null,3,null,4,null,5,null,6]
        root = TreeNode(2)
        current = root
        for val in [3, 4, 5, 6]:
            current.right = TreeNode(val)
            current = current.right
        self.assertEqual(min_depth(root), 5)

    def test_empty_tree(self):
        self.assertEqual(min_depth(None), 0)

if __name__ == '__main__':
    unittest.main(verbosity=2)
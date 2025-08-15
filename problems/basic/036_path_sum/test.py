"""
Test cases for Path Sum
Problem ID: 036
"""

import unittest
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent))

from solution import has_path_sum, TreeNode

class TestPathSum(unittest.TestCase):

    def test_example_1(self):
        # Tree: [5,4,8,11,null,13,4,7,2,null,null,null,1]
        root = TreeNode(5)
        root.left = TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2)))
        root.right = TreeNode(8, TreeNode(13), TreeNode(4, None, TreeNode(1)))
        self.assertTrue(has_path_sum(root, 22))

    def test_example_2(self):
        # Tree: [1,2,3]
        root = TreeNode(1, TreeNode(2), TreeNode(3))
        self.assertFalse(has_path_sum(root, 5))

    def test_empty_tree(self):
        self.assertFalse(has_path_sum(None, 0))

if __name__ == '__main__':
    unittest.main(verbosity=2)
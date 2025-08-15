"""
Test cases for Same Tree
Problem ID: 030
"""

import unittest
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent))

from solution import is_same_tree, TreeNode

class TestSameTree(unittest.TestCase):

    def test_example_1(self):
        # Both trees: [1,2,3]
        p = TreeNode(1, TreeNode(2), TreeNode(3))
        q = TreeNode(1, TreeNode(2), TreeNode(3))
        self.assertTrue(is_same_tree(p, q))

    def test_example_2(self):
        # p = [1,2], q = [1,null,2]
        p = TreeNode(1, TreeNode(2), None)
        q = TreeNode(1, None, TreeNode(2))
        self.assertFalse(is_same_tree(p, q))

    def test_both_empty(self):
        self.assertTrue(is_same_tree(None, None))

    def test_one_empty(self):
        p = TreeNode(1)
        self.assertFalse(is_same_tree(p, None))

if __name__ == '__main__':
    unittest.main(verbosity=2)
"""
Test cases for Symmetric Tree
Problem ID: 031
"""

import unittest
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent))

from solution import is_symmetric, TreeNode

class TestSymmetricTree(unittest.TestCase):

    def test_example_1(self):
        # Tree: [1,2,2,3,4,4,3]
        root = TreeNode(1)
        root.left = TreeNode(2, TreeNode(3), TreeNode(4))
        root.right = TreeNode(2, TreeNode(4), TreeNode(3))
        self.assertTrue(is_symmetric(root))

    def test_example_2(self):
        # Tree: [1,2,2,null,3,null,3]
        root = TreeNode(1)
        root.left = TreeNode(2, None, TreeNode(3))
        root.right = TreeNode(2, None, TreeNode(3))
        self.assertFalse(is_symmetric(root))

    def test_single_node(self):
        root = TreeNode(1)
        self.assertTrue(is_symmetric(root))

if __name__ == '__main__':
    unittest.main(verbosity=2)
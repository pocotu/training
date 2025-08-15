"""
Test cases for Binary Tree Preorder Traversal
Problem ID: 043
"""

import unittest
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent))

from solution import preorder_traversal, TreeNode

class TestPreorderTraversal(unittest.TestCase):

    def test_example_1(self):
        # Tree: [1,null,2,3]
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.left = TreeNode(3)
        self.assertEqual(preorder_traversal(root), [1, 2, 3])

    def test_empty_tree(self):
        self.assertEqual(preorder_traversal(None), [])

    def test_single_node(self):
        root = TreeNode(1)
        self.assertEqual(preorder_traversal(root), [1])

if __name__ == '__main__':
    unittest.main(verbosity=2)
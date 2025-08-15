"""
Test cases for Binary Tree Inorder Traversal
Problem ID: 029
"""

import unittest
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent))

from solution import inorder_traversal, TreeNode

class TestInorderTraversal(unittest.TestCase):

    def test_example_1(self):
        # Tree: [1,null,2,3]
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.left = TreeNode(3)
        self.assertEqual(inorder_traversal(root), [1, 3, 2])

    def test_empty_tree(self):
        self.assertEqual(inorder_traversal(None), [])

    def test_single_node(self):
        root = TreeNode(1)
        self.assertEqual(inorder_traversal(root), [1])

if __name__ == '__main__':
    unittest.main(verbosity=2)
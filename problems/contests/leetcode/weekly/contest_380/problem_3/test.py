#!/usr/bin/env python3
"""
Unit tests for Maximum Binary Array After Change (Problem LC_W380_P3)

Tests binary tree algorithms and operations.
"""

import unittest
import sys
from pathlib import Path

# Add the parent directory to sys.path to import solution
sys.path.append(str(Path(__file__).parent))

try:
    from solution import MaximumBinaryArrayAfterChange, TreeNode
except ImportError:
    # Fallback if solution file doesn't exist yet
    class TreeNode:
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right
    
    class MaximumBinaryArrayAfterChange:
        def maximum_binary_array_after_change(self, root):
            raise NotImplementedError("Solution not implemented yet")


class TestMaximumBinaryArrayAfterChange(unittest.TestCase):
    """Test cases for Maximum Binary Array After Change."""
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.solution = MaximumBinaryArrayAfterChange()
    
    def create_tree(self, values):
        """Helper method to create binary tree from list."""
        if not values:
            return None
        
        root = TreeNode(values[0])
        queue = [root]
        i = 1
        
        while queue and i < len(values):
            node = queue.pop(0)
            
            if i < len(values) and values[i] is not None:
                node.left = TreeNode(values[i])
                queue.append(node.left)
            i += 1
            
            if i < len(values) and values[i] is not None:
                node.right = TreeNode(values[i])
                queue.append(node.right)
            i += 1
        
        return root
    
    def test_empty_tree(self):
        """Test edge case with empty tree."""
        root = None
        result = self.solution.maximum_binary_array_after_change(root)
        self.assertIsNotNone(result, "Should handle empty tree")
    
    def test_single_node(self):
        """Test tree with single node."""
        root = TreeNode(1)
        result = self.solution.maximum_binary_array_after_change(root)
        self.assertIsNotNone(result, "Should handle single node")
    
    def test_balanced_tree(self):
        """Test balanced binary tree."""
        # Tree: [1, 2, 3, 4, 5, 6, 7]
        root = self.create_tree([1, 2, 3, 4, 5, 6, 7])
        result = self.solution.maximum_binary_array_after_change(root)
        self.assertIsNotNone(result, "Should handle balanced tree")
    
    def test_left_skewed_tree(self):
        """Test left-skewed tree."""
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(3)
        result = self.solution.maximum_binary_array_after_change(root)
        self.assertIsNotNone(result, "Should handle left-skewed tree")
    
    def test_right_skewed_tree(self):
        """Test right-skewed tree."""
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.right = TreeNode(3)
        result = self.solution.maximum_binary_array_after_change(root)
        self.assertIsNotNone(result, "Should handle right-skewed tree")
    
    def test_large_tree(self):
        """Test performance with large tree."""
        # Create a complete binary tree with 1000+ nodes
        values = list(range(1, 1024))
        root = self.create_tree(values)
        
        import time
        start_time = time.time()
        result = self.solution.maximum_binary_array_after_change(root)
        end_time = time.time()
        
        self.assertLess(end_time - start_time, 1.0, "Should be efficient")
        self.assertIsNotNone(result, "Should handle large trees")


if __name__ == "__main__":
    unittest.main(verbosity=2)

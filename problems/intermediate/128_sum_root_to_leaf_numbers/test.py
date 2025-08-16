import pytest
from solution import TreeNode, sum_numbers, sum_numbers_iterative

def create_tree_from_list(values):
    """Helper function to create tree from list representation"""
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

class TestSumRootToLeafNumbers:
    
    def test_example_1(self):
        """Test case: [1,2,3] should return 25"""
        root = create_tree_from_list([1, 2, 3])
        assert sum_numbers(root) == 25
        assert sum_numbers_iterative(root) == 25
    
    def test_example_2(self):
        """Test case: [4,9,0,5,1] should return 1026"""
        root = create_tree_from_list([4, 9, 0, 5, 1])
        assert sum_numbers(root) == 1026
        assert sum_numbers_iterative(root) == 1026
    
    def test_single_node(self):
        """Test case: single node [1] should return 1"""
        root = TreeNode(1)
        assert sum_numbers(root) == 1
        assert sum_numbers_iterative(root) == 1
    
    def test_linear_tree(self):
        """Test case: linear tree 1->2->3 should return 123"""
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(3)
        assert sum_numbers(root) == 123
        assert sum_numbers_iterative(root) == 123
    
    def test_with_zeros(self):
        """Test case: tree with zeros [1,0,1,0,1,0,1]"""
        root = create_tree_from_list([1, 0, 1, 0, 1, 0, 1])
        # Paths: 1->0->0 = 100, 1->0->1 = 101, 1->1->0 = 110, 1->1->1 = 111
        expected = 100 + 101 + 110 + 111
        assert sum_numbers(root) == expected
        assert sum_numbers_iterative(root) == expected
    
    def test_empty_tree(self):
        """Test case: empty tree should return 0"""
        assert sum_numbers(None) == 0
        assert sum_numbers_iterative(None) == 0

if __name__ == "__main__":
    pytest.main([__file__])

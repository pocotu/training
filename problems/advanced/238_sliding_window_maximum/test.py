import pytest
from solution import max_sliding_window, max_sliding_window_segment_tree, max_sliding_window_brute_force

class TestSlidingWindowMaximum:
    
    def test_example_1(self):
        """Test case: [1,3,-1,-3,5,3,6,7], k=3 should return [3,3,5,5,6,7]"""
        nums = [1,3,-1,-3,5,3,6,7]
        k = 3
        expected = [3,3,5,5,6,7]
        
        assert max_sliding_window(nums, k) == expected
        assert max_sliding_window_segment_tree(nums, k) == expected
        assert max_sliding_window_brute_force(nums, k) == expected
    
    def test_single_element(self):
        """Test case: [1], k=1 should return [1]"""
        nums = [1]
        k = 1
        expected = [1]
        
        assert max_sliding_window(nums, k) == expected
        assert max_sliding_window_segment_tree(nums, k) == expected
        assert max_sliding_window_brute_force(nums, k) == expected
    
    def test_window_size_one(self):
        """Test case: [1,-1], k=1 should return [1,-1]"""
        nums = [1, -1]
        k = 1
        expected = [1, -1]
        
        assert max_sliding_window(nums, k) == expected
        assert max_sliding_window_segment_tree(nums, k) == expected
        assert max_sliding_window_brute_force(nums, k) == expected
    
    def test_window_equals_array_size(self):
        """Test case: [9,11], k=2 should return [11]"""
        nums = [9, 11]
        k = 2
        expected = [11]
        
        assert max_sliding_window(nums, k) == expected
        assert max_sliding_window_segment_tree(nums, k) == expected
        assert max_sliding_window_brute_force(nums, k) == expected
    
    def test_decreasing_array(self):
        """Test case: decreasing array [5,4,3,2,1], k=3"""
        nums = [5, 4, 3, 2, 1]
        k = 3
        expected = [5, 4, 3]  # First element is always max in each window
        
        assert max_sliding_window(nums, k) == expected
        assert max_sliding_window_segment_tree(nums, k) == expected
        assert max_sliding_window_brute_force(nums, k) == expected
    
    def test_increasing_array(self):
        """Test case: increasing array [1,2,3,4,5], k=3"""
        nums = [1, 2, 3, 4, 5]
        k = 3
        expected = [3, 4, 5]  # Last element is always max in each window
        
        assert max_sliding_window(nums, k) == expected
        assert max_sliding_window_segment_tree(nums, k) == expected
        assert max_sliding_window_brute_force(nums, k) == expected
    
    def test_duplicate_elements(self):
        """Test case with duplicate maximum elements"""
        nums = [1, 3, 3, 3, 1]
        k = 3
        expected = [3, 3, 3]
        
        assert max_sliding_window(nums, k) == expected
        assert max_sliding_window_segment_tree(nums, k) == expected
        assert max_sliding_window_brute_force(nums, k) == expected
    
    def test_negative_numbers(self):
        """Test case with all negative numbers"""
        nums = [-1, -3, -2, -4]
        k = 2
        expected = [-1, -2, -2]  # Maximum of each pair
        
        assert max_sliding_window(nums, k) == expected
        assert max_sliding_window_segment_tree(nums, k) == expected
        assert max_sliding_window_brute_force(nums, k) == expected
    
    def test_large_window(self):
        """Test case with large window size"""
        nums = [7, 2, 4, 1, 8, 3]
        k = 4
        expected = [7, 8, 8]
        
        assert max_sliding_window(nums, k) == expected
        assert max_sliding_window_segment_tree(nums, k) == expected
        assert max_sliding_window_brute_force(nums, k) == expected
    
    def test_empty_array(self):
        """Test edge case: empty array"""
        nums = []
        k = 1
        expected = []
        
        assert max_sliding_window(nums, k) == expected
        assert max_sliding_window_segment_tree(nums, k) == expected
        assert max_sliding_window_brute_force(nums, k) == expected

if __name__ == "__main__":
    pytest.main([__file__])

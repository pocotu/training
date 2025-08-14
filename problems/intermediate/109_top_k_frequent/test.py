"""
Test cases for Top K Frequent Elements problem
Problem ID: 109
"""

import pytest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from solution import top_k_frequent

class TestTopKFrequent:
    """Test class for Top K Frequent Elements problem"""
    
    def test_example_1(self):
        """Test example 1 from LeetCode"""
        nums = [1,1,1,2,2,3]
        k = 2
        result = top_k_frequent(nums, k)
        expected = [1, 2]  # Order may vary
        assert sorted(result) == sorted(expected)
    
    def test_example_2(self):
        """Test example 2 from LeetCode"""
        nums = [1]
        k = 1
        result = top_k_frequent(nums, k)
        expected = [1]
        assert result == expected
    
    def test_all_same_frequency(self):
        """Test when all elements have same frequency"""
        nums = [1, 2, 3, 4]
        k = 2
        result = top_k_frequent(nums, k)
        # Any 2 elements are valid
        assert len(result) == 2
        assert all(num in nums for num in result)
    
    def test_k_equals_unique_count(self):
        """Test when k equals number of unique elements"""
        nums = [1, 1, 2, 2, 3, 3]
        k = 3
        result = top_k_frequent(nums, k)
        expected = [1, 2, 3]
        assert sorted(result) == sorted(expected)
    
    def test_single_element_multiple_times(self):
        """Test single element appearing multiple times"""
        nums = [5, 5, 5, 5, 5]
        k = 1
        result = top_k_frequent(nums, k)
        assert result == [5]
    
    def test_different_frequencies(self):
        """Test elements with different frequencies"""
        nums = [1, 1, 1, 2, 2, 3]  # 1:3, 2:2, 3:1
        k = 1
        result = top_k_frequent(nums, k)
        assert result == [1]  # Most frequent
    
    def test_large_k(self):
        """Test with larger k"""
        nums = [1,2,3,4,5,6,7,8,9,10] * 2 + [1,1,1] + [2,2]
        # Frequencies: 1:5, 2:4, others:2 each
        k = 3
        result = top_k_frequent(nums, k)
        
        # 1 and 2 should definitely be in top 3
        assert 1 in result
        assert 2 in result
        assert len(result) == 3
    
    def test_negative_numbers(self):
        """Test with negative numbers"""
        nums = [-1, -1, -2, -2, -2, -3]
        k = 2
        result = top_k_frequent(nums, k)
        expected = [-2, -1]  # -2 appears 3 times, -1 appears 2 times
        assert sorted(result) == sorted(expected)
    
    def test_mixed_positive_negative(self):
        """Test with mixed positive and negative numbers"""
        nums = [1, -1, 1, -1, -1]
        k = 1
        result = top_k_frequent(nums, k)
        assert result == [-1]  # -1 appears 3 times, 1 appears 2 times
    
    def test_result_length(self):
        """Test that result always has length k"""
        test_cases = [
            ([1,1,1,2,2,3], 1),
            ([1,1,1,2,2,3], 2),
            ([1,1,1,2,2,3], 3),
            ([1,2,3,4,5], 3),
        ]
        
        for nums, k in test_cases:
            result = top_k_frequent(nums, k)
            assert len(result) == k
    
    def test_frequency_order(self):
        """Test that results are in correct frequency order"""
        nums = [1]*5 + [2]*3 + [3]*1 + [4]*4
        k = 3
        result = top_k_frequent(nums, k)
        
        # Count frequencies
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        # Get frequencies of result
        result_freqs = [freq[num] for num in result]
        
        # Should be in descending order (or at least non-ascending)
        assert result_freqs == sorted(result_freqs, reverse=True)

if __name__ == "__main__":
    pytest.main([__file__, "-v"])

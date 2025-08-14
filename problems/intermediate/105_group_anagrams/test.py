"""
Test cases for Group Anagrams problem
Problem ID: 105
"""

import pytest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from solution import group_anagrams

class TestGroupAnagrams:
    """Test class for Group Anagrams problem"""
    
    def test_example_1(self):
        """Test example 1 from LeetCode"""
        strs = ["eat","tea","tan","ate","nat","bat"]
        result = group_anagrams(strs)
        
        # Convert to sets for easier comparison
        result_sets = [set(group) for group in result]
        expected_sets = [{"eat","tea","ate"}, {"tan","nat"}, {"bat"}]
        
        assert len(result) == 3
        for expected_group in expected_sets:
            assert expected_group in result_sets
    
    def test_example_2(self):
        """Test example 2 from LeetCode"""
        strs = [""]
        expected = [[""]]
        result = group_anagrams(strs)
        assert result == expected
    
    def test_example_3(self):
        """Test example 3 from LeetCode"""
        strs = ["a"]
        expected = [["a"]]
        result = group_anagrams(strs)
        assert result == expected
    
    def test_no_anagrams(self):
        """Test strings with no anagrams"""
        strs = ["abc", "def", "ghi"]
        result = group_anagrams(strs)
        
        # Each string should be in its own group
        assert len(result) == 3
        for group in result:
            assert len(group) == 1
    
    def test_all_anagrams(self):
        """Test strings that are all anagrams of each other"""
        strs = ["abc", "bca", "cab", "acb"]
        result = group_anagrams(strs)
        
        # Should be one group with all strings
        assert len(result) == 1
        assert set(result[0]) == set(strs)
    
    def test_empty_input(self):
        """Test empty input"""
        strs = []
        result = group_anagrams(strs)
        assert result == []
    
    def test_single_character_strings(self):
        """Test single character strings"""
        strs = ["a", "b", "a", "c", "b"]
        result = group_anagrams(strs)
        
        # Convert to sets for comparison
        result_sets = [set(group) for group in result]
        
        # Should have groups: {a,a}, {b,b}, {c}
        assert len(result) == 3
        
        # Check that 'a' appears twice in one group
        a_group = next(group for group in result if 'a' in group)
        assert a_group.count('a') == 2
    
    def test_case_sensitivity(self):
        """Test case sensitivity (if applicable)"""
        strs = ["Ab", "Ba", "ab", "ba"]
        result = group_anagrams(strs)
        
        # "Ab" and "Ba" should be anagrams
        # "ab" and "ba" should be anagrams
        # But "Ab" and "ab" are not anagrams (different cases)
        assert len(result) == 2
    
    def test_different_lengths(self):
        """Test strings of different lengths"""
        strs = ["a", "aa", "aaa", "aa", "a"]
        result = group_anagrams(strs)
        
        # Should group by length: {"a","a"}, {"aa","aa"}, {"aaa"}
        assert len(result) == 3
        
        # Find groups
        single_a = next(group for group in result if len(group[0]) == 1)
        double_a = next(group for group in result if len(group[0]) == 2)
        triple_a = next(group for group in result if len(group[0]) == 3)
        
        assert len(single_a) == 2
        assert len(double_a) == 2
        assert len(triple_a) == 1
    
    def test_preserve_original_strings(self):
        """Test that original strings are preserved"""
        strs = ["eat", "tea", "ate"]
        result = group_anagrams(strs)
        
        # All original strings should appear exactly once
        all_strings = [s for group in result for s in group]
        assert sorted(all_strings) == sorted(strs)

if __name__ == "__main__":
    pytest.main([__file__, "-v"])

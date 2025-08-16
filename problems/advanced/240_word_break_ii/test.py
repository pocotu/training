"""
Test cases for Word Break II (Problem 240)
"""

import pytest
from solution import word_break, word_break_optimized, word_break_trie, word_break_dp

class TestWordBreakII:
    
    def test_basic_case_1(self):
        """Test basic word break with multiple solutions"""
        s = "catsanddog"
        wordDict = ["cat", "cats", "and", "sand", "dog"]
        expected = ["cats and dog", "cat sand dog"]
        
        result1 = sorted(word_break(s, wordDict))
        result2 = sorted(word_break_optimized(s, wordDict))
        result3 = sorted(word_break_trie(s, wordDict))
        result4 = sorted(word_break_dp(s, wordDict))
        
        expected_sorted = sorted(expected)
        assert result1 == expected_sorted
        assert result2 == expected_sorted
        assert result3 == expected_sorted
        assert result4 == expected_sorted
    
    def test_basic_case_2(self):
        """Test with overlapping words"""
        s = "pineapplepenapple"
        wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
        expected = ["pine apple pen apple", "pineapple pen apple", "pine applepen apple"]
        
        result1 = sorted(word_break(s, wordDict))
        result2 = sorted(word_break_optimized(s, wordDict))
        result3 = sorted(word_break_trie(s, wordDict))
        result4 = sorted(word_break_dp(s, wordDict))
        
        expected_sorted = sorted(expected)
        assert result1 == expected_sorted
        assert result2 == expected_sorted
        assert result3 == expected_sorted
        assert result4 == expected_sorted
    
    def test_no_solution(self):
        """Test case with no possible word break"""
        s = "catsandog"
        wordDict = ["cats", "dog", "sand", "and", "cat"]
        expected = []
        
        assert word_break(s, wordDict) == expected
        assert word_break_optimized(s, wordDict) == expected
        assert word_break_trie(s, wordDict) == expected
        assert word_break_dp(s, wordDict) == expected
    
    def test_single_word(self):
        """Test with single word"""
        s = "leetcode"
        wordDict = ["leet", "code"]
        expected = ["leet code"]
        
        result1 = word_break(s, wordDict)
        result2 = word_break_optimized(s, wordDict)
        result3 = word_break_trie(s, wordDict)
        result4 = word_break_dp(s, wordDict)
        
        assert result1 == expected
        assert result2 == expected
        assert result3 == expected
        assert result4 == expected
    
    def test_empty_string(self):
        """Test with empty string"""
        s = ""
        wordDict = ["a", "b"]
        expected = [""]  # Empty string can be broken into empty sentence
        
        assert word_break(s, wordDict) == expected
        assert word_break_optimized(s, wordDict) == expected
        assert word_break_trie(s, wordDict) == expected
        assert word_break_dp(s, wordDict) == expected
    
    def test_single_character_words(self):
        """Test with single character words"""
        s = "abc"
        wordDict = ["a", "b", "c"]
        expected = ["a b c"]
        
        result1 = word_break(s, wordDict)
        result2 = word_break_optimized(s, wordDict)
        result3 = word_break_trie(s, wordDict)
        result4 = word_break_dp(s, wordDict)
        
        assert result1 == expected
        assert result2 == expected
        assert result3 == expected
        assert result4 == expected
    
    def test_repeated_words(self):
        """Test with repeated word usage"""
        s = "aaaa"
        wordDict = ["aa", "aaa"]
        expected = ["aa aa"]
        
        result1 = word_break(s, wordDict)
        result2 = word_break_optimized(s, wordDict)
        result3 = word_break_trie(s, wordDict)
        result4 = word_break_dp(s, wordDict)
        
        assert result1 == expected
        assert result2 == expected
        assert result3 == expected
        assert result4 == expected
    
    def test_multiple_valid_breaks(self):
        """Test with many possible combinations"""
        s = "abcd"
        wordDict = ["a", "abc", "b", "cd"]
        expected = ["a b cd", "abc d"]
        
        # Note: This expects "abc d" but "d" is not in wordDict
        # Let's fix this test case
        s = "abcd"
        wordDict = ["a", "abc", "b", "cd", "d"]
        expected = ["a b cd", "abc d"]
        
        result1 = sorted(word_break(s, wordDict))
        result2 = sorted(word_break_optimized(s, wordDict))
        result3 = sorted(word_break_trie(s, wordDict))
        result4 = sorted(word_break_dp(s, wordDict))
        
        expected_sorted = sorted(expected)
        assert result1 == expected_sorted
        assert result2 == expected_sorted
        assert result3 == expected_sorted
        assert result4 == expected_sorted
    
    def test_word_prefix_overlap(self):
        """Test with words that are prefixes of others"""
        s = "cars"
        wordDict = ["car", "ca", "rs"]
        expected = ["ca rs"]
        
        result1 = word_break(s, wordDict)
        result2 = word_break_optimized(s, wordDict)
        result3 = word_break_trie(s, wordDict)
        result4 = word_break_dp(s, wordDict)
        
        assert result1 == expected
        assert result2 == expected
        assert result3 == expected
        assert result4 == expected
    
    def test_long_string(self):
        """Test with longer string"""
        s = "goalspecial"
        wordDict = ["go", "goal", "goals", "special"]
        expected = ["goal special"]
        
        result1 = word_break(s, wordDict)
        result2 = word_break_optimized(s, wordDict)
        result3 = word_break_trie(s, wordDict)
        result4 = word_break_dp(s, wordDict)
        
        assert result1 == expected
        assert result2 == expected
        assert result3 == expected
        assert result4 == expected

# Performance tests
class TestWordBreakIIPerformance:
    
    def test_performance_comparison(self):
        """Compare performance of different approaches"""
        s = "aaaaaaaaaa"  # 10 a's
        wordDict = ["a", "aa", "aaa", "aaaa", "aaaaa"]
        
        # All approaches should work but with different performance
        result1 = word_break(s, wordDict)
        result2 = word_break_optimized(s, wordDict)
        result3 = word_break_trie(s, wordDict)
        result4 = word_break_dp(s, wordDict)
        
        # All should return the same results
        assert len(result1) > 0
        assert len(result1) == len(result2) == len(result3) == len(result4)
        assert set(result1) == set(result2) == set(result3) == set(result4)
    
    def test_edge_case_no_break_possible(self):
        """Test early termination when no break is possible"""
        s = "aaaaaaaaab"
        wordDict = ["a", "aa", "aaa", "aaaa", "aaaaa"]
        
        # Should return empty list quickly
        assert word_break_optimized(s, wordDict) == []

if __name__ == "__main__":
    pytest.main([__file__])

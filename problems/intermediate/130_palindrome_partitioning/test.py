import pytest
from solution import partition, partition_optimized, partition_expand_center

class TestPalindromePartitioning:
    
    def test_example_1(self):
        """Test case: 'aab' should return [['a','a','b'],['aa','b']]"""
        s = "aab"
        expected = [["a","a","b"],["aa","b"]]
        
        result1 = partition(s)
        result2 = partition_optimized(s)
        result3 = partition_expand_center(s)
        
        # Sort results for comparison since order might vary
        for result in [result1, result2, result3]:
            result.sort()
        expected.sort()
        
        assert result1 == expected
        assert result2 == expected  
        assert result3 == expected
    
    def test_single_character(self):
        """Test case: single character 'a'"""
        s = "a"
        expected = [["a"]]
        
        assert partition(s) == expected
        assert partition_optimized(s) == expected
        assert partition_expand_center(s) == expected
    
    def test_all_same_characters(self):
        """Test case: 'aaa' - multiple valid partitions"""
        s = "aaa"
        expected = [["a","a","a"], ["a","aa"], ["aa","a"], ["aaa"]]
        
        result1 = partition(s)
        result2 = partition_optimized(s)
        result3 = partition_expand_center(s)
        
        for result in [result1, result2, result3]:
            result.sort()
        expected.sort()
        
        assert result1 == expected
        assert result2 == expected
        assert result3 == expected
    
    def test_no_multi_char_palindromes(self):
        """Test case: 'abcd' - only single character palindromes"""
        s = "abcd"
        expected = [["a","b","c","d"]]
        
        assert partition(s) == expected
        assert partition_optimized(s) == expected
        assert partition_expand_center(s) == expected
    
    def test_full_palindrome(self):
        """Test case: 'racecar' - entire string is palindrome"""
        s = "racecar"
        
        result1 = partition(s)
        result2 = partition_optimized(s)
        result3 = partition_expand_center(s)
        
        # Should include the full string as one partition
        assert ["racecar"] in result1
        assert ["racecar"] in result2
        assert ["racecar"] in result3
        
        # Should also include single character partition
        assert ["r","a","c","e","c","a","r"] in result1
        assert ["r","a","c","e","c","a","r"] in result2
        assert ["r","a","c","e","c","a","r"] in result3
    
    def test_alternating_pattern(self):
        """Test case: 'abab' """
        s = "abab"
        expected = [["a","b","a","b"], ["a","bab"], ["aba","b"]]
        
        result1 = partition(s)
        result2 = partition_optimized(s)
        result3 = partition_expand_center(s)
        
        for result in [result1, result2, result3]:
            result.sort()
        expected.sort()
        
        assert result1 == expected
        assert result2 == expected
        assert result3 == expected
    
    def test_complex_case(self):
        """Test case with multiple palindromic substrings"""
        s = "abccba"
        
        result1 = partition(s)
        result2 = partition_optimized(s)
        result3 = partition_expand_center(s)
        
        # Should include the full palindrome
        assert ["abccba"] in result1
        assert ["abccba"] in result2
        assert ["abccba"] in result3
        
        # Should include middle palindrome
        assert ["a","bccb","a"] in result1
        assert ["a","bccb","a"] in result2
        assert ["a","bccb","a"] in result3
        
        # Check all solutions have same length
        assert len(result1) == len(result2) == len(result3)

if __name__ == "__main__":
    pytest.main([__file__])

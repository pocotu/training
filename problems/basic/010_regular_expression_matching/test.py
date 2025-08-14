#!/usr/bin/env python3
"""
Unit tests for Regular Expression Matching (Problem 010)

Tests the solution implementation with various test cases including:
- Basic functionality
- Edge cases
- Performance validation
"""

import unittest
import sys
from pathlib import Path

# Add the parent directory to sys.path to import solution
sys.path.append(str(Path(__file__).parent))

try:
    from solution import RegularExpressionMatching
except ImportError:
    # Fallback if solution file doesn't exist yet
    class RegularExpressionMatching:
        def regular_expression_matching(self, *args):
            raise NotImplementedError("Solution not implemented yet")


class TestRegularExpressionMatching(unittest.TestCase):
    """Test cases for Regular Expression Matching."""
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.solution = RegularExpressionMatching()
    
    def test_basic_case(self):
        """Test basic functionality."""
        # Test case 1: Basic example
        result = self.solution.regular_expression_matching("example_input")
        expected = "expected_output"
        self.assertEqual(result, expected, "Basic case failed")
    
    def test_edge_case_empty(self):
        """Test edge case with empty input."""
        result = self.solution.regular_expression_matching("")
        expected = ""  # Adjust based on problem requirements
        self.assertEqual(result, expected, "Empty input case failed")
    
    def test_edge_case_single(self):
        """Test edge case with single element."""
        result = self.solution.regular_expression_matching("single")
        expected = "single"  # Adjust based on problem requirements
        self.assertEqual(result, expected, "Single element case failed")
    
    def test_multiple_cases(self):
        """Test multiple different cases."""
        test_cases = [
            ("input1", "output1"),
            ("input2", "output2"),
            ("input3", "output3"),
        ]
        
        for input_val, expected in test_cases:
            with self.subTest(input=input_val):
                result = self.solution.regular_expression_matching(input_val)
                self.assertEqual(result, expected, f"Failed for input: {input_val}")
    
    def test_performance(self):
        """Test performance with larger inputs."""
        # Create a larger test case
        large_input = "large_test_input" * 1000
        
        # Test should complete in reasonable time
        import time
        start_time = time.time()
        result = self.solution.regular_expression_matching(large_input)
        end_time = time.time()
        
        # Should complete within 1 second for most problems
        self.assertLess(end_time - start_time, 1.0, "Solution too slow")
        self.assertIsNotNone(result, "Should return a valid result")


if __name__ == "__main__":
    # Run the tests
    unittest.main(verbosity=2)

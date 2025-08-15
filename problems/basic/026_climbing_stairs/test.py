"""
Test cases for Climbing Stairs
Problem ID: 026
"""

import unittest
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent))

from solution import climb_stairs, climb_stairs_recursive, climb_stairs_dp

class TestClimbingStairs(unittest.TestCase):

    def test_example_1(self):
        """Test example 1 from problem statement"""
        self.assertEqual(climb_stairs(2), 2)

    def test_example_2(self):
        """Test example 2 from problem statement"""
        self.assertEqual(climb_stairs(3), 3)

    def test_base_cases(self):
        """Test base cases"""
        self.assertEqual(climb_stairs(1), 1)

    def test_larger_cases(self):
        """Test larger inputs"""
        self.assertEqual(climb_stairs(4), 5)
        self.assertEqual(climb_stairs(5), 8)

    def test_fibonacci_pattern(self):
        """Test that it follows Fibonacci pattern"""
        # F(1)=1, F(2)=2, F(3)=3, F(4)=5, F(5)=8
        expected = [1, 2, 3, 5, 8, 13, 21]
        for i, exp in enumerate(expected, 1):
            self.assertEqual(climb_stairs(i), exp)

if __name__ == '__main__':
    unittest.main(verbosity=2)
"""
Test cases for Stack Implementation
Problem ID: F049
"""

import unittest
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent))

from solution import Stack

class TestStackImplementation(unittest.TestCase):

    def test_stack_operations(self):
        stack = Stack()
        
        # Test empty stack
        self.assertTrue(stack.is_empty())
        
        # Test push and peek
        stack.push(1)
        self.assertEqual(stack.peek(), 1)
        self.assertFalse(stack.is_empty())
        
        # Test multiple pushes
        stack.push(2)
        stack.push(3)
        self.assertEqual(stack.peek(), 3)
        
        # Test pop
        self.assertEqual(stack.pop(), 3)
        self.assertEqual(stack.peek(), 2)
        self.assertEqual(stack.pop(), 2)
        self.assertEqual(stack.pop(), 1)
        self.assertTrue(stack.is_empty())

if __name__ == '__main__':
    unittest.main(verbosity=2)
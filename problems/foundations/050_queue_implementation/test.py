"""
Test cases for Queue Implementation
Problem ID: F050
"""

import unittest
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent))

from solution import Queue

class TestQueueImplementation(unittest.TestCase):

    def test_queue_operations(self):
        queue = Queue()
        
        # Test empty queue
        self.assertTrue(queue.is_empty())
        
        # Test enqueue and front
        queue.enqueue(1)
        self.assertEqual(queue.front(), 1)
        self.assertFalse(queue.is_empty())
        
        # Test multiple enqueues
        queue.enqueue(2)
        queue.enqueue(3)
        self.assertEqual(queue.front(), 1)
        
        # Test dequeue
        self.assertEqual(queue.dequeue(), 1)
        self.assertEqual(queue.front(), 2)
        self.assertEqual(queue.dequeue(), 2)
        self.assertEqual(queue.dequeue(), 3)
        self.assertTrue(queue.is_empty())

if __name__ == '__main__':
    unittest.main(verbosity=2)
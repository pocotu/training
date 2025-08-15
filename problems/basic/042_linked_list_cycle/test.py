"""
Test cases for Linked List Cycle
Problem ID: 042
"""

import unittest
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent))

from solution import has_cycle, ListNode

class TestLinkedListCycle(unittest.TestCase):

    def test_example_1(self):
        # Create cycle: [3,2,0,-4] with pos=1
        head = ListNode(3)
        node2 = ListNode(2)
        node3 = ListNode(0)
        node4 = ListNode(-4)
        head.next = node2
        node2.next = node3
        node3.next = node4
        node4.next = node2  # Creates cycle
        self.assertTrue(has_cycle(head))

    def test_example_2(self):
        # Create cycle: [1,2] with pos=0
        head = ListNode(1)
        node2 = ListNode(2)
        head.next = node2
        node2.next = head  # Creates cycle
        self.assertTrue(has_cycle(head))

    def test_no_cycle(self):
        # No cycle: [1,2,3]
        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = ListNode(3)
        self.assertFalse(has_cycle(head))

    def test_empty_list(self):
        self.assertFalse(has_cycle(None))

if __name__ == '__main__':
    unittest.main(verbosity=2)
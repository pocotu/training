"""
Test cases for Remove Duplicates from Sorted List
Problem ID: 027
"""

import unittest
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent))

from solution import delete_duplicates, create_linked_list, linked_list_to_array

class TestRemoveDuplicates(unittest.TestCase):

    def test_example_1(self):
        head = create_linked_list([1, 1, 2])
        result = delete_duplicates(head)
        self.assertEqual(linked_list_to_array(result), [1, 2])

    def test_example_2(self):
        head = create_linked_list([1, 1, 2, 3, 3])
        result = delete_duplicates(head)
        self.assertEqual(linked_list_to_array(result), [1, 2, 3])

    def test_empty_list(self):
        result = delete_duplicates(None)
        self.assertIsNone(result)

    def test_single_element(self):
        head = create_linked_list([1])
        result = delete_duplicates(head)
        self.assertEqual(linked_list_to_array(result), [1])

if __name__ == '__main__':
    unittest.main(verbosity=2)
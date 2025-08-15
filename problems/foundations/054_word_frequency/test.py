"""
Test cases for Word Frequency
Problem ID: F054
"""

import unittest
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent))

from solution import word_frequency

class TestWordFrequency(unittest.TestCase):

    def test_word_frequency(self):
        self.assertEqual(word_frequency("hello world hello"), {"hello": 2, "world": 1})
        self.assertEqual(word_frequency("The quick brown fox"), {"the": 1, "quick": 1, "brown": 1, "fox": 1})
        self.assertEqual(word_frequency(""), {})
        self.assertEqual(word_frequency("test test test"), {"test": 3})

if __name__ == '__main__':
    unittest.main(verbosity=2)
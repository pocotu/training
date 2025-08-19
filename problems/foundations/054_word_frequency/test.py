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
        # Test 1: Caso básico
        self.assertEqual(word_frequency("hello world hello"), {"hello": 2, "world": 1})
        
        # Test 2: Mayúsculas y minúsculas
        self.assertEqual(word_frequency("The quick brown fox"), {"the": 1, "quick": 1, "brown": 1, "fox": 1})
        
        # Test 3: String vacío
        self.assertEqual(word_frequency(""), {})
        
        # Test 4: Repetición simple
        self.assertEqual(word_frequency("test test test"), {"test": 3})
        
        # Test 5: Con puntuación
        self.assertEqual(word_frequency("Hello, world! Hello world."), {"hello": 2, "world": 2})
        
        # Test 6: Puntuación múltiple
        self.assertEqual(word_frequency("Hi! How are you? Fine, thanks."), {"hi": 1, "how": 1, "are": 1, "you": 1, "fine": 1, "thanks": 1})

if __name__ == '__main__':
    unittest.main(verbosity=2)
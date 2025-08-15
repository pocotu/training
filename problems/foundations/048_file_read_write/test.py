"""
Test cases for File Read Write
Problem ID: F048
"""

import unittest
import sys
import os
from pathlib import Path

sys.path.append(str(Path(__file__).parent))

from solution import write_and_read_file

class TestFileReadWrite(unittest.TestCase):

    def tearDown(self):
        # Clean up test files
        test_files = ["test.txt", "example.txt", "empty.txt"]
        for file in test_files:
            if os.path.exists(file):
                os.remove(file)

    def test_write_and_read_file(self):
        result = write_and_read_file("Hello World", "test.txt")
        self.assertEqual(result, "Hello World")
        
        result = write_and_read_file("Python is great!", "example.txt")
        self.assertEqual(result, "Python is great!")
        
        result = write_and_read_file("", "empty.txt")
        self.assertEqual(result, "")

if __name__ == '__main__':
    unittest.main(verbosity=2)
import unittest
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent))

from solution import create_graph

class TestGraphTheoryBasics(unittest.TestCase):
    
    def test_create_graph(self):
        # Test 1: Grafo básico
        edges = [("A", "B"), ("A", "C"), ("B", "D")]
        result = create_graph(edges)
        expected = {
            "A": ["B", "C"], 
            "B": ["A", "D"], 
            "C": ["A"], 
            "D": ["B"]
        }
        self.assertEqual(result, expected)
        
        # Test 2: Grafo simple
        edges2 = [("1", "2")]
        result2 = create_graph(edges2)
        expected2 = {"1": ["2"], "2": ["1"]}
        self.assertEqual(result2, expected2)
        
        # Test 3: Lista vacía
        edges3 = []
        result3 = create_graph(edges3)
        self.assertEqual(result3, {})

if __name__ == '__main__':
    unittest.main()

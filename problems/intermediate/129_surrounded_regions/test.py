import pytest
from solution import solve, solve_bfs
import copy

class TestSurroundedRegions:
    
    def test_example_1(self):
        """Test standard surrounded regions case"""
        board = [["X","X","X","X"],
                 ["X","O","O","X"],
                 ["X","X","O","X"],
                 ["X","O","X","X"]]
        
        expected = [["X","X","X","X"],
                   ["X","X","X","X"],
                   ["X","X","X","X"],
                   ["X","O","X","X"]]
        
        board_copy = copy.deepcopy(board)
        solve(board)
        assert board == expected
        
        solve_bfs(board_copy)
        assert board_copy == expected
    
    def test_single_cell(self):
        """Test single cell case"""
        board = [["X"]]
        expected = [["X"]]
        
        board_copy = copy.deepcopy(board)
        solve(board)
        assert board == expected
        
        solve_bfs(board_copy)
        assert board_copy == expected
    
    def test_all_border_connected(self):
        """Test case where all O's are connected to border"""
        board = [["O","O"],
                 ["O","O"]]
        expected = [["O","O"],
                   ["O","O"]]
        
        board_copy = copy.deepcopy(board)
        solve(board)
        assert board == expected
        
        solve_bfs(board_copy)
        assert board_copy == expected
    
    def test_no_o_cells(self):
        """Test case with no O cells"""
        board = [["X","X"],
                 ["X","X"]]
        expected = [["X","X"],
                   ["X","X"]]
        
        board_copy = copy.deepcopy(board)
        solve(board)
        assert board == expected
        
        solve_bfs(board_copy)
        assert board_copy == expected
    
    def test_complex_pattern(self):
        """Test more complex pattern"""
        board = [["X","O","X","O","X"],
                 ["O","X","O","X","O"],
                 ["X","O","X","O","X"],
                 ["O","X","O","X","O"]]
        
        # All O's touch borders, so none should be captured
        expected = [["X","O","X","O","X"],
                   ["O","X","O","X","O"],
                   ["X","O","X","O","X"],
                   ["O","X","O","X","O"]]
        
        board_copy = copy.deepcopy(board)
        solve(board)
        assert board == expected
        
        solve_bfs(board_copy)
        assert board_copy == expected
    
    def test_isolated_region(self):
        """Test completely isolated O region"""
        board = [["X","X","X","X","X"],
                 ["X","O","O","O","X"],
                 ["X","O","X","O","X"],
                 ["X","O","O","O","X"],
                 ["X","X","X","X","X"]]
        
        expected = [["X","X","X","X","X"],
                   ["X","X","X","X","X"],
                   ["X","X","X","X","X"],
                   ["X","X","X","X","X"],
                   ["X","X","X","X","X"]]
        
        board_copy = copy.deepcopy(board)
        solve(board)
        assert board == expected
        
        solve_bfs(board_copy)
        assert board_copy == expected

if __name__ == "__main__":
    pytest.main([__file__])

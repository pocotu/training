import pytest
from solution import shortest_path_binary_matrix, shortest_path_binary_matrix_astar, shortest_path_binary_matrix_bidirectional

class TestShortestPathBinaryMatrix:
    
    def test_example_1(self):
        """Test case: [[0,1],[1,0]] should return 2"""
        grid = [[0,1],[1,0]]
        expected = 2
        
        assert shortest_path_binary_matrix(grid) == expected
        assert shortest_path_binary_matrix_astar(grid) == expected
        assert shortest_path_binary_matrix_bidirectional(grid) == expected
    
    def test_example_2(self):
        """Test case: [[0,0,0],[1,1,0],[1,1,0]] should return 4"""
        grid = [[0,0,0],[1,1,0],[1,1,0]]
        expected = 4
        
        assert shortest_path_binary_matrix(grid) == expected
        assert shortest_path_binary_matrix_astar(grid) == expected
        assert shortest_path_binary_matrix_bidirectional(grid) == expected
    
    def test_blocked_start(self):
        """Test case: [[1,0,0],[1,1,0],[1,1,0]] should return -1"""
        grid = [[1,0,0],[1,1,0],[1,1,0]]
        expected = -1
        
        assert shortest_path_binary_matrix(grid) == expected
        assert shortest_path_binary_matrix_astar(grid) == expected
        assert shortest_path_binary_matrix_bidirectional(grid) == expected
    
    def test_single_cell(self):
        """Test case: [[0]] should return 1"""
        grid = [[0]]
        expected = 1
        
        assert shortest_path_binary_matrix(grid) == expected
        assert shortest_path_binary_matrix_astar(grid) == expected
        assert shortest_path_binary_matrix_bidirectional(grid) == expected
    
    def test_single_cell_blocked(self):
        """Test case: [[1]] should return -1"""
        grid = [[1]]
        expected = -1
        
        assert shortest_path_binary_matrix(grid) == expected
        assert shortest_path_binary_matrix_astar(grid) == expected
        assert shortest_path_binary_matrix_bidirectional(grid) == expected
    
    def test_direct_diagonal(self):
        """Test case: direct diagonal path possible"""
        grid = [[0,0,0],
                [0,1,0],
                [0,0,0]]
        expected = 3  # (0,0) -> (1,1) -> (2,2) but (1,1) is blocked, so diagonal
        
        result1 = shortest_path_binary_matrix(grid)
        result2 = shortest_path_binary_matrix_astar(grid)
        result3 = shortest_path_binary_matrix_bidirectional(grid)
        
        assert result1 == result2 == result3
        assert result1 >= 3  # Should find some path
    
    def test_no_path(self):
        """Test case: completely blocked path"""
        grid = [[0,1,1],
                [1,1,1],
                [1,1,0]]
        expected = -1
        
        assert shortest_path_binary_matrix(grid) == expected
        assert shortest_path_binary_matrix_astar(grid) == expected
        assert shortest_path_binary_matrix_bidirectional(grid) == expected
    
    def test_all_zeros(self):
        """Test case: all zeros - shortest diagonal path"""
        grid = [[0,0,0],
                [0,0,0],
                [0,0,0]]
        expected = 3  # Diagonal path: (0,0) -> (1,1) -> (2,2)
        
        assert shortest_path_binary_matrix(grid) == expected
        assert shortest_path_binary_matrix_astar(grid) == expected
        assert shortest_path_binary_matrix_bidirectional(grid) == expected
    
    def test_zigzag_path(self):
        """Test case requiring zigzag path"""
        grid = [[0,1,0,0,0],
                [0,1,0,1,0],
                [0,0,0,1,0],
                [1,1,1,1,0],
                [0,0,0,0,0]]
        
        result1 = shortest_path_binary_matrix(grid)
        result2 = shortest_path_binary_matrix_astar(grid)
        result3 = shortest_path_binary_matrix_bidirectional(grid)
        
        # All algorithms should find same shortest path
        assert result1 == result2 == result3
        assert result1 > 0  # Should find a path
    
    def test_blocked_end(self):
        """Test case: end position blocked"""
        grid = [[0,0,0],
                [0,0,0],
                [0,0,1]]
        expected = -1
        
        assert shortest_path_binary_matrix(grid) == expected
        assert shortest_path_binary_matrix_astar(grid) == expected
        assert shortest_path_binary_matrix_bidirectional(grid) == expected
    
    def test_large_grid(self):
        """Test case: larger grid"""
        grid = [[0,0,0,0,0],
                [1,1,0,1,0],
                [0,0,0,1,0],
                [0,1,0,0,0],
                [0,0,0,0,0]]
        
        result1 = shortest_path_binary_matrix(grid)
        result2 = shortest_path_binary_matrix_astar(grid)
        result3 = shortest_path_binary_matrix_bidirectional(grid)
        
        # All should find same optimal path
        assert result1 == result2 == result3
        assert result1 > 0

if __name__ == "__main__":
    pytest.main([__file__])

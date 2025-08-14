"""
Solution for N-Queens
Problem ID: 206
LeetCode Problem: https://leetcode.com/problems/n-queens/

The n-queens puzzle is the problem of placing n queens on an n×n chessboard
such that no two queens attack each other.
"""

def solve_n_queens_basic(n: int) -> list[list[str]]:
    """
    Basic backtracking approach.
    
    Args:
        n: Size of the chessboard (n x n)
        
    Returns:
        All possible solutions as list of boards
        
    Time Complexity: O(n!)
    Space Complexity: O(n²)
    """
    def is_safe(board, row, col):
        """Check if placing queen at (row, col) is safe."""
        # Check column
        for i in range(row):
            if board[i][col] == 'Q':
                return False
        
        # Check diagonal (top-left to bottom-right)
        i, j = row - 1, col - 1
        while i >= 0 and j >= 0:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j -= 1
        
        # Check diagonal (top-right to bottom-left)
        i, j = row - 1, col + 1
        while i >= 0 and j < n:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j += 1
        
        return True
    
    def backtrack(board, row):
        """Recursive backtracking function."""
        if row == n:
            # Found a solution
            result.append([''.join(row) for row in board])
            return
        
        for col in range(n):
            if is_safe(board, row, col):
                board[row][col] = 'Q'
                backtrack(board, row + 1)
                board[row][col] = '.'
    
    result = []
    board = [['.' for _ in range(n)] for _ in range(n)]
    backtrack(board, 0)
    return result

def solve_n_queens_optimized(n: int) -> list[list[str]]:
    """
    Optimized backtracking with conflict tracking.
    
    Args:
        n: Size of the chessboard (n x n)
        
    Returns:
        All possible solutions as list of boards
        
    Time Complexity: O(n!)
    Space Complexity: O(n)
    """
    def backtrack(row):
        if row == n:
            # Convert column positions to board representation
            board = []
            for r in range(n):
                row_str = '.' * cols[r] + 'Q' + '.' * (n - cols[r] - 1)
                board.append(row_str)
            result.append(board)
            return
        
        for col in range(n):
            # Check conflicts using sets for O(1) lookup
            if (col not in col_used and 
                (row - col) not in diag1_used and 
                (row + col) not in diag2_used):
                
                # Place queen
                cols[row] = col
                col_used.add(col)
                diag1_used.add(row - col)
                diag2_used.add(row + col)
                
                backtrack(row + 1)
                
                # Remove queen (backtrack)
                col_used.remove(col)
                diag1_used.remove(row - col)
                diag2_used.remove(row + col)
    
    result = []
    cols = [-1] * n  # cols[i] = column position of queen in row i
    col_used = set()
    diag1_used = set()  # row - col
    diag2_used = set()  # row + col
    
    backtrack(0)
    return result

def solve_n_queens_bit_manipulation(n: int) -> list[list[str]]:
    """
    Bit manipulation approach for maximum efficiency.
    
    Args:
        n: Size of the chessboard (n x n)
        
    Returns:
        All possible solutions as list of boards
        
    Time Complexity: O(n!)
    Space Complexity: O(n)
    """
    def backtrack(row, cols_mask, diag1_mask, diag2_mask):
        if row == n:
            result.append(construct_board())
            return
        
        # Available positions = positions not blocked by any conflict
        available = ((1 << n) - 1) & ~(cols_mask | diag1_mask | diag2_mask)
        
        while available:
            # Get rightmost available position
            pos = available & -available
            available &= available - 1  # Remove this position
            
            # Find column number
            col = (pos - 1).bit_length() - 1
            queens[row] = col
            
            backtrack(
                row + 1,
                cols_mask | pos,
                (diag1_mask | pos) << 1,
                (diag2_mask | pos) >> 1
            )
    
    def construct_board():
        """Convert queen positions to board representation."""
        board = []
        for r in range(n):
            row_str = '.' * queens[r] + 'Q' + '.' * (n - queens[r] - 1)
            board.append(row_str)
        return board
    
    result = []
    queens = [-1] * n
    backtrack(0, 0, 0, 0)
    return result

# Main function for the problem
def solveNQueens(n: int) -> list[list[str]]:
    """
    Main solution function using optimized approach.
    """
    return solve_n_queens_optimized(n)

if __name__ == "__main__":
    # Test cases
    test_cases = [1, 2, 3, 4, 5, 6, 7, 8]
    
    print("=" * 60)
    print("N-QUEENS - COMPREHENSIVE TESTING")
    print("=" * 60)
    
    algorithms = [
        ("Basic Backtracking", solve_n_queens_basic),
        ("Optimized Backtracking", solve_n_queens_optimized),
        ("Bit Manipulation", solve_n_queens_bit_manipulation),
    ]
    
    for n in test_cases:
        print(f"\nN-Queens for n = {n}:")
        
        results = []
        for name, func in algorithms:
            try:
                import time
                start_time = time.time()
                result = func(n)
                end_time = time.time()
                
                results.append(result)
                print(f"  {name}: {len(result)} solutions in {end_time - start_time:.6f}s")
                
                # Verify all algorithms give same results
                if len(results) > 1 and results[-1] != results[0]:
                    print(f"    WARNING: Results differ from first algorithm!")
                
            except Exception as e:
                print(f"  {name}: ERROR - {e}")
        
        # Show first solution for small n
        if n <= 4 and results and len(results[0]) > 0:
            print(f"  First solution:")
            for row in results[0][0]:
                print(f"    {row}")
    
    # Performance comparison for larger n
    print("\n" + "=" * 60)
    print("PERFORMANCE COMPARISON")
    print("=" * 60)
    
    performance_test_sizes = [8, 9, 10]
    
    for n in performance_test_sizes:
        print(f"\nPerformance test for n = {n}:")
        
        for name, func in algorithms:
            try:
                import time
                start_time = time.time()
                result = func(n)
                end_time = time.time()
                
                print(f"  {name}: {len(result)} solutions in {end_time - start_time:.6f}s")
                
            except Exception as e:
                print(f"  {name}: ERROR - {e}")
    
    # Solution validation
    print("\n" + "=" * 60)
    print("SOLUTION VALIDATION")
    print("=" * 60)
    
    def validate_solution(board):
        """Validate that a board solution is correct."""
        n = len(board)
        queens = []
        
        # Find queen positions
        for r in range(n):
            for c in range(n):
                if board[r][c] == 'Q':
                    queens.append((r, c))
        
        if len(queens) != n:
            return False, f"Expected {n} queens, found {len(queens)}"
        
        # Check conflicts
        for i in range(n):
            for j in range(i + 1, n):
                r1, c1 = queens[i]
                r2, c2 = queens[j]
                
                # Same row (shouldn't happen in our implementation)
                if r1 == r2:
                    return False, f"Queens at ({r1},{c1}) and ({r2},{c2}) in same row"
                
                # Same column
                if c1 == c2:
                    return False, f"Queens at ({r1},{c1}) and ({r2},{c2}) in same column"
                
                # Same diagonal
                if abs(r1 - r2) == abs(c1 - c2):
                    return False, f"Queens at ({r1},{c1}) and ({r2},{c2}) in same diagonal"
        
        return True, "Valid solution"
    
    # Validate some solutions
    for n in [4, 8]:
        solutions = solveNQueens(n)
        print(f"\nValidating solutions for n = {n}:")
        
        valid_count = 0
        for i, solution in enumerate(solutions[:5]):  # Check first 5 solutions
            is_valid, message = validate_solution(solution)
            if is_valid:
                valid_count += 1
            print(f"  Solution {i + 1}: {message}")
        
        print(f"  Validated {valid_count}/{min(5, len(solutions))} solutions")
    
    # Expected solution counts (for verification)
    expected_counts = {
        1: 1, 2: 0, 3: 0, 4: 2, 5: 10, 6: 4, 7: 40, 8: 92,
        9: 352, 10: 724, 11: 2680, 12: 14200
    }
    
    print("\n" + "=" * 60)
    print("SOLUTION COUNT VERIFICATION")
    print("=" * 60)
    
    for n in range(1, 9):
        actual = len(solveNQueens(n))
        expected = expected_counts.get(n, "Unknown")
        status = "✓" if actual == expected else "✗"
        print(f"n = {n}: {actual} solutions {status} (expected: {expected})")

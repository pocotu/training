"""
Surrounded Regions - LeetCode Problem #130
Problem ID: 129

Given an m x n matrix board containing 'X' and 'O', capture all regions 
that are 4-directionally surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

Time Complexity: O(m*n)
Space Complexity: O(m*n) worst case for recursion
"""

def solve(board):
    """
    Capture surrounded regions by modifying board in-place.
    
    Args:
        board: List[List[str]] - matrix containing 'X' and 'O'
    """
    if not board or not board[0]:
        return
    
    m, n = len(board), len(board[0])
    
    def dfs(i, j):
        """Mark connected 'O's from border as safe"""
        if (i < 0 or i >= m or j < 0 or j >= n or 
            board[i][j] != 'O'):
            return
        
        # Mark as temporary safe
        board[i][j] = '#'
        
        # Explore all 4 directions
        dfs(i + 1, j)
        dfs(i - 1, j)
        dfs(i, j + 1)
        dfs(i, j - 1)
    
    # Step 1: Mark all 'O's connected to borders as safe
    # Check first and last rows
    for j in range(n):
        if board[0][j] == 'O':
            dfs(0, j)
        if board[m-1][j] == 'O':
            dfs(m-1, j)
    
    # Check first and last columns
    for i in range(m):
        if board[i][0] == 'O':
            dfs(i, 0)
        if board[i][n-1] == 'O':
            dfs(i, n-1)
    
    # Step 2: Convert remaining 'O's to 'X' and restore safe ones
    for i in range(m):
        for j in range(n):
            if board[i][j] == 'O':
                board[i][j] = 'X'  # Capture surrounded region
            elif board[i][j] == '#':
                board[i][j] = 'O'  # Restore safe region

# Alternative BFS solution
from collections import deque

def solve_bfs(board):
    """BFS solution for surrounded regions"""
    if not board or not board[0]:
        return
    
    m, n = len(board), len(board[0])
    queue = deque()
    
    # Add all border 'O's to queue
    for i in range(m):
        for j in range(n):
            if (board[i][j] == 'O' and 
                (i == 0 or i == m-1 or j == 0 or j == n-1)):
                queue.append((i, j))
                board[i][j] = '#'
    
    # BFS to mark all connected 'O's as safe
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    while queue:
        i, j = queue.popleft()
        for di, dj in directions:
            ni, nj = i + di, j + dj
            if (0 <= ni < m and 0 <= nj < n and board[ni][nj] == 'O'):
                board[ni][nj] = '#'
                queue.append((ni, nj))
    
    # Restore board state
    for i in range(m):
        for j in range(n):
            if board[i][j] == 'O':
                board[i][j] = 'X'
            elif board[i][j] == '#':
                board[i][j] = 'O'

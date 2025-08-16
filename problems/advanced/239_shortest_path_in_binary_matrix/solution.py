"""
Shortest Path in Binary Matrix - LeetCode Problem #1091
Problem ID: 239

Given an n x n binary matrix grid, return the length of the shortest clear 
path from top-left to bottom-right. If there is no such path, return -1.

A clear path is a path from top-left to bottom-right such that:
- All the visited cells of the path are 0.
- All the adjacent cells of the path are 8-directionally connected.

Time Complexity: O(n^2)
Space Complexity: O(n^2)
"""

from collections import deque
import heapq

def shortest_path_binary_matrix(grid):
    """
    Find shortest path using BFS.
    
    Args:
        grid: List[List[int]] - binary matrix
        
    Returns:
        int: shortest path length or -1 if no path
    """
    n = len(grid)
    
    # Check if start or end is blocked
    if grid[0][0] == 1 or grid[n-1][n-1] == 1:
        return -1
    
    # Special case: single cell
    if n == 1:
        return 1
    
    # 8 directions: up, down, left, right, and 4 diagonals
    directions = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
    
    queue = deque([(0, 0, 1)])  # (row, col, distance)
    visited = {(0, 0)}
    
    while queue:
        row, col, dist = queue.popleft()
        
        # Check if we reached the destination
        if row == n-1 and col == n-1:
            return dist
        
        # Explore all 8 directions
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            
            if (0 <= new_row < n and 0 <= new_col < n and 
                grid[new_row][new_col] == 0 and 
                (new_row, new_col) not in visited):
                
                visited.add((new_row, new_col))
                queue.append((new_row, new_col, dist + 1))
    
    return -1

# Alternative A* implementation for optimal pathfinding
def shortest_path_binary_matrix_astar(grid):
    """
    A* algorithm implementation for shortest path.
    """
    n = len(grid)
    
    if grid[0][0] == 1 or grid[n-1][n-1] == 1:
        return -1
    
    if n == 1:
        return 1
    
    def heuristic(row, col):
        """Manhattan distance heuristic"""
        return max(abs(row - (n-1)), abs(col - (n-1)))
    
    directions = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
    
    # Priority queue: (f_score, g_score, row, col)
    heap = [(heuristic(0, 0), 0, 0, 0)]
    visited = set()
    
    while heap:
        f_score, g_score, row, col = heapq.heappop(heap)
        
        if (row, col) in visited:
            continue
            
        visited.add((row, col))
        
        if row == n-1 and col == n-1:
            return g_score + 1
        
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            
            if (0 <= new_row < n and 0 <= new_col < n and 
                grid[new_row][new_col] == 0 and 
                (new_row, new_col) not in visited):
                
                new_g_score = g_score + 1
                new_f_score = new_g_score + heuristic(new_row, new_col)
                heapq.heappush(heap, (new_f_score, new_g_score, new_row, new_col))
    
    return -1

# Bidirectional BFS for even better performance
def shortest_path_binary_matrix_bidirectional(grid):
    """
    Bidirectional BFS implementation.
    """
    n = len(grid)
    
    if grid[0][0] == 1 or grid[n-1][n-1] == 1:
        return -1
    
    if n == 1:
        return 1
    
    directions = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
    
    # Forward and backward queues
    queue_forward = deque([(0, 0, 1)])
    queue_backward = deque([(n-1, n-1, 1)])
    
    visited_forward = {(0, 0): 1}
    visited_backward = {(n-1, n-1): 1}
    
    def expand(queue, visited, other_visited):
        if not queue:
            return -1
            
        row, col, dist = queue.popleft()
        
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            
            if (0 <= new_row < n and 0 <= new_col < n and 
                grid[new_row][new_col] == 0):
                
                if (new_row, new_col) in other_visited:
                    return dist + other_visited[(new_row, new_col)]
                
                if (new_row, new_col) not in visited:
                    visited[(new_row, new_col)] = dist + 1
                    queue.append((new_row, new_col, dist + 1))
        
        return -1
    
    while queue_forward or queue_backward:
        # Expand forward
        if queue_forward:
            result = expand(queue_forward, visited_forward, visited_backward)
            if result != -1:
                return result
        
        # Expand backward
        if queue_backward:
            result = expand(queue_backward, visited_backward, visited_forward)
            if result != -1:
                return result
    
    return -1

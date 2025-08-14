"""
Solution Template for Competitive Programming Problems

This template provides a standard structure for implementing solutions.
Modify according to the specific problem requirements.

Problem: [Problem Title]
ID: [Problem ID]
Difficulty: [basic | intermediate | advanced]
Source: [Platform Name]
URL: [Problem URL]

Time Complexity: O(?)
Space Complexity: O(?)
"""

from typing import List, Optional, Dict, Set, Tuple, Any
import collections
import heapq
import bisect
import math
import sys

class Solution:
    """
    Main solution class for the problem.
    Use this structure for LeetCode-style problems.
    """
    
    def solve(self, *args) -> Any:
        """
        Main solution method.
        
        Args:
            *args: Problem-specific input parameters
            
        Returns:
            Problem-specific output type
            
        Example:
            For Two Sum problem:
            def solve(self, nums: List[int], target: int) -> List[int]:
        """
        # TODO: Implement the solution
        pass
    
    def helper_method(self, param):
        """
        Helper method for complex solutions.
        Use this for breaking down the solution into smaller parts.
        """
        pass

# Alternative function-based approach
def solve(*args) -> Any:
    """
    Function-based solution (alternative to class-based).
    Use this for simpler problems or when class structure is not needed.
    
    Args:
        *args: Problem-specific input parameters
        
    Returns:
        Problem-specific output type
    """
    # TODO: Implement the solution
    pass

# Common utility functions for competitive programming
def binary_search(arr: List[int], target: int) -> int:
    """Binary search implementation"""
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def dfs(graph: Dict[int, List[int]], start: int, visited: Set[int]) -> None:
    """Depth-First Search template"""
    if start in visited:
        return
    visited.add(start)
    for neighbor in graph.get(start, []):
        dfs(graph, neighbor, visited)

def bfs(graph: Dict[int, List[int]], start: int) -> List[int]:
    """Breadth-First Search template"""
    visited = set()
    queue = collections.deque([start])
    result = []
    
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            result.append(node)
            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    queue.append(neighbor)
    
    return result

def quick_sort(arr: List[int]) -> List[int]:
    """Quick sort implementation"""
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def merge_sort(arr: List[int]) -> List[int]:
    """Merge sort implementation"""
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left: List[int], right: List[int]) -> List[int]:
    """Merge two sorted arrays"""
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Dynamic Programming templates
def dp_1d_template(n: int) -> int:
    """1D Dynamic Programming template"""
    dp = [0] * (n + 1)
    dp[0] = 1  # Base case
    
    for i in range(1, n + 1):
        # Recurrence relation
        dp[i] = dp[i - 1]  # Modify based on problem
    
    return dp[n]

def dp_2d_template(m: int, n: int) -> int:
    """2D Dynamic Programming template"""
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Initialize base cases
    for i in range(m + 1):
        dp[i][0] = 1
    for j in range(n + 1):
        dp[0][j] = 1
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # Recurrence relation
            dp[i][j] = dp[i-1][j] + dp[i][j-1]  # Modify based on problem
    
    return dp[m][n]

# Backtracking template
def backtrack(path: List[Any], choices: List[Any], result: List[List[Any]], target_length: int) -> None:
    """Backtracking template"""
    # Base case
    if len(path) == target_length:
        result.append(path[:])  # Make a copy
        return
    
    for choice in choices:
        # Make choice
        path.append(choice)
        
        # Recurse with filtered choices for next level if needed
        backtrack(path, choices, result, target_length)
        
        # Undo choice (backtrack)
        path.pop()

# Tree traversal templates
class TreeNode:
    """Binary tree node definition"""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorder_traversal(root: Optional[TreeNode]) -> List[int]:
    """Inorder traversal: Left -> Root -> Right"""
    if not root:
        return []
    return inorder_traversal(root.left) + [root.val] + inorder_traversal(root.right)

def preorder_traversal(root: Optional[TreeNode]) -> List[int]:
    """Preorder traversal: Root -> Left -> Right"""
    if not root:
        return []
    return [root.val] + preorder_traversal(root.left) + preorder_traversal(root.right)

def postorder_traversal(root: Optional[TreeNode]) -> List[int]:
    """Postorder traversal: Left -> Right -> Root"""
    if not root:
        return []
    return postorder_traversal(root.left) + postorder_traversal(root.right) + [root.val]

def level_order_traversal(root: Optional[TreeNode]) -> List[List[int]]:
    """Level order traversal (BFS)"""
    if not root:
        return []
    
    result = []
    queue = collections.deque([root])
    
    while queue:
        level_size = len(queue)
        level = []
        
        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(level)
    
    return result

# Input/Output helpers for competitive programming
def read_int():
    """Read single integer from input"""
    return int(input())

def read_ints():
    """Read multiple integers from a line"""
    return list(map(int, input().split()))

def read_string():
    """Read string from input"""
    return input().strip()

def read_strings():
    """Read multiple strings from a line"""
    return input().split()

# Common patterns and tricks
def two_pointers_template(arr: List[int], target: int) -> bool:
    """Two pointers technique template"""
    left, right = 0, len(arr) - 1
    
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            return True
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    
    return False

def sliding_window_template(s: str, k: int) -> int:
    """Sliding window technique template"""
    left = 0
    max_length = 0
    char_count = {}
    
    for right in range(len(s)):
        # Expand window
        char_count[s[right]] = char_count.get(s[right], 0) + 1
        
        # Contract window if needed
        while len(char_count) > k:
            char_count[s[left]] -= 1
            if char_count[s[left]] == 0:
                del char_count[s[left]]
            left += 1
        
        # Update result
        max_length = max(max_length, right - left + 1)
    
    return max_length

# Main execution block
if __name__ == "__main__":
    # Test the solution locally
    solution = Solution()
    
    # Example test case
    # result = solution.solve(test_input)
    # print(f"Result: {result}")
    
    # For competitive programming platforms that require specific I/O
    # Uncomment and modify as needed:
    
    # # Read input
    # n = read_int()
    # arr = read_ints()
    # 
    # # Solve
    # result = solve(arr, n)
    # 
    # # Output result
    # print(result)
    
    pass

"""
Template Usage Instructions:

1. PROBLEM SETUP:
   - Fill in the problem information at the top (title, ID, difficulty, etc.)
   - Update the time and space complexity comments

2. CHOOSE SOLUTION APPROACH:
   - Use Solution class for LeetCode-style problems
   - Use solve() function for simpler problems
   - Choose based on your preference and problem requirements

3. IMPLEMENT SOLUTION:
   - Replace the pass statement in solve() method with your implementation
   - Use helper methods for complex solutions
   - Import additional modules if needed

4. USE UTILITY FUNCTIONS:
   - Leverage the provided templates for common algorithms
   - Modify templates to fit your specific problem needs
   - Add custom utility functions as required

5. INPUT/OUTPUT:
   - For online judges: use read_int(), read_ints(), etc.
   - For LeetCode: use the class-based approach
   - Test locally using the __main__ block

6. TESTING:
   - Use the __main__ block for local testing
   - Create test cases to verify your solution
   - Run with the corresponding test.py file

7. OPTIMIZATION:
   - Profile your solution for large inputs
   - Consider time and space complexity requirements
   - Use appropriate data structures and algorithms

Common Algorithm Patterns:
- Two Pointers: For array problems with sorted data
- Sliding Window: For substring/subarray problems
- DFS/BFS: For tree and graph problems
- Dynamic Programming: For optimization problems
- Backtracking: For combinatorial problems
- Binary Search: For search problems in sorted data
"""

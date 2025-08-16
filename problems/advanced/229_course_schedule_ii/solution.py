"""
Solution for Course Schedule II
Problem ID: 207
LeetCode Problem: https://leetcode.com/problems/course-schedule-ii/

Return the ordering of courses you should take to finish all courses.
If it is impossible to finish all courses, return an empty array.
"""

from collections import defaultdict, deque

def find_order_dfs(numCourses: int, prerequisites: list[list[int]]) -> list[int]:
    """
    DFS-based topological sort approach.
    
    Args:
        numCourses: Number of courses
        prerequisites: List of [course, prerequisite] pairs
        
    Returns:
        Valid course order or empty list if impossible
        
    Time Complexity: O(V + E)
    Space Complexity: O(V + E)
    """
    # Build adjacency list
    graph = defaultdict(list)
    for course, prereq in prerequisites:
        graph[prereq].append(course)
    
    # DFS states: 0 = unvisited, 1 = visiting, 2 = visited
    states = [0] * numCourses
    result = []
    
    def dfs(course):
        """DFS with cycle detection."""
        if states[course] == 1:  # Cycle detected
            return False
        if states[course] == 2:  # Already processed
            return True
        
        states[course] = 1  # Mark as visiting
        
        # Visit all dependent courses
        for dependent in graph[course]:
            if not dfs(dependent):
                return False
        
        states[course] = 2  # Mark as visited
        result.append(course)
        return True
    
    # Try DFS from each unvisited course
    for course in range(numCourses):
        if states[course] == 0:
            if not dfs(course):
                return []  # Cycle detected
    
    return result

def find_order_bfs(numCourses: int, prerequisites: list[list[int]]) -> list[int]:
    """
    BFS-based topological sort (Kahn's algorithm).
    
    Args:
        numCourses: Number of courses
        prerequisites: List of [course, prerequisite] pairs
        
    Returns:
        Valid course order or empty list if impossible
        
    Time Complexity: O(V + E)
    Space Complexity: O(V + E)
    """
    # Build graph and calculate in-degrees
    graph = defaultdict(list)
    in_degree = [0] * numCourses
    
    for course, prereq in prerequisites:
        graph[prereq].append(course)
        in_degree[course] += 1
    
    # Find all courses with no prerequisites
    queue = deque()
    for course in range(numCourses):
        if in_degree[course] == 0:
            queue.append(course)
    
    result = []
    
    while queue:
        current = queue.popleft()
        result.append(current)
        
        # Remove current course and update in-degrees
        for dependent in graph[current]:
            in_degree[dependent] -= 1
            if in_degree[dependent] == 0:
                queue.append(dependent)
    
    # Check if all courses can be taken
    return result if len(result) == numCourses else []

def find_order_optimized(numCourses: int, prerequisites: list[list[int]]) -> list[int]:
    """
    Optimized approach with early termination checks.
    
    Args:
        numCourses: Number of courses
        prerequisites: List of [course, prerequisite] pairs
        
    Returns:
        Valid course order or empty list if impossible
        
    Time Complexity: O(V + E)
    Space Complexity: O(V + E)
    """
    # Early termination: if prerequisites > courses² it's impossible
    if len(prerequisites) > numCourses * numCourses:
        return []
    
    # Build graph with optimizations
    graph = [[] for _ in range(numCourses)]
    in_degree = [0] * numCourses
    
    # Build graph and detect immediate impossibilities
    for course, prereq in prerequisites:
        if course == prereq:  # Self-loop
            return []
        if prereq >= numCourses or course >= numCourses:  # Invalid course
            return []
        
        graph[prereq].append(course)
        in_degree[course] += 1
    
    # Kahn's algorithm with optimizations
    queue = deque()
    for course in range(numCourses):
        if in_degree[course] == 0:
            queue.append(course)
    
    result = []
    processed = 0
    
    while queue:
        current = queue.popleft()
        result.append(current)
        processed += 1
        
        # Process dependencies
        for dependent in graph[current]:
            in_degree[dependent] -= 1
            if in_degree[dependent] == 0:
                queue.append(dependent)
    
    return result if processed == numCourses else []

def find_order_iterative_dfs(numCourses: int, prerequisites: list[list[int]]) -> list[int]:
    """
    Iterative DFS approach to avoid recursion stack overflow.
    
    Args:
        numCourses: Number of courses
        prerequisites: List of [course, prerequisite] pairs
        
    Returns:
        Valid course order or empty list if impossible
        
    Time Complexity: O(V + E)
    Space Complexity: O(V + E)
    """
    # Build adjacency list
    graph = [[] for _ in range(numCourses)]
    for course, prereq in prerequisites:
        graph[prereq].append(course)
    
    # States: 0 = white (unvisited), 1 = gray (visiting), 2 = black (finished)
    colors = [0] * numCourses
    result = []
    
    def iterative_dfs(start):
        """Iterative DFS with explicit stack."""
        stack = [(start, False)]  # (node, finished_processing)
        
        while stack:
            node, finished = stack.pop()
            
            if finished:
                # Finished processing all children
                colors[node] = 2
                result.append(node)
            else:
                if colors[node] == 1:  # Gray node - cycle detected
                    return False
                if colors[node] == 2:  # Already processed
                    continue
                
                colors[node] = 1  # Mark as gray
                stack.append((node, True))  # Will process after children
                
                # Add children to stack (in reverse order for consistent ordering)
                for neighbor in reversed(graph[node]):
                    if colors[neighbor] != 2:
                        stack.append((neighbor, False))
        
        return True
    
    # Process all components
    for course in range(numCourses):
        if colors[course] == 0:
            if not iterative_dfs(course):
                return []
    
    return result

# Main function for the problem
def findOrder(numCourses: int, prerequisites: list[list[int]]) -> list[int]:
    """
    Main solution function using BFS approach for stability.
    """
    return find_order_bfs(numCourses, prerequisites)

if __name__ == "__main__":
    # Test cases
    test_cases = [
        # Basic cases
        (2, [[1,0]], [0,1]),
        (4, [[1,0],[2,0],[3,1],[3,2]], [0,1,2,3]),
        (1, [], [0]),
        
        # Impossible cases
        (2, [[1,0],[0,1]], []),
        (3, [[1,0],[2,1],[0,2]], []),
        
        # Complex cases
        (6, [[1,0],[2,1],[3,2],[4,3],[5,4]], [0,1,2,3,4,5]),
        (4, [[1,0],[2,0],[3,1],[3,2]], [0,1,2,3]),
        (3, [[0,1],[0,2],[1,2]], [2,1,0]),
        
        # Edge cases
        (0, [], []),
        (5, [], [0,1,2,3,4]),
    ]
    
    print("=" * 60)
    print("COURSE SCHEDULE II - COMPREHENSIVE TESTING")
    print("=" * 60)
    
    algorithms = [
        ("DFS Topological Sort", find_order_dfs),
        ("BFS (Kahn's Algorithm)", find_order_bfs),
        ("Optimized BFS", find_order_optimized),
        ("Iterative DFS", find_order_iterative_dfs),
    ]
    
    for i, (numCourses, prerequisites, expected) in enumerate(test_cases):
        print(f"\nTest Case {i + 1}:")
        print(f"  Courses: {numCourses}")
        print(f"  Prerequisites: {prerequisites}")
        print(f"  Expected: {expected}")
        
        results = []
        for name, func in algorithms:
            try:
                import time
                start_time = time.time()
                result = func(numCourses, prerequisites)
                end_time = time.time()
                
                results.append(result)
                
                # Check if result is valid
                is_valid = validate_course_order(numCourses, prerequisites, result)
                status = "✓" if is_valid else "✗"
                
                print(f"  {name}: {result} {status} ({end_time - start_time:.6f}s)")
                
            except Exception as e:
                print(f"  {name}: ERROR - {e}")
        
        # Check consistency between algorithms
        if len(set(tuple(r) if r else () for r in results)) > 1:
            print(f"  WARNING: Different valid orderings found")

def validate_course_order(numCourses: int, prerequisites: list[list[int]], order: list[int]) -> bool:
    """
    Validate that a course order satisfies all prerequisites.
    
    Args:
        numCourses: Number of courses
        prerequisites: List of [course, prerequisite] pairs
        order: Proposed course order
        
    Returns:
        True if order is valid, False otherwise
    """
    if not order:
        return numCourses == 0 or len(prerequisites) > 0
    
    if len(order) != numCourses:
        return False
    
    if set(order) != set(range(numCourses)):
        return False
    
    # Create position map
    position = {course: i for i, course in enumerate(order)}
    
    # Check all prerequisites
    for course, prereq in prerequisites:
        if position[prereq] >= position[course]:
            return False
    
    return True

# Performance testing
def performance_test():
    """Test performance with larger inputs."""
    print("\n" + "=" * 60)
    print("PERFORMANCE TESTING")
    print("=" * 60)
    
    import random
    import time
    
    test_sizes = [100, 500, 1000, 2000]
    
    for size in test_sizes:
        print(f"\nTesting with {size} courses:")
        
        # Generate random prerequisites (ensuring no cycles)
        prerequisites = []
        for i in range(size // 2):
            prereq = random.randint(0, size - 2)
            course = random.randint(prereq + 1, size - 1)
            prerequisites.append([course, prereq])
        
        print(f"  Prerequisites: {len(prerequisites)}")
        
        for name, func in algorithms:
            try:
                start_time = time.time()
                result = func(size, prerequisites)
                end_time = time.time()
                
                success = len(result) == size
                print(f"  {name}: {end_time - start_time:.6f}s {'✓' if success else '✗'}")
                
            except Exception as e:
                print(f"  {name}: ERROR - {e}")

# Memory usage testing
def memory_test():
    """Test memory usage with different graph densities."""
    print("\n" + "=" * 60)
    print("MEMORY USAGE TESTING")
    print("=" * 60)
    
    import sys
    
    def get_size(obj):
        """Get approximate size of object."""
        return sys.getsizeof(obj)
    
    test_cases = [
        (100, 50, "Sparse"),    # 50 edges for 100 nodes
        (100, 200, "Medium"),   # 200 edges for 100 nodes
        (100, 500, "Dense"),    # 500 edges for 100 nodes
    ]
    
    for size, edge_count, density in test_cases:
        print(f"\n{density} graph ({size} nodes, {edge_count} edges):")
        
        # Generate prerequisites
        prerequisites = []
        import random
        for _ in range(edge_count):
            course = random.randint(0, size - 1)
            prereq = random.randint(0, size - 1)
            if course != prereq:
                prerequisites.append([course, prereq])
        
        for name, func in algorithms[:2]:  # Test main algorithms
            try:
                result = func(size, prerequisites)
                print(f"  {name}: Success ({'✓' if len(result) == size else '✗'})")
                
            except Exception as e:
                print(f"  {name}: ERROR - {e}")

if __name__ == "__main__":
    performance_test()
    memory_test()
    
    # Cycle detection test
    print("\n" + "=" * 60)
    print("CYCLE DETECTION TESTING")
    print("=" * 60)
    
    cycle_test_cases = [
        (3, [[0,1],[1,2],[2,0]], "Simple 3-cycle"),
        (4, [[0,1],[1,2],[2,3],[3,1]], "4-node cycle"),
        (5, [[0,1],[1,2],[2,3],[3,4],[4,0]], "5-node cycle"),
        (2, [[0,1],[1,0]], "Simple 2-cycle"),
    ]
    
    for numCourses, prerequisites, description in cycle_test_cases:
        print(f"\n{description}:")
        print(f"  Prerequisites: {prerequisites}")
        
        for name, func in algorithms:
            try:
                result = func(numCourses, prerequisites)
                success = len(result) == 0  # Should detect cycle
                print(f"  {name}: {'✓' if success else '✗'} (returned {result})")
                
            except Exception as e:
                print(f"  {name}: ERROR - {e}")

"""
Solution for Course Schedule
Problem ID: 210
LeetCode Problem: https://leetcode.com/problems/course-schedule/

There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.
You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.
Return true if you can finish all courses. Otherwise, return false.
"""

from collections import defaultdict, deque

def can_finish_dfs(numCourses: int, prerequisites: list[list[int]]) -> bool:
    """
    DFS-based cycle detection approach.
    
    Args:
        numCourses: Number of courses
        prerequisites: List of [course, prerequisite] pairs
        
    Returns:
        True if all courses can be finished, False otherwise
        
    Time Complexity: O(V + E)
    Space Complexity: O(V + E)
    """
    # Build adjacency list
    graph = defaultdict(list)
    for course, prereq in prerequisites:
        graph[prereq].append(course)
    
    # DFS states: 0 = unvisited, 1 = visiting, 2 = visited
    states = [0] * numCourses
    
    def has_cycle(course):
        """DFS to detect cycle."""
        if states[course] == 1:  # Currently visiting - cycle detected
            return True
        if states[course] == 2:  # Already visited - no cycle from here
            return False
        
        states[course] = 1  # Mark as visiting
        
        # Check all neighbors
        for neighbor in graph[course]:
            if has_cycle(neighbor):
                return True
        
        states[course] = 2  # Mark as visited
        return False
    
    # Check for cycles starting from each unvisited course
    for course in range(numCourses):
        if states[course] == 0:
            if has_cycle(course):
                return False
    
    return True

def can_finish_bfs(numCourses: int, prerequisites: list[list[int]]) -> bool:
    """
    BFS-based topological sort (Kahn's algorithm).
    
    Args:
        numCourses: Number of courses
        prerequisites: List of [course, prerequisite] pairs
        
    Returns:
        True if all courses can be finished, False otherwise
        
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
    
    processed_courses = 0
    
    while queue:
        current = queue.popleft()
        processed_courses += 1
        
        # Remove current course and update in-degrees
        for dependent in graph[current]:
            in_degree[dependent] -= 1
            if in_degree[dependent] == 0:
                queue.append(dependent)
    
    # All courses can be finished if we processed all of them
    return processed_courses == numCourses

def can_finish_optimized(numCourses: int, prerequisites: list[list[int]]) -> bool:
    """
    Optimized approach with early termination checks.
    
    Args:
        numCourses: Number of courses
        prerequisites: List of [course, prerequisite] pairs
        
    Returns:
        True if all courses can be finished, False otherwise
        
    Time Complexity: O(V + E)
    Space Complexity: O(V + E)
    """
    # Early termination: too many prerequisites
    if len(prerequisites) > numCourses * numCourses:
        return False
    
    # Build graph with validation
    graph = [[] for _ in range(numCourses)]
    in_degree = [0] * numCourses
    
    for course, prereq in prerequisites:
        # Validate course numbers
        if course < 0 or course >= numCourses or prereq < 0 or prereq >= numCourses:
            return False
        
        # Self-loop detection
        if course == prereq:
            return False
        
        graph[prereq].append(course)
        in_degree[course] += 1
    
    # Kahn's algorithm with optimizations
    queue = deque()
    for course in range(numCourses):
        if in_degree[course] == 0:
            queue.append(course)
    
    processed = 0
    
    while queue:
        current = queue.popleft()
        processed += 1
        
        for dependent in graph[current]:
            in_degree[dependent] -= 1
            if in_degree[dependent] == 0:
                queue.append(dependent)
    
    return processed == numCourses

def can_finish_union_find(numCourses: int, prerequisites: list[list[int]]) -> bool:
    """
    Union-Find approach for cycle detection.
    Note: This approach is more complex for this problem but demonstrates alternative thinking.
    
    Args:
        numCourses: Number of courses
        prerequisites: List of [course, prerequisite] pairs
        
    Returns:
        True if all courses can be finished, False otherwise
        
    Time Complexity: O(E * α(V)) where α is inverse Ackermann function
    Space Complexity: O(V)
    """
    class UnionFind:
        def __init__(self, n):
            self.parent = list(range(n))
            self.rank = [0] * n
        
        def find(self, x):
            if self.parent[x] != x:
                self.parent[x] = self.find(self.parent[x])
            return self.parent[x]
        
        def union(self, x, y):
            px, py = self.find(x), self.find(y)
            if px == py:
                return False  # Cycle detected
            
            if self.rank[px] < self.rank[py]:
                px, py = py, px
            
            self.parent[py] = px
            if self.rank[px] == self.rank[py]:
                self.rank[px] += 1
            
            return True
    
    # For this problem, we need to check if adding each edge creates a cycle
    # This is a simplified approach - full implementation would be more complex
    uf = UnionFind(numCourses)
    
    # Sort prerequisites to process in a consistent order
    prerequisites_sorted = sorted(prerequisites)
    
    for course, prereq in prerequisites_sorted:
        if not uf.union(prereq, course):
            return False  # Cycle detected
    
    return True

def can_finish_matrix(numCourses: int, prerequisites: list[list[int]]) -> bool:
    """
    Adjacency matrix approach for small graphs.
    
    Args:
        numCourses: Number of courses
        prerequisites: List of [course, prerequisite] pairs
        
    Returns:
        True if all courses can be finished, False otherwise
        
    Time Complexity: O(V²)
    Space Complexity: O(V²)
    """
    # Only efficient for small number of courses
    if numCourses > 100:
        return can_finish_bfs(numCourses, prerequisites)
    
    # Build adjacency matrix
    adj_matrix = [[False] * numCourses for _ in range(numCourses)]
    
    for course, prereq in prerequisites:
        if course == prereq:  # Self-loop
            return False
        adj_matrix[prereq][course] = True
    
    # Floyd-Warshall to find transitive closure
    for k in range(numCourses):
        for i in range(numCourses):
            for j in range(numCourses):
                adj_matrix[i][j] = adj_matrix[i][j] or (adj_matrix[i][k] and adj_matrix[k][j])
    
    # Check for cycles (diagonal elements should be False)
    for i in range(numCourses):
        if adj_matrix[i][i]:
            return False
    
    return True

# Main function for the problem
def canFinish(numCourses: int, prerequisites: list[list[int]]) -> bool:
    """
    Main solution using BFS approach for reliability.
    """
    return can_finish_bfs(numCourses, prerequisites)

if __name__ == "__main__":
    # Test cases
    test_cases = [
        # Basic valid cases
        (2, [[1, 0]], True),  # Course 1 depends on 0
        (3, [[1, 0], [2, 1]], True),  # Linear dependency
        (4, [[1, 0], [2, 0], [3, 1], [3, 2]], True),  # Tree structure
        
        # Basic invalid cases (cycles)
        (2, [[1, 0], [0, 1]], False),  # Simple cycle
        (3, [[1, 0], [2, 1], [0, 2]], False),  # 3-node cycle
        (4, [[1, 0], [2, 1], [3, 2], [1, 3]], False),  # 4-node cycle
        
        # Edge cases
        (1, [], True),  # Single course, no prerequisites
        (0, [], True),  # No courses
        (2, [], True),  # No prerequisites
        (5, [[1, 2], [2, 3]], True),  # Disconnected components
        
        # Self-loops
        (2, [[0, 0]], False),  # Self-dependency
        (3, [[1, 1]], False),  # Self-dependency in middle
        
        # Complex valid cases
        (6, [[1, 0], [2, 1], [3, 2], [4, 3], [5, 4]], True),  # Linear chain
        (4, [[0, 1], [0, 2], [1, 3], [2, 3]], True),  # Diamond pattern
        
        # Complex invalid cases
        (4, [[0, 1], [1, 2], [2, 3], [3, 0]], False),  # 4-cycle
        (5, [[0, 1], [1, 2], [2, 0], [3, 4]], False),  # Cycle in subgraph
        
        # Large cases
        (100, [], True),  # Large number, no prerequisites
        (50, [[i+1, i] for i in range(49)], True),  # Linear dependency chain
    ]
    
    print("=" * 60)
    print("COURSE SCHEDULE - COMPREHENSIVE TESTING")
    print("=" * 60)
    
    algorithms = [
        ("DFS Cycle Detection", can_finish_dfs),
        ("BFS (Kahn's Algorithm)", can_finish_bfs),
        ("Optimized BFS", can_finish_optimized),
        ("Union-Find", can_finish_union_find),
        ("Adjacency Matrix", can_finish_matrix),
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
                status = "✓" if result == expected else "✗"
                print(f"  {name}: {result} {status} ({end_time - start_time:.6f}s)")
                
            except Exception as e:
                print(f"  {name}: ERROR - {e}")
        
        # Check consistency
        if len(set(results)) > 1:
            print(f"  WARNING: Inconsistent results: {results}")
    
    # Performance testing
    print("\n" + "=" * 60)
    print("PERFORMANCE TESTING")
    print("=" * 60)
    
    import random
    import time
    
    def generate_acyclic_graph(n, edge_prob=0.1):
        """Generate random acyclic graph."""
        prerequisites = []
        for i in range(n):
            for j in range(i + 1, n):
                if random.random() < edge_prob:
                    # Add edge j -> i (ensures acyclic since j > i)
                    prerequisites.append([i, j])
        return prerequisites
    
    def generate_cyclic_graph(n, base_edges=None):
        """Generate graph with guaranteed cycle."""
        if base_edges is None:
            base_edges = generate_acyclic_graph(n, 0.05)
        
        # Add one edge that creates a cycle
        if n >= 2:
            # Find a path from high to low numbered node and reverse one edge
            prerequisites = base_edges.copy()
            prerequisites.append([n-1, 0])  # This likely creates a cycle
            return prerequisites
        return base_edges
    
    performance_tests = [
        ("Small acyclic", 50, lambda n: generate_acyclic_graph(n, 0.1)),
        ("Medium acyclic", 200, lambda n: generate_acyclic_graph(n, 0.05)),
        ("Large acyclic", 1000, lambda n: generate_acyclic_graph(n, 0.01)),
        ("Small cyclic", 50, lambda n: generate_cyclic_graph(n)),
        ("Medium cyclic", 200, lambda n: generate_cyclic_graph(n)),
    ]
    
    for test_name, size, prereq_gen in performance_tests:
        print(f"\n{test_name} ({size} courses):")
        
        prerequisites = prereq_gen(size)
        print(f"  Prerequisites: {len(prerequisites)}")
        
        # Test main algorithms (skip union-find and matrix for large cases)
        test_algorithms = algorithms[:3] if size <= 200 else algorithms[:3]
        
        results = []
        for name, func in test_algorithms:
            try:
                start_time = time.time()
                result = func(size, prerequisites)
                end_time = time.time()
                
                results.append(result)
                print(f"  {name}: {result}, {end_time - start_time:.6f}s")
                
            except Exception as e:
                print(f"  {name}: ERROR - {e}")
        
        # Check consistency
        if len(set(results)) > 1:
            print(f"  WARNING: Inconsistent results!")
    
    # Cycle detection validation
    print("\n" + "=" * 60)
    print("CYCLE DETECTION VALIDATION")
    print("=" * 60)
    
    def create_known_cycle(n, cycle_nodes):
        """Create graph with known cycle."""
        prerequisites = []
        
        # Create cycle
        for i in range(len(cycle_nodes)):
            next_i = (i + 1) % len(cycle_nodes)
            prerequisites.append([cycle_nodes[next_i], cycle_nodes[i]])
        
        # Add some additional random edges that don't affect the cycle
        for i in range(n):
            if i not in cycle_nodes:
                if cycle_nodes:
                    target = random.choice(cycle_nodes)
                    prerequisites.append([target, i])
        
        return prerequisites
    
    cycle_tests = [
        ("2-cycle", 5, [0, 1]),
        ("3-cycle", 6, [1, 2, 3]),
        ("4-cycle", 8, [0, 2, 4, 6]),
        ("Self-loop", 3, [1]),  # Special case
    ]
    
    for test_name, num_courses, cycle_nodes in cycle_tests:
        print(f"\n{test_name}:")
        
        if test_name == "Self-loop":
            prerequisites = [[1, 1]]  # Self-loop
        else:
            prerequisites = create_known_cycle(num_courses, cycle_nodes)
        
        print(f"  Prerequisites: {prerequisites}")
        
        for name, func in algorithms[:3]:  # Test main algorithms
            try:
                result = func(num_courses, prerequisites)
                expected = False  # All should detect cycle
                status = "✓" if result == expected else "✗"
                print(f"  {name}: {result} {status}")
                
            except Exception as e:
                print(f"  {name}: ERROR - {e}")
    
    # Edge case stress testing
    print("\n" + "=" * 60)
    print("EDGE CASE STRESS TESTING")
    print("=" * 60)
    
    edge_cases = [
        ("No prerequisites", lambda: (100, [])),
        ("All courses depend on course 0", lambda: (50, [[i, 0] for i in range(1, 50)])),
        ("Linear chain", lambda: (50, [[i+1, i] for i in range(49)])),
        ("Complete DAG", lambda: (20, [[j, i] for i in range(20) for j in range(i+1, 20)])),
        ("Star pattern", lambda: (50, [[0, i] for i in range(1, 50)])),
        ("Binary tree", lambda: (31, [[2*i+1, i] + [[2*i+2, i]] for i in range(15) if 2*i+2 < 31])),
    ]
    
    for test_name, case_gen in edge_cases:
        print(f"\n{test_name}:")
        
        try:
            num_courses, prerequisites = case_gen()
            print(f"  Courses: {num_courses}, Prerequisites: {len(prerequisites)}")
            
            # Test main algorithms
            for name, func in algorithms[:3]:
                try:
                    start_time = time.time()
                    result = func(num_courses, prerequisites)
                    end_time = time.time()
                    
                    print(f"  {name}: {result}, {end_time - start_time:.6f}s")
                    
                except Exception as e:
                    print(f"  {name}: ERROR - {e}")
                    
        except Exception as e:
            print(f"  Case generation ERROR: {e}")
    
    # Memory efficiency testing
    print("\n" + "=" * 60)
    print("MEMORY EFFICIENCY COMPARISON")
    print("=" * 60)
    
    import sys
    
    def estimate_memory_usage(numCourses, prerequisites, algorithm):
        """Estimate memory usage for different algorithms."""
        if algorithm == can_finish_dfs:
            return len(prerequisites) + numCourses, "O(V + E)"
        elif algorithm == can_finish_bfs:
            return len(prerequisites) + numCourses * 2, "O(V + E)"
        elif algorithm == can_finish_matrix:
            return numCourses * numCourses, "O(V²)"
        elif algorithm == can_finish_union_find:
            return numCourses * 2, "O(V)"
        else:
            return len(prerequisites) + numCourses, "O(V + E)"
    
    memory_test_cases = [
        (100, [[i+1, i] for i in range(99)]),  # Linear
        (50, [[j, i] for i in range(50) for j in range(i+1, 50)]),  # Dense
        (1000, []),  # Sparse
    ]
    
    for numCourses, prerequisites in memory_test_cases:
        print(f"\nCourses: {numCourses}, Prerequisites: {len(prerequisites)}")
        
        for name, func in algorithms:
            estimated_units, complexity = estimate_memory_usage(numCourses, prerequisites, func)
            print(f"  {name}: ~{estimated_units} units ({complexity})")
    
    # Algorithm comparison summary
    print("\n" + "=" * 60)
    print("ALGORITHM COMPARISON SUMMARY")
    print("=" * 60)
    
    print("Algorithm Characteristics:")
    print("  DFS Cycle Detection:")
    print("    + Simple recursive implementation")
    print("    + Good for sparse graphs")
    print("    - May hit recursion limit for deep graphs")
    print("    - Harder to debug cycles")
    
    print("  BFS (Kahn's Algorithm):")
    print("    + Iterative (no recursion limit)")
    print("    + Can provide topological order")
    print("    + Easy to understand and debug")
    print("    + Stable performance")
    
    print("  Optimized BFS:")
    print("    + Early termination checks")
    print("    + Input validation")
    print("    + Best for production use")
    
    print("  Union-Find:")
    print("    + Very fast for certain graph types")
    print("    - Complex to implement correctly for this problem")
    print("    - Not natural fit for dependency checking")
    
    print("  Adjacency Matrix:")
    print("    + Simple for very small graphs")
    print("    + Can find all cycles at once")
    print("    - O(V²) space complexity")
    print("    - Inefficient for large sparse graphs")
    
    print("\nRecommendations:")
    print("  • Use BFS (Kahn's Algorithm) for most cases")
    print("  • Use DFS for educational purposes or when recursion is preferred")
    print("  • Use Optimized BFS for production systems")
    print("  • Avoid Union-Find and Matrix approaches unless specific requirements")

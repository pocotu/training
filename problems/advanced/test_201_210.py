#!/usr/bin/env python3
"""
Comprehensive Test Suite for Advanced Problems 201-210
Phase 6 Testing Implementation
"""

import sys
import os
import time
import random
import string
from typing import List, Any, Callable, Dict, Tuple
import traceback

# Add the parent directory to path to import solutions
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Import all solution modules
try:
    from wildcard_matching.solution import *
    from trapping_rain_water.solution import *
    from n_queens.solution import *
    from course_schedule_ii.solution import *
    from implement_trie.solution import *
    from happy_number.solution import *
    from remove_linked_list_elements.solution import *
    from count_primes.solution import *
    from minimum_size_subarray_sum.solution import *
    from course_schedule.solution import *
except ImportError as e:
    print(f"Warning: Could not import some modules: {e}")
    print("Make sure all solution files are in the correct directory structure")
    # Define placeholder functions for testing
    def is_match_dp(s, p): return s == p
    def is_match_recursive(s, p): return s == p
    def is_match_iterative(s, p): return s == p
    def is_match_optimized(s, p): return s == p
    def trap_two_pointers(height): return 0
    def trap_stack(height): return 0
    def trap_dp(height): return 0
    def solve_n_queens_backtracking(n): return []
    def solve_n_queens_optimized(n): return []
    def solve_n_queens_bit_manipulation(n): return []
    def find_order_dfs(numCourses, prerequisites): return []
    def find_order_bfs_kahn(numCourses, prerequisites): return []
    def find_order_bfs_indegree(numCourses, prerequisites): return []
    def find_order_optimized(numCourses, prerequisites): return []
    class Trie:
        def __init__(self): pass
        def insert(self, word): pass
        def search(self, word): return True
        def starts_with(self, prefix): return True
    def is_happy_hash_set(n): return True
    def is_happy_floyd_cycle(n): return True
    def is_happy_mathematical(n): return True
    def is_happy_recursive(n): return True
    def is_happy_optimized(n): return True
    class ListNode:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next
    def remove_elements_iterative(head, val): return head
    def remove_elements_recursive(head, val): return head
    def remove_elements_dummy_head(head, val): return head
    def remove_elements_two_pointers(head, val): return head
    def remove_elements_optimized(head, val): return head
    def count_primes_sieve(n): return 0
    def count_primes_sieve_optimized(n): return 0
    def count_primes_segmented_sieve(n): return 0
    def count_primes_mathematical(n): return 0
    def count_primes_wheel_factorization(n): return 0
    def count_primes_parallel(n): return 0
    def min_subarray_len_sliding_window(target, nums): return 0
    def min_subarray_len_two_pointers(target, nums): return 0
    def min_subarray_len_binary_search(target, nums): return 0
    def min_subarray_len_prefix_sum(target, nums): return 0
    def min_subarray_len_optimized(target, nums): return 0
    def can_finish_dfs(numCourses, prerequisites): return True
    def can_finish_bfs_kahn(numCourses, prerequisites): return True
    def can_finish_bfs_indegree(numCourses, prerequisites): return True
    def can_finish_union_find(numCourses, prerequisites): return True
    def can_finish_optimized(numCourses, prerequisites): return True

class TestRunner:
    """Comprehensive test runner for advanced problems."""
    
    def __init__(self):
        self.total_tests = 0
        self.passed_tests = 0
        self.failed_tests = 0
        self.test_results = {}
        
    def run_test(self, test_name: str, test_func: Callable, *args, **kwargs) -> bool:
        """Run a single test and track results."""
        self.total_tests += 1
        
        try:
            start_time = time.time()
            result = test_func(*args, **kwargs)
            end_time = time.time()
            
            self.passed_tests += 1
            self.test_results[test_name] = {
                'status': 'PASSED',
                'time': end_time - start_time,
                'result': result
            }
            print(f"✓ {test_name} - PASSED ({end_time - start_time:.4f}s)")
            return True
            
        except Exception as e:
            self.failed_tests += 1
            self.test_results[test_name] = {
                'status': 'FAILED',
                'error': str(e),
                'traceback': traceback.format_exc()
            }
            print(f"✗ {test_name} - FAILED: {e}")
            return False
    
    def print_summary(self):
        """Print test summary."""
        print("\n" + "=" * 60)
        print("TEST SUMMARY")
        print("=" * 60)
        print(f"Total Tests: {self.total_tests}")
        print(f"Passed: {self.passed_tests}")
        print(f"Failed: {self.failed_tests}")
        print(f"Success Rate: {(self.passed_tests/self.total_tests)*100:.1f}%" if self.total_tests > 0 else "0%")
        
        if self.failed_tests > 0:
            print("\nFailed Tests:")
            for test_name, result in self.test_results.items():
                if result['status'] == 'FAILED':
                    print(f"  - {test_name}: {result['error']}")

def test_wildcard_matching():
    """Test wildcard matching problem (201)."""
    print("\n" + "=" * 50)
    print("TESTING PROBLEM 201: WILDCARD MATCHING")
    print("=" * 50)
    
    runner = TestRunner()
    
    # Test cases: (s, p, expected)
    test_cases = [
        ("aa", "a", False),
        ("aa", "*", True),
        ("cb", "?a", False),
        ("adceb", "*a*b*", True),
        ("acdcb", "a*c?b", False),
        ("", "*", True),
        ("", "?", False),
        ("a", "*a*", True),
        ("mississippi", "m??*ss*?i*pi", False),
        ("abcdef", "a*f", True),
    ]
    
    algorithms = [
        ("DP Bottom-up", is_match_dp),
        ("DP Top-down", is_match_recursive),
        ("Iterative", is_match_iterative),
        ("Optimized", is_match_optimized),
    ]
    
    for i, (s, p, expected) in enumerate(test_cases):
        for algo_name, algo_func in algorithms:
            test_name = f"WildcardMatch_{algo_name}_Case{i+1}"
            
            def test_func():
                result = algo_func(s, p)
                assert result == expected, f"Expected {expected}, got {result} for s='{s}', p='{p}'"
                return result
            
            runner.run_test(test_name, test_func)
    
    # Performance test
    def performance_test():
        large_s = "a" * 1000 + "b" * 1000
        large_p = "*" + "a" * 500 + "*" + "b" * 500 + "*"
        
        start_time = time.time()
        result = is_match_optimized(large_s, large_p)
        end_time = time.time()
        
        assert isinstance(result, bool), "Result should be boolean"
        assert end_time - start_time < 1.0, "Should complete within 1 second"
        return f"Performance test passed in {end_time - start_time:.4f}s"
    
    runner.run_test("WildcardMatch_Performance", performance_test)
    runner.print_summary()
    return runner

def test_trapping_rain_water():
    """Test trapping rain water problem (202)."""
    print("\n" + "=" * 50)
    print("TESTING PROBLEM 202: TRAPPING RAIN WATER")
    print("=" * 50)
    
    runner = TestRunner()
    
    # Test cases: (height, expected)
    test_cases = [
        ([0,1,0,2,1,0,1,3,2,1,2,1], 6),
        ([4,2,0,3,2,5], 9),
        ([1], 0),
        ([1,1], 0),
        ([2,1,2], 1),
        ([3,0,2,0,4], 7),
        ([0,0,0], 0),
        ([5,4,3,2,1], 0),
        ([1,2,3,4,5], 0),
        ([2,0,2], 2),
    ]
    
    algorithms = [
        ("Two Pointers", trap_two_pointers),
        ("Stack", trap_stack),
        ("DP", trap_dp),
    ]
    
    for i, (height, expected) in enumerate(test_cases):
        for algo_name, algo_func in algorithms:
            test_name = f"TrapRainWater_{algo_name}_Case{i+1}"
            
            def test_func():
                result = algo_func(height)
                assert result == expected, f"Expected {expected}, got {result} for height={height}"
                return result
            
            runner.run_test(test_name, test_func)
    
    # Edge case tests
    def edge_case_test():
        # Empty array
        assert trap_two_pointers([]) == 0
        
        # Large array
        large_height = [random.randint(0, 10) for _ in range(1000)]
        result = trap_two_pointers(large_height)
        assert result >= 0, "Water trapped should be non-negative"
        
        return "Edge cases passed"
    
    runner.run_test("TrapRainWater_EdgeCases", edge_case_test)
    runner.print_summary()
    return runner

def test_n_queens():
    """Test N-Queens problem (203)."""
    print("\n" + "=" * 50)
    print("TESTING PROBLEM 203: N-QUEENS")
    print("=" * 50)
    
    runner = TestRunner()
    
    # Test cases: (n, expected_count)
    test_cases = [
        (1, 1),
        (2, 0),
        (3, 0),
        (4, 2),
        (5, 10),
        (6, 4),
        (7, 40),
        (8, 92),
    ]
    
    algorithms = [
        ("Backtracking", solve_n_queens_backtracking),
        ("Optimized", solve_n_queens_optimized),
        ("Bit Manipulation", solve_n_queens_bit_manipulation),
    ]
    
    for i, (n, expected_count) in enumerate(test_cases):
        for algo_name, algo_func in algorithms:
            test_name = f"NQueens_{algo_name}_N{n}"
            
            def test_func():
                result = algo_func(n)
                assert len(result) == expected_count, f"Expected {expected_count} solutions, got {len(result)} for n={n}"
                
                # Validate each solution
                for solution in result:
                    assert len(solution) == n, f"Solution should have {n} rows"
                    for row in solution:
                        assert len(row) == n, f"Each row should have {n} columns"
                        assert row.count('Q') == 1, "Each row should have exactly one queen"
                
                return len(result)
            
            runner.run_test(test_name, test_func)
    
    # Performance test for reasonable size
    def performance_test():
        start_time = time.time()
        result = solve_n_queens_optimized(9)
        end_time = time.time()
        
        assert len(result) == 352, "9-queens should have 352 solutions"
        assert end_time - start_time < 5.0, "Should complete within 5 seconds"
        return f"Performance test passed in {end_time - start_time:.4f}s"
    
    runner.run_test("NQueens_Performance", performance_test)
    runner.print_summary()
    return runner

def test_course_schedule_ii():
    """Test Course Schedule II problem (204)."""
    print("\n" + "=" * 50)
    print("TESTING PROBLEM 204: COURSE SCHEDULE II")
    print("=" * 50)
    
    runner = TestRunner()
    
    # Test cases: (numCourses, prerequisites, has_valid_order)
    test_cases = [
        (2, [[1,0]], True),
        (4, [[1,0],[2,0],[3,1],[3,2]], True),
        (1, [], True),
        (2, [[1,0],[0,1]], False),  # Cycle
        (3, [[0,1],[0,2],[1,2]], True),
        (4, [[1,0],[2,1],[3,2],[1,3]], False),  # Cycle
        (0, [], True),
    ]
    
    algorithms = [
        ("DFS", find_order_dfs),
        ("BFS Kahn", find_order_bfs_kahn),
        ("BFS Indegree", find_order_bfs_indegree),
        ("Optimized", find_order_optimized),
    ]
    
    for i, (num_courses, prerequisites, has_valid_order) in enumerate(test_cases):
        for algo_name, algo_func in algorithms:
            test_name = f"CourseScheduleII_{algo_name}_Case{i+1}"
            
            def test_func():
                result = algo_func(num_courses, prerequisites)
                
                if has_valid_order:
                    assert len(result) == num_courses, f"Should return all {num_courses} courses"
                    assert len(set(result)) == num_courses, "Should return unique courses"
                    
                    # Validate topological order
                    course_position = {course: idx for idx, course in enumerate(result)}
                    for course, prereq in prerequisites:
                        assert course_position[prereq] < course_position[course], \
                            f"Prerequisite {prereq} should come before {course}"
                else:
                    assert result == [], "Should return empty list for cyclic dependencies"
                
                return len(result)
            
            runner.run_test(test_name, test_func)
    
    # Large test case
    def large_test():
        # Create a large DAG
        num_courses = 100
        prerequisites = [[i, i-1] for i in range(1, num_courses)]
        
        result = find_order_optimized(num_courses, prerequisites)
        assert len(result) == num_courses, "Should handle large input"
        
        return "Large test passed"
    
    runner.run_test("CourseScheduleII_LargeTest", large_test)
    runner.print_summary()
    return runner

def test_implement_trie():
    """Test Trie implementation problem (205)."""
    print("\n" + "=" * 50)
    print("TESTING PROBLEM 205: IMPLEMENT TRIE")
    print("=" * 50)
    
    runner = TestRunner()
    
    # Test basic functionality
    def basic_functionality_test():
        trie = Trie()
        
        # Test insert and search
        trie.insert("apple")
        assert trie.search("apple") == True
        assert trie.search("app") == False
        
        # Test starts_with
        assert trie.starts_with("app") == True
        
        # Insert another word
        trie.insert("app")
        assert trie.search("app") == True
        
        return "Basic functionality passed"
    
    runner.run_test("Trie_BasicFunctionality", basic_functionality_test)
    
    # Test edge cases
    def edge_cases_test():
        trie = Trie()
        
        # Empty string
        trie.insert("")
        assert trie.search("") == True
        
        # Single character
        trie.insert("a")
        assert trie.search("a") == True
        assert trie.starts_with("a") == True
        
        # Overlapping words
        trie.insert("abc")
        trie.insert("abcd")
        trie.insert("ab")
        
        assert trie.search("ab") == True
        assert trie.search("abc") == True
        assert trie.search("abcd") == True
        assert trie.search("abcde") == False
        assert trie.starts_with("abcd") == True
        
        return "Edge cases passed"
    
    runner.run_test("Trie_EdgeCases", edge_cases_test)
    
    # Performance test
    def performance_test():
        trie = Trie()
        
        # Insert many words
        words = [f"word{i}" for i in range(1000)]
        
        start_time = time.time()
        for word in words:
            trie.insert(word)
        insert_time = time.time() - start_time
        
        start_time = time.time()
        for word in words:
            assert trie.search(word) == True
        search_time = time.time() - start_time
        
        assert insert_time < 1.0, "Insert should be fast"
        assert search_time < 1.0, "Search should be fast"
        
        return f"Performance test passed (insert: {insert_time:.4f}s, search: {search_time:.4f}s)"
    
    runner.run_test("Trie_Performance", performance_test)
    runner.print_summary()
    return runner

def test_happy_number():
    """Test Happy Number problem (206)."""
    print("\n" + "=" * 50)
    print("TESTING PROBLEM 206: HAPPY NUMBER")
    print("=" * 50)
    
    runner = TestRunner()
    
    # Test cases: (n, expected)
    test_cases = [
        (19, True),
        (2, False),
        (1, True),
        (7, True),
        (10, True),
        (13, True),
        (23, True),
        (28, True),
        (44, True),
        (82, True),
        (3, False),
        (4, False),
        (5, False),
        (6, False),
        (8, False),
        (9, False),
    ]
    
    algorithms = [
        ("Hash Set", is_happy_hash_set),
        ("Floyd Cycle", is_happy_floyd_cycle),
        ("Mathematical", is_happy_mathematical),
        ("Recursive", is_happy_recursive),
        ("Optimized", is_happy_optimized),
    ]
    
    for i, (n, expected) in enumerate(test_cases):
        for algo_name, algo_func in algorithms:
            test_name = f"HappyNumber_{algo_name}_N{n}"
            
            def test_func():
                result = algo_func(n)
                assert result == expected, f"Expected {expected}, got {result} for n={n}"
                return result
            
            runner.run_test(test_name, test_func)
    
    # Large number test
    def large_number_test():
        large_n = 999999999
        result = is_happy_optimized(large_n)
        assert isinstance(result, bool), "Should return boolean"
        
        return f"Large number test passed for n={large_n}"
    
    runner.run_test("HappyNumber_LargeNumber", large_number_test)
    runner.print_summary()
    return runner

def test_remove_linked_list_elements():
    """Test Remove Linked List Elements problem (207)."""
    print("\n" + "=" * 50)
    print("TESTING PROBLEM 207: REMOVE LINKED LIST ELEMENTS")
    print("=" * 50)
    
    runner = TestRunner()
    
    def list_to_array(head):
        """Convert linked list to array for comparison."""
        result = []
        current = head
        while current:
            result.append(current.val)
            current = current.next
        return result
    
    def array_to_list(arr):
        """Convert array to linked list."""
        if not arr:
            return None
        
        head = ListNode(arr[0])
        current = head
        for val in arr[1:]:
            current.next = ListNode(val)
            current = current.next
        return head
    
    # Test cases: (input_array, val, expected_array)
    test_cases = [
        ([1,2,6,3,4,5,6], 6, [1,2,3,4,5]),
        ([], 1, []),
        ([7,7,7,7], 7, []),
        ([1,2,3], 4, [1,2,3]),
        ([1], 1, []),
        ([1,1], 1, []),
        ([1,2,2,3,3,3], 3, [1,2,2]),
    ]
    
    algorithms = [
        ("Iterative", remove_elements_iterative),
        ("Recursive", remove_elements_recursive),
        ("Dummy Head", remove_elements_dummy_head),
        ("Two Pointers", remove_elements_two_pointers),
        ("Optimized", remove_elements_optimized),
    ]
    
    for i, (input_arr, val, expected_arr) in enumerate(test_cases):
        for algo_name, algo_func in algorithms:
            test_name = f"RemoveElements_{algo_name}_Case{i+1}"
            
            def test_func():
                head = array_to_list(input_arr)
                result_head = algo_func(head, val)
                result_arr = list_to_array(result_head)
                
                assert result_arr == expected_arr, \
                    f"Expected {expected_arr}, got {result_arr} for input={input_arr}, val={val}"
                
                return result_arr
            
            runner.run_test(test_name, test_func)
    
    # Large list test
    def large_list_test():
        # Create large list with pattern
        large_input = [1, 2] * 5000 + [3] * 1000
        head = array_to_list(large_input)
        
        start_time = time.time()
        result_head = remove_elements_optimized(head, 3)
        end_time = time.time()
        
        result_arr = list_to_array(result_head)
        expected_length = 10000  # Only 1s and 2s remain
        
        assert len(result_arr) == expected_length, f"Expected length {expected_length}, got {len(result_arr)}"
        assert all(val in [1, 2] for val in result_arr), "Should only contain 1s and 2s"
        assert end_time - start_time < 1.0, "Should complete within 1 second"
        
        return f"Large list test passed in {end_time - start_time:.4f}s"
    
    runner.run_test("RemoveElements_LargeList", large_list_test)
    runner.print_summary()
    return runner

def test_count_primes():
    """Test Count Primes problem (208)."""
    print("\n" + "=" * 50)
    print("TESTING PROBLEM 208: COUNT PRIMES")
    print("=" * 50)
    
    runner = TestRunner()
    
    # Test cases: (n, expected)
    test_cases = [
        (10, 4),   # 2, 3, 5, 7
        (0, 0),
        (1, 0),
        (2, 0),
        (3, 1),    # 2
        (5, 2),    # 2, 3
        (20, 8),   # 2, 3, 5, 7, 11, 13, 17, 19
        (100, 25),
        (1000, 168),
    ]
    
    algorithms = [
        ("Sieve Basic", count_primes_sieve),
        ("Sieve Optimized", count_primes_sieve_optimized),
        ("Segmented Sieve", count_primes_segmented_sieve),
        ("Mathematical", count_primes_mathematical),
        ("Wheel Factorization", count_primes_wheel_factorization),
        ("Parallel", count_primes_parallel),
    ]
    
    for i, (n, expected) in enumerate(test_cases):
        for algo_name, algo_func in algorithms:
            test_name = f"CountPrimes_{algo_name}_N{n}"
            
            def test_func():
                result = algo_func(n)
                assert result == expected, f"Expected {expected}, got {result} for n={n}"
                return result
            
            runner.run_test(test_name, test_func)
    
    # Performance test
    def performance_test():
        large_n = 100000
        
        start_time = time.time()
        result = count_primes_sieve_optimized(large_n)
        end_time = time.time()
        
        assert result > 0, "Should find primes"
        assert end_time - start_time < 3.0, "Should complete within 3 seconds"
        
        return f"Performance test passed for n={large_n} in {end_time - start_time:.4f}s"
    
    runner.run_test("CountPrimes_Performance", performance_test)
    runner.print_summary()
    return runner

def test_minimum_size_subarray_sum():
    """Test Minimum Size Subarray Sum problem (209)."""
    print("\n" + "=" * 50)
    print("TESTING PROBLEM 209: MINIMUM SIZE SUBARRAY SUM")
    print("=" * 50)
    
    runner = TestRunner()
    
    # Test cases: (target, nums, expected)
    test_cases = [
        (7, [2,3,1,2,4,3], 2),
        (4, [1,4,4], 1),
        (11, [1,1,1,1,1,1,1,1], 0),
        (15, [1,2,3,4,5], 5),
        (3, [1,1,1,1], 0),
        (6, [10,2,3], 1),
        (5, [2,3,1,1,1,1,1], 2),
        (1, [1], 1),
        (100, [1,2,3], 0),
    ]
    
    algorithms = [
        ("Sliding Window", min_subarray_len_sliding_window),
        ("Two Pointers", min_subarray_len_two_pointers),
        ("Binary Search", min_subarray_len_binary_search),
        ("Prefix Sum", min_subarray_len_prefix_sum),
        ("Optimized", min_subarray_len_optimized),
    ]
    
    for i, (target, nums, expected) in enumerate(test_cases):
        for algo_name, algo_func in algorithms:
            test_name = f"MinSubarraySum_{algo_name}_Case{i+1}"
            
            def test_func():
                result = algo_func(target, nums)
                assert result == expected, \
                    f"Expected {expected}, got {result} for target={target}, nums={nums}"
                return result
            
            runner.run_test(test_name, test_func)
    
    # Large array test
    def large_array_test():
        target = 1000000
        nums = list(range(1, 2001))  # [1, 2, 3, ..., 2000]
        
        start_time = time.time()
        result = min_subarray_len_optimized(target, nums)
        end_time = time.time()
        
        # Verify result manually
        expected = 0  # Sum from 1 to 2000 is much larger than target
        for i in range(len(nums)):
            current_sum = 0
            for j in range(i, len(nums)):
                current_sum += nums[j]
                if current_sum >= target:
                    if expected == 0 or j - i + 1 < expected:
                        expected = j - i + 1
                    break
        
        assert result == expected, f"Expected {expected}, got {result}"
        assert end_time - start_time < 1.0, "Should complete within 1 second"
        
        return f"Large array test passed in {end_time - start_time:.4f}s"
    
    runner.run_test("MinSubarraySum_LargeArray", large_array_test)
    runner.print_summary()
    return runner

def test_course_schedule():
    """Test Course Schedule problem (210)."""
    print("\n" + "=" * 50)
    print("TESTING PROBLEM 210: COURSE SCHEDULE")
    print("=" * 50)
    
    runner = TestRunner()
    
    # Test cases: (numCourses, prerequisites, expected)
    test_cases = [
        (2, [[1,0]], True),
        (2, [[1,0],[0,1]], False),
        (1, [], True),
        (3, [[0,1],[0,2],[1,2]], True),
        (4, [[0,1],[1,2],[2,3],[3,1]], False),  # Cycle
        (5, [[1,4],[2,4],[3,1],[3,2]], True),
        (0, [], True),
        (20, [[0,10],[3,18],[5,5],[6,11],[11,14],[13,1],[15,1],[17,4]], False),  # Self-loop
    ]
    
    algorithms = [
        ("DFS", can_finish_dfs),
        ("BFS Kahn", can_finish_bfs_kahn),
        ("BFS Indegree", can_finish_bfs_indegree),
        ("Union Find", can_finish_union_find),
        ("Optimized", can_finish_optimized),
    ]
    
    for i, (num_courses, prerequisites, expected) in enumerate(test_cases):
        for algo_name, algo_func in algorithms:
            test_name = f"CourseSchedule_{algo_name}_Case{i+1}"
            
            def test_func():
                result = algo_func(num_courses, prerequisites)
                assert result == expected, \
                    f"Expected {expected}, got {result} for numCourses={num_courses}, prerequisites={prerequisites}"
                return result
            
            runner.run_test(test_name, test_func)
    
    # Stress test with large graph
    def stress_test():
        num_courses = 1000
        # Create a large DAG (no cycles)
        prerequisites = [[i, i-1] for i in range(1, num_courses)]
        
        start_time = time.time()
        result = can_finish_optimized(num_courses, prerequisites)
        end_time = time.time()
        
        assert result == True, "Large DAG should be completable"
        assert end_time - start_time < 2.0, "Should complete within 2 seconds"
        
        return f"Stress test passed in {end_time - start_time:.4f}s"
    
    runner.run_test("CourseSchedule_StressTest", stress_test)
    runner.print_summary()
    return runner

def main():
    """Run all tests for problems 201-210."""
    print("=" * 80)
    print("COMPREHENSIVE TEST SUITE FOR ADVANCED PROBLEMS 201-210")
    print("Phase 6 Testing Implementation")
    print("=" * 80)
    
    overall_runner = TestRunner()
    
    # Run all test functions
    test_functions = [
        test_wildcard_matching,
        test_trapping_rain_water,
        test_n_queens,
        test_course_schedule_ii,
        test_implement_trie,
        test_happy_number,
        test_remove_linked_list_elements,
        test_count_primes,
        test_minimum_size_subarray_sum,
        test_course_schedule,
    ]
    
    test_results = []
    
    for test_func in test_functions:
        try:
            result = test_func()
            test_results.append(result)
            overall_runner.total_tests += result.total_tests
            overall_runner.passed_tests += result.passed_tests
            overall_runner.failed_tests += result.failed_tests
        except Exception as e:
            print(f"\nERROR running {test_func.__name__}: {e}")
            overall_runner.failed_tests += 1
    
    # Print overall summary
    print("\n" + "=" * 80)
    print("OVERALL TEST SUMMARY FOR PROBLEMS 201-210")
    print("=" * 80)
    print(f"Total Tests Run: {overall_runner.total_tests}")
    print(f"Total Passed: {overall_runner.passed_tests}")
    print(f"Total Failed: {overall_runner.failed_tests}")
    
    if overall_runner.total_tests > 0:
        success_rate = (overall_runner.passed_tests / overall_runner.total_tests) * 100
        print(f"Overall Success Rate: {success_rate:.1f}%")
        
        if success_rate >= 95:
            print("🎉 EXCELLENT: All problems are working correctly!")
        elif success_rate >= 85:
            print("✅ GOOD: Most problems are working correctly")
        elif success_rate >= 70:
            print("⚠️  WARNING: Some problems need attention")
        else:
            print("❌ CRITICAL: Many problems have issues")
    
    # Problem-specific summary
    print("\nProblem-Specific Results:")
    problem_names = [
        "201: Wildcard Matching",
        "202: Trapping Rain Water", 
        "203: N-Queens",
        "204: Course Schedule II",
        "205: Implement Trie",
        "206: Happy Number",
        "207: Remove Linked List Elements",
        "208: Count Primes",
        "209: Minimum Size Subarray Sum",
        "210: Course Schedule",
    ]
    
    for i, (name, result) in enumerate(zip(problem_names, test_results)):
        if i < len(test_results):
            status = "✅" if result.failed_tests == 0 else "❌"
            print(f"  {status} {name}: {result.passed_tests}/{result.total_tests} tests passed")
    
    print("\n" + "=" * 80)
    print("Testing completed for Advanced Problems 201-210")
    print("=" * 80)

if __name__ == "__main__":
    main()

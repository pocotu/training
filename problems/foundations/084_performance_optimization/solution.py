"""
Solution for Performance Optimization
Problem ID: F084
"""

import time
import functools
from collections import defaultdict

def measure_execution_time(func):
    # TODO: Implement your solution here
    pass

def memoize(func):
    cache = {}
    
    @functools.wraps(func)
    def wrapper(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result
    return wrapper

@memoize
def fibonacci_optimized(n):
    if n <= 1:
        return n
    return fibonacci_optimized(n - 1) + fibonacci_optimized(n - 2)

def fibonacci_naive(n):
    if n <= 1:
        return n
    return fibonacci_naive(n - 1) + fibonacci_naive(n - 2)

def list_comprehension_vs_loop(data):
    # List comprehension
    start_time = time.time()
    result1 = [x * 2 for x in data if x % 2 == 0]
    lc_time = time.time() - start_time
    
    # Traditional loop
    start_time = time.time()
    result2 = []
    for x in data:
        if x % 2 == 0:
            result2.append(x * 2)
    loop_time = time.time() - start_time
    
    return {
        "list_comprehension_time": lc_time,
        "loop_time": loop_time,
        "speedup": loop_time / lc_time if lc_time > 0 else 1,
        "results_equal": result1 == result2
    }

def optimize_data_structure_access(data_size=1000):
    # Create test data
    test_data = list(range(data_size))
    
    # List lookup
    start_time = time.time()
    for i in range(100):
        _ = data_size // 2 in test_data
    list_time = time.time() - start_time
    
    # Set lookup
    test_set = set(test_data)
    start_time = time.time()
    for i in range(100):
        _ = data_size // 2 in test_set
    set_time = time.time() - start_time
    
    # Dict lookup
    test_dict = {x: True for x in test_data}
    start_time = time.time()
    for i in range(100):
        _ = data_size // 2 in test_dict
    dict_time = time.time() - start_time
    
    return {
        "list_time": list_time,
        "set_time": set_time,
        "dict_time": dict_time,
        "set_speedup": list_time / set_time if set_time > 0 else 1
    }

def memory_efficient_processing(data):
    """
    Demonstrate memory-efficient data processing using generators.
    Args:
        data (list): input data
    Returns:
        dict: processing results
    """
    # Generator approach (memory efficient)
    def process_generator(data):
        for item in data:
            if item % 2 == 0:
                yield item * item
    
    # List approach (memory intensive)
    def process_list(data):
        return [item * item for item in data if item % 2 == 0]
    
    # Compare approaches
    gen_result = list(process_generator(data))
    list_result = process_list(data)
    
    return {
        "generator_result": gen_result[:10],  # Show first 10 for display
        "list_result": list_result[:10],
        "results_equal": gen_result == list_result,
        "total_results": len(gen_result)
    }

@measure_execution_time
def performance_test_suite():
    """
    Run comprehensive performance tests.
    Returns:
        dict: test results
    """
    print("Running performance optimization tests...")
    
    # Test data
    large_data = list(range(10000))
    
    # Test 1: Data structure comparison
    ds_results = optimize_data_structure_access(1000)
    print(f"Set lookup is {ds_results['set_speedup']:.2f}x faster than list lookup")
    
    # Test 2: List comprehension vs loop
    lc_results = list_comprehension_vs_loop(large_data)
    print(f"List comprehension is {lc_results['speedup']:.2f}x faster than loop")
    
    # Test 3: Memory efficient processing
    mem_results = memory_efficient_processing(large_data)
    print(f"Processed {mem_results['total_results']} items efficiently")
    
    return {
        "data_structure_test": ds_results,
        "list_comprehension_test": lc_results,
        "memory_efficiency_test": mem_results
    }

def main():
    """
    Función principal para 084_performance_optimization
    """
    print("Performance Optimization Examples:")
    
    # Run performance tests
    results = performance_test_suite()
    
    # Test memoized Fibonacci
    print("\nTesting optimized Fibonacci:")
    result = fibonacci_optimized(10)
    print(f"Fibonacci(10) = {result}")
    
    return True

if __name__ == "__main__":
    result = main()
    print(f"Resultado: {result}")

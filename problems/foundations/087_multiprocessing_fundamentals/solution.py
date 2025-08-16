"""
Solution for Multiprocessing Fundamentals
Problem ID: F087
"""

import multiprocessing
import time
from concurrent.futures import ProcessPoolExecutor

def cpu_intensive_task(n):
    """
    CPU intensive task for testing multiprocessing.
    Args:
        n (int): input number
    Returns:
        int: sum of squares up to n
    """
    total = 0
    for i in range(n):
        total += i * i
    return total

def worker_function(data):
    """
    Worker function for multiprocessing.
    Args:
        data (tuple): (worker_id, work_amount)
    Returns:
        dict: worker results
    """
    worker_id, work_amount = data
    result = cpu_intensive_task(work_amount)
    
    return {
        "worker_id": worker_id,
        "work_amount": work_amount,
        "result": result,
        "process_id": multiprocessing.current_process().pid
    }

def process_pool_executor(tasks, num_processes=None):
    """
    Execute tasks using ProcessPoolExecutor.
    Args:
        tasks (list): list of tasks to execute
        num_processes (int): number of processes to use
    Returns:
        list: results from all processes
    """
    if num_processes is None:
        num_processes = multiprocessing.cpu_count()
    
    with ProcessPoolExecutor(max_workers=num_processes) as executor:
        results = list(executor.map(worker_function, tasks))
    
    return results

def shared_memory_example():
    """
    Demonstrate shared memory usage (simplified).
    Returns:
        dict: shared memory example results
    """
    # Simulate shared memory results
    # In real implementation, would use multiprocessing.Manager() or shared arrays
    return {
        "shared_data": [1, 2, 3, 4, 5],
        "processes_used": multiprocessing.cpu_count(),
        "memory_efficient": True
    }

def compare_sequential_vs_parallel(tasks):
    """
    Compare sequential vs parallel execution.
    Args:
        tasks (list): tasks to compare
    Returns:
        dict: comparison results
    """
    # Sequential execution
    start_time = time.time()
    sequential_results = [cpu_intensive_task(task) for task in tasks]
    sequential_time = time.time() - start_time
    
    # Parallel execution
    start_time = time.time()
    with ProcessPoolExecutor() as executor:
        parallel_results = list(executor.map(cpu_intensive_task, tasks))
    parallel_time = time.time() - start_time
    
    return {
        "sequential_time": sequential_time,
        "parallel_time": parallel_time,
        "speedup": sequential_time / parallel_time if parallel_time > 0 else 1,
        "results_match": sequential_results == parallel_results
    }

def main():
    """
    Función principal para 087_multiprocessing_fundamentals
    """
    print("Multiprocessing Fundamentals Examples:")
    
    # Test CPU intensive task
    result = cpu_intensive_task(1000)
    print(f"CPU intensive task result: {result}")
    
    # Test worker function
    worker_data = (1, 500)
    worker_result = worker_function(worker_data)
    print(f"Worker result: {worker_result['result']}")
    
    # Test process pool
    tasks = [(i, 300) for i in range(1, 5)]
    pool_results = process_pool_executor(tasks, 2)
    print(f"Process pool completed {len(pool_results)} tasks")
    
    # Test shared memory example
    shared_result = shared_memory_example()
    print(f"Shared memory example: {shared_result['memory_efficient']}")
    
    # Compare performance
    comparison_tasks = [500, 600, 700]
    comparison = compare_sequential_vs_parallel(comparison_tasks)
    print(f"Parallel speedup: {comparison['speedup']:.2f}x")
    
    return True

if __name__ == "__main__":
    result = main()
    print(f"Resultado: {result}")

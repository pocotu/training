"""
Solution for Multithreading Basics
Problem ID: F086
"""

import threading
import time
from concurrent.futures import ThreadPoolExecutor

class ThreadSafeCounter:
    """
    Contador thread-safe usando Lock
    """
    def __init__(self):
        """
        Constructor del contador thread-safe
        """
        self._value = 0
        self._lock = threading.Lock()
    
    def increment(self):
        """
        Incrementa el contador de manera thread-safe
        """
        with self._lock:
            self._value += 1
    
    def get_value(self):
        """
        Obtiene el valor actual del contador
        Returns:
            int: valor actual del contador
        """
        with self._lock:
            return self._value

def parallel_task_execution(tasks, num_threads):
    """
    Ejecuta tareas en paralelo usando ThreadPoolExecutor
    Args:
        tasks (list): lista de valores para procesar
        num_threads (int): número de threads a usar
    Returns:
        list: resultados de las tareas procesadas
    """
    def square_task(x):
        """Simple task that squares a number."""
        return x * x
    
    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        results = list(executor.map(square_task, tasks))
    
    return results

def thread_safe_counter():
    """
    Retorna una nueva instancia del contador thread-safe
    Returns:
        ThreadSafeCounter: instancia del contador
    """
    return ThreadSafeCounter()

def worker_pool_example(tasks, num_workers=4):
    """
    Ejemplo de pool de workers
    Args:
        tasks (list): tareas a procesar
        num_workers (int): número de workers
    Returns:
        list: resultados del procesamiento
    """
    def worker_task(task_data):
        """Worker task that processes task data."""
        time.sleep(0.01)  # Simulate work
        return f"Processed {task_data}"
    
    # Si tasks es un número, crear lista de tareas
    if isinstance(tasks, int):
        task_list = list(range(1, tasks + 1))
    else:
        task_list = tasks
    
    with ThreadPoolExecutor(max_workers=num_workers) as executor:
        results = list(executor.map(worker_task, task_list))
    
    return results

def main():
    """
    Función principal para 086_multithreading_basics
    """
    print("Multithreading Basics Examples:")
    
    # Test thread-safe counter
    counter = thread_safe_counter()
    counter.increment()
    counter.increment()
    print(f"Counter value: {counter.get_value()}")
    
    # Test parallel task execution
    tasks = [1, 2, 3, 4]
    results = parallel_task_execution(tasks, 2)
    print(f"Parallel results: {results}")
    
    # Test worker pool
    test_tasks = ["task1", "task2", "task3"]
    pool_results = worker_pool_example(test_tasks, 2)
    print(f"Worker pool completed {len(pool_results)} tasks")
    
    return True

if __name__ == "__main__":
    result = main()
    print(f"Resultado: {result}")

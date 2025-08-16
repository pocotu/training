import unittest
import time
import threading
from solution import parallel_task_execution, thread_safe_counter, worker_pool_example, ThreadSafeCounter

class TestMultithreadingBasics(unittest.TestCase):
    
    def test_thread_safe_counter_basic(self):
        """Test contador thread-safe básico"""
        counter = thread_safe_counter()
        self.assertIsInstance(counter, ThreadSafeCounter)
        self.assertEqual(counter.get_value(), 0)
        
        counter.increment()
        self.assertEqual(counter.get_value(), 1)
    
    def test_thread_safe_counter_multiple_threads(self):
        """Test contador con múltiples threads"""
        counter = thread_safe_counter()
        threads = []
        
        def increment_multiple():
            for _ in range(100):
                counter.increment()
        
        # Crear 10 threads que incrementen 100 veces cada uno
        for _ in range(10):
            thread = threading.Thread(target=increment_multiple)
            threads.append(thread)
            thread.start()
        
        # Esperar que todos terminen
        for thread in threads:
            thread.join()
        
        # El resultado debe ser exactamente 1000 (thread-safe)
        self.assertEqual(counter.get_value(), 1000)
    
    def test_parallel_task_execution(self):
        """Test ejecución paralela de tareas"""
        def square(x):
            time.sleep(0.1)  # Simular trabajo
            return x ** 2
        
        tasks = [1, 2, 3, 4]
        start_time = time.time()
        results = parallel_task_execution(tasks, 2)
        end_time = time.time()
        
        self.assertEqual(sorted(results), [1, 4, 9, 16])
        # Debe ser más rápido que ejecución secuencial
        self.assertLess(end_time - start_time, 0.3)  # Menos de 0.3s vs 0.4s secuencial
    
    def test_worker_pool_example(self):
        """Test pool de workers"""
        data = ["test1", "test2", "test3", "test4"]
        results = worker_pool_example(data)
        
        self.assertIsInstance(results, list)
        self.assertEqual(len(results), len(data))
        
        # Verificar que los datos fueron procesados
        for result in results:
            self.assertIsNotNone(result)
    
    def test_parallel_vs_sequential_performance(self):
        """Test diferencia de rendimiento paralelo vs secuencial"""
        def slow_task(x):
            time.sleep(0.05)
            return x * 2
        
        tasks = [1, 2, 3, 4, 5, 6]
        
        # Tiempo secuencial (aproximado)
        sequential_time = len(tasks) * 0.05
        
        # Tiempo paralelo
        start_time = time.time()
        results = parallel_task_execution(tasks, 3)
        parallel_time = time.time() - start_time
        
        self.assertEqual(len(results), len(tasks))
        # El tiempo paralelo debe ser significativamente menor
        self.assertLess(parallel_time, sequential_time * 0.8)

if __name__ == '__main__':
    unittest.main()

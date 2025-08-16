# [F086] Multithreading Basics

## Problema

Implementa tres funciones que demuestran conceptos básicos de multithreading:

1. `parallel_task_execution(tasks, num_threads)` - ejecuta tareas en paralelo
2. `thread_safe_counter()` - contador thread-safe con lock
3. `worker_pool_example(data_list)` - procesa datos usando ThreadPoolExecutor

## Ejemplos

### Función parallel_task_execution:
```python
def slow_task(n):
    time.sleep(1)
    return n ** 2

tasks = [1, 2, 3, 4, 5]
results = parallel_task_execution(tasks, 3)
print(results)  # [1, 4, 9, 16, 25] - en ~2 segundos en lugar de 5
```

### Función thread_safe_counter:
```python
counter = thread_safe_counter()
# Usar en múltiples threads sin race conditions
counter.increment()  # Thread-safe
counter.get_value()  # Thread-safe
```

### Función worker_pool_example:
```python
data = ["file1.txt", "file2.txt", "file3.txt"]
results = worker_pool_example(data)
print(results)  # Procesamiento paralelo de archivos
```

## Restricciones
- Usar threading module y ThreadPoolExecutor
- thread_safe_counter debe usar Lock para sincronización
- parallel_task_execution debe manejar excepciones en threads
- worker_pool_example debe usar with statement para pool cleanup
- Demostrar diferencia de rendimiento vs ejecución secuencial

## Conceptos a Practicar
- Threading module básico
- ThreadPoolExecutor para pools de threads
- Locks para thread safety
- Manejo de resultados concurrentes

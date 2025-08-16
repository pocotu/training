# [F087] Multiprocessing Fundamentals

## Problema

Implementa tres funciones que demuestran conceptos de multiprocessing:

1. `cpu_intensive_task(numbers)` - procesa números usando múltiples procesos
2. `process_pool_executor(data, func)` - ejecuta función en pool de procesos
3. `shared_memory_example()` - demuestra comunicación entre procesos

## Ejemplos

### Función cpu_intensive_task:
```python
def is_prime(n):
    # CPU-intensive function
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True

numbers = [982451653, 982451654, 982451655, 982451656]
results = cpu_intensive_task(numbers)
print(results)  # [True, False, False, False] - usando múltiples cores
```

### Función process_pool_executor:
```python
data = [1, 4, 9, 16, 25]
results = process_pool_executor(data, lambda x: x ** 0.5)
print(results)  # [1.0, 2.0, 3.0, 4.0, 5.0]
```

### Función shared_memory_example:
```python
# Demuestra Queue, Pipe o Value para comunicación
result = shared_memory_example()
print(result)  # Datos compartidos entre procesos
```

## Restricciones
- Usar multiprocessing module
- process_pool_executor debe usar ProcessPoolExecutor
- shared_memory_example debe usar Queue o Pipe
- Demostrar ventaja en tareas CPU-intensivas
- Manejar serialización de datos correctamente

## Conceptos a Practicar
- Multiprocessing vs multithreading
- ProcessPoolExecutor
- Comunicación inter-proceso
- CPU-bound vs I/O-bound tasks

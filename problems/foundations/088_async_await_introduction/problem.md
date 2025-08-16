# [F088] Async Await Introduction

## Problema

Implementa tres funciones asíncronas que demuestran programación async/await:

1. `async_fetch_data(urls)` - simula fetch de múltiples URLs concurrentemente
2. `async_file_processor(filenames)` - procesa archivos de manera asíncrona
3. `async_producer_consumer()` - patrón productor-consumidor con asyncio

## Ejemplos

### Función async_fetch_data:
```python
import asyncio

urls = ["http://api1.com", "http://api2.com", "http://api3.com"]
results = asyncio.run(async_fetch_data(urls))
print(results)  # Datos de todas las URLs concurrentemente
```

### Función async_file_processor:
```python
files = ["file1.txt", "file2.txt", "file3.txt"]
results = asyncio.run(async_file_processor(files))
print(results)  # Contenido procesado de todos los archivos
```

### Función async_producer_consumer:
```python
result = asyncio.run(async_producer_consumer())
print(result)  # Resultados del patrón productor-consumidor
```

## Restricciones
- Usar async/await syntax
- async_fetch_data debe usar aiohttp o simular requests
- async_file_processor debe usar aiofiles o async file handling
- async_producer_consumer debe usar asyncio.Queue
- Demostrar concurrencia real (no secuencial)
- Usar asyncio.gather() para ejecutar tareas concurrentemente

## Conceptos a Practicar
- Async/await syntax
- Event loop básico
- Concurrencia vs paralelismo
- asyncio.gather() y asyncio.Queue

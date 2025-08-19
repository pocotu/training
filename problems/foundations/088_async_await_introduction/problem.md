# [F088] String Manipulation Advanced

## Problema

Implementa tres funciones para manipulación avanzada de strings:

1. `remove_duplicates_string(text)` - elimina caracteres duplicados consecutivos
2. `compress_string(text)` - comprime string usando conteo (ej: "aaa" → "a3")  
3. `expand_string(compressed)` - expande string comprimido de vuelta

**Foundations**: Se enfoca en algoritmos de procesamiento de strings, conceptos fundamentales.

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

# [F084] Performance Optimization

## Problema

Implementa tres funciones que demuestran técnicas de optimización:
1. `slow_fibonacci(n)` y `fast_fibonacci(n)` - compara recursivo vs memoización
2. `profile_function(func, *args)` - mide tiempo y memoria de ejecución
3. `optimize_data_processing(data_list)` - optimiza procesamiento de datos

## Ejemplos

### Funciones fibonacci:
```
Input: slow_fibonacci(10), fast_fibonacci(10)
Output: (55, 55)  # mismo resultado, diferente velocidad
```

### Función profile_function:
```
Input: profile_function(sum, [1, 2, 3, 4, 5])
Output: {"result": 15, "time_seconds": 0.001, "memory_mb": 0.1}
```

### Función optimize_data_processing:
```
Input: optimize_data_processing([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
Output: [2, 8, 18, 32, 50]  # cuadrados de números pares, optimizado
```

## Restricciones
- slow_fibonacci debe usar recursión pura
- fast_fibonacci debe usar memoización (lru_cache o dict)
- profile_function debe medir tiempo real y uso aproximado de memoria
- optimize_data_processing debe usar técnicas eficientes (comprensiones, generadores)
- Comparar complejidades temporales en comentarios

## Conceptos a Practicar
- Análisis de complejidad temporal y espacial
- Técnicas de memoización
- Profiling y benchmarking
- Optimización de algoritmos y estructuras de datos

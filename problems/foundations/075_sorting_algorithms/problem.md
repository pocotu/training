# [F075] Algorithm Implementation - Sorting

## Problema

Implementa dos algoritmos de ordenamiento básicos:
1. `insertion_sort(arr)` - ordena usando insertion sort
2. `selection_sort(arr)` - ordena usando selection sort
3. `compare_algorithms(arr)` - compara tiempo de ejecución de ambos

## Ejemplos

### Función insertion_sort:
```
Input: insertion_sort([64, 34, 25, 12, 22, 11, 90])
Output: [11, 12, 22, 25, 34, 64, 90]
```

### Función selection_sort:
```
Input: selection_sort([64, 34, 25, 12, 22, 11, 90])
Output: [11, 12, 22, 25, 34, 64, 90]
```

### Función compare_algorithms:
```
Input: compare_algorithms([5, 2, 8, 1, 9])
Output: {"insertion_sort": 0.001, "selection_sort": 0.002}
```

## Restricciones
- Implementar los algoritmos desde cero (no usar sorted())
- Los algoritmos deben modificar el array in-place
- compare_algorithms debe retornar diccionario con tiempos en segundos
- Usar time.time() para medir rendimiento

## Conceptos a Practicar
- Algoritmos de ordenamiento
- Análisis de complejidad
- Medición de rendimiento
- Manipulación de listas in-place

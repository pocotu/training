# [F075] Simple Sorting

## Problema

Escribe una función llamada `simple_sort` que reciba una lista de números `numbers` y devuelva una nueva lista con los elementos ordenados de menor a mayor usando el algoritmo de ordenamiento burbuja (bubble sort) manual.

**Simplificado para Foundations**: Se enfoca en implementar un algoritmo básico de ordenamiento, sin comparaciones de rendimiento.

## Ejemplos

### Ejemplo 1:
```
Input: simple_sort([64, 34, 25, 12, 22])
Output: [12, 22, 25, 34, 64]
```

### Ejemplo 2:
```
Input: simple_sort([5, 2, 8, 1])
Output: [1, 2, 5, 8]
```

### Ejemplo 3:
```
Input: simple_sort([])
Output: []
```

## Restricciones

- `numbers` será una lista de números enteros
- Implementar algoritmo bubble sort manualmente (no usar sort() ni sorted())
- Devolver nueva lista sin modificar la original
- Manejar lista vacía correctamente
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

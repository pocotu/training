# [038] Pascal's Triangle II

## Problema

Dado un índice de fila `rowIndex`, devuelve la fila `rowIndex` del triángulo de Pascal.

En el triángulo de Pascal, cada número es la suma de los dos números directamente encima de él.

## Input/Output
- **Input**: `rowIndex` - índice de la fila (0-indexado)
- **Output**: Lista representando la fila rowIndex

## Constraints
- 0 ≤ rowIndex ≤ 33

## Ejemplos

### Ejemplo 1:
```
Input: rowIndex = 3
Output: [1,3,3,1]
```

### Ejemplo 2:
```
Input: rowIndex = 0
Output: [1]
```

### Ejemplo 3:
```
Input: rowIndex = 1
Output: [1,1]
```

## Tags
array, dynamic-programming

## Notas Adicionales
- **Complejidad de tiempo esperada**: O(rowIndex²)
- **Complejidad de espacio esperada**: O(rowIndex)
- **Conceptos clave**: Optimización de espacio, Pascal's Triangle
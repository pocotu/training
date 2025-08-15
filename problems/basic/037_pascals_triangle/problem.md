# [037] Pascal's Triangle

## Problema

Dado un entero `numRows`, devuelve las primeras numRows del triángulo de Pascal.

En el triángulo de Pascal, cada número es la suma de los dos números directamente encima de él.

## Input/Output
- **Input**: `numRows` - número de filas
- **Output**: Lista de listas representando el triángulo de Pascal

## Constraints
- 1 ≤ numRows ≤ 30

## Ejemplos

### Ejemplo 1:
```
Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
```

### Ejemplo 2:
```
Input: numRows = 1
Output: [[1]]
```

## Tags
array, dynamic-programming

## Notas Adicionales
- **Complejidad de tiempo esperada**: O(numRows²)
- **Complejidad de espacio esperada**: O(numRows²)
- **Conceptos clave**: Triángulo de Pascal, programación dinámica
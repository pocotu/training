# [F068] Matrix Operations

## Problema

Implementa tres funciones básicas para operar con matrices (listas de listas):
1. `matrix_add(matrix1, matrix2)` - suma dos matrices
2. `matrix_transpose(matrix)` - transpone una matriz
3. `matrix_diagonal_sum(matrix)` - calcula la suma de la diagonal principal

## Ejemplos

### Función matrix_add:
```
Input: 
matrix1 = [[1, 2], [3, 4]]
matrix2 = [[5, 6], [7, 8]]
Output: [[6, 8], [10, 12]]
```

### Función matrix_transpose:
```
Input: [[1, 2, 3], [4, 5, 6]]
Output: [[1, 4], [2, 5], [3, 6]]
```

### Función matrix_diagonal_sum:
```
Input: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
Output: 15 (1 + 5 + 9)
```

## Restricciones
- Las matrices tienen dimensiones válidas para cada operación
- matrix_add: ambas matrices tienen las mismas dimensiones
- matrix_diagonal_sum: solo para matrices cuadradas
- Los elementos son números enteros
- Las matrices pueden ser de 1x1 hasta 10x10

## Conceptos a Practicar
- Listas anidadas (matrices)
- Bucles anidados
- Indexación bidimensional
- Operaciones matemáticas con matrices

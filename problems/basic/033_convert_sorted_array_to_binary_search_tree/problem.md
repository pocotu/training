# [033] Convert Sorted Array to Binary Search Tree

## Problema

Dado un array de enteros `nums` donde los elementos están ordenados en orden ascendente, conviértelo en un árbol de búsqueda binario balanceado en altura.

## Input/Output
- **Input**: `nums` - array ordenado de enteros
- **Output**: Raíz del BST balanceado

## Constraints
- 1 ≤ nums.length ≤ 10^4
- -10^4 ≤ nums[i] ≤ 10^4
- nums está ordenado en orden estrictamente creciente

## Ejemplos

### Ejemplo 1:
```
Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
```

### Ejemplo 2:
```
Input: nums = [1,3]
Output: [3,1] o [1,null,3]
```

## Tags
array, divide-and-conquer, tree, binary-search-tree, binary-tree

## Notas Adicionales
- **Complejidad de tiempo esperada**: O(n)
- **Complejidad de espacio esperada**: O(log n)
- **Conceptos clave**: BST, divide y vencerás, árbol balanceado
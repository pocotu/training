# [028] Merge Sorted Array

## Problema

Se te dan dos arrays de enteros `nums1` y `nums2`, ordenados en orden no decreciente, y dos enteros `m` y `n`, representando el número de elementos en `nums1` y `nums2` respectivamente.

Fusiona `nums1` y `nums2` en un solo array ordenado en orden no decreciente.

## Input/Output
- **Input**: `nums1` (array con espacio extra), `m`, `nums2`, `n`
- **Output**: Modifica `nums1` in-place

## Constraints
- nums1.length == m + n
- nums2.length == n
- 0 ≤ m, n ≤ 200
- 1 ≤ m + n ≤ 200

## Ejemplos

### Ejemplo 1:
```
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
```

### Ejemplo 2:
```
Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
```

## Tags
array, two-pointers, sorting

## Notas Adicionales
- **Complejidad de tiempo esperada**: O(m + n)
- **Complejidad de espacio esperada**: O(1)
- **Conceptos clave**: Merge de arrays, two pointers, modificación in-place
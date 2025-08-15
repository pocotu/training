# [045] Intersection of Two Arrays II

## Problema

Dados dos arrays de enteros `nums1` y `nums2`, devuelve un array de su intersección. Cada elemento en el resultado debe aparecer tantas veces como se muestra en ambos arrays y puedes devolver el resultado en cualquier orden.

## Input/Output
- **Input**: `nums1`, `nums2` - dos arrays de enteros
- **Output**: Array con la intersección (con duplicados)

## Constraints
- 1 ≤ nums1.length, nums2.length ≤ 1000
- 0 ≤ nums1[i], nums2[i] ≤ 1000

## Ejemplos

### Ejemplo 1:
```
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
```

### Ejemplo 2:
```
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9] o [9,4]
```

## Explicación
A diferencia de la intersección simple, aquí debemos considerar la frecuencia de cada elemento. Si un elemento aparece 2 veces en nums1 y 3 veces en nums2, debe aparecer min(2,3) = 2 veces en el resultado.

## Hints
- Usa un hashmap para contar frecuencias
- Considera el enfoque de two pointers si los arrays están ordenados
- Piensa en la optimización de espacio

## Tags
array, hash-table, two-pointers, binary-search, sorting

## Notas Adicionales
- **Complejidad de tiempo esperada**: O(m + n)
- **Complejidad de espacio esperada**: O(min(m,n))
- **Dificultad**: Easy
- **Conceptos clave**: Intersección con duplicados, conteo de frecuencias, hashmap
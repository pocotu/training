# [F053] List Flattening

## Problema

Escribe una función llamada `flatten_list` que reciba una lista de listas `nested_list` y devuelva una lista plana con todos los elementos. Asume que solo hay un nivel de anidamiento.

## Ejemplos

### Ejemplo 1:
```
Input: nested_list = [[1, 2], [3, 4], [5]]
Output: [1, 2, 3, 4, 5]
```

### Ejemplo 2:
```
Input: nested_list = [['a', 'b'], ['c'], ['d', 'e', 'f']]
Output: ['a', 'b', 'c', 'd', 'e', 'f']
```

## Tags
list, flattening, iteration, foundations

## Notas Adicionales
- **Complejidad de tiempo**: O(n) donde n es el total de elementos
- **Complejidad de espacio**: O(n)
- **Conceptos clave**: Iteración anidada, list comprehension
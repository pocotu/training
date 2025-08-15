# [027] Remove Duplicates from Sorted List

## Problema

Dada la cabeza de una lista enlazada ordenada, elimina todos los duplicados de modo que cada elemento aparezca solo una vez. Devuelve la lista enlazada también ordenada.

## Input/Output
- **Input**: `head` - cabeza de una lista enlazada ordenada
- **Output**: Cabeza de la lista enlazada sin duplicados

## Constraints
- El número de nodos en la lista está en el rango [0, 300]
- -100 ≤ Node.val ≤ 100
- La lista está garantizada de estar ordenada en orden ascendente

## Ejemplos

### Ejemplo 1:
```
Input: head = [1,1,2]
Output: [1,2]
```

### Ejemplo 2:
```
Input: head = [1,1,2,3,3]
Output: [1,2,3]
```

## Tags
linked-list, two-pointers

## Notas Adicionales
- **Complejidad de tiempo esperada**: O(n)
- **Complejidad de espacio esperada**: O(1)
- **Conceptos clave**: Lista enlazada, eliminación de duplicados
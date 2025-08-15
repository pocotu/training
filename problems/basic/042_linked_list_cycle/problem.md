# [042] Linked List Cycle

## Problema

Dado `head`, la cabeza de una lista enlazada, determina si la lista enlazada tiene un ciclo.

Hay un ciclo en una lista enlazada si hay algún nodo en la lista que se puede alcanzar nuevamente siguiendo continuamente el puntero `next`. Internamente, `pos` se usa para denotar el índice del nodo al que está conectado el puntero de cola. **Nota que `pos` no se pasa como parámetro**.

Devuelve `true` si hay un ciclo en la lista enlazada. De lo contrario, devuelve `false`.

## Input/Output
- **Input**: `head` - cabeza de la lista enlazada
- **Output**: `True` si hay ciclo, `False` en caso contrario

## Constraints
- El número de nodos en la lista está en el rango [0, 10^4]
- -10^5 ≤ Node.val ≤ 10^5
- pos es -1 o un índice válido en la lista enlazada

## Ejemplos

### Ejemplo 1:
```
Input: head = [3,2,0,-4], pos = 1
Output: true
Explicación: Hay un ciclo en la lista enlazada, donde la cola se conecta al segundo nodo.
```

### Ejemplo 2:
```
Input: head = [1,2], pos = 0
Output: true
Explicación: Hay un ciclo en la lista enlazada, donde la cola se conecta al primer nodo.
```

## Tags
hash-table, linked-list, two-pointers

## Notas Adicionales
- **Complejidad de tiempo esperada**: O(n)
- **Complejidad de espacio esperada**: O(1)
- **Conceptos clave**: Floyd's cycle detection, two pointers, fast-slow pointers
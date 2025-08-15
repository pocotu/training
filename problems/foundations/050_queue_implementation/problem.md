# [F050] Queue Implementation

## Problema

Implementa una clase `Queue` con los métodos básicos: `enqueue(item)` para agregar un elemento al final, `dequeue()` para remover y devolver el primer elemento, `front()` para ver el primer elemento sin removerlo, e `is_empty()` para verificar si está vacía.

## Ejemplos

### Ejemplo 1:
```
Input: queue = Queue(); queue.enqueue(1); queue.enqueue(2); queue.dequeue()
Output: 1
```

### Ejemplo 2:
```
Input: queue = Queue(); queue.enqueue(5); queue.front()
Output: 5
```

## Tags
data-structure, queue, implementation, foundations

## Notas Adicionales
- **Complejidad de tiempo**: O(1) para todas las operaciones
- **Complejidad de espacio**: O(n) donde n es el número de elementos
- **Conceptos clave**: Estructura de datos FIFO, implementación de queue
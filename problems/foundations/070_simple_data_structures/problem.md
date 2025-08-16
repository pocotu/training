# [F070] Simple Data Structures

## Problema

Implementa dos estructuras de datos básicas usando clases:

### 1. SimpleStack
- `push(item)` - agrega un elemento al tope
- `pop()` - remueve y devuelve el elemento del tope (None si está vacía)
- `peek()` - devuelve el elemento del tope sin removerlo (None si está vacía)
- `is_empty()` - devuelve True si la pila está vacía
- `size()` - devuelve el número de elementos

### 2. SimpleQueue
- `enqueue(item)` - agrega un elemento al final
- `dequeue()` - remueve y devuelve el primer elemento (None si está vacía)
- `front()` - devuelve el primer elemento sin removerlo (None si está vacía)
- `is_empty()` - devuelve True si la cola está vacía
- `size()` - devuelve el número de elementos

## Ejemplos

### SimpleStack:
```python
stack = SimpleStack()
stack.push(1)
stack.push(2)
print(stack.peek())     # Output: 2
print(stack.pop())      # Output: 2
print(stack.size())     # Output: 1
```

### SimpleQueue:
```python
queue = SimpleQueue()
queue.enqueue(1)
queue.enqueue(2)
print(queue.front())    # Output: 1
print(queue.dequeue())  # Output: 1
print(queue.size())     # Output: 1
```

## Restricciones
- Usar listas internas para almacenar los elementos
- No usar collections.deque u otras estructuras avanzadas
- Manejar casos de estructuras vacías devolviendo None

## Conceptos a Practicar
- Clases y métodos
- Principios LIFO (Stack) y FIFO (Queue)
- Encapsulación de datos
- Manejo de casos borde

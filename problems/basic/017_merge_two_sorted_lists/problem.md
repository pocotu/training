# [017] Merge Two Sorted Lists

## Problema
Fusiona dos listas enlazadas ordenadas y devuelve una nueva lista ordenada. La nueva lista debe crearse uniendo los nodos de las dos listas originales.

## Input/Output
- **Input**: `list1` (ListNode) - Cabeza de la primera lista enlazada ordenada
- **Input**: `list2` (ListNode) - Cabeza de la segunda lista enlazada ordenada  
- **Output**: `ListNode` - Cabeza de la nueva lista enlazada ordenada fusionada

## Constraints
- El número de nodos en ambas listas está en el rango [0, 50]
- -100 ≤ Node.val ≤ 100
- Ambas listas están ordenadas en orden no decreciente

## Ejemplos

### Ejemplo 1:
```
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
```

### Ejemplo 2:
```
Input: list1 = [], list2 = []
Output: []
```

### Ejemplo 3:
```
Input: list1 = [], list2 = [0]
Output: [0]
```

## Explicación
Utiliza dos punteros para recorrer ambas listas simultáneamente:
1. Compara los valores actuales de ambas listas
2. Toma el menor valor y avanza el puntero de esa lista
3. Conecta el nodo seleccionado a la lista resultado
4. Continúa hasta que ambas listas se agoten
5. Si una lista se agota antes, conecta el resto de la otra lista

## Tags
linked-list, recursion, two-pointers, easy, leetcode

## Notas Adicionales
- **Complejidad de tiempo**: O(n + m)
- **Complejidad de espacio**: O(1) iterativo, O(n + m) recursivo
- **Dificultad**: Easy
- **Conceptos clave**: Lista enlazada, fusión de listas ordenadas, two pointers

---

### Instrucciones para completar:
1. Visitar https://leetcode.com/problems/problem-21/
2. Copiar el enunciado completo en la sección "Problema"
3. Actualizar Input/Output con información específica
4. Copiar constraints exactos de LeetCode
5. Copiar todos los ejemplos de LeetCode
6. Agregar explicación detallada del approach
7. Incluir tags apropiados del repositorio
8. Actualizar complejidades después de resolver
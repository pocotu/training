# [034] Balanced Binary Tree

## Problema

Dado un árbol binario, determina si está balanceado en altura.

Un árbol binario balanceado en altura es un árbol binario en el que la profundidad de los dos subárboles de cada nodo nunca difiere en más de uno.

## Input/Output
- **Input**: `root` - raíz del árbol binario
- **Output**: `True` si está balanceado, `False` en caso contrario

## Constraints
- El número de nodos en el árbol está en el rango [0, 5000]
- -10^4 ≤ Node.val ≤ 10^4

## Ejemplos

### Ejemplo 1:
```
Input: root = [3,9,20,null,null,15,7]
Output: true
```

### Ejemplo 2:
```
Input: root = [1,2,2,3,3,null,null,4,4]
Output: false
```

## Tags
tree, depth-first-search, binary-tree

## Notas Adicionales
- **Complejidad de tiempo esperada**: O(n)
- **Complejidad de espacio esperada**: O(n)
- **Conceptos clave**: Árbol balanceado, DFS, altura de árboles
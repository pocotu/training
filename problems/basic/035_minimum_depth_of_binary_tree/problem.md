# [035] Minimum Depth of Binary Tree

## Problema

Dado un árbol binario, encuentra su profundidad mínima.

La profundidad mínima es el número de nodos a lo largo del camino más corto desde el nodo raíz hasta la hoja más cercana.

## Input/Output
- **Input**: `root` - raíz del árbol binario
- **Output**: Profundidad mínima del árbol

## Constraints
- El número de nodos en el árbol está en el rango [0, 10^5]
- -1000 ≤ Node.val ≤ 1000

## Ejemplos

### Ejemplo 1:
```
Input: root = [3,9,20,null,null,15,7]
Output: 2
```

### Ejemplo 2:
```
Input: root = [2,null,3,null,4,null,5,null,6]
Output: 5
```

## Tags
tree, depth-first-search, breadth-first-search, binary-tree

## Notas Adicionales
- **Complejidad de tiempo esperada**: O(n)
- **Complejidad de espacio esperada**: O(n)
- **Conceptos clave**: Profundidad mínima, BFS, DFS
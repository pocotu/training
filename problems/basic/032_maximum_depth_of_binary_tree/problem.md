# [032] Maximum Depth of Binary Tree

## Problema

Dado el `root` de un árbol binario, devuelve su profundidad máxima.

La profundidad máxima de un árbol binario es el número de nodos a lo largo del camino más largo desde el nodo raíz hasta la hoja más lejana.

## Input/Output
- **Input**: `root` - raíz del árbol binario
- **Output**: Profundidad máxima del árbol

## Constraints
- El número de nodos en el árbol está en el rango [0, 10^4]
- -100 ≤ Node.val ≤ 100

## Ejemplos

### Ejemplo 1:
```
Input: root = [3,9,20,null,null,15,7]
Output: 3
```

### Ejemplo 2:
```
Input: root = [1,null,2]
Output: 2
```

## Tags
tree, depth-first-search, breadth-first-search, binary-tree

## Notas Adicionales
- **Complejidad de tiempo esperada**: O(n)
- **Complejidad de espacio esperada**: O(n)
- **Conceptos clave**: Profundidad de árboles, DFS, BFS, recursión
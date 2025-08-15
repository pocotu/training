# [043] Binary Tree Preorder Traversal

## Problema

Dado el `root` de un árbol binario, devuelve el recorrido preorder de los valores de sus nodos.

## Input/Output
- **Input**: `root` - raíz del árbol binario
- **Output**: Lista con el recorrido preorder

## Constraints
- El número de nodos en el árbol está en el rango [0, 100]
- -100 ≤ Node.val ≤ 100

## Ejemplos

### Ejemplo 1:
```
Input: root = [1,null,2,3]
Output: [1,2,3]
```

### Ejemplo 2:
```
Input: root = []
Output: []
```

### Ejemplo 3:
```
Input: root = [1]
Output: [1]
```

## Tags
stack, tree, depth-first-search, binary-tree

## Notas Adicionales
- **Complejidad de tiempo esperada**: O(n)
- **Complejidad de espacio esperada**: O(n)
- **Conceptos clave**: Preorder traversal, DFS, stack-based iteration
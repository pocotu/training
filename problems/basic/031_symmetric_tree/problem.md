# [031] Symmetric Tree

## Problema

Dado el `root` de un árbol binario, verifica si es un espejo de sí mismo (es decir, simétrico alrededor de su centro).

## Input/Output
- **Input**: `root` - raíz del árbol binario
- **Output**: `True` si es simétrico, `False` en caso contrario

## Constraints
- El número de nodos en el árbol está en el rango [1, 1000]
- -100 ≤ Node.val ≤ 100

## Ejemplos

### Ejemplo 1:
```
Input: root = [1,2,2,3,4,4,3]
Output: true
```

### Ejemplo 2:
```
Input: root = [1,2,2,null,3,null,3]
Output: false
```

## Tags
tree, depth-first-search, breadth-first-search, binary-tree

## Notas Adicionales
- **Complejidad de tiempo esperada**: O(n)
- **Complejidad de espacio esperada**: O(n)
- **Conceptos clave**: Simetría de árboles, DFS, BFS
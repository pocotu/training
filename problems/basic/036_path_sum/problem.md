# [036] Path Sum

## Problema

Dado el `root` de un árbol binario y un entero `targetSum`, devuelve `true` si el árbol tiene un camino de raíz a hoja tal que la suma de todos los valores a lo largo del camino sea igual a `targetSum`.

Una hoja es un nodo sin hijos.

## Input/Output
- **Input**: `root` - raíz del árbol binario, `targetSum` - suma objetivo
- **Output**: `True` si existe el camino, `False` en caso contrario

## Constraints
- El número de nodos en el árbol está en el rango [0, 5000]
- -1000 ≤ Node.val ≤ 1000
- -1000 ≤ targetSum ≤ 1000

## Ejemplos

### Ejemplo 1:
```
Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true
```

### Ejemplo 2:
```
Input: root = [1,2,3], targetSum = 5
Output: false
```

## Tags
tree, depth-first-search, binary-tree

## Notas Adicionales
- **Complejidad de tiempo esperada**: O(n)
- **Complejidad de espacio esperada**: O(n)
- **Conceptos clave**: Path sum, DFS, backtracking
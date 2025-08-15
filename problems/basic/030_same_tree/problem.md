# [030] Same Tree

## Problema

Dados los roots de dos árboles binarios `p` y `q`, escribe una función para verificar si son iguales o no.

Dos árboles binarios se consideran iguales si son estructuralmente idénticos y los nodos tienen el mismo valor.

## Input/Output
- **Input**: `p`, `q` - roots de dos árboles binarios
- **Output**: `True` si son iguales, `False` en caso contrario

## Constraints
- El número de nodos en ambos árboles está en el rango [0, 100]
- -10^4 ≤ Node.val ≤ 10^4

## Ejemplos

### Ejemplo 1:
```
Input: p = [1,2,3], q = [1,2,3]
Output: true
```

### Ejemplo 2:
```
Input: p = [1,2], q = [1,null,2]
Output: false
```

## Tags
tree, depth-first-search, binary-tree

## Notas Adicionales
- **Complejidad de tiempo esperada**: O(min(m,n))
- **Complejidad de espacio esperada**: O(min(m,n))
- **Conceptos clave**: Comparación de árboles, DFS, recursión
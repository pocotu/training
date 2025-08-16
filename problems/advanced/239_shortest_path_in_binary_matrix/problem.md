# [239] Shortest Path in Binary Matrix

## Problema
Dado una matriz binaria `grid` de `n x n`, retorna la longitud del camino más corto **libre** desde la esquina superior izquierda `(0, 0)` hasta la esquina inferior derecha `(n-1, n-1)`. Si no existe tal camino, retorna `-1`.

Un camino **libre** es un camino desde `(0, 0)` hasta `(n-1, n-1)` tal que:
- Todas las celdas visitadas del camino son `0`
- Todas las celdas adyacentes del camino están conectadas **8-direccionalmente** (horizontal, vertical y diagonal)

La **longitud del camino** es el número de celdas visitadas en el camino.

## Input/Output
- **Input**: `grid` (List[List[int]] - matriz binaria n x n)
- **Output**: int - longitud del camino más corto, o -1 si no existe

## Constraints
- n == grid.length
- n == grid[i].length  
- 1 ≤ n ≤ 100
- grid[i][j] es 0 o 1

## Ejemplos

### Ejemplo 1:
```
Input: grid = [[0,1],[1,0]]
Output: 2
Explicación:
0 1
1 0
Camino: (0,0) → (1,1)
```

### Ejemplo 2:
```
Input: grid = [[0,0,0],[1,1,0],[1,1,0]]
Output: 4
Explicación:
0 0 0
1 1 0  
1 1 0
Camino: (0,0) → (0,1) → (0,2) → (1,2) → (2,2)
```

### Ejemplo 3:
```
Input: grid = [[1,0,0],[1,1,0],[1,1,0]]
Output: -1
Explicación: No hay camino desde (0,0) porque grid[0][0] = 1
```

### Ejemplo 4 (Edge Case):
```
Input: grid = [[0]]
Output: 1
```

## Explicación
Necesitamos encontrar el camino más corto en un grafo no ponderado, lo cual es perfecto para BFS. El movimiento es en 8 direcciones (incluyendo diagonales).

## Hints
- Usa BFS ya que necesitas el camino más corto
- Verifica que las celdas inicial y final sean 0
- Considera las 8 direcciones: horizontal, vertical y diagonal
- Usa una cola para BFS y marca celdas visitadas

## Tags
matrix, bfs, shortest-path, graph

## Notas Adicionales
- **Complejidad de tiempo esperada**: O(n²) para BFS en matriz n×n
- **Complejidad de espacio esperada**: O(n²) para la cola y matriz visitada

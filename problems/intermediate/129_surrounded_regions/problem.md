# [129] Surrounded Regions

## Problema
Dada una matriz bidimensional `board` que contiene `'X'` y `'O'`, captura todas las regiones rodeadas.

Una región es capturada rodeándola con `'X'` en las cuatro direcciones.

Cualquier `'O'` que esté conectada a una `'O'` en el borde de la matriz no será capturada.

## Input/Output
- **Input**: `board` (List[List[str]] - matriz de caracteres 'X' y 'O')
- **Output**: Modifica la matriz in-place, no retorna nada

## Constraints
- m == board.length
- n == board[i].length
- 1 ≤ m, n ≤ 200
- board[i][j] es 'X' o 'O'

## Ejemplos

### Ejemplo 1:
```
Input: board = [["X","X","X","X"],
                ["X","O","O","X"],
                ["X","X","O","X"],
                ["X","O","X","X"]]

Output: [["X","X","X","X"],
         ["X","X","X","X"],
         ["X","X","X","X"],
         ["X","O","X","X"]]

Explicación: Las regiones rodeadas no deben estar en el borde, por lo que cualquier 'O' 
en el borde o conectado a una 'O' en el borde no será volteado a 'X'.
```

### Ejemplo 2:
```
Input: board = [["X"]]
Output: [["X"]]
```

### Ejemplo 3 (Edge Case):
```
Input: board = [["O","O"],
                ["O","O"]]
Output: [["O","O"],
         ["O","O"]]
Explicación: Todos los 'O' están conectados al borde.
```

## Explicación
La clave es identificar qué 'O's están conectadas al borde. Estas no pueden ser capturadas. Las 'O's que no están conectadas al borde pueden ser capturadas (convertidas a 'X').

## Hints
- Empieza desde los bordes y marca todas las 'O's conectadas
- Usa DFS/BFS desde cada 'O' en el borde
- Las 'O's no marcadas pueden ser capturadas
- Considera usar un carácter temporal para marcar

## Tags
matrix, dfs, bfs, union-find

## Notas Adicionales
- **Complejidad de tiempo esperada**: O(m*n)
- **Complejidad de espacio esperada**: O(m*n) en el peor caso para recursión

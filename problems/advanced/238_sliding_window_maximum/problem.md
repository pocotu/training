# [238] Sliding Window Maximum

## Problema
Dado un array de enteros `nums`, hay una ventana deslizante de tamaño `k` que se mueve desde la parte izquierda del array hasta la derecha. Solo puedes ver los `k` números en la ventana. Cada vez que la ventana deslizante se mueve una posición a la derecha.

Retorna el *máximo de la ventana deslizante*.

## Input/Output
- **Input**: `nums` (List[int] - array de enteros), `k` (int - tamaño de ventana)
- **Output**: List[int] - array con el máximo de cada ventana

## Constraints
- 1 ≤ nums.length ≤ 10^5
- -10^4 ≤ nums[i] ≤ 10^4
- 1 ≤ k ≤ nums.length

## Ejemplos

### Ejemplo 1:
```
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explicación: 
Ventana posición                Máximo
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
```

### Ejemplo 2:
```
Input: nums = [1], k = 1
Output: [1]
```

### Ejemplo 3 (Edge Case):
```
Input: nums = [1,-1], k = 1
Output: [1,-1]
```

### Ejemplo 4:
```
Input: nums = [9,11], k = 2
Output: [11]
```

## Explicación
Para cada ventana de tamaño k, necesitamos encontrar el elemento máximo eficientemente. Una solución ingenua sería O(nk), pero podemos usar una deque monotónica para lograr O(n).

## Hints
- Usa una deque (double-ended queue) para mantener elementos en orden decreciente
- Almacena índices en lugar de valores para manejar elementos duplicados
- Elimina elementos fuera de la ventana actual
- Elimina elementos menores que el elemento actual desde atrás

## Tags
array, deque, sliding-window, monotonic-queue

## Notas Adicionales
- **Complejidad de tiempo esperada**: O(n) - cada elemento entra y sale de la deque una vez
- **Complejidad de espacio esperada**: O(k) para la deque

# [001] Two Sum

## Problema
Dado un array de números enteros `nums` y un número entero `target`, devuelve los índices de los dos números que sumen el `target`.

Puedes asumir que cada entrada tiene exactamente una solución, y no puedes usar el mismo elemento dos veces.

Puedes devolver la respuesta en cualquier orden.

## Input/Output
- **Input**: `nums` (array de enteros), `target` (entero)
- **Output**: Array de dos enteros representando los índices

## Constraints
- 2 ≤ nums.length ≤ 10^4
- -10^9 ≤ nums[i] ≤ 10^9
- -10^9 ≤ target ≤ 10^9
- Solo existe una solución válida

## Ejemplos

### Ejemplo 1:
```
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explicación: nums[0] + nums[1] = 2 + 7 = 9
```

### Ejemplo 2:
```
Input: nums = [3,2,4], target = 6
Output: [1,2]
```

### Ejemplo 3:
```
Input: nums = [3,3], target = 6
Output: [0,1]
```

## Explicación
La clave está en usar un hashmap para almacenar los números que ya hemos visto junto con sus índices. Para cada número actual, calculamos su complemento (target - número actual) y verificamos si ya existe en el hashmap.

## Hints
- Usar un hashmap para almacenar números vistos con sus índices
- Para cada número, buscar su complemento (target - número)
- Complejidad objetivo: O(n) tiempo, O(n) espacio

## Tags
hashmap, array

## Notas Adicionales
- **Complejidad de tiempo esperada**: O(n)
- **Complejidad de espacio esperada**: O(n)
- **Dificultad**: Easy
- **Conceptos clave**: Hashmap, complement search pattern

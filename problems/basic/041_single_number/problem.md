# [041] Single Number

## Problema

Dado un array no vacío de enteros `nums`, cada elemento aparece dos veces excepto uno. Encuentra ese único elemento.

Debes implementar una solución con complejidad de tiempo lineal y usar solo espacio extra constante.

## Input/Output
- **Input**: `nums` - array de enteros
- **Output**: El único elemento que aparece una vez

## Constraints
- 1 ≤ nums.length ≤ 3 * 10^4
- -3 * 10^4 ≤ nums[i] ≤ 3 * 10^4
- Cada elemento en el array aparece dos veces excepto uno que aparece exactamente una vez

## Ejemplos

### Ejemplo 1:
```
Input: nums = [2,2,1]
Output: 1
```

### Ejemplo 2:
```
Input: nums = [4,1,2,1,2]
Output: 4
```

### Ejemplo 3:
```
Input: nums = [1]
Output: 1
```

## Tags
array, bit-manipulation

## Notas Adicionales
- **Complejidad de tiempo esperada**: O(n)
- **Complejidad de espacio esperada**: O(1)
- **Conceptos clave**: XOR operation, bit manipulation
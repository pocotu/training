# [026] Climbing Stairs

## Problema

Estás subiendo una escalera. Se necesitan `n` pasos para llegar a la cima.

Cada vez puedes subir 1 o 2 escalones. ¿De cuántas maneras distintas puedes subir a la cima?

## Input/Output
- **Input**: Un entero `n` (1 ≤ n ≤ 45)
- **Output**: Número de maneras distintas de subir la escalera

## Constraints
- 1 ≤ n ≤ 45

## Ejemplos

### Ejemplo 1:
```
Input: n = 2
Output: 2
Explicación: Hay dos maneras de subir a la cima.
1. 1 paso + 1 paso
2. 2 pasos
```

### Ejemplo 2:
```
Input: n = 3
Output: 3
Explicación: Hay tres maneras de subir a la cima.
1. 1 paso + 1 paso + 1 paso
2. 1 paso + 2 pasos
3. 2 pasos + 1 paso
```

## Explicación
Este es un problema clásico de programación dinámica. El número de maneras de llegar al escalón n es la suma de las maneras de llegar al escalón (n-1) y al escalón (n-2).

## Hints
- Piensa en términos de la secuencia de Fibonacci
- Usa programación dinámica para optimizar
- Considera tanto el enfoque recursivo como iterativo

## Tags
dynamic-programming, fibonacci, math, memoization

## Notas Adicionales
- **Complejidad de tiempo esperada**: O(n)
- **Complejidad de espacio esperada**: O(1)
- **Dificultad**: Easy
- **Conceptos clave**: Programación dinámica, secuencia de Fibonacci
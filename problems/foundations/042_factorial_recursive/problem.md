# [F042] Factorial Recursive

## Problema

Escribe una función llamada `factorial` que reciba un número entero no negativo `n` y devuelva su factorial usando **recursión**. El factorial de n (n!) es el producto de todos los números enteros positivos menores o iguales a n.

**Casos base**: 
- factorial(0) = 1
- factorial(1) = 1

**Caso recursivo**: 
- factorial(n) = n × factorial(n-1)

## Ejemplos

### Ejemplo 1:
```
Input: n = 5
Output: 120
```

### Ejemplo 2:
```
Input: n = 0
Output: 1
```

### Ejemplo 3:
```
Input: n = 3
Output: 6
```

## Restricciones

- `n` será un entero en el rango [0, 10]
- La función debe usar **exclusivamente** recursión (no usar bucles)
- Se debe implementar correctamente los casos base

## Tags
recursion, math, basic, foundations

## Notas Adicionales
- **Complejidad de tiempo**: O(n)
- **Complejidad de espacio**: O(n)
- **Conceptos clave**: Recursión, caso base, matemáticas
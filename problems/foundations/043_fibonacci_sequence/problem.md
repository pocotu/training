# [F043] Fibonacci Sequence

## Problema

Escribe una función llamada `fibonacci` que reciba un número entero no negativo `n` y devuelva el n-ésimo número de la secuencia de Fibonacci usando **iteración** (bucles).

La secuencia de Fibonacci se define como:
- F(0) = 0
- F(1) = 1  
- F(n) = F(n-1) + F(n-2) para n > 1

**Método requerido**: Debe usar iteración con bucles (no recursión).

## Ejemplos

### Ejemplo 1:
```
Input: n = 0
Output: 0
```

### Ejemplo 2:
```
Input: n = 1
Output: 1
```

### Ejemplo 3:
```
Input: n = 6
Output: 8
```

## Restricciones

- `n` será un entero en el rango [0, 20]
- La función debe usar **exclusivamente** iteración (no recursión)
- Se debe manejar correctamente los casos base (n=0 y n=1)

## Tags
recursion, math, sequence, foundations

## Notas Adicionales
- **Complejidad de tiempo**: O(2^n) recursivo, O(n) iterativo
- **Complejidad de espacio**: O(n) recursivo, O(1) iterativo
- **Conceptos clave**: Secuencias, recursión o iteración
# [F056] GCD Algorithm

## Problema

Escribe una función llamada `gcd` que reciba dos números enteros no negativos `a` y `b` y devuelva su máximo común divisor (GCD) usando el algoritmo de Euclides.

**Casos especiales**:
- Si uno de los números es 0, el GCD es el otro número (si es positivo)
- Si ambos números son 0, devolver 0
- Se garantiza que los números serán no negativos

## Ejemplos

### Ejemplo 1:
```
Input: a = 48, b = 18
Output: 6
```

### Ejemplo 2:
```
Input: a = 17, b = 13
Output: 1
```

### Ejemplo 3:
```
Input: a = 100, b = 25
Output: 25
```

### Ejemplo 4:
```
Input: a = 0, b = 5
Output: 5
```

## Restricciones

- `a` y `b` serán enteros no negativos (>= 0)
- Al menos uno de los números será > 0 (excepto el caso a=0, b=0)
- Usar el algoritmo de Euclides

## Tags
math, gcd, euclidean-algorithm, foundations

## Notas Adicionales
- **Complejidad de tiempo**: O(log(min(a,b)))
- **Complejidad de espacio**: O(1) iterativo, O(log(min(a,b))) recursivo
- **Conceptos clave**: Algoritmo de Euclides, máximo común divisor
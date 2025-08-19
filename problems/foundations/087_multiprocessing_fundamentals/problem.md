# [F087] Mathematical Functions

## Problema

Implementa tres funciones para operaciones matemáticas básicas:

1. `calculate_factorial(n)` - calcula factorial de un número
2. `calculate_power(base, exponent)` - calcula potencia de un número
3. `calculate_gcd(a, b)` - calcula máximo común divisor

**Foundations**: Se enfoca en operaciones matemáticas fundamentales con algoritmos básicos.

## Ejemplos

### Función calculate_factorial:
```
Input: calculate_factorial(5)
Output: 120  # 5! = 5 * 4 * 3 * 2 * 1
```

### Función calculate_power:
```
Input: calculate_power(2, 3)
Output: 8  # 2^3 = 8
```

### Función calculate_gcd:
```
Input: calculate_gcd(48, 18)
Output: 6  # GCD de 48 y 18 es 6
```

## Restricciones
- calculate_factorial debe manejar n >= 0, retornar 1 para n = 0
- calculate_power debe funcionar con exponentes enteros positivos
- calculate_gcd debe usar algoritmo de Euclides
- Validar entradas positivas
- No usar funciones built-in como math.factorial

## Conceptos a Practicar
- Recursión e iteración
- Algoritmos matemáticos clásicos
- Validación de entrada
- Casos base en recursión
- CPU-bound vs I/O-bound tasks

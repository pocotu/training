# [F003] Arithmetic Operations

## Problema

Escribe una función llamada `perform_operations` que reciba dos números, `a` y `b`, como argumentos. La función debe devolver una tupla con los resultados de las siguientes operaciones en este orden:

1.  Suma (`a + b`)
2.  Resta (`a - b`)
3.  Multiplicación (`a * b`)
4.  División (`a / b`) - Si `b` es 0, devolver `None` para esta operación

## Ejemplos

### Ejemplo 1:
```
Input: a = 10, b = 5
Output: (15, 5, 50, 2.0)
```

### Ejemplo 2:
```
Input: a = 20, b = 4
Output: (24, 16, 80, 5.0)
```

### Ejemplo 3:
```
Input: a = 10, b = 0
Output: (10, 10, 0, None)
```

## Constraints

- La función debe llamarse `perform_operations`.
- Los números `a` y `b` pueden ser enteros o flotantes.
- Si `b` es 0, la división debe devolver `None`.

# [F060] Simple Calculator

## Problema

Escribe una función llamada `calculate` que reciba dos números (int o float) `a` y `b`, y un operador string `operator` ('+', '-', '*', '/') y devuelva el resultado de la operación.

**Manejo de errores**:
- Si el operador no es válido, devolver "Error"
- Si hay división por cero, devolver "Error"
- Para división, el resultado debe ser float
- Para otros operadores, preservar el tipo (int si ambos son int, float si hay algún float)

## Ejemplos

### Ejemplo 1:
```
Input: a = 10, b = 5, operator = '+'
Output: 15
```

### Ejemplo 2:
```
Input: a = 10, b = 0, operator = '/'
Output: "Error"
```

### Ejemplo 3:
```
Input: a = 6, b = 2, operator = '*'
Output: 12
```

### Ejemplo 4:
```
Input: a = 10, b = 3, operator = '/'
Output: 3.3333333333333335
```

## Restricciones

- `a` y `b` serán números (int o float)
- `operator` será un string con uno de: '+', '-', '*', '/'
- División por cero debe devolver "Error"
- Operadores inválidos deben devolver "Error"

## Tags
math, calculator, operations, foundations

## Notas Adicionales
- **Complejidad de tiempo**: O(1)
- **Complejidad de espacio**: O(1)
- **Conceptos clave**: Operaciones matemáticas, manejo de errores, condicionales
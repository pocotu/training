# [F072] Try-Except Basics

## Problema

Escribe una función llamada `safe_division` que reciba dos números `a` y `b`, y devuelva el resultado de `a / b`. Si ocurre una división por cero, la función debe capturar la excepción y devolver el string `"Error: División por cero"`.

**Simplificado para Foundations**: Se enfoca en el concepto básico de try-except con un solo caso de uso.

## Ejemplos

### Ejemplo 1:
```
Input: safe_division(10, 2)
Output: 5.0
```

### Ejemplo 2:
```
Input: safe_division(10, 0)
Output: "Error: División por cero"
```

### Ejemplo 3:
```
Input: safe_division(7, 2)
Output: 3.5
```

## Restricciones

- `a` y `b` serán números (int o float)
- Usar try-except para capturar ZeroDivisionError
- Devolver el string exacto "Error: División por cero" para el caso de error

Input: safe_list_access([1, 2, 3], 5)
Output: "Error: Índice fuera de rango"
```

### Función safe_int_conversion:
```
Input: safe_int_conversion("123")
Output: 123

Input: safe_int_conversion("abc")
Output: "Error: No se puede convertir a entero"
```

## Restricciones
- Usar try-except blocks apropiadamente
- Retornar el resultado correcto cuando sea posible
- Retornar mensajes de error específicos cuando haya excepciones
- No permitir que las excepciones se propaguen

## Conceptos a Practicar
- Try-except básico
- Manejo de excepciones específicas
- ZeroDivisionError, IndexError, ValueError
- Control de flujo con excepciones

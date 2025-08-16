# [F072] Exception Handling Basics

## Problema

Implementa tres funciones que manejan diferentes tipos de excepciones:
1. `safe_division(a, b)` - realiza división manejando ZeroDivisionError
2. `safe_list_access(lst, index)` - accede a lista manejando IndexError
3. `safe_int_conversion(value)` - convierte a entero manejando ValueError

## Ejemplos

### Función safe_division:
```
Input: safe_division(10, 2)
Output: 5.0

Input: safe_division(10, 0)
Output: "Error: División por cero"
```

### Función safe_list_access:
```
Input: safe_list_access([1, 2, 3], 1)
Output: 2

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

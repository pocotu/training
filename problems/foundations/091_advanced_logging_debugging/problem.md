# [F091] Debug and Error Handling Functions

## Problema

Implementa tres funciones para debugging y manejo de errores básico:

1. `debug_print(message, level)` - imprime mensajes con diferentes niveles
2. `safe_divide(a, b)` - división con manejo de errores 
3. `validate_input(value, data_type)` - valida tipos de entrada

**Foundations**: Se enfoca en debugging básico y manejo de errores, conceptos esenciales.

## Ejemplos

### Función debug_print:
```
Input: debug_print("Usuario conectado", "INFO")
Output: [INFO] Usuario conectado

Input: debug_print("Error de conexión", "ERROR")
Output: [ERROR] Error de conexión
```

### Función safe_divide:
```
Input: safe_divide(10, 2)
Output: 5.0

Input: safe_divide(10, 0)  
Output: None  # Maneja división por cero
```

### Función validate_input:
```
Input: validate_input("123", "int")
Output: True

Input: validate_input("abc", "int")
Output: False
```

## Restricciones
- debug_print debe aceptar niveles: "INFO", "WARNING", "ERROR"
- safe_divide debe retornar None para división por cero
- validate_input debe soportar tipos: "int", "float", "str"
- Imprimir mensajes de debug con formato [NIVEL] mensaje
- No usar librerías de logging externas

## Conceptos a Practicar
- Manejo básico de errores con try/except
- Validación de tipos de datos
- Formateo de strings para debugging
- Condicionales para diferentes niveles

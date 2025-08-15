# [F059] Password Validator

## Problema

Escribe una función llamada `is_valid_password` que reciba un string `password` y devuelva `True` si cumple con los siguientes criterios: al menos 8 caracteres, contiene al menos una letra mayúscula, una minúscula, un dígito y un carácter especial (!@#$%^&*).

## Ejemplos

### Ejemplo 1:
```
Input: password = "MyPass123!"
Output: True
```

### Ejemplo 2:
```
Input: password = "weakpass"
Output: False
```

### Ejemplo 3:
```
Input: password = "NoSpecial123"
Output: False
```

## Tags
string, validation, regex, security, foundations

## Notas Adicionales
- **Complejidad de tiempo**: O(n) donde n es la longitud del password
- **Complejidad de espacio**: O(1)
- **Conceptos clave**: Validación de strings, seguridad, caracteres especiales
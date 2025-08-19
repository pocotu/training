# [F031] Iterating Dictionary Items

## Problema

Escribe una función llamada `format_dictionary` que reciba un diccionario `d` y devuelva una lista de strings, donde cada string tenga el formato "key: value".

## Ejemplos

### Ejemplo 1:
```
Input: d = {"name": "John", "age": 30}
Output: ["name: John", "age: 30"]
```

### Ejemplo 2:
```
Input: d = {}
Output: []
```

## Constraints

- La función debe llamarse `format_dictionary`.
- Usar el método `.items()` para iterar el diccionario.
- El orden de los elementos en la lista puede variar (dictionaries no garantizan orden en Python < 3.7).
- El diccionario puede estar vacío.

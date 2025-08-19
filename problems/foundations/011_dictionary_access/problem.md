# [F011] Dictionary Access

## Problema

Escribe una función llamada `get_dictionary_value` que reciba un diccionario `d` y una clave `key`. La función debe devolver el valor asociado a esa clave en el diccionario. Si la clave no existe, debe devolver `None`.

## Ejemplos

### Ejemplo 1:
```
Input: d = {"name": "John", "age": 30}, key = "name"
Output: "John"
```

### Ejemplo 2:
```
Input: d = {"name": "John", "age": 30}, key = "age"
Output: 30
```

### Ejemplo 3:
```
Input: d = {"name": "John", "age": 30}, key = "city"
Output: None
```

## Constraints

- La función debe llamarse `get_dictionary_value`.
- Si la clave no existe, devolver `None` (no lanzar KeyError).
- Usar el método `.get()` o manejar la excepción apropiadamente.

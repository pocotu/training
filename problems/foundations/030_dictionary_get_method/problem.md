# [F030] Dictionary get() method

## Problema

Escribe una función llamada `get_value_safely` que reciba un diccionario `d` y una clave `key`. La función debe usar el método `get()` para devolver el valor asociado a la clave. Si la clave no existe, debe devolver "Not Found".

## Ejemplos

### Ejemplo 1:
```
Input: d = {"name": "John", "age": 30}, key = "name"
Output: "John"
```

### Ejemplo 2:
```
Input: d = {"name": "John"}, key = "age"
Output: "Not Found"
```

## Constraints

- La función debe llamarse `get_value_safely`.
- Usar específicamente el método `.get()` del diccionario.
- Si la clave no existe, devolver exactamente "Not Found".
- El diccionario puede estar vacío.

# [F032] Dictionary Comprehensions

## Problema

Escribe una función llamada `create_squared_dict` que reciba una lista de números `lst` y devuelva un diccionario donde las claves sean los números de la lista y los valores sean sus cuadrados. Debes usar una "dictionary comprehension".

## Ejemplos

### Ejemplo 1:
```
Input: lst = [1, 2, 3]
Output: {1: 1, 2: 4, 3: 9}
```

### Ejemplo 2:
```
Input: lst = []
Output: {}
```

### Ejemplo 3:
```
Input: lst = [-2, 0, 2]
Output: {-2: 4, 0: 0, 2: 4}
```

## Constraints

- La función debe llamarse `create_squared_dict`.
- DEBE usar dictionary comprehension: `{k: v for ...}`.
- La lista puede estar vacía.
- Los números pueden ser negativos, positivos o cero.

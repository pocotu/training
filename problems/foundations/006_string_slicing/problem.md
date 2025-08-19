# [F006] String Slicing

## Problema

Escribe una función llamada `get_substring` que reciba un string `s`, un índice de inicio `start`, y un índice de fin `end`. La función debe devolver el substring desde `start` hasta `end-1`.

## Ejemplos

### Ejemplo 1:
```
Input: s = "Hello, World!", start = 7, end = 12
Output: "World"
```

### Ejemplo 2:
```
Input: s = "Python", start = 0, end = 3
Output: "Pyt"
```

## Constraints

- La función debe llamarse `get_substring`.
- Los índices `start` y `end` siempre serán válidos para el string dado.
- `start` será menor o igual que `end`.
- `0 ≤ start ≤ end ≤ len(s)`.

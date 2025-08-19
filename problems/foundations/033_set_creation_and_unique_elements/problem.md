# [F033] Set Creation and Unique Elements

## Problema

Escribe una función llamada `get_unique_elements` que reciba una lista `lst` y devuelva una lista con los elementos únicos de la lista original. **Importante**: Debes usar un `set` para identificar elementos únicos, pero el resultado final debe ser una lista.

**Nota**: El orden final no necesita mantenerse (es aceptable cualquier orden).

## Ejemplos

### Ejemplo 1:
```
Input: lst = [1, 2, 2, 3, 1, 4]
Output: [1, 2, 3, 4] (orden puede variar)
```

### Ejemplo 2:
```
Input: lst = []
Output: []
```

### Ejemplo 3:
```
Input: lst = [5, 5, 5]
Output: [5]
```

## Constraints

- La función debe llamarse `get_unique_elements`.
- DEBE usar un `set` internamente para encontrar elementos únicos.
- El resultado debe ser una `list`.
- La lista puede estar vacía.
- El orden de los elementos únicos en el resultado puede variar.

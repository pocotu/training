# [F009] List Methods

## Problema

Escribe una función llamada `use_list_methods` que reciba una lista `lst`. La función debe hacer lo siguiente:
1. Crear una **copia** de la lista original (no modificar la lista original).
2. Añadir el número 4 al final de la copia.
3. Eliminar el elemento en el índice 1 de la copia.
4. Devolver la lista modificada.

**Importante**: La lista original NO debe ser modificada.

## Ejemplos

### Ejemplo 1:
```
Input: lst = [1, 2, 3]
Output: [1, 3, 4]
Lista original después: [1, 2, 3] (sin cambios)
```

### Ejemplo 2:
```
Input: lst = [5, 10, 15, 20]
Output: [5, 15, 20, 4]
Lista original después: [5, 10, 15, 20] (sin cambios)
```

## Constraints

- La función debe llamarse `use_list_methods`.
- La lista original NO debe ser modificada.
- La lista siempre tendrá al menos 2 elementos.
- Debe usar métodos de lista como `.append()` y `.pop()` o `.remove()`.

# [F044] Bubble Sort

## Problema

Escribe una función llamada `bubble_sort` que reciba una lista de números `lst` y devuelva la lista con los elementos ordenados de menor a mayor usando el algoritmo bubble sort.

**Importante**: Especifica claramente si la función debe:
1. **Modificar la lista original** (in-place sorting) - return None
2. **Devolver una nueva lista** ordenada - return new_list

**Para este ejercicio**: La función debe **modificar la lista original** y **no devolver nada** (return None).

## Ejemplos

### Ejemplo 1:
```
Input: lst = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(lst)  # Modifica lst in-place
print(lst)  # Output: [11, 12, 22, 25, 34, 64, 90]
```

### Ejemplo 2:
```
Input: lst = [5, 2, 8, 1, 9]
bubble_sort(lst)  # Modifica lst in-place
print(lst)  # Output: [1, 2, 5, 8, 9]
```

### Ejemplo 3:
```
Input: lst = []
bubble_sort(lst)  # Lista vacía
print(lst)  # Output: []
```

## Restricciones

- `lst` será una lista de números enteros
- Longitud de la lista: [0, 100]
- La función debe modificar la lista original (in-place)
- La función no debe devolver nada (return None)

## Tags
sorting, algorithm, bubble-sort, foundations

## Notas Adicionales
- **Complejidad de tiempo**: O(n²)
- **Complejidad de espacio**: O(1)
- **Conceptos clave**: Algoritmos de ordenamiento, comparaciones, intercambios
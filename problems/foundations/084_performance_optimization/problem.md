# [F084] Number Comparison Functions

## Problema

Implementa tres funciones básicas para comparar números:
1. `find_maximum(numbers_list)` - encuentra el mayor número en una lista
2. `find_minimum(numbers_list)` - encuentra el menor número en una lista  
3. `compare_numbers(a, b)` - compara dos números y retorna el resultado

**Foundations**: Se enfoca en operaciones básicas de comparación y búsqueda en listas.

## Ejemplos

### Función find_maximum:
```
Input: find_maximum([5, 2, 8, 1, 9])
Output: 9
```

### Función find_minimum:
```
Input: find_minimum([5, 2, 8, 1, 9])
Output: 1
```

### Función compare_numbers:
```
Input: compare_numbers(5, 3)
Output: "5 es mayor que 3"

Input: compare_numbers(2, 7)  
Output: "2 es menor que 7"

Input: compare_numbers(4, 4)
Output: "4 es igual a 4"
```

## Restricciones
- find_maximum debe retornar None si la lista está vacía
- find_minimum debe retornar None si la lista está vacía
- compare_numbers debe retornar strings con el formato exacto mostrado
- Validar que las listas contengan solo números
- No usar funciones built-in max() y min()

## Conceptos a Practicar
- Iteración sobre listas
- Comparaciones numéricas
- Manejo de casos edge (listas vacías)
- Validación de entrada
- Optimización de algoritmos y estructuras de datos

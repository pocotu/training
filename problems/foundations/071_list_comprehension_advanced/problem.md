# [F071] List Comprehension Advanced

## Problema

Escribe una función llamada `filter_and_square` que reciba una lista de números `numbers` y devuelva una nueva lista con solo los números pares elevados al cuadrado, usando list comprehension.

**Simplificado para Foundations**: Se enfoca en una sola función con list comprehension básica.

## Ejemplos

### Ejemplo 1:
```
Input: [1, 2, 3, 4, 5, 6]
Output: [4, 16, 36]  # Solo números pares (2,4,6) elevados al cuadrado
```

### Ejemplo 2:
```
Input: [1, 3, 5, 7]
Output: []  # No hay números pares
```

### Ejemplo 3:
```
Input: [2, 4, 8]
Output: [4, 16, 64]
```

## Restricciones

- `numbers` será una lista de números enteros
- Usar exclusivamente list comprehension
- Devolver nueva lista (no modificar original)
- Manejar lista vacía correctamente
```
Input: ["abc", "hello", "hi", "python"]
Output: ["ABC", "hello", "HI", "python"]  # len=3,5,2,6 → impar,impar,par,par
```

## Restricciones
- Usar obligatoriamente list comprehensions
- No usar bucles for/while tradicionales
- Las listas pueden tener de 0 a 100 elementos
- Los números están entre -100 y 100

## Conceptos a Practicar
- List comprehensions con condiciones
- Comprehensions anidadas
- Operaciones condicionales en comprehensions
- Transformaciones de datos funcionales

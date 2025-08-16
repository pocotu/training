# [F071] List Comprehension Advanced

## Problema

Implementa tres funciones que utilizan list comprehensions avanzadas:
1. `filter_and_square(numbers)` - filtra números pares y los eleva al cuadrado
2. `nested_multiplication(matrix)` - multiplica todos los elementos de una matriz 2D por 2
3. `conditional_transform(words)` - convierte a mayúsculas si la longitud es par, a minúsculas si es impar

## Ejemplos

### Función filter_and_square:
```
Input: [1, 2, 3, 4, 5, 6]
Output: [4, 16, 36]  # Solo números pares (2,4,6) elevados al cuadrado
```

### Función nested_multiplication:
```
Input: [[1, 2], [3, 4], [5, 6]]
Output: [[2, 4], [6, 8], [10, 12]]
```

### Función conditional_transform:
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

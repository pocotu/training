# [F077] Iterator and Generator Basics

## Problema

Implementa tres funciones usando iteradores y generadores:
1. `fibonacci_generator(n)` - genera primeros n números de Fibonacci
2. `even_numbers_iterator(start, end)` - itera números pares en rango
3. `process_large_data(data_list)` - procesa datos usando generador

## Ejemplos

### Función fibonacci_generator:
```
Input: list(fibonacci_generator(7))
Output: [0, 1, 1, 2, 3, 5, 8]
```

### Función even_numbers_iterator:
```
Input: list(even_numbers_iterator(1, 10))
Output: [2, 4, 6, 8, 10]
```

### Función process_large_data:
```
Input: list(process_large_data([1, 2, 3, 4, 5]))
Output: [2, 4, 6, 8, 10]  # duplica cada número
```

## Restricciones
- fibonacci_generator debe usar yield
- even_numbers_iterator debe usar yield
- process_large_data debe usar generador para eficiencia de memoria
- No generar todas las secuencias en memoria de una vez

## Conceptos a Practicar
- Generadores con yield
- Iteradores personalizados
- Evaluación perezosa (lazy evaluation)
- Eficiencia de memoria

# [F049] Deque and Advanced Collections

## Problema

Implementa tres funciones usando collections.deque y otras estructuras avanzadas:

1. `sliding_window_max(arr, k)` - encuentra máximo en ventana deslizante usando deque
2. `palindrome_checker_deque(text)` - verifica palíndromo usando deque
3. `counter_analysis(text)` - analiza frecuencias usando Counter

## Ejemplos

### Función sliding_window_max:
```python
# Encuentra el máximo en cada ventana de tamaño k
arr = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
result = sliding_window_max(arr, k)
print(result)  # [3, 3, 5, 5, 6, 7]
```

### Función palindrome_checker_deque:
```python
text = "A man a plan a canal Panama"
result = palindrome_checker_deque(text)
print(result)  # True
```

### Función counter_analysis:
```python
text = "hello world hello python"
analysis = counter_analysis(text)
print(analysis)
# {
#   "most_common": [("l", 3), ("o", 3), ("h", 2)],
#   "unique_chars": 12,
#   "total_chars": 23
# }
```

## Restricciones
- Usar collections.deque para sliding_window_max
- Usar collections.deque para palindrome_checker_deque (ignorar espacios y mayúsculas)
- Usar collections.Counter para counter_analysis
- sliding_window_max debe ser eficiente O(n)
- Retornar resultados en formato especificado

## Conceptos a Practicar
- Deque para operaciones eficientes en ambos extremos
- Algoritmo de ventana deslizante
- Counter para análisis de frecuencias
- Estructuras de datos especializadas

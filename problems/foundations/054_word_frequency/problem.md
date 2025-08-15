# [F054] Word Frequency

## Problema

Escribe una función llamada `word_frequency` que reciba un string `text` y devuelva un diccionario con la frecuencia de cada palabra. Las palabras deben ser convertidas a minúsculas y se debe ignorar la puntuación básica.

## Ejemplos

### Ejemplo 1:
```
Input: text = "hello world hello"
Output: {"hello": 2, "world": 1}
```

### Ejemplo 2:
```
Input: text = "The quick brown fox"
Output: {"the": 1, "quick": 1, "brown": 1, "fox": 1}
```

## Tags
dictionary, string, frequency, counting, foundations

## Notas Adicionales
- **Complejidad de tiempo**: O(n) donde n es el número de caracteres
- **Complejidad de espacio**: O(k) donde k es el número de palabras únicas
- **Conceptos clave**: Diccionarios, conteo, procesamiento de texto
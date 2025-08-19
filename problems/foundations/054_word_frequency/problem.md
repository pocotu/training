# [F054] Word Frequency

## Problema

Escribe una función llamada `word_frequency` que reciba un string `text` y devuelva un diccionario con la frecuencia de cada palabra. 

**Reglas de procesamiento**:
- Convertir todas las palabras a minúsculas
- Remover signos de puntuación básicos: .,!?;:
- Dividir el texto por espacios en blanco
- Ignorar palabras vacías después del procesamiento

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

### Ejemplo 3:
```
Input: text = "Hello, world! Hello world."
Output: {"hello": 2, "world": 2}
```

## Restricciones

- El texto será un string válido
- Se deben remover únicamente los caracteres: .,!?;:
- Las palabras se separan por espacios en blanco  
- Resultado debe estar en minúsculas

## Tags
dictionary, string, frequency, counting, foundations

## Notas Adicionales
- **Complejidad de tiempo**: O(n) donde n es el número de caracteres
- **Complejidad de espacio**: O(k) donde k es el número de palabras únicas
- **Conceptos clave**: Diccionarios, conteo, procesamiento de texto
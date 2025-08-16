# [F066] Word Counter

## Problema

Escribe una función llamada `count_words` que reciba un texto y devuelva un diccionario con la frecuencia de cada palabra. Las palabras deben ser convertidas a minúsculas y se debe ignorar la puntuación. Solo contar palabras que tengan 2 o más caracteres.

## Ejemplos

### Ejemplo 1:
```
Input: "Hello world! Hello Python world."
Output: {
    'hello': 2,
    'world': 2,
    'python': 1
}
```

### Ejemplo 2:
```
Input: "The quick brown fox jumps over the lazy dog."
Output: {
    'the': 2,
    'quick': 1,
    'brown': 1,
    'fox': 1,
    'jumps': 1,
    'over': 1,
    'lazy': 1,
    'dog': 1
}
```

### Ejemplo 3:
```
Input: "a I am happy"
Output: {
    'am': 1,
    'happy': 1
}
```

## Restricciones
- El texto puede contener letras, números, espacios y puntuación
- Convertir todo a minúsculas
- Ignorar palabras de 1 carácter
- Considerar solo caracteres alfanuméricos para formar palabras

## Conceptos a Practicar
- Procesamiento de texto
- Diccionarios y conteo
- Manipulación de strings
- Expresiones regulares (opcional)

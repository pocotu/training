# [F085] Text Processing Functions

## Problema

Crea tres funciones para procesar texto básico:
1. `count_characters(text)` - cuenta caracteres, excluyendo espacios
2. `reverse_words(sentence)` - invierte el orden de las palabras
3. `capitalize_words(text)` - capitaliza la primera letra de cada palabra

**Foundations**: Se enfoca en operaciones básicas de strings, conceptos fundamentales de Python.

## Ejemplos

### Función count_characters:
```
Input: count_characters("Hola mundo")
Output: 9  # No cuenta espacios
```

### Función reverse_words:
```
Input: reverse_words("Hola mundo Python")
Output: "Python mundo Hola"
```

### Función capitalize_words:
```
Input: capitalize_words("hola mundo python")
Output: "Hola Mundo Python"
```

## Restricciones
- count_characters debe excluir espacios del conteo
- reverse_words debe mantener un solo espacio entre palabras
- capitalize_words debe capitalizar solo la primera letra de cada palabra
- Validar que las entradas sean strings
- Manejar strings vacíos apropiadamente
- No usar métodos built-in como title() para capitalize_words

## Conceptos a Practicar
- Manipulación de strings
- Métodos de strings básicos (split, join)
- Iteración sobre caracteres
- Condicionales con strings
- Integración de múltiples componentes

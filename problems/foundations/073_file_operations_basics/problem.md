# [F073] String Lines Processing

## Problema

Escribe una función llamada `count_lines` que reciba un string `text` con múltiples líneas (separadas por saltos de línea `\n`) y devuelva el número total de líneas no vacías.

**Simplificado para Foundations**: Se enfoca en procesamiento de texto básico en lugar de operaciones de archivos complejas.

## Ejemplos

### Ejemplo 1:
```
Input: count_lines("Línea 1\nLínea 2\nLínea 3")
Output: 3
```

### Ejemplo 2:
```
Input: count_lines("Hola\n\nMundo\n")
Output: 2  # Una línea vacía no cuenta
```

### Ejemplo 3:
```
Input: count_lines("")
Output: 0
```

## Restricciones

- El texto puede contener líneas vacías (solo espacios en blanco)
- Las líneas vacías no deben contarse
- Una línea con solo espacios se considera vacía
- Usar métodos básicos de string (split, strip)
```
Input: count_words_in_file("test.txt") # contenido: "Hola mundo Python es genial"
Output: 5
```

## Restricciones
- Usar with statement para manejo de archivos
- Manejar FileNotFoundError apropiadamente
- write_lines_to_file debe retornar True si es exitoso
- read_lines_from_file debe retornar lista vacía si archivo no existe
- count_words_in_file debe retornar 0 si archivo no existe

## Conceptos a Practicar
- Operaciones de archivo con with statement
- Lectura y escritura de texto
- Manejo de excepciones con archivos
- Split y join de strings

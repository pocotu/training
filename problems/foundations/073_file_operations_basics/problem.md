# [F073] File Operations Basics

## Problema

Implementa tres funciones para operaciones básicas con archivos:
1. `write_lines_to_file(filename, lines)` - escribe lista de líneas a archivo
2. `read_lines_from_file(filename)` - lee todas las líneas de un archivo
3. `count_words_in_file(filename)` - cuenta palabras en un archivo

## Ejemplos

### Función write_lines_to_file:
```
Input: write_lines_to_file("test.txt", ["Hola", "Mundo", "Python"])
Output: True (archivo creado exitosamente)
```

### Función read_lines_from_file:
```
Input: read_lines_from_file("test.txt")
Output: ["Hola\n", "Mundo\n", "Python\n"]
```

### Función count_words_in_file:
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

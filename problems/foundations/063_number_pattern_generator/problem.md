# [F063] Number Pattern Generator

## Problema

Escribe una función llamada `generate_pattern` que reciba un número `n` y genere un patrón numérico en forma de pirámide. La función debe devolver una lista de strings, donde cada string representa una fila del patrón.

## Ejemplos

### Ejemplo 1:
```
Input: n = 3
Output: [
    "  1  ",
    " 1 2 ",
    "1 2 3"
]
```

### Ejemplo 2:
```
Input: n = 4
Output: [
    "   1   ",
    "  1 2  ",
    " 1 2 3 ",
    "1 2 3 4"
]
```

### Ejemplo 3:
```
Input: n = 1
Output: ["1"]
```

## Restricciones
- 1 ≤ n ≤ 9
- Los números están separados por espacios
- Cada fila debe estar centrada respecto a la fila más larga

## Conceptos a Practicar
- Bucles anidados
- Manipulación de strings
- Formateo y alineación de texto
- Patrones matemáticos

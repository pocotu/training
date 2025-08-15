# [040] Valid Palindrome

## Problema

Una frase es un palíndromo si, después de convertir todas las letras mayúsculas a minúsculas y eliminar todos los caracteres no alfanuméricos, se lee igual hacia adelante y hacia atrás. Los caracteres alfanuméricos incluyen letras y números.

Dado un string `s`, devuelve `true` si es un palíndromo, o `false` en caso contrario.

## Input/Output
- **Input**: `s` - string a verificar
- **Output**: `True` si es palíndromo, `False` en caso contrario

## Constraints
- 1 ≤ s.length ≤ 2 * 10^5
- s consiste solo de caracteres ASCII imprimibles

## Ejemplos

### Ejemplo 1:
```
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explicación: "amanaplanacanalpanama" es un palíndromo.
```

### Ejemplo 2:
```
Input: s = "race a car"
Output: false
Explicación: "raceacar" no es un palíndromo.
```

## Tags
two-pointers, string

## Notas Adicionales
- **Complejidad de tiempo esperada**: O(n)
- **Complejidad de espacio esperada**: O(1)
- **Conceptos clave**: Two pointers, string processing, palindrome
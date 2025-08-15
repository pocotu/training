# [F057] Anagram Check

## Problema

Escribe una función llamada `are_anagrams` que reciba dos strings `str1` y `str2` y devuelva `True` si son anagramas, `False` en caso contrario. Dos palabras son anagramas si contienen exactamente las mismas letras con la misma frecuencia.

## Ejemplos

### Ejemplo 1:
```
Input: str1 = "listen", str2 = "silent"
Output: True
```

### Ejemplo 2:
```
Input: str1 = "hello", str2 = "world"
Output: False
```

### Ejemplo 3:
```
Input: str1 = "evil", str2 = "vile"
Output: True
```

## Tags
string, anagram, sorting, frequency, foundations

## Notas Adicionales
- **Complejidad de tiempo**: O(n log n) con sorting, O(n) con counting
- **Complejidad de espacio**: O(1) con sorting, O(k) con counting donde k es el alfabeto
- **Conceptos clave**: Anagramas, ordenamiento, conteo de caracteres
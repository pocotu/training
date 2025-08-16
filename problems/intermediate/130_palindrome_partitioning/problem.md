# [130] Palindrome Partitioning

## Problema
Dada una cadena `s`, particiona `s` tal que cada subcadena de la partición sea un palíndromo. 

Retorna todas las particiones palíndromas posibles de `s`.

## Input/Output
- **Input**: `s` (string - cadena de caracteres en minúsculas)
- **Output**: List[List[str]] - todas las particiones palíndromas posibles

## Constraints
- 1 ≤ s.length ≤ 16
- s contiene solo letras inglesas en minúsculas

## Ejemplos

### Ejemplo 1:
```
Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]
Explicación: 
- "a", "a", "b" son todos palíndromos
- "aa", "b" son todos palíndromos
```

### Ejemplo 2:
```
Input: s = "raceacar"
Output: [["r","a","c","e","a","c","a","r"],
         ["r","a","c","e","aca","r"],
         ["r","a","c","eae","c","a","r"],
         ["r","ace","a","c","a","r"],
         ["race","a","c","a","r"],
         ["r","a","cec","a","r"],
         ["r","aceca","r"],
         ["raceacar"]]
```

### Ejemplo 3 (Edge Case):
```
Input: s = "a"
Output: [["a"]]
```

## Explicación
Necesitamos encontrar todas las formas de dividir la cadena donde cada parte sea un palíndromo. Usamos backtracking para explorar todas las posibles particiones.

## Hints
- Usa backtracking para explorar todas las particiones
- Para cada posición, prueba todas las subcadenas que empiecen ahí
- Verifica si cada subcadena es un palíndromo antes de continuar
- Optimiza la verificación de palíndromos con DP si es necesario

## Tags
string, backtracking, dynamic-programming

## Notas Adicionales
- **Complejidad de tiempo esperada**: O(n * 2^n) donde n es la longitud de la cadena
- **Complejidad de espacio esperada**: O(n) para la recursión

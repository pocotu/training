# [016] Valid Parentheses

## Problema
Dada una cadena `s` que contiene solo los caracteres `'('`, `')'`, `'{'`, `'}'`, `'['` y `']'`, determina si la cadena de entrada es válida.

Una cadena de entrada es válida si:
1. Los paréntesis abiertos se cierran con el mismo tipo de paréntesis.
2. Los paréntesis abiertos se cierran en el orden correcto.
3. Cada paréntesis de cierre tiene un paréntesis de apertura correspondiente del mismo tipo.

## Input/Output
- **Input**: `s` (string) - Cadena que contiene paréntesis
- **Output**: `bool` - True si la cadena es válida, False en caso contrario

## Constraints
- 1 ≤ s.length ≤ 10^4
- s consiste solo en paréntesis `'()[]{}'`

## Ejemplos

### Ejemplo 1:
```
Input: s = "()"
Output: True
```

### Ejemplo 2:
```
Input: s = "()[]{}"
Output: True
```

### Ejemplo 3:
```
Input: s = "(]"
Output: False
```

### Ejemplo 4:
```
Input: s = "([)]"
Output: False
```

### Ejemplo 5:
```
Input: s = "{[]}"
Output: True
```

## Explicación
Utiliza una pila (stack) para rastrear los paréntesis de apertura. Para cada carácter:
1. Si es un paréntesis de apertura (`(`, `{`, `[`), lo empuja a la pila
2. Si es un paréntesis de cierre (`)`, `}`, `]`), verifica si coincide con el último paréntesis de apertura en la pila
3. Si coincide, retira el paréntesis de la pila; si no, la cadena es inválida
4. Al final, la pila debe estar vacía para que la cadena sea válida

## Tags
stack, string, easy, leetcode

## Notas Adicionales
- **Complejidad de tiempo**: O(n)
- **Complejidad de espacio**: O(n)
- **Dificultad**: Easy
- **Conceptos clave**: Stack (pila), matching de caracteres

---

### Instrucciones para completar:
1. Visitar https://leetcode.com/problems/problem-20/
2. Copiar el enunciado completo en la sección "Problema"
3. Actualizar Input/Output con información específica
4. Copiar constraints exactos de LeetCode
5. Copiar todos los ejemplos de LeetCode
6. Agregar explicación detallada del approach
7. Incluir tags apropiados del repositorio
8. Actualizar complejidades después de resolver
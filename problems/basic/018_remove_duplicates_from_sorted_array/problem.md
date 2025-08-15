# [018] Remove Duplicates from Sorted Array

## Problema
Dado un array de enteros `nums` ordenado en orden no decreciente, elimina los duplicados in-place de tal manera que cada elemento único aparezca solo una vez. El orden relativo de los elementos debe mantenerse igual. Luego devuelve el número de elementos únicos en `nums`.

Considera el número de elementos únicos de `nums` como `k`, para ser aceptado, necesitas hacer lo siguiente:
- Cambia el array `nums` de tal manera que los primeros `k` elementos de `nums` contengan los elementos únicos en el orden en que estaban presentes en `nums` inicialmente
- Los elementos restantes de `nums` no son importantes, así como el tamaño de `nums`
- Devuelve `k`

## Input/Output
- **Input**: `nums` (List[int]) - Array de enteros ordenado con posibles duplicados
- **Output**: `int` - Número de elementos únicos

## Constraints
- 1 ≤ nums.length ≤ 3 * 10^4
- -100 ≤ nums[i] ≤ 100
- `nums` está ordenado en orden no decreciente

## Ejemplos

### Ejemplo 1:
```
Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explicación: La función debe devolver k = 2, con los primeros dos elementos de nums siendo 1 y 2 respectivamente.
```

### Ejemplo 2:
```
Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
Explicación: La función debe devolver k = 5, con los primeros cinco elementos de nums siendo 0, 1, 2, 3, y 4 respectivamente.
```

## Explicación
Utiliza la técnica de dos punteros:
1. Un puntero lento (`i`) marca la posición del próximo elemento único
2. Un puntero rápido (`j`) explora el array
3. Cuando encuentras un elemento diferente, lo colocas en la posición del puntero lento y avanzas ambos punteros

## Tags
array, two-pointers, easy, leetcode

## Notas Adicionales
- **Complejidad de tiempo**: O(n)
- **Complejidad de espacio**: O(1)
- **Dificultad**: Easy
- **Conceptos clave**: Two pointers, modificación in-place

---

### Instrucciones para completar:
1. Visitar https://leetcode.com/problems/problem-26/
2. Copiar el enunciado completo en la sección "Problema"
3. Actualizar Input/Output con información específica
4. Copiar constraints exactos de LeetCode
5. Copiar todos los ejemplos de LeetCode
6. Agregar explicación detallada del approach
7. Incluir tags apropiados del repositorio
8. Actualizar complejidades después de resolver
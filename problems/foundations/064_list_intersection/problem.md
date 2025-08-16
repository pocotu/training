# [F064] List Intersection

## Problema

Escribe una función llamada `find_intersection` que reciba dos listas y devuelva una nueva lista con los elementos que están presentes en ambas listas (intersección). Los elementos del resultado deben aparecer en el mismo orden que en la primera lista y sin duplicados.

## Ejemplos

### Ejemplo 1:
```
Input: list1 = [1, 2, 3, 4], list2 = [3, 4, 5, 6]
Output: [3, 4]
```

### Ejemplo 2:
```
Input: list1 = ['a', 'b', 'c'], list2 = ['b', 'c', 'd']
Output: ['b', 'c']
```

### Ejemplo 3:
```
Input: list1 = [1, 2, 2, 3], list2 = [2, 3, 3, 4]
Output: [2, 3]
```

### Ejemplo 4:
```
Input: list1 = [1, 2, 3], list2 = [4, 5, 6]
Output: []
```

## Restricciones
- Las listas pueden tener de 0 a 1000 elementos
- Los elementos pueden ser números, strings o cualquier tipo comparable
- El resultado no debe tener elementos duplicados
- Mantener el orden de la primera lista

## Conceptos a Practicar
- Operaciones con listas
- Uso de sets para verificación rápida
- Eliminación de duplicados
- Orden de elementos

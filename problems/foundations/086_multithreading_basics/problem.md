# [F086] List Operations and Processing

## Problema

Implementa tres funciones para operaciones avanzadas con listas:

1. `combine_lists(list1, list2)` - combina dos listas alternando elementos
2. `group_by_length(words_list)` - agrupa palabras por longitud
3. `flatten_nested_list(nested_list)` - aplana lista anidada

**Foundations**: Se enfoca en operaciones con listas, concepto fundamental para estructuras de datos.

## Ejemplos

### Función combine_lists:
```
Input: combine_lists([1, 2, 3], ["a", "b", "c"])
Output: [1, "a", 2, "b", 3, "c"]
```

### Función group_by_length:
```
Input: group_by_length(["casa", "carro", "sol", "luna", "estrella"])
Output: {3: ["sol"], 4: ["casa", "luna"], 5: ["carro"], 8: ["estrella"]}
```

### Función flatten_nested_list:
```
Input: flatten_nested_list([[1, 2], [3, 4, 5], [6]])
Output: [1, 2, 3, 4, 5, 6]
```

## Restricciones
- combine_lists debe alternar elementos hasta agotar ambas listas
- Si una lista es más larga, añadir elementos restantes al final
- group_by_length debe retornar diccionario con longitud como clave
- flatten_nested_list debe manejar listas anidadas de un solo nivel
- Validar que las entradas sean listas válidas

## Conceptos a Practicar
- Manipulación avanzada de listas
- Comprensiones de listas y diccionarios
- Iteración simultánea sobre múltiples listas
- Agrupación y clasificación de datos
- Manejo de resultados concurrentes

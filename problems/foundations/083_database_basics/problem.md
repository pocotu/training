# [F083] Data Storage Using Lists

## Problema

Implementa tres funciones para operaciones básicas de almacenamiento de datos usando listas:
1. `create_user_list()` - crea lista vacía de usuarios
2. `add_user(users_list, name, email, age)` - añade usuario a la lista
3. `get_users_by_age(users_list, min_age)` - obtiene usuarios por edad mínima

**Foundations**: Se enfoca en manejo básico de listas y diccionarios, conceptos fundamentales de Python.

## Ejemplos

### Función create_user_list:
```
Input: create_user_list()
Output: []  # Lista vacía
```

### Función add_user:
```
Input: add_user([], "Ana García", "ana@email.com", 28)
Output: [{"id": 1, "name": "Ana García", "email": "ana@email.com", "age": 28}]
```

### Función get_users_by_age:
```
Input: get_users_by_age([{"id": 1, "name": "Ana García", "email": "ana@email.com", "age": 28}], 25)
Output: [{"id": 1, "name": "Ana García", "email": "ana@email.com", "age": 28}]
```

## Restricciones
- create_user_list debe retornar lista vacía
- add_user debe asignar ID automáticamente (basado en longitud + 1)
- add_user debe retornar la lista actualizada con el nuevo usuario
- get_users_by_age debe filtrar usuarios con edad >= min_age
- Los usuarios deben ser diccionarios con claves: id, name, email, age
- Validar que age sea un entero positivo

## Conceptos a Practicar
- Manejo de listas de diccionarios
- Operaciones de filtrado
- Generación automática de IDs
- Validación de datos de entrada
- Mapeo de resultados a estructuras Python

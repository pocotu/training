# [F083] Database Basics with SQLite

## Problema

Implementa tres funciones para operaciones básicas de base de datos:
1. `create_users_table(db_name)` - crea tabla de usuarios
2. `add_user(db_name, name, email, age)` - añade usuario
3. `get_users_by_age(db_name, min_age)` - obtiene usuarios por edad mínima

## Ejemplos

### Función create_users_table:
```
Input: create_users_table("test.db")
Output: True (tabla creada)
# Tabla: users (id INTEGER PRIMARY KEY, name TEXT, email TEXT, age INTEGER)
```

### Función add_user:
```
Input: add_user("test.db", "Ana García", "ana@email.com", 28)
Output: 1  # ID del usuario insertado
```

### Función get_users_by_age:
```
Input: get_users_by_age("test.db", 25)
Output: [{"id": 1, "name": "Ana García", "email": "ana@email.com", "age": 28}]
```

## Restricciones
- Usar sqlite3 módulo de Python
- create_users_table debe usar IF NOT EXISTS
- add_user debe retornar ID del registro insertado
- get_users_by_age debe retornar lista de diccionarios
- Manejar excepciones de base de datos apropiadamente
- Cerrar conexiones correctamente

## Conceptos a Practicar
- Operaciones CRUD básicas
- Conexiones a base de datos
- Consultas SQL con parámetros
- Manejo de cursores y conexiones
- Mapeo de resultados a estructuras Python

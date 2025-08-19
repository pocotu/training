# [F082] Dictionary Data Processing

## Problema

Escribe una función llamada `process_user_data` que reciba un diccionario `user_data` con información de usuarios y devuelva un diccionario resumen con estadísticas básicas.

**Foundations**: Se enfoca en procesamiento básico de diccionarios y listas, conceptos fundamentales de Python.

## Ejemplos

### Ejemplo 1:
```
Input: {"users": [{"name": "Ana", "age": 25}, {"name": "Bob", "age": 30}]}
Output: {"total_users": 2, "average_age": 27.5, "names": ["Ana", "Bob"]}
```

### Ejemplo 2:
```
Input: {"users": []}
Output: {"total_users": 0, "average_age": 0, "names": []}
```

### Ejemplo 3:
```
Input: {"users": [{"name": "Charlie", "age": 35}]}
Output: {"total_users": 1, "average_age": 35.0, "names": ["Charlie"]}
```

## Restricciones

- `user_data` será un diccionario con clave "users" (lista de diccionarios)
- Cada usuario tiene claves "name" y "age"  
- Si no hay usuarios, average_age debe ser 0
- Devolver diccionario con las tres claves: "total_users", "average_age", "names"
- La edad promedio debe ser un float
- Los nombres deben estar en el mismo orden que en la lista original

## Conceptos a Practicar
- Manejo de diccionarios
- Iteración sobre listas
- Cálculo de promedios
- Construcción de estructuras de datos

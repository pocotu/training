# [F092] Settings Management with Dictionaries

## Problema

Implementa tres funciones para manejo básico de configuraciones:

1. `create_settings(defaults)` - crea diccionario de configuraciones con valores por defecto
2. `update_setting(settings, key, value)` - actualiza una configuración específica
3. `get_setting(settings, key, default)` - obtiene configuración con valor por defecto

**Foundations**: Se enfoca en manejo de diccionarios para configuraciones, concepto básico pero importante.

## Ejemplos

### Función create_settings:
```
Input: create_settings({"theme": "light", "language": "es", "auto_save": True})
Output: {"theme": "light", "language": "es", "auto_save": True}
```

### Función update_setting:
```
Input: update_setting({"theme": "light"}, "theme", "dark")
Output: {"theme": "dark"}
```

### Función get_setting:
```
Input: get_setting({"theme": "dark"}, "language", "en")
Output: "en"  # Retorna default porque 'language' no existe
```

## Restricciones
- create_settings debe crear copia del diccionario de defaults
- update_setting debe modificar el diccionario y retornarlo actualizado
- get_setting debe retornar default si la clave no existe
- Validar que settings sea un diccionario
- Manejar claves None o vacías apropiadamente

## Conceptos a Practicar
- Manipulación de diccionarios
- Valores por defecto
- Métodos de diccionarios (get, update)
- Validación de tipos básica

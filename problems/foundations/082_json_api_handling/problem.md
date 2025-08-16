# [F082] JSON and API Handling

## Problema

Implementa tres funciones para manejo de JSON y APIs:
1. `process_json_file(filename)` - lee y procesa archivo JSON
2. `create_api_request(url, data)` - simula request HTTP con datos
3. `parse_api_response(response)` - procesa respuesta de API

## Ejemplos

### Función process_json_file:
```
# archivo.json: {"usuarios": [{"nombre": "Ana", "edad": 25}]}
Input: process_json_file("archivo.json")
Output: {"total_usuarios": 1, "edad_promedio": 25}
```

### Función create_api_request:
```
Input: create_api_request("https://api.ejemplo.com", {"user": "test"})
Output: {"method": "POST", "url": "https://api.ejemplo.com", "data": {"user": "test"}, "status": "sent"}
```

### Función parse_api_response:
```
Input: parse_api_response('{"success": true, "data": {"id": 123}}')
Output: {"is_valid": True, "success": True, "extracted_id": 123}
```

## Restricciones
- Usar módulos json para parsing
- process_json_file debe manejar FileNotFoundError
- create_api_request debe simular (no hacer request real)
- parse_api_response debe validar JSON válido
- Retornar estructuras de datos apropiadas

## Conceptos a Practicar
- Parsing y serialización JSON
- Manejo de APIs REST
- Validación de datos
- Procesamiento de respuestas HTTP

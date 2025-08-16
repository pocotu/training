# [F048] CSV Data Processing

## Problema

Implementa tres funciones para procesamiento de datos CSV:

1. `create_csv(filename, headers, data)` - crea archivo CSV con headers y datos
2. `read_csv_to_dict(filename)` - lee CSV y convierte a lista de diccionarios  
3. `analyze_csv_data(filename, column)` - analiza columna específica (promedio, máximo, mínimo)

## Ejemplos

### Función create_csv:
```python
headers = ["name", "age", "salary"]
data = [
    ["Ana", 25, 50000],
    ["Luis", 30, 60000],
    ["María", 28, 55000]
]
create_csv("employees.csv", headers, data)
# Crea archivo CSV con formato correcto
```

### Función read_csv_to_dict:
```python
result = read_csv_to_dict("employees.csv")
print(result)
# Output: [
#   {"name": "Ana", "age": "25", "salary": "50000"},
#   {"name": "Luis", "age": "30", "salary": "60000"},
#   {"name": "María", "age": "28", "salary": "55000"}
# ]
```

### Función analyze_csv_data:
```python
stats = analyze_csv_data("employees.csv", "salary")
print(stats)
# Output: {"average": 55000.0, "max": 60000, "min": 50000, "count": 3}
```

## Restricciones
- Usar módulo csv de Python
- create_csv debe manejar cualquier número de columnas
- read_csv_to_dict debe retornar lista de diccionarios
- analyze_csv_data debe convertir valores numéricos automáticamente
- Manejar archivos inexistentes con try-except

## Conceptos a Practicar
- Procesamiento de archivos CSV
- Conversión de datos entre formatos
- Análisis estadístico básico
- Manejo de datos estructurados

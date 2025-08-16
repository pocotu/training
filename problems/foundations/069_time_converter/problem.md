# [F069] Time Converter

## Problema

Implementa tres funciones para convertir tiempo:
1. `seconds_to_hms(seconds)` - convierte segundos a formato "HH:MM:SS"
2. `hms_to_seconds(time_str)` - convierte formato "HH:MM:SS" a segundos totales
3. `add_time(time1, time2)` - suma dos tiempos en formato "HH:MM:SS"

## Ejemplos

### Función seconds_to_hms:
```
Input: 3661
Output: "01:01:01"

Input: 7200
Output: "02:00:00"
```

### Función hms_to_seconds:
```
Input: "01:01:01"
Output: 3661

Input: "02:00:00"
Output: 7200
```

### Función add_time:
```
Input: "01:30:45", "02:15:30"
Output: "03:46:15"

Input: "23:45:30", "00:30:45"
Output: "24:16:15"
```

## Restricciones
- Los segundos de entrada están entre 0 y 86400 (24 horas)
- El formato de tiempo es siempre "HH:MM:SS" con ceros a la izquierda
- La suma de tiempos puede exceder 24 horas
- Todos los valores son válidos (no hay verificación de errores)

## Conceptos a Practicar
- Operaciones matemáticas (división, módulo)
- Formateo de strings
- Parsing de strings
- Manipulación de tiempo

# [F079] Context Managers

## Problema

Implementa tres context managers:
1. `TimerContext` - mide tiempo de ejecución de bloque de código
2. `FileManager(filename, mode)` - maneja archivos con logging
3. `temp_directory()` - crea y limpia directorio temporal

## Ejemplos

### Context manager TimerContext:
```python
with TimerContext():
    time.sleep(1)
    print("Operación completada")
# Output: "Bloque ejecutado en 1.001 segundos"
```

### Context manager FileManager:
```python
with FileManager("test.txt", "w") as f:
    f.write("Hola mundo")
# Automáticamente cierra archivo y registra operación
```

### Context manager temp_directory:
```python
with temp_directory() as temp_dir:
    # Usar directorio temporal
    with open(f"{temp_dir}/temp.txt", "w") as f:
        f.write("temporal")
# Directorio se limpia automáticamente
```

## Restricciones
- Implementar usando __enter__ y __exit__ methods
- TimerContext debe imprimir tiempo al finalizar
- FileManager debe registrar apertura y cierre en logs
- temp_directory debe crear directorio único y limpiarlo al salir
- Manejar excepciones apropiadamente en __exit__

## Conceptos a Practicar
- Context managers con __enter__ y __exit__
- Manejo de recursos automático
- Limpieza de recursos en caso de excepciones
- Logging y debugging

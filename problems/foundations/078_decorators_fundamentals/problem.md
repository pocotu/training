# [F078] Decorators Fundamentals

## Problema

Implementa tres decoradores básicos:
1. `@timing_decorator` - mide tiempo de ejecución de función
2. `@retry_decorator(max_attempts)` - reintenta función en caso de error
3. `@validate_types(*types)` - valida tipos de argumentos

## Ejemplos

### Decorador timing_decorator:
```python
@timing_decorator
def slow_function():
    time.sleep(1)
    return "completado"

# Output: "Función ejecutada en 1.001 segundos"
```

### Decorador retry_decorator:
```python
@retry_decorator(3)
def unreliable_function():
    if random.random() < 0.7:
        raise Exception("Error aleatorio")
    return "éxito"
```

### Decorador validate_types:
```python
@validate_types(int, str)
def process_data(number, text):
    return f"{text}: {number}"

process_data(42, "resultado")  # OK
process_data("42", "resultado")  # Raise TypeError
```

## Restricciones
- timing_decorator debe imprimir tiempo en formato "Función ejecutada en X segundos"
- retry_decorator debe intentar max_attempts veces antes de fallar
- validate_types debe levantar TypeError con mensaje descriptivo
- Usar functools.wraps para preservar metadata

## Conceptos a Practicar
- Decoradores con y sin parámetros
- Funciones de orden superior
- Manejo de argumentos *args y **kwargs
- Preservación de metadata con functools.wraps

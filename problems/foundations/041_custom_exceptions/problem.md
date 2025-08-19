# [F041] Custom Exceptions and Error Handling

## Problema

Crea dos clases de excepción personalizadas y una función que las utilice:

1. **InvalidAgeError** - hereda de ValueError, para edades inválidas (< 0 o > 150)
2. **InsufficientFundsError** - hereda de Exception, para fondos insuficientes  
3. **validate_person(name, age, balance)** - función que valide datos

### Requisitos específicos:
- `InvalidAgeError`: debe incluir la edad inválida en el mensaje
- `InsufficientFundsError`: debe almacenar balance y amount como atributos
- `validate_person`: debe retornar True si todos los datos son válidos

## Ejemplos

### Excepciones personalizadas:
```python
class InvalidAgeError(ValueError):
    """Excepción para edad inválida"""
    pass

class InsufficientFundsError(Exception):
    """Excepción para fondos insuficientes"""
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(f"Saldo insuficiente: ${balance}, necesita: ${amount}")
```

### Función validate_person:
```python
try:
    validate_person("Ana", 25, 1000)
    print("Persona válida")
except (InvalidAgeError, InsufficientFundsError) as e:
    print(f"Error: {e}")
```

## Restricciones
- InvalidAgeError debe heredar de ValueError
- InsufficientFundsError debe incluir balance y amount en el mensaje
- validate_person debe levantar InvalidAgeError si edad < 0 o > 150
- validate_person debe levantar InsufficientFundsError si balance < 0
- Usar super().__init__() en constructores de excepción

## Conceptos a Practicar
- Creación de excepciones personalizadas
- Herencia de excepciones built-in
- Manejo de múltiples tipos de excepción
- Mensajes de error informativos

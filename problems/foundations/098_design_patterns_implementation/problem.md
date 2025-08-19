# [F098] Basic Class Concepts

## Problema

Implementa tres clases básicas que demuestran conceptos fundamentales de OOP:

1. `Counter` - clase simple con métodos increment/decrement/get_value
2. `BankAccount` - clase con atributos privados y métodos de depósito/retiro
3. `Student` - clase con constructor, atributos y método de cálculo de promedio

**Foundations**: Se enfoca en conceptos básicos de clases y objetos, esenciales en programación.

## Ejemplos

### Singleton Pattern:
```python
class DatabaseConnection(Singleton):
    def __init__(self):
        self.connection = None
    
    def connect(self):
        return "Connected to DB"

db1 = DatabaseConnection()
db2 = DatabaseConnection()
assert db1 is db2  # Misma instancia
```

### Factory Pattern:
```python
class ShapeFactory:
    @staticmethod
    def create_shape(shape_type, **kwargs):
        # Retorna Circle, Rectangle, o Triangle según tipo
        pass

factory = ShapeFactory()
circle = factory.create_shape("circle", radius=5)
rectangle = factory.create_shape("rectangle", width=10, height=20)
```

### Observer Pattern:
```python
class NewsAgency(Subject):
    def __init__(self):
        self._observers = []
        self._news = ""

class NewsChannel(Observer):
    def update(self, news):
        print(f"Breaking: {news}")

agency = NewsAgency()
channel1 = NewsChannel("CNN")
channel2 = NewsChannel("BBC")

agency.attach(channel1)
agency.attach(channel2)
agency.set_news("Python 4.0 Released!")  # Notifica a ambos canales
```

## Restricciones
- Singleton debe impedir múltiples instancias
- Factory debe soportar al menos 3 tipos diferentes
- Observer debe permitir attach/detach dinámico
- Implementar interfaces/clases base apropiadas
- Seguir principios SOLID

## Conceptos a Practicar
- Patrones de diseño GoF
- Metaclasses para Singleton
- Abstract Factory pattern
- Publisher-Subscriber pattern
- Desacoplamiento de código

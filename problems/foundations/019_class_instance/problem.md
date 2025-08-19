# [F019] Class Instance

## Problema

Define una clase llamada `Person`. La clase debe tener un constructor `__init__` que reciba un argumento `name` y lo asigne a un atributo de la instancia llamado `name`.

## Ejemplos

### Ejemplo 1:
```
person = Person("John")
print(person.name)  # Output: "John"
```

### Ejemplo 2:
```
person1 = Person("Alice")
person2 = Person("Bob")
print(person1.name)  # Output: "Alice"
print(person2.name)  # Output: "Bob"
```

## Constraints

- La clase debe llamarse `Person`.
- El constructor debe recibir exactamente un argumento `name` (además de `self`).
- El atributo debe llamarse `name` y ser accesible como `instance.name`.

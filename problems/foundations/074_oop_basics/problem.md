# [F074] Object-Oriented Programming Basics

## Problema

Crea una clase `Student` con las siguientes características:
1. Atributos: `name`, `age`, `grades` (lista de calificaciones)
2. Método `add_grade(grade)` - añade calificación a la lista
3. Método `get_average()` - calcula promedio de calificaciones
4. Método `get_info()` - retorna string con información del estudiante

## Ejemplos

### Creación y uso de la clase:
```python
student = Student("Ana", 20)
student.add_grade(85)
student.add_grade(92)
student.add_grade(78)

print(student.get_average())  # Output: 85.0
print(student.get_info())     # Output: "Ana (20 años) - Promedio: 85.0"
```

## Restricciones
- Constructor debe inicializar name, age y grades (lista vacía)
- get_average() debe retornar 0.0 si no hay calificaciones
- get_info() debe seguir el formato exacto mostrado
- Todos los atributos deben ser públicos

## Conceptos a Practicar
- Definición de clases
- Constructor (__init__)
- Métodos de instancia
- Atributos de instancia
- Formateo de strings

# [F065] Grade Calculator

## Problema

Escribe una función llamada `calculate_grade` que reciba una lista de calificaciones (números del 0 al 100) y devuelva un diccionario con las siguientes estadísticas:
- `average`: promedio de las calificaciones
- `letter_grade`: letra correspondiente (A, B, C, D, F)
- `highest`: calificación más alta
- `lowest`: calificación más baja
- `passing`: cantidad de calificaciones aprobatorias (≥ 60)

## Escala de Calificaciones
- A: 90-100
- B: 80-89
- C: 70-79
- D: 60-69
- F: 0-59

## Ejemplos

### Ejemplo 1:
```
Input: [85, 92, 78, 90, 88]
Output: {
    'average': 86.6,
    'letter_grade': 'B',
    'highest': 92,
    'lowest': 78,
    'passing': 5
}
```

### Ejemplo 2:
```
Input: [45, 67, 89, 52]
Output: {
    'average': 63.25,
    'letter_grade': 'D',
    'highest': 89,
    'lowest': 45,
    'passing': 2
}
```

## Restricciones
- La lista siempre tiene al menos 1 calificación
- Todas las calificaciones están entre 0 y 100
- El promedio debe redondearse a 1 decimal

## Conceptos a Practicar
- Operaciones matemáticas básicas
- Diccionarios
- Condicionales múltiples
- Funciones de agregación (min, max)

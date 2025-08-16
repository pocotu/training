# [F081] Unit Testing Fundamentals

## Problema

Crea una clase `Calculator` y su correspondiente test suite completo:
1. Clase `Calculator` con métodos: add, subtract, multiply, divide, power
2. `TestCalculator` con tests para todos los casos (normales y edge cases)
3. Función `run_test_coverage()` que ejecute y reporte cobertura

## Ejemplos

### Clase Calculator:
```python
calc = Calculator()
print(calc.add(2, 3))      # 5
print(calc.divide(10, 2))  # 5.0
print(calc.power(2, 3))    # 8
```

### Test cases:
```python
class TestCalculator(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(self.calc.add(2, 3), 5)
    
    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            self.calc.divide(10, 0)
```

### Función run_test_coverage:
```
Input: run_test_coverage()
Output: "Tests ejecutados: 15, Exitosos: 15, Fallidos: 0, Cobertura: 100%"
```

## Restricciones
- Calculator.divide debe levantar ValueError si divisor es 0
- Incluir tests para valores positivos, negativos, cero y decimales
- Usar setUp y tearDown apropiadamente
- run_test_coverage debe retornar estadísticas como string
- Incluir al menos 15 test cases diferentes

## Conceptos a Practicar
- Diseño de test suites
- Test cases comprehensivos
- Manejo de excepciones en tests
- setUp y tearDown methods
- Assertions múltiples

# [F081] Simple Calculator

## Problema

Escribe una función llamada `calculator` que reciba tres parámetros: dos números `a` y `b`, y una operación `operation` (string: "add", "subtract", "multiply", "divide"). La función debe devolver el resultado de la operación.

**Simplificado para Foundations**: Se enfoca en lógica condicional básica y operaciones matemáticas.

## Ejemplos

### Ejemplo 1:
```
Input: calculator(5, 3, "add")
Output: 8
```

### Ejemplo 2:
```
Input: calculator(10, 2, "divide")
Output: 5.0
```

### Ejemplo 3:
```
Input: calculator(4, 3, "multiply")
Output: 12
```

## Restricciones

- `a` y `b` serán números (int o float)
- `operation` será uno de: "add", "subtract", "multiply", "divide"
- Para división por cero, devolver "Error"
- Para operación inválida, devolver "Error"
    
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

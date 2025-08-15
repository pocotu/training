# [039] Best Time to Buy and Sell Stock

## Problema

Se te da un array `prices` donde `prices[i]` es el precio de una acción dada en el día i.

Quieres maximizar tu ganancia eligiendo un solo día para comprar una acción y eligiendo un día diferente en el futuro para vender esa acción.

Devuelve la ganancia máxima que puedes lograr de esta transacción. Si no puedes lograr ninguna ganancia, devuelve 0.

## Input/Output
- **Input**: `prices` - array de precios de acciones
- **Output**: Ganancia máxima posible

## Constraints
- 1 ≤ prices.length ≤ 10^5
- 0 ≤ prices[i] ≤ 10^4

## Ejemplos

### Ejemplo 1:
```
Input: prices = [7,1,5,3,6,4]
Output: 5
Explicación: Compra en el día 2 (precio = 1) y vende en el día 5 (precio = 6), ganancia = 6-1 = 5.
```

### Ejemplo 2:
```
Input: prices = [7,6,4,3,1]
Output: 0
Explicación: En este caso, no se realiza ninguna transacción y la ganancia máxima = 0.
```

## Tags
array, dynamic-programming

## Notas Adicionales
- **Complejidad de tiempo esperada**: O(n)
- **Complejidad de espacio esperada**: O(1)
- **Conceptos clave**: Máximo profit, one-pass algorithm, tracking minimum
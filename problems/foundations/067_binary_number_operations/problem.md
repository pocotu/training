# [F067] Binary Number Operations

## Problema

Implementa tres funciones para trabajar con números binarios:
1. `decimal_to_binary(num)` - convierte un número decimal a binario (string)
2. `binary_to_decimal(binary_str)` - convierte un string binario a decimal
3. `binary_add(bin1, bin2)` - suma dos números binarios y devuelve el resultado en binario

## Ejemplos

### Función decimal_to_binary:
```
Input: 10
Output: "1010"

Input: 7
Output: "111"
```

### Función binary_to_decimal:
```
Input: "1010"
Output: 10

Input: "111"
Output: 7
```

### Función binary_add:
```
Input: "1010", "111"
Output: "10001"

Input: "101", "110"
Output: "1011"
```

## Restricciones
- Los números decimales son enteros positivos (0-1000)
- Los strings binarios solo contienen '0' y '1'
- No uses las funciones built-in bin() o int() con base 2
- Implementa la lógica manualmente

## Conceptos a Practicar
- Sistemas numéricos
- Algoritmos de conversión
- Operaciones bit a bit
- Manipulación de strings

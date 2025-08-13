# 📝 Ejercicio 02: Suma Simple

**Dificultad:** ⭐ (Muy Fácil)  
**Conceptos:** Entrada de datos, operaciones básicas  
**Tiempo estimado:** 10 minutos

## 🎯 **Objetivo:**
Lee dos números y muestra su suma.

## 📋 **Problema:**
Escribe un programa que lea dos números enteros y muestre su suma.

### **Entrada:**
Una línea con dos números enteros separados por espacio.

### **Salida:**
Un número entero que es la suma de los dos números de entrada.

### **Ejemplo:**
```
Entrada: 5 3
Salida: 8
```

### **Más ejemplos:**
```
Entrada: 10 -2
Salida: 8

Entrada: 0 100
Salida: 100
```

## 💡 **Pistas:**
<details>
<summary>💭 Pista 1 (clic para ver)</summary>

En Python: usa `input().split()` y `map(int, ...)` para leer dos números
En C++: usa `cin >> a >> b` para leer dos variables
</details>

<details>
<summary>💭 Pista 2 (clic para ver)</summary>

Recuerda que en Python `input()` devuelve texto, necesitas convertir a entero con `int()`
</details>

## ✅ **Soluciones:**

<details>
<summary>🐍 Solución en Python</summary>

```python
# Leer dos números en una línea
a, b = map(int, input().split())

# Calcular la suma
suma = a + b

# Mostrar el resultado
print(suma)
```

**Versión más corta:**
```python
a, b = map(int, input().split())
print(a + b)
```
</details>

<details>
<summary>⚡ Solución en C++</summary>

```cpp
#include <iostream>
using namespace std;

int main() {
    int a, b;
    
    // Leer dos números
    cin >> a >> b;
    
    // Calcular y mostrar la suma
    cout << a + b << endl;
    
    return 0;
}
```
</details>

## 🧪 **Prueba tu solución:**

Prueba con estos casos:
1. Entrada: `5 3` → Salida esperada: `8`
2. Entrada: `10 -2` → Salida esperada: `8`
3. Entrada: `0 0` → Salida esperada: `0`

## 🎓 **¿Qué aprendiste?**
- Cómo leer múltiples valores en una línea
- Realizar operaciones matemáticas básicas
- Mostrar el resultado

---

**➡️ Siguiente: [03-calculadora-basica.md](03-calculadora-basica.md)** 🧮

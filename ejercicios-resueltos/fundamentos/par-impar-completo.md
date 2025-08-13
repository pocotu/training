# 🎓 Par o Impar - Análisis Completo

Un análisis profundo del problema más básico de programación competitiva.

## 📋 **Enunciado del problema:**
Dado un número entero, determina si es par o impar.

**Entrada:** Un entero n (-10^9 ≤ n ≤ 10^9)  
**Salida:** "Par" si es par, "Impar" si es impar

### **Ejemplos:**
```
Entrada: 4    → Salida: Par
Entrada: 7    → Salida: Impar  
Entrada: 0    → Salida: Par
Entrada: -3   → Salida: Impar
```

## 🤔 **Análisis inicial:**

### **¿Qué nos piden?**
- Clasificar un número según su paridad
- Un número es par si es divisible por 2
- Un número es impar si no es divisible por 2

### **¿Qué necesitamos saber?**
- Operador módulo (%) para obtener el resto de una división
- Condicionales (if/else)
- Entrada y salida básica

## 💡 **Estrategia:**

### **Enfoque matemático:**
Un número n es par si n % 2 == 0, caso contrario es impar.

### **¿Por qué funciona?**
- El operador % devuelve el resto de la división
- Si n % 2 == 0, significa que n es divisible por 2 → par
- Si n % 2 == 1 (o != 0), significa que sobra 1 → impar

## ⚙️ **Implementación paso a paso:**

### **Paso 1:** Leer el número
### **Paso 2:** Calcular n % 2  
### **Paso 3:** Comparar con 0
### **Paso 4:** Mostrar resultado correspondiente

## 🐍 **Solución en Python:**

### **Versión básica (para principiantes):**
```python
# Leer el número
n = int(input())

# Calcular el resto de dividir por 2
resto = n % 2

# Verificar la paridad
if resto == 0:
    print("Par")
else:
    print("Impar")
```

### **Versión optimizada:**
```python
n = int(input())
print("Par" if n % 2 == 0 else "Impar")
```

### **Versión con función:**
```python
def es_par(n):
    return n % 2 == 0

n = int(input())
if es_par(n):
    print("Par")
else:
    print("Impar")
```

## ⚡ **Solución en C++:**

### **Versión básica:**
```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;
    
    if (n % 2 == 0) {
        cout << "Par" << endl;
    } else {
        cout << "Impar" << endl;
    }
    
    return 0;
}
```

### **Versión optimizada:**
```cpp
#include <iostream>
using namespace std;

int main() {
    int n;
    cin >> n;
    cout << (n % 2 == 0 ? "Par" : "Impar") << endl;
    return 0;
}
```

## 🧪 **Casos de prueba explicados:**

### **Caso 1: Número positivo par**
```
Entrada: 4
4 % 2 = 0 → Es par
Salida: Par ✅
```

### **Caso 2: Número positivo impar**
```
Entrada: 7  
7 % 2 = 1 → Es impar
Salida: Impar ✅
```

### **Caso 3: Cero**
```
Entrada: 0
0 % 2 = 0 → Es par (cero es par por definición)
Salida: Par ✅
```

### **Caso 4: Número negativo**
```
Entrada: -3
-3 % 2 = -1 (en algunos lenguajes) o 1
En ambos casos != 0 → Es impar
Salida: Impar ✅
```

## 📈 **Análisis de complejidad:**

- **Tiempo:** O(1) - Operación constante
- **Espacio:** O(1) - Solo usamos variables auxiliares constantes

## 🎯 **Variaciones del problema:**

### **Variación 1: Múltiples casos**
```
Entrada:
3
4
7
0

Salida:
Par
Impar
Par
```

**Solución:**
```python
t = int(input())
for _ in range(t):
    n = int(input())
    print("Par" if n % 2 == 0 else "Impar")
```

### **Variación 2: Array de números**
```
Entrada: 5
1 2 3 4 5

Salida: 
Impar Par Impar Par Impar
```

**Solución:**
```python
n = int(input())
numeros = list(map(int, input().split()))
resultado = []
for num in numeros:
    resultado.append("Par" if num % 2 == 0 else "Impar")
print(" ".join(resultado))
```

## ❌ **Errores comunes que evitar:**

### **Error 1: Confundir operadores**
```python
❌ if n / 2 == 0:     # División, no módulo
✅ if n % 2 == 0:     # Módulo correcto
```

### **Error 2: No manejar números negativos**
```python
❌ Solo probar con números positivos
✅ Probar también con -1, -2, -3, etc.
```

### **Error 3: Olvidar el caso cero**
```python
❌ No considerar que 0 es par
✅ Recordar que 0 % 2 == 0
```

### **Error 4: Formato de salida incorrecto**
```python
❌ print("par")      # Minúscula
❌ print("PAR")      # Mayúscula completa
✅ print("Par")      # Como pide el problema
```

## 🎓 **¿Qué aprendiste?**

- ✅ Uso del operador módulo (%)
- ✅ Condicionales simples
- ✅ Manejo de casos especiales (cero, negativos)
- ✅ Optimización de código (operador ternario)
- ✅ Importancia del formato exacto de salida

## 🚀 **¿Qué sigue?**

- Problemas con múltiples condiciones
- Rangos de números (mayor, menor, entre valores)
- Operaciones matemáticas más complejas

---

**➡️ Siguiente ejemplo: [suma-array-variaciones.md](suma-array-variaciones.md)** ➕

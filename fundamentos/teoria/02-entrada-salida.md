# 📥📤 Entrada y Salida de Datos

En programación competitiva, **leer la entrada correctamente** es crucial. Un error aquí puede arruinar tu solución perfecta.

## 🎯 **¿Por qué es importante?**

Los problemas de competencia tienen un formato específico:
- 📄 **Entrada:** Datos que tu programa debe leer
- 🧮 **Procesamiento:** Tu algoritmo trabaja con esos datos  
- 📋 **Salida:** Resultado que debes mostrar exactamente como pide

## 🐍 **Entrada y Salida en Python**

### **Leer una línea:**
```python
# Leer un número entero
n = int(input())

# Leer una cadena
nombre = input()

# Leer un número decimal
precio = float(input())
```

### **Leer múltiples valores en una línea:**
```python
# Ejemplo: "5 3" -> a=5, b=3
a, b = map(int, input().split())

# Ejemplo: "Juan 25 1.75" -> nombre, edad, altura
nombre, edad, altura = input().split()
edad = int(edad)
altura = float(altura)
```

### **Leer una lista de números:**
```python
# Ejemplo: "1 2 3 4 5" -> [1, 2, 3, 4, 5]
numeros = list(map(int, input().split()))
```

### **Mostrar resultados:**
```python
# Imprimir un valor
print(resultado)

# Imprimir múltiples valores separados por espacio
print(a, b, c)

# Imprimir sin salto de línea
print(valor, end=" ")

# Formato específico
print(f"La respuesta es {resultado}")
```

## ⚡ **Entrada y Salida en C++**

### **Leer valores básicos:**
```cpp
#include <iostream>
using namespace std;

int main() {
    // Leer un número entero
    int n;
    cin >> n;
    
    // Leer múltiples valores
    int a, b;
    cin >> a >> b;
    
    // Leer una cadena (una palabra)
    string palabra;
    cin >> palabra;
    
    // Leer una línea completa
    string linea;
    getline(cin, linea);
    
    return 0;
}
```

### **Leer arrays/vectores:**
```cpp
#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n;
    cin >> n;  // Tamaño del array
    
    vector<int> numeros(n);
    for(int i = 0; i < n; i++) {
        cin >> numeros[i];
    }
    
    return 0;
}
```

### **Mostrar resultados:**
```cpp
// Imprimir un valor
cout << resultado << endl;

// Imprimir múltiples valores
cout << a << " " << b << " " << c << endl;

// Imprimir sin salto de línea
cout << valor << " ";
```

## 📝 **Patrones comunes de entrada:**

### **Patrón 1: Un solo caso**
```
Entrada:
5 3

Tu código:
```
```python
# Python
a, b = map(int, input().split())
print(a + b)
```
```cpp
// C++
int a, b;
cin >> a >> b;
cout << a + b << endl;
```

### **Patrón 2: Múltiples casos de prueba**
```
Entrada:
3     (número de casos)
5 3   (caso 1)
2 7   (caso 2)  
1 1   (caso 3)

Tu código:
```
```python
# Python
t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    print(a + b)
```
```cpp
// C++
int t;
cin >> t;
while(t--) {
    int a, b;
    cin >> a >> b;
    cout << a + b << endl;
}
```

### **Patrón 3: Array de números**
```
Entrada:
5           (tamaño)
1 2 3 4 5   (elementos)

Tu código:
```
```python
# Python
n = int(input())
arr = list(map(int, input().split()))
print(sum(arr))
```
```cpp
// C++
int n;
cin >> n;
vector<int> arr(n);
for(int i = 0; i < n; i++) {
    cin >> arr[i];
}
```

## ⚡ **Optimización para C++:**

Para problemas con mucha entrada/salida:
```cpp
#include <iostream>
using namespace std;

int main() {
    // Acelera entrada/salida
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    
    // Tu código aquí...
    
    return 0;
}
```

## 🧪 **Ejercicio práctico:**

**Problema:** Lee dos números y muestra su suma, resta, multiplicación y división.

**Entrada:**
```
10 3
```

**Salida esperada:**
```
Suma: 13
Resta: 7
Multiplicación: 30
División: 3.33
```

### **Tu turno:** ¡Intenta resolverlo antes de ver la solución!

<details>
<summary>🔍 Ver solución en Python</summary>

```python
a, b = map(int, input().split())
print(f"Suma: {a + b}")
print(f"Resta: {a - b}")
print(f"Multiplicación: {a * b}")
print(f"División: {a / b:.2f}")
```
</details>

<details>
<summary>🔍 Ver solución en C++</summary>

```cpp
#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    int a, b;
    cin >> a >> b;
    
    cout << "Suma: " << a + b << endl;
    cout << "Resta: " << a - b << endl;
    cout << "Multiplicación: " << a * b << endl;
    cout << "División: " << fixed << setprecision(2) << (double)a / b << endl;
    
    return 0;
}
```
</details>

## ✅ **Checkpoint:**
Antes de continuar, asegúrate de que puedes:
- [ ] Leer un número entero
- [ ] Leer múltiples números en una línea
- [ ] Leer un array de números
- [ ] Mostrar resultados con el formato correcto
- [ ] Manejar múltiples casos de prueba

---

**➡️ Siguiente: [03-condicionales.md](03-condicionales.md)** 🔀

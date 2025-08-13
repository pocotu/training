# 🚀 Sintaxis Básica para Programación Competitiva

En programación competitiva necesitas escribir código rápido y eficiente. Aquí aprenderás lo esencial.

## 🐍 **Python - Tu primera opción (recomendado para principiantes)**

### **¿Por qué Python?**
- ✅ Sintaxis simple y clara
- ✅ Menos código para mismas funciones
- ✅ Ideal para aprender algoritmos sin complicarse con sintaxis
- ❌ Más lento que C++ (pero suficiente para la mayoría de problemas)

### **Conceptos básicos:**

```python
# Variables - no necesitas declararlas
numero = 42
texto = "Hola mundo"
decimal = 3.14
es_verdad = True

# Tipos de datos básicos
entero = 10          # int
decimal = 10.5       # float
cadena = "texto"     # string
booleano = True      # bool

# Listas (arrays dinámicos)
numeros = [1, 2, 3, 4, 5]
nombres = ["Ana", "Luis", "Maria"]

# Imprimir en pantalla
print("Hola mundo")
print("El resultado es:", numero)
```

## ⚡ **C++ - La opción profesional**

### **¿Por qué C++?**
- ✅ Estándar en competencias internacionales
- ✅ Muy rápido en ejecución
- ✅ Control completo sobre memoria
- ❌ Sintaxis más compleja
- ❌ Más código para funciones simples

### **Conceptos básicos:**

```cpp
#include <iostream>
using namespace std;

int main() {
    // Variables - debes declararlas con tipo
    int numero = 42;
    string texto = "Hola mundo";
    double decimal = 3.14;
    bool es_verdad = true;
    
    // Arrays (tamaño fijo)
    int numeros[5] = {1, 2, 3, 4, 5};
    
    // Vectores (arrays dinámicos)
    vector<int> lista = {1, 2, 3, 4, 5};
    
    // Imprimir en pantalla
    cout << "Hola mundo" << endl;
    cout << "El resultado es: " << numero << endl;
    
    return 0;
}
```

## 📝 **Ejercicio práctico:**

**Crea tu primer programa que:**
1. Declare una variable con tu edad
2. Declare una variable con tu nombre
3. Imprima: "Hola, soy [nombre] y tengo [edad] años"

### **Solución en Python:**
```python
edad = 20
nombre = "Maria"
print(f"Hola, soy {nombre} y tengo {edad} años")
```

### **Solución en C++:**
```cpp
#include <iostream>
#include <string>
using namespace std;

int main() {
    int edad = 20;
    string nombre = "Maria";
    cout << "Hola, soy " << nombre << " y tengo " << edad << " años" << endl;
    return 0;
}
```

## 🎯 **¿Qué lenguaje elegir?**

### **Elige Python si:**
- 🆕 Eres completamente nuevo en programación
- 📚 Quieres enfocarte en aprender algoritmos
- ⏰ Prefieres escribir código rápidamente

### **Elige C++ si:**
- 💻 Ya tienes experiencia programando
- 🏆 Planeas competir a nivel internacional
- ⚡ Te importa la velocidad de ejecución

## ✅ **Checkpoint:**
Antes de continuar, asegúrate de que puedes:
- [ ] Crear variables de diferentes tipos
- [ ] Usar cout/print para mostrar información
- [ ] Compilar/ejecutar tu programa sin errores

---

**➡️ Siguiente: [02-entrada-salida.md](02-entrada-salida.md)** 📖

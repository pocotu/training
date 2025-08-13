# 🚀 Cómo Empezar en Programación Competitiva

Una guía completa para configurar tu entorno y dar tus primeros pasos.

## 🎯 **Requisitos previos**

### **Conocimientos mínimos:**
- [ ] **Programación básica** en cualquier lenguaje (variables, if/else, bucles)
- [ ] **Matemáticas de secundaria** (álgebra básica, no necesitas cálculo)
- [ ] **Inglés básico** para leer problemas (muchos están en inglés)
- [ ] **Ganas de aprender** y paciencia (es difícil al principio)

### **Equipo necesario:**
- [ ] **Computadora** con internet (no necesita ser potente)
- [ ] **2-3 horas libres por semana** mínimo para ver progreso
- [ ] **Ambiente tranquilo** para concentrarte

## 💻 **Configuración del entorno**

### **Paso 1: Elige tu lenguaje**

#### **🐍 Python (recomendado para principiantes):**
**Ventajas:**
- ✅ Sintaxis simple y clara
- ✅ Menos líneas de código
- ✅ Ideal para aprender algoritmos
- ✅ Funciones built-in útiles

**Desventajas:**
- ❌ Más lento que C++
- ❌ Algunos problemas requieren optimización extra

**¿Cuándo elegir Python?**
- Eres nuevo en programación
- Quieres enfocarte en algoritmos, no en sintaxis
- Prefieres escribir código rápido

#### **⚡ C++ (estándar en competencias):**
**Ventajas:**
- ✅ Muy rápido en ejecución
- ✅ Estándar en competencias internacionales
- ✅ Control completo sobre rendimiento
- ✅ Bibliotecas optimizadas (STL)

**Desventajas:**
- ❌ Sintaxis más compleja
- ❌ Más líneas de código
- ❌ Manejo manual de memoria

**¿Cuándo elegir C++?**
- Ya tienes experiencia programando
- Planeas competir seriamente
- Te importa la velocidad de ejecución

### **Paso 2: Instalar herramientas**

#### **Para Python:**

**Windows:**
1. Descarga Python desde [python.org](https://python.org)
2. Instala VS Code desde [code.visualstudio.com](https://code.visualstudio.com)
3. Instala extensión "Python" en VS Code
4. Verifica en terminal: `python --version`

**macOS/Linux:**
```bash
# macOS (con Homebrew)
brew install python3

# Ubuntu/Debian
sudo apt-get install python3 python3-pip

# Verificar
python3 --version
```

#### **Para C++:**

**Windows:**
1. Instala MinGW-w64 o Visual Studio Community
2. Instala VS Code
3. Instala extensión "C/C++"
4. Verifica en terminal: `g++ --version`

**macOS:**
```bash
# Instalar Xcode command line tools
xcode-select --install

# Verificar
g++ --version
```

**Linux:**
```bash
# Ubuntu/Debian
sudo apt-get install build-essential

# Fedora
sudo dnf install gcc-c++

# Verificar
g++ --version
```

### **Paso 3: Configurar VS Code**

#### **Extensiones esenciales:**
- **Python**: Para desarrollo en Python
- **C/C++**: Para desarrollo en C++
- **Code Runner**: Para ejecutar código rápidamente
- **Competitive Programming Helper**: Automatiza tareas comunes

#### **Configuración recomendada:**
```json
// settings.json
{
    "code-runner.executorMap": {
        "python": "python -u",
        "cpp": "cd $dir && g++ -o $fileNameWithoutExt $fileName -std=c++17 && ./$fileNameWithoutExt"
    },
    "code-runner.runInTerminal": true,
    "files.autoSave": "afterDelay"
}
```

## 🌐 **Crear cuentas en plataformas**

### **Paso 1: Codeforces**
1. Ve a [codeforces.com](https://codeforces.com)
2. Crea cuenta → "Register"
3. Elige un handle (nombre de usuario) memorable
4. Verifica tu email

### **Paso 2: AtCoder**
1. Ve a [atcoder.jp](https://atcoder.jp)
2. Crea cuenta → "Sign Up"
3. Mismo handle que Codeforces (recomendado)

### **Paso 3: LeetCode**
1. Ve a [leetcode.com](https://leetcode.com)
2. Crea cuenta (puedes usar Google/GitHub)
3. Mantén consistencia en usernames

## 🧪 **Tu primer problema**

### **Problema clásico: A + B**

**Enunciado:** Lee dos números enteros A y B, muestra su suma.

**Entrada:**
```
5 3
```

**Salida:**
```
8
```

#### **Solución en Python:**
```python
# Leer dos números
a, b = map(int, input().split())

# Mostrar la suma
print(a + b)
```

#### **Solución en C++:**
```cpp
#include <iostream>
using namespace std;

int main() {
    int a, b;
    cin >> a >> b;
    cout << a + b << endl;
    return 0;
}
```

### **¿Dónde practicar este problema?**
- **Codeforces:** Busca "A+B" en problemset
- **AtCoder:** ABC001 - A
- **LeetCode:** No tienen este formato exacto

## 🎯 **Tu primer día (plan de 2 horas)**

### **Hora 1: Configuración**
- [ ] **30 min:** Instalar todo (Python/C++ + VS Code)
- [ ] **15 min:** Crear cuentas en plataformas
- [ ] **15 min:** Probar que todo funciona

### **Hora 2: Primera práctica**
- [ ] **30 min:** Resolver "A+B" en ambos lenguajes
- [ ] **15 min:** Resolver 2-3 problemas más de AtCoder ABC (problemas A)
- [ ] **15 min:** Explorar interfaces de las plataformas

## 📅 **Tu primera semana**

### **Día 1:** Configuración + primer problema
### **Día 2:** 3-4 problemas tipo A de AtCoder
### **Día 3:** Descanso o leer teoría básica
### **Día 4:** 3-4 problemas más, experimentar con entrada/salida
### **Día 5:** Revisar soluciones de otros, comparar estilos
### **Día 6:** Participar en AtCoder ABC (virtual) - solo problemas A
### **Día 7:** Reflexionar sobre la semana, planear la siguiente

## 🆘 **Problemas comunes y soluciones**

### **"Mi código no compila"**
- ✅ Verifica sintaxis básica
- ✅ Asegúrate de tener las bibliotecas correctas
- ✅ En C++: revisa los includes y using namespace

### **"Wrong Answer"**
- ✅ Lee el problema de nuevo, cuidadosamente
- ✅ Prueba con los casos de ejemplo manualmente
- ✅ Verifica el formato de salida exacto

### **"Time Limit Exceeded"**
- ✅ En Python: usa `input = sys.stdin.readline`
- ✅ En C++: usa `ios_base::sync_with_stdio(false)`
- ✅ Revisa si tu algoritmo es eficiente

### **"No entiendo el problema"**
- ✅ Lee varias veces, despacio
- ✅ Dibuja los casos de ejemplo en papel
- ✅ Busca el problema en foros o YouTube

## 🎉 **¡Felicitaciones!**

Si llegaste hasta aquí y resolviste tu primer problema, ¡ya eres oficialmente un programador competitivo principiante!

### **🎯 ¿Qué sigue?**
1. Ve a [fundamentos/](../fundamentos/) para aprender sintaxis sistemáticamente
2. Resuelve 1-2 problemas diarios por 2 semanas
3. Cuando te sientas cómodo, avanza a [intermedio/](../intermedio/)

### **📊 Objetivos para tu primer mes:**
- [ ] Resolver 30+ problemas tipo A
- [ ] Participar en 2+ concursos virtuales
- [ ] Elegir tu lenguaje principal (Python o C++)
- [ ] Entender cómo leer entrada y mostrar salida correctamente

---

**➡️ Siguiente: [fundamentos/README.md](../fundamentos/README.md)** 📚

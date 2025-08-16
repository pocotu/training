# 🏆 Competitive Programming Practice

## �🚀 Instalación y Configuración

### Prerequisitos
- Python 3.8+
- Git

### Instalación
```bash
# 1. Clonar el repositorio
git clone <repo-url>
cd training

# 2. Instalar dependencias
pip install pytest PyYAML
```

## 📚 Cómo Usar el Proyecto

### 1. Elegir un Problema por Categoría

#### 🟢 **Foundations (F001-F070)** - Fundamentos de Python
Ideal para principiantes, cubre conceptos básicos de programación.
```bash
# Ver problemas de fundamentos
ls problems/foundations/
# Ejemplos: variables, funciones, clases, estructuras básicas
```

#### 🟡 **Basic (001-045)** - Algoritmos Básicos  
Algoritmos fundamentales y estructuras de datos básicas.
```bash
# Ver problemas básicos
ls problems/basic/
# Ejemplos: two sum, binary search, sorting algorithms
```

#### 🟠 **Intermediate (101-130)** - Nivel Intermedio
Algoritmos intermedios y estructuras de datos avanzadas.
```bash
# Ver problemas intermedios
ls problems/intermediate/
# Ejemplos: trees, graphs, dynamic programming básico
```

#### 🔴 **Advanced (201-240)** - Nivel Avanzado
Problemas complejos de nivel competitivo.
```bash
# Ver problemas avanzados  
ls problems/advanced/
# Ejemplos: advanced DP, graph algorithms, complex data structures
```

### 2. Resolver un Problema
```bash
# Navegar al problema elegido
cd problems/basic/001_two_sum/

# Leer el enunciado
cat problem.md

# Ver metadata del problema
cat meta.yaml

# Implementar la solución en solution.py
# Ejecutar tests
pytest test.py -v
```


## 🎯 Comandos Principales

### Sistema de Tracking Avanzado
```bash
# Ver estadísticas completas del proyecto
python tools/tracker.py

### Ejecutar Tests
```powershell
# Test de un problema específico
pytest problems\foundations\001_hello_world\test.py -v
pytest problems\basic\001_two_sum\test.py -v
pytest problems\intermediate\101_add_two_numbers\test.py -v
pytest problems\advanced\201_wildcard_matching\test.py -v

# Test de toda una categoría
pytest problems\foundations -v
pytest problems\basic -v
pytest problems\intermediate -v
pytest problems\advanced -v

# Test de todo el repositorio
pytest problems -v
```

### Herramientas de Desarrollo
```bash
# Generar nuevos problemas automáticamente
python tools/leetcode_scraper.py <número> <dificultad>

# Tracking de contests
python tools/contest_tracker.py

# Marcar problema como resuelto
echo "F001" >> solved.txt  # Para foundations
echo "001" >> solved.txt  # Para basic
echo "101" >> solved.txt  # Para intermediate
echo "201" >> solved.txt  # Para advanced
```

## ⚡ Flujo de Trabajo Recomendado

### Para Principiantes (Ruta Foundations → Basic)
1. **Empezar con Foundations**: `cd problems/foundations/001_hello_world/`
2. **Leer**: `cat problem.md` → entender conceptos básicos
3. **Implementar**: editar `solution.py` con fundamentos de Python
4. **Probar**: `pytest test.py -v`
5. **Avanzar**: completar F001-F070 antes de pasar a Basic

### Para Nivel Intermedio (Ruta Basic → Intermediate)
1. **Explorar Basic**: `ls problems/basic/` → algoritmos fundamentales
2. **Leer enunciado**: `cat problem.md` + `cat meta.yaml`
3. **Implementar**: múltiples enfoques en `solution.py`
4. **Probar**: `pytest test.py -v`
5. **Progreso**: `python tools/tracker.py`
6. **Avanzar**: pasar a Intermediate después de dominar Basic

### Para Nivel Avanzado (Ruta Advanced)
1. **Seleccionar problema**: `problems/advanced/` → problemas complejos
2. **Análizar**: estudiar constraints y casos edge
3. **Múltiples soluciones**: implementar diferentes algoritmos
4. **Optimización**: analizar complejidad temporal y espacial
5. **Testing exhaustivo**: casos edge y performance

## 🛠️ Herramientas y Características

### 📊 **Sistema de Tracking Inteligente**
```bash
python tools/tracker.py
```
- **Conteo automático**: Detecta todos los ejercicios automáticamente
- **Estadísticas por dificultad**: Foundations, Basic, Intermediate, Advanced
- **Estadísticas por fuente**: LeetCode, Internal, Custom, Codeforces  
- **Detección de inconsistencias**: Valida metadata vs ubicación física
- **Progreso personalizado**: Lee desde `solved.txt`
- **Encoding robusto**: Maneja Unicode en Windows correctamente

### 🔧 **Generador de Problemas**
```bash
python tools/leetcode_scraper.py <numero> <dificultad>
```
- Crea automáticamente estructura completa de problema
- Descarga enunciado desde LeetCode
- Genera templates de solución y testing
- Crea metadata estructurada

### 🏆 **Sistema de Contests**
```bash
python tools/contest_tracker.py
```
- Tracking de contests en tiempo real
- Simulación de ambiente competitivo
- Métricas de performance


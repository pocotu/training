# 🏆 Competitive Programming Practice

## 🚀 Instalación y Configuración

### Prerequisitos
- Python 3.8+
- Git

### Instalación
```bash
# 1. Clonar el repositorio
git clone <repo-url>
cd competitive-programming-practice

# 2. Instalar dependencias
pip install pytest PyYAML
```

## 📚 Cómo Usar el Proyecto

### 1. Elegir un Problema
```bash
# Ver problemas disponibles por categoría
ls problems/basic/      # Problemas básicos (001-099)
ls problems/intermediate/   # Problemas intermedios (101-199) 
ls problems/advanced/   # Problemas avanzados (201-299)
```

### 2. Resolver un Problema
```bash
# Navegar al problema elegido
cd problems/basic/001_two_sum/

# Leer el enunciado
cat problem.md

# Implementar la solución en solution.py
# Ejecutar tests
pytest test.py -v
```

### 3. Ver Tu Progreso
```bash
# Ver estadísticas generales
python tools/tracker.py

# Ver progreso detallado
python tools/tracker.py --detailed
```

## 🎯 Comandos Principales

### Ejecutar Tests
```powershell
# Test de un problema específico
pytest problems\basic\001_two_sum\test.py -v

# Test de toda una categoría
pytest problems\basic -v

# Test de todo el repositorio
pytest problems -v
```

### Agregar Nuevos Problemas
```bash
# Crear problema automáticamente desde LeetCode
python tools/leetcode_scraper.py <número> <dificultad>

# Ejemplos:
python tools/leetcode_scraper.py 153 intermediate
python tools/leetcode_scraper.py 42 advanced
```

### Tracking de Progreso
```bash
# Ver resumen de progreso
python tools/tracker.py

# Marcar problema como resuelto (se agrega automáticamente al resolver)
echo "001" >> solved.txt
```

## ⚡ Flujo de Trabajo Recomendado

1. **Explorar**: `ls problems/basic/` → elegir problema
2. **Leer**: `cat problem.md` → entender el enunciado
3. **Implementar**: editar `solution.py`
4. **Probar**: `pytest test.py -v`
5. **Verificar progreso**: `python tools/tracker.py`

## 📊 Categorías de Problemas

- **🟢 Basic**: Problemas fundamentales (15-30 min)
- **🟡 Intermediate**: Algoritmos intermedios (30-60 min)  
- **🔴 Advanced**: Problemas complejos (60+ min)

## 🛠️ Herramientas Útiles

```bash
# Ver progreso general
python tools/tracker.py

# Crear nuevo problema
python tools/leetcode_scraper.py <numero> <dificultad>

# Contest tracking (requiere PyYAML)
python tools/contest_tracker.py
```

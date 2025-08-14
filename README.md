# 🏆 Competitive Programming Practice

### 📋 Prerequisitos
- **Python 3.8+** (Verificado compatible con 3.8, 3.9, 3.10, 3.11, 3.12)
- **Git** para clonar el repositorio
- **Conexión a internet** para usar scraping tools (opcional)

### ⚡ Instalación Rápida
```bash
# 1. Clonar el repositorio
git clone <repo-url>
cd competitive-programming-practice

# 2. Instalar dependencias mínimas
pip install pytest  # Para ejecutar tests
# pip install pyyaml  # Opcional: para herramientas avanzadas

# 3. Verificar instalación
python tools/tracker.py  # Debería mostrar estadísticas
```

### 🎮 Uso Inmediato
```bash
# Ver progreso general del repositorio
python tools/tracker.py

# Ver estadísticas de contests (requiere PyYAML)
python tools/contest_tracker.py

# Ejecutar todos los tests (Bash/Linux/macOS)
./tools/run_tests.sh

# Crear nuevo problema de LeetCode automáticamente
python tools/leetcode_scraper.py 153 intermediate
```

## 🧭 Cómo usar este proyecto (rápido)

Si solo quieres practicar y correr tests, ignora los archivos YAML. Te basta con tres cosas: `problem.md` (leer), `solution.py` (programar), `test.py` (probar).

1) Abrir un problema
- Ve a `problems/<nivel>/<id_nombre>/` (por ejemplo: `problems/intermediate/0002-add-two-numbers/`).
- Lee el enunciado en `problem.md`.

2) Implementar
- Edita `solution.py` y crea/usa las funciones o clases que `test.py` importa.

3) Ejecutar tests (Windows PowerShell)
- Problema específico:
```powershell
pytest problems\intermediate\0002-add-two-numbers\test.py -v
```
- Una categoría completa:
```powershell
pytest problems\intermediate -v
```
- Todo el repositorio:
```powershell
pytest problems -v
```

Notas
- El script `tools/run_tests.sh` es para Bash (WSL/macOS/Linux). En Windows usa directamente `pytest` como arriba.
- Los YAML (`meta.yaml`) son solo metadata para herramientas; no necesitas tocarlos para resolver problemas.

## 📊 Sistema de Seguimiento y Métricas

### 🎯 Categorías de Dificultad:
- **🟢 Basic (001-015)**: Problemas fundamentales - LeetCode Easy
  - Enfoque: Arrays, strings, matemáticas básicas
  - Tiempo esperado: 15-30 minutos por problema
  - Ideal para: Beginners y warm-up
  
- **🟡 Intermediate (101-120)**: Algoritmos intermedios - LeetCode Medium  
  - Enfoque: DP, árboles, grafos, sliding window
  - Tiempo esperado: 30-60 minutos por problema
  - Ideal para: Preparación de interviews
  
- **🔴 Advanced (201-215)**: Problemas complejos - LeetCode Hard
  - Enfoque: Algoritmos avanzados, optimizaciones
  - Tiempo esperado: 60+ minutos por problema
  - Ideal para: Contests y challenges avanzados

### 🏆 Plataformas Integradas:
- **LeetCode**: Weekly, Biweekly, Daily challenges
- **Codeforces**: Div2, Div3, Educational rounds
- **Extensible**: Preparado para HackerRank, AtCoder, etc.

### 📈 Métricas Automatizadas:
- Total de problemas resueltos por dificultad
- Porcentaje de completitud por categoría
- Tests passing rate
- Tiempo promedio de resolución
- Progress tracking en `solved.txt`

## 🎯 Flujo de Trabajo Completo

### 1. 🔍 Explorar y Elegir Problema
```bash
# Ver todos los problemas disponibles
ls problems/basic/     # 15 problemas básicos
ls problems/intermediate/  # 28 problemas intermedios  
ls problems/advanced/  # 27 problemas avanzados

# Navegar a un problema específico
cd problems/basic/001_two_sum/
ls  # Verás: meta.yaml, problem.md, test.py, solution.py
```

### 2. 📖 Leer Enunciado y Metadata
```bash
# Leer el enunciado completo
cat problem.md  # Descripción, ejemplos, constraints

# Ver metadata del problema
cat meta.yaml   # Dificultad, tags, tiempo límite, etc.
```

### 3. 💻 Implementar Solución
```python
# Editar solution.py en la carpeta del problema
def two_sum(nums, target):
    """
    Tu implementación aquí
    
    Args:
        nums: List[int] - Lista de números
        target: int - Número objetivo
    
    Returns:
        List[int] - Índices de los dos números
    """
    # Implementación
    pass
```

### 4. 🧪 Ejecutar Tests
```bash
# Ejecutar tests específicos del problema actual
pytest test.py -v

# Ejecutar tests de toda una categoría
pytest ../basic/ -v

# Ejecutar TODOS los tests del repositorio
cd ../../  # Volver al root
./tools/run_tests.sh

# Tests con detalles de coverage
pytest --cov=. problems/basic/001_two_sum/test.py
```

### 5. ✅ Marcar como Resuelto
```bash
# Agregar manualmente a solved.txt
echo "001" >> ../../solved.txt

# Verificar progreso actualizado
python ../../tools/tracker.py
```

## 🛠️ Herramientas Profesionales

### 📊 Tracker de Progreso (`tracker.py`)
```bash
python tools/tracker.py

# Salida ejemplo:
# 📊 COMPETITIVE PROGRAMMING PROGRESS
# ====================================
# 🟢 Basic: 9/15 (60.0%)
# 🟡 Intermediate: 15/28 (53.6%) 
# 🔴 Advanced: 8/27 (29.6%)
# 📈 Total: 32/70 (45.7%)
```

### 🏆 Contest Tracker (`contest_tracker.py`)
```bash
python tools/contest_tracker.py   # Requiere: pip install pyyaml

# Muestra:
# - Resumen por plataforma y tipo
# - Detalle por contest y problemas
# - Análisis de rendimiento básico
```

### ⚡ LeetCode Scraper (`leetcode_scraper.py`)
```bash
# Sintaxis: python tools/leetcode_scraper.py <número> <dificultad>
python tools/leetcode_scraper.py 153 intermediate

# Crea automáticamente:
# problems/intermediate/153_find_minimum/
# ├── problem.md     # Enunciado completo
# ├── meta.yaml      # Metadata estructurada
# ├── test.py        # Tests base
# └── solution.py    # Template de solución
```

### 🧪 Test Runner (`run_tests.sh`)
```bash
# Ejecutar todos los tests con reporte completo
./tools/run_tests.sh

# Salida incluye:
# - Tests pasados/fallidos por categoría
# - Tiempo de ejecución
# - Coverage de código
# - Resumen de problemas sin tests
```

## 📝 Política de Soluciones y Formatos

### 📄 Estructura de Archivos por Problema
Cada problema sigue una estructura estandarizada:

```
problems/[category]/[id]_[name]/
├── problem.md      # Enunciado completo del problema
├── meta.yaml       # Metadata estructurada
├── solution.py     # Solución principal
├── test.py         # Tests automatizados con pytest
└── README.md       # Notas adicionales (opcional)
```

### 🏷️ Formato de Metadata (`meta.yaml`)
```yaml
id: "001"
title: "Two Sum"
difficulty: "basic"              # basic, intermediate, advanced
tags: ["array", "hashmap"]       # Tags técnicos
time_limit_minutes: 15          # Tiempo objetivo
source: "leetcode"              # Plataforma origen
source_problem_id: "1"          # ID en la plataforma
url: "https://leetcode.com/problems/two-sum/"
solved: false                   # Estado de resolución
date_added: "2025-08-14"        # Fecha de creación
```

### 📖 Formato de Enunciado (`problem.md`)
```markdown
# [001] Two Sum

## 📋 Descripción
Descripción clara y concisa del problema...

## 📥 Input
- Formato de entrada con tipos de datos
- Rango de valores permitidos

## 📤 Output  
- Formato esperado de salida
- Tipo de retorno específico

## ⚠️ Constraints
- n == nums.length
- 2 ≤ n ≤ 10^4
- -10^9 ≤ nums[i] ≤ 10^9

## 💡 Ejemplos

### Ejemplo 1:
```
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: nums[0] + nums[1] == 9
```

### Ejemplo 2:
```
Input: nums = [3,2,4], target = 6
Output: [1,2]
```
```

### 🧪 Formato de Tests (`test.py`)
```python
import pytest
from solution import two_sum

class TestTwoSum:
    def test_basic_case(self):
        assert two_sum([2,7,11,15], 9) == [0,1]
    
    def test_edge_case(self):
        assert two_sum([3,3], 6) == [0,1]
    
    def test_negative_numbers(self):
        assert two_sum([-1,-2,-3,-4,-5], -8) == [2,4]

    @pytest.mark.parametrize("nums,target,expected", [
        ([2,7,11,15], 9, [0,1]),
        ([3,2,4], 6, [1,2]),
        ([3,3], 6, [0,1])
    ])
    def test_multiple_cases(self, nums, target, expected):
        assert two_sum(nums, target) == expected
```

## 🏷️ Sistema de Tags Técnicos

### 📊 Estructuras de Datos:
- `array`, `string`, `hashmap`, `set`
- `stack`, `queue`, `deque`, `heap`
- `linked-list`, `doubly-linked-list`
- `binary-tree`, `bst`, `trie`
- `graph`, `matrix`, `sparse-table`

### ⚡ Algoritmos:
- `two-pointer`, `sliding-window`, `prefix-sum`
- `binary-search`, `ternary-search`
- `dfs`, `bfs`, `topological-sort`
- `dp`, `memoization`, `tabulation`
- `greedy`, `backtracking`, `divide-conquer`

### 🧮 Matemáticas y Lógica:
- `math`, `number-theory`, `modular-arithmetic`
- `combinatorics`, `probability`, `geometry`
- `bit-manipulation`, `bitmasking`

### 🚀 Avanzados:
- `segment-tree`, `fenwick-tree`, `sparse-table`
- `union-find`, `kmp`, `rolling-hash`
- `flow-networks`, `bipartite-matching`

## 🎯 Guía de Agregar Problemas de Plataformas

### ➕ Desde LeetCode (Automático)
```bash
# Usar el scraper automático
python tools/leetcode_scraper.py <problem_number> <difficulty>

# Ejemplos:
python tools/leetcode_scraper.py 153 intermediate
python tools/leetcode_scraper.py 42 advanced
python tools/leetcode_scraper.py 1 basic
```

### ➕ Manualmente (Cualquier Plataforma)
```bash
# 1. Crear directorio con formato correcto
mkdir problems/intermediate/151_new_problem

# 2. Copiar templates (Bash/WSL). En Windows copia archivos manualmente desde templates/
cp templates/* problems/intermediate/151_new_problem/

# 3. Editar archivos según el problema
# - Modificar meta.yaml con datos correctos
# - Escribir problem.md con enunciado
# - Implementar test.py con casos de prueba
# - Crear solution.py base

# 4. Validar con tests
# Windows PowerShell
pytest problems\intermediate\151_new_problem\test.py
# Bash/WSL/macOS
# pytest problems/intermediate/151_new_problem/test.py
```

### 🎯 KPIs Principales
```bash
python tools/tracker.py --detailed

# Output ejemplo:
# 📊 DETAILED PROGRESS REPORT
# ===========================
# Overall: 32/70 problems (45.7%)
# 
# By Difficulty:
# 🟢 Basic: 12/15 (80.0%) - STRONG
# 🟡 Intermediate: 15/28 (53.6%) - AVERAGE  
# 🔴 Advanced: 5/27 (18.5%) - FOCUS NEEDED
#
# By Topic:
# Array: 15/20 (75.0%)
# DP: 8/15 (53.3%)
# Graph: 4/12 (33.3%)
#
# Recent Activity:
# Last 7 days: 5 problems solved
# Avg time/problem: 28 minutes
# Success rate: 78%
```
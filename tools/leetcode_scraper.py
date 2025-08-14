#!/usr/bin/env python3
"""
Competitive Programming Practice - LeetCode Problem Scraper

Herramienta para crear estructuras rápidas de problemas de LeetCode.
Genera carpetas con templates listos para usar.

Uso:
    python tools/leetcode_scraper.py <problem_number> [difficulty]
    python tools/leetcode_scraper.py 153 intermediate
    python tools/leetcode_scraper.py 1 basic
    python tools/leetcode_scraper.py 297 advanced
    
Características:
- Crea carpeta con nombre estándar
- Genera meta.yaml con información básica
- Copia templates de problem.md y test.py
- Asigna ID automáticamente según dificultad
"""

import os
import sys
import shutil
import argparse
from pathlib import Path
from typing import Optional, Dict
from datetime import datetime

class Colors:
    """Colores para terminal"""
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    END = '\033[0m'

class LeetCodeScraper:
    """Generador de estructura para problemas de LeetCode"""
    
    def __init__(self, repo_path: str = "."):
        self.repo_path = Path(repo_path)
        self.problems_path = self.repo_path / "problems"
        self.templates_path = self.repo_path / "templates"
        
        # Mapeo de dificultades
        self.difficulty_mapping = {
            "easy": "basic",
            "medium": "intermediate", 
            "hard": "advanced",
            "basic": "basic",
            "intermediate": "intermediate",
            "advanced": "advanced"
        }
        
        # Rangos de IDs por dificultad
        self.id_ranges = {
            "basic": (1, 99),
            "intermediate": (101, 199),
            "advanced": (201, 299)
        }
        
        # Verificar estructura del repositorio
        self._verify_repository_structure()
    
    def _verify_repository_structure(self) -> None:
        """Verificar que la estructura del repositorio sea correcta"""
        required_dirs = [
            self.problems_path,
            self.problems_path / "basic",
            self.problems_path / "intermediate", 
            self.problems_path / "advanced",
            self.templates_path
        ]
        
        for dir_path in required_dirs:
            if not dir_path.exists():
                print(f"{Colors.RED}❌ Error: Directorio requerido no encontrado: {dir_path}{Colors.END}")
                print(f"{Colors.YELLOW}   Asegúrate de ejecutar desde el directorio raíz del repositorio{Colors.END}")
                sys.exit(1)
        
        # Verificar templates
        required_templates = [
            self.templates_path / "meta_template.yaml",
            self.templates_path / "problem_template.md",
            self.templates_path / "test_template.py"
        ]
        
        for template in required_templates:
            if not template.exists():
                print(f"{Colors.YELLOW}⚠️  Template no encontrado: {template}{Colors.END}")
    
    def _get_next_available_id(self, difficulty: str) -> str:
        """Obtener el siguiente ID disponible para una dificultad"""
        difficulty_dir = self.problems_path / difficulty
        
        # Obtener IDs existentes
        existing_ids = set()
        if difficulty_dir.exists():
            for problem_dir in difficulty_dir.iterdir():
                if problem_dir.is_dir():
                    # Extraer ID del nombre del directorio
                    dir_name = problem_dir.name
                    if '_' in dir_name:
                        potential_id = dir_name.split('_')[0]
                        if potential_id.isdigit():
                            existing_ids.add(int(potential_id))
        
        # Encontrar el siguiente ID disponible en el rango
        start_range, end_range = self.id_ranges[difficulty]
        for i in range(start_range, end_range + 1):
            if i not in existing_ids:
                return f"{i:03d}"
        
        # Si no hay IDs disponibles en el rango, usar el siguiente después del máximo
        if existing_ids:
            next_id = max(existing_ids) + 1
            return f"{next_id:03d}"
        else:
            return f"{start_range:03d}"
    
    def _normalize_title(self, title: str) -> str:
        """Normalizar título para nombre de carpeta"""
        # Convertir a minúsculas y reemplazar espacios/caracteres especiales
        normalized = title.lower()
        normalized = ''.join(c if c.isalnum() else '_' for c in normalized)
        normalized = '_'.join(filter(None, normalized.split('_')))  # Remover underscores múltiples
        return normalized[:50]  # Limitar longitud
    
    def _create_meta_yaml(self, problem_id: str, leetcode_number: str, difficulty: str, title: str = None) -> str:
        """Crear contenido del archivo meta.yaml"""
        if title is None:
            title = f"LeetCode {leetcode_number}"
        
        current_date = datetime.now().strftime("%Y-%m-%d")
        
        # Tiempo estimado por dificultad
        time_estimates = {
            "basic": 20,
            "intermediate": 45,
            "advanced": 90
        }
        
        meta_content = f'''# Meta information for LeetCode Problem {leetcode_number}
# Generated automatically by leetcode_scraper.py

# Basic Information (REQUIRED)
id: "{problem_id}"
title: "{title}"
difficulty: "{difficulty}"

# Problem Classification (REQUIRED)
tags: 
  - "to_categorize"                   # TODO: Update with actual tags after reading problem
  - "leetcode"                        # Platform tag

# Time and Source Information (REQUIRED)
time_minutes: {time_estimates[difficulty]}        # Estimated solve time for {difficulty} level
source: "leetcode"
problem_id: "{leetcode_number}"
url: "https://leetcode.com/problems/problem-{leetcode_number}/"

# Contest Information (OPTIONAL - remove if not a contest problem)
# contest_info:
#   type: "weekly"                    # weekly | biweekly | daily
#   number: "XXX"                     # Contest number
#   position: "1"                     # Problem position (1, 2, 3, 4)
#   date: "{current_date}"            # Contest date

# Problem Characteristics (OPTIONAL)
complexity:
  time: "O(?)"                        # TODO: Update after solving
  space: "O(?)"                       # TODO: Update after solving

# Learning Objectives (OPTIONAL)
learning_objectives:
  - "Practice core algorithm concepts"
  - "Improve problem-solving speed"
  - "Master {difficulty}-level techniques"

# Additional Notes (OPTIONAL)
notes: "Generated by leetcode_scraper.py on {current_date}. Please update with actual problem information."

# TODO List for completion:
# 1. Update title with actual problem name
# 2. Replace URL with correct LeetCode problem URL
# 3. Add appropriate tags from the official tag list
# 4. Update time and space complexity after solving
# 5. Remove or complete contest_info section
# 6. Add meaningful learning objectives'''
        
        return meta_content
    
    def _create_problem_md(self, problem_id: str, leetcode_number: str, title: str = None) -> str:
        """Crear contenido del archivo problem.md"""
        if title is None:
            title = f"LeetCode {leetcode_number}"
        
        problem_content = f'''# [{problem_id}] {title}

## Problema
[TODO: Copiar el enunciado completo del problema desde LeetCode]

Visita: https://leetcode.com/problems/problem-{leetcode_number}/

## Input/Output
- **Input**: [TODO: Describir formato de entrada]
- **Output**: [TODO: Describir formato de salida esperado]

## Constraints
- [TODO: Copiar constraints desde LeetCode]
- Ejemplo: n ≤ 10^4
- Ejemplo: values ≤ 10^9

## Ejemplos

### Ejemplo 1:
```
Input: [TODO: Copiar desde LeetCode]
Output: [TODO: Copiar desde LeetCode]
```

### Ejemplo 2:
```
Input: [TODO: Copiar desde LeetCode]
Output: [TODO: Copiar desde LeetCode]
```

### Ejemplo 3 (Edge Case):
```
Input: [TODO: Agregar caso límite]
Output: [TODO: Salida esperada]
```

## Explicación
[TODO: Explicar el algoritmo y la lógica de solución]

## Hints
- [TODO: Agregar pista sobre estructura de datos]
- [TODO: Agregar pista sobre algoritmo]
- [TODO: Agregar pista sobre complejidad]

## Tags
[TODO: Agregar tags apropiados], leetcode

## Notas Adicionales
- **Complejidad de tiempo esperada**: O(?)
- **Complejidad de espacio esperada**: O(?)
- **Dificultad**: {leetcode_number}
- **Conceptos clave**: [TODO: Enumerar conceptos a practicar]

---

### Instrucciones para completar:
1. Visitar https://leetcode.com/problems/problem-{leetcode_number}/
2. Copiar el enunciado completo en la sección "Problema"
3. Actualizar Input/Output con información específica
4. Copiar constraints exactos de LeetCode
5. Copiar todos los ejemplos de LeetCode
6. Agregar explicación detallada del approach
7. Incluir tags apropiados del repositorio
8. Actualizar complejidades después de resolver'''
        
        return problem_content
    
    def _create_test_py(self, problem_id: str, leetcode_number: str) -> str:
        """Crear contenido básico para test.py"""
        test_content = f'''"""
Test cases for LeetCode Problem {leetcode_number}
Problem ID: {problem_id}

This file contains test cases for the LeetCode problem.
Update the test cases with actual examples from the problem statement.

Usage:
    pytest test.py -v
"""

import pytest
import sys
import os

# Add the current directory to the Python path to import solution
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# TODO: Uncomment and update import based on your solution function name
# from solution import solution_function_name

class TestLeetCode{leetcode_number}:
    """Test class for LeetCode Problem {leetcode_number}"""
    
    def test_example_1(self):
        """Test example 1 from LeetCode"""
        # TODO: Update with actual test case from LeetCode
        # Example:
        # input_data = example_input_1
        # expected_output = expected_result_1
        # assert solution_function_name(input_data) == expected_output
        
        # Placeholder assertion - remove when implementing actual tests
        assert True, "Replace this with actual test case from LeetCode example 1"
    
    def test_example_2(self):
        """Test example 2 from LeetCode"""
        # TODO: Update with actual test case from LeetCode
        assert True, "Replace this with actual test case from LeetCode example 2"
    
    def test_edge_cases(self):
        """Test edge cases"""
        # TODO: Add edge cases like:
        # - Minimum input size
        # - Maximum input size (within constraints)
        # - Empty inputs (if applicable)
        # - Single element inputs
        # - Boundary values
        
        assert True, "Add edge cases based on problem constraints"
    
    def test_corner_cases(self):
        """Test corner cases specific to this problem"""
        # TODO: Add problem-specific corner cases like:
        # - Special values (zeros, negatives, etc.)
        # - Duplicate values
        # - Sorted/reverse-sorted inputs
        # - Any problem-specific edge conditions
        
        assert True, "Add corner cases specific to this LeetCode problem"

# TODO: Uncomment when you have a solution implemented
# def test_solution_exists():
#     """Test that solution file and function exist"""
#     try:
#         from solution import solution_function_name
#         assert callable(solution_function_name)
#     except ImportError:
#         pytest.fail("solution.py file or solution function not found")

if __name__ == "__main__":
    # Run tests when script is executed directly
    pytest.main([__file__, "-v"])

"""
Instructions for completing the tests:

1. COPY EXAMPLES FROM LEETCODE:
   - Go to https://leetcode.com/problems/problem-{leetcode_number}/
   - Copy all provided examples into test_example_1, test_example_2, etc.

2. UPDATE IMPORTS:
   - Create solution.py with your solution function
   - Update the import statement with the correct function name

3. ADD EDGE CASES:
   - Test minimum and maximum input sizes
   - Test boundary values from constraints
   - Test empty inputs if applicable

4. ADD CORNER CASES:
   - Test problem-specific edge conditions
   - Consider special values and patterns

5. RUN TESTS:
   - Run: pytest test.py -v
   - Ensure all tests pass with your solution

6. PERFORMANCE TESTING (optional):
   - Add tests with large inputs to verify time complexity
   - Test with maximum constraint values
"""'''
        
        return test_content
    
    def create_leetcode_problem(self, leetcode_number: str, difficulty: str = "basic", title: str = None) -> None:
        """Crear estructura completa para un problema de LeetCode"""
        
        # Normalizar dificultad
        difficulty = self.difficulty_mapping.get(difficulty.lower(), "basic")
        
        # Obtener ID automáticamente
        problem_id = self._get_next_available_id(difficulty)
        
        # Crear nombre de carpeta
        if title:
            normalized_title = self._normalize_title(title)
            folder_name = f"{problem_id}_{normalized_title}"
        else:
            folder_name = f"{problem_id}_leetcode_{leetcode_number}"
        
        # Crear ruta de carpeta
        problem_dir = self.problems_path / difficulty / folder_name
        
        print(f"{Colors.CYAN}🚀 Creando problema de LeetCode {leetcode_number}...{Colors.END}")
        print(f"{Colors.BLUE}   ID asignado: {problem_id}{Colors.END}")
        print(f"{Colors.BLUE}   Dificultad: {difficulty}{Colors.END}")
        print(f"{Colors.BLUE}   Carpeta: {problem_dir.relative_to(self.repo_path)}{Colors.END}")
        
        # Verificar si ya existe
        if problem_dir.exists():
            print(f"{Colors.YELLOW}⚠️  La carpeta ya existe: {problem_dir}{Colors.END}")
            response = input(f"{Colors.YELLOW}¿Sobrescribir? (y/N): {Colors.END}")
            if response.lower() != 'y':
                print(f"{Colors.RED}❌ Operación cancelada{Colors.END}")
                return
            shutil.rmtree(problem_dir)
        
        # Crear carpeta
        problem_dir.mkdir(parents=True, exist_ok=True)
        
        # Crear archivos
        print(f"{Colors.GREEN}📁 Creando estructura de archivos...{Colors.END}")
        
        # 1. meta.yaml
        meta_content = self._create_meta_yaml(problem_id, leetcode_number, difficulty, title)
        (problem_dir / "meta.yaml").write_text(meta_content, encoding='utf-8')
        print(f"{Colors.GREEN}   ✅ meta.yaml{Colors.END}")
        
        # 2. problem.md
        problem_content = self._create_problem_md(problem_id, leetcode_number, title)
        (problem_dir / "problem.md").write_text(problem_content, encoding='utf-8')
        print(f"{Colors.GREEN}   ✅ problem.md{Colors.END}")
        
        # 3. test.py
        test_content = self._create_test_py(problem_id, leetcode_number)
        (problem_dir / "test.py").write_text(test_content, encoding='utf-8')
        print(f"{Colors.GREEN}   ✅ test.py{Colors.END}")
        
        # 4. Crear solution.py placeholder (opcional)
        solution_placeholder = f'''"""
Solution for LeetCode Problem {leetcode_number}
Problem ID: {problem_id}

TODO: Implement your solution here

Problem URL: https://leetcode.com/problems/problem-{leetcode_number}/
"""

def solve():
    """
    TODO: Implement your solution
    
    Args:
        # Add parameters based on problem requirements
        
    Returns:
        # Return type based on problem requirements
    """
    pass

# Alternative class-based solution (for LeetCode submission format)
class Solution:
    def solutionMethod(self):
        """
        TODO: Implement solution method with correct name and signature
        """
        pass

if __name__ == "__main__":
    # Test your solution locally
    print("Testing solution...")
    result = solve()
    print(f"Result: {{result}}")
'''
        (problem_dir / "solution.py").write_text(solution_placeholder, encoding='utf-8')
        print(f"{Colors.GREEN}   ✅ solution.py (placeholder){Colors.END}")
        
        print()
        print(f"{Colors.GREEN}🎉 ¡Problema creado exitosamente!{Colors.END}")
        print()
        print(f"{Colors.BOLD}📋 Próximos pasos:{Colors.END}")
        print(f"{Colors.YELLOW}1. Visitar: https://leetcode.com/problems/problem-{leetcode_number}/{Colors.END}")
        print(f"{Colors.YELLOW}2. Copiar enunciado completo en problem.md{Colors.END}")
        print(f"{Colors.YELLOW}3. Actualizar meta.yaml con información correcta{Colors.END}")
        print(f"{Colors.YELLOW}4. Implementar solución en solution.py{Colors.END}")
        print(f"{Colors.YELLOW}5. Escribir tests en test.py{Colors.END}")
        print(f"{Colors.YELLOW}6. Ejecutar tests: pytest {problem_dir.relative_to(self.repo_path)}/test.py -v{Colors.END}")
        print()
        
        # Mostrar información adicional
        print(f"{Colors.BLUE}📊 Información adicional:{Colors.END}")
        print(f"   📂 Ubicación: {problem_dir}")
        print(f"   🆔 ID interno: {problem_id}")
        print(f"   🏷️  Dificultad: {difficulty}")
        print(f"   🔗 URL LeetCode: https://leetcode.com/problems/problem-{leetcode_number}/")

def main():
    """Función principal"""
    parser = argparse.ArgumentParser(
        description="Generador de estructura para problemas de LeetCode",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Ejemplos de uso:
  python tools/leetcode_scraper.py 1                    # Two Sum (básico)
  python tools/leetcode_scraper.py 15 intermediate      # 3Sum (intermedio)
  python tools/leetcode_scraper.py 297 advanced         # Serialize and Deserialize Binary Tree
  python tools/leetcode_scraper.py 153 intermediate "Find Minimum in Rotated Sorted Array"

Dificultades disponibles:
  basic, easy          -> problems/basic/ (ID: 001-099)
  intermediate, medium -> problems/intermediate/ (ID: 101-199)  
  advanced, hard       -> problems/advanced/ (ID: 201-299)
        """
    )
    
    parser.add_argument('leetcode_number', type=str,
                       help='Número del problema en LeetCode (ej: 1, 153, 297)')
    parser.add_argument('difficulty', nargs='?', default='basic',
                       help='Dificultad: basic|intermediate|advanced (default: basic)')
    parser.add_argument('--title', '-t', type=str,
                       help='Título personalizado del problema')
    parser.add_argument('--list', '-l', action='store_true',
                       help='Listar problemas existentes por dificultad')
    
    args = parser.parse_args()
    
    # Verificar directorio
    if not Path("problems").exists():
        print(f"{Colors.RED}❌ Error: Debes ejecutar desde el directorio raíz del repositorio{Colors.END}")
        print(f"{Colors.YELLOW}   cd competitive-programming-practice && python tools/leetcode_scraper.py{Colors.END}")
        sys.exit(1)
    
    scraper = LeetCodeScraper()
    
    if args.list:
        # Listar problemas existentes
        print(f"{Colors.CYAN}📋 Problemas existentes:{Colors.END}")
        for difficulty in ["basic", "intermediate", "advanced"]:
            diff_path = Path("problems") / difficulty
            if diff_path.exists():
                problems = [d.name for d in diff_path.iterdir() if d.is_dir()]
                print(f"\n{Colors.BOLD}{difficulty.upper()}: {len(problems)} problemas{Colors.END}")
                for problem in sorted(problems)[:5]:  # Mostrar solo 5
                    print(f"  • {problem}")
                if len(problems) > 5:
                    print(f"  ... y {len(problems) - 5} más")
        return
    
    # Validar número de LeetCode
    if not args.leetcode_number.isdigit():
        print(f"{Colors.RED}❌ Error: El número de problema debe ser numérico{Colors.END}")
        sys.exit(1)
    
    # Crear problema
    scraper.create_leetcode_problem(
        args.leetcode_number,
        args.difficulty,
        args.title
    )

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Competitive Programming Practice - Progress Tracker

Sistema de seguimiento de progreso para el repositorio de práctica.
Analiza problemas resueltos y genera estadísticas detalladas.

Uso:
    python tools/tracker.py                    # Mostrar progreso completo
    python tools/tracker.py --detailed         # Mostrar detalles por problema
    python tools/tracker.py --platform leetcode # Filtrar por plataforma
    python tools/tracker.py --difficulty basic # Filtrar por dificultad
    python tools/tracker.py --export           # Exportar a archivo CSV
"""

import os
import sys
# import yaml  # Commented out - using fallback parsing instead
import argparse
import csv
from pathlib import Path
from collections import defaultdict, Counter
from datetime import datetime
from typing import Dict, List, Set, Optional, Tuple, Any

# Simple YAML parser fallback (basic functionality)
def parse_simple_yaml(content: str) -> Dict[str, Any]:
    """Simple YAML parser for basic key-value pairs"""
    result = {}
    for line in content.split('\n'):
        line = line.strip()
        if ':' in line and not line.startswith('#'):
            key, value = line.split(':', 1)
            key = key.strip().strip('"\'')
            value = value.strip().strip('"\'')
            
            # Convert common types
            if value.lower() in ['true', 'yes']:
                value = True
            elif value.lower() in ['false', 'no']:
                value = False
            elif value.isdigit():
                value = int(value)
            elif value.startswith('[') and value.endswith(']'):
                # Simple list parsing
                value = [item.strip().strip('"\'') for item in value[1:-1].split(',') if item.strip()]
            
            result[key] = value
    return result

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

class ProgressTracker:
    """Sistema principal de seguimiento de progreso"""
    
    def __init__(self, repo_path: str = "."):
        self.repo_path = Path(repo_path)
        self.problems_path = self.repo_path / "problems"
        self.solved_file = self.repo_path / "solved.txt"
        
        # Datos del análisis
        self.solved_problems: Set[str] = set()
        self.problems_data: List[Dict] = []
        self.stats = defaultdict(lambda: {"total": 0, "solved": 0})
        
        # Cargar datos
        self._load_solved_problems()
        self._scan_problems()
    
    def _load_solved_problems(self) -> None:
        """Cargar lista de problemas resueltos desde solved.txt"""
        if not self.solved_file.exists():
            print(f"{Colors.YELLOW}⚠️  Archivo solved.txt no encontrado. Creando uno vacío...{Colors.END}")
            self.solved_file.touch()
            return
        
        try:
            with open(self.solved_file, 'r', encoding='utf-8') as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith('#'):
                        self.solved_problems.add(line)
        except Exception as e:
            print(f"{Colors.RED}❌ Error leyendo solved.txt: {e}{Colors.END}")
    
    def _scan_problems(self) -> None:
        """Escanear todos los problemas y cargar metadata"""
        if not self.problems_path.exists():
            print(f"{Colors.RED}❌ Directorio problems/ no encontrado{Colors.END}")
            return
        
        # Escanear carpetas de dificultad
        for difficulty_dir in ["basic", "intermediate", "advanced"]:
            difficulty_path = self.problems_path / difficulty_dir
            if difficulty_path.exists():
                self._scan_difficulty_folder(difficulty_path, difficulty_dir)
        
        # Escanear contests
        contests_path = self.problems_path / "contests"
        if contests_path.exists():
            self._scan_contests_folder(contests_path)
    
    def _scan_difficulty_folder(self, folder_path: Path, difficulty: str) -> None:
        """Escanear carpeta de dificultad específica"""
        for problem_dir in folder_path.iterdir():
            if problem_dir.is_dir():
                self._process_problem_directory(problem_dir, difficulty)
    
    def _scan_contests_folder(self, contests_path: Path) -> None:
        """Escanear carpeta de contests recursivamente"""
        for platform_dir in contests_path.iterdir():
            if platform_dir.is_dir():
                for contest_type_dir in platform_dir.iterdir():
                    if contest_type_dir.is_dir():
                        for contest_dir in contest_type_dir.iterdir():
                            if contest_dir.is_dir():
                                for problem_dir in contest_dir.iterdir():
                                    if problem_dir.is_dir():
                                        self._process_problem_directory(problem_dir, "contest")
    
    def _process_problem_directory(self, problem_dir: Path, difficulty: str) -> None:
        """Procesar directorio individual de problema"""
        meta_file = problem_dir / "meta.yaml"
        
        if not meta_file.exists():
            # Crear entrada básica sin metadata
            problem_id = self._extract_id_from_dirname(problem_dir.name)
            if problem_id:
                problem_data = {
                    'id': problem_id,
                    'title': problem_dir.name,
                    'difficulty': difficulty,
                    'source': 'unknown',
                    'tags': [],
                    'path': str(problem_dir),
                    'has_meta': False,
                    'has_test': (problem_dir / "test.py").exists(),
                    'has_solution': (problem_dir / "solution.py").exists()
                }
                self.problems_data.append(problem_data)
                self._update_stats(problem_data)
            return
        
        try:
            with open(meta_file, 'r', encoding='utf-8') as f:
                content = f.read()
                meta_data = parse_simple_yaml(content) or {}
            
            # Procesar metadata
            problem_data = {
                'id': meta_data.get('id', ''),
                'title': meta_data.get('title', problem_dir.name),
                'difficulty': meta_data.get('difficulty', difficulty),
                'source': meta_data.get('source', 'unknown'),
                'tags': meta_data.get('tags', []),
                'time_minutes': meta_data.get('time_minutes', 0),
                'url': meta_data.get('url', ''),
                'path': str(problem_dir),
                'has_meta': True,
                'has_test': (problem_dir / "test.py").exists(),
                'has_solution': (problem_dir / "solution.py").exists(),
                'contest_info': meta_data.get('contest_info', {})
            }
            
            self.problems_data.append(problem_data)
            self._update_stats(problem_data)
            
        except Exception as e:
            print(f"{Colors.YELLOW}⚠️  Error procesando {meta_file}: {e}{Colors.END}")
    
    def _extract_id_from_dirname(self, dirname: str) -> Optional[str]:
        """Extraer ID del nombre de directorio (ej: 001_two_sum -> 001)"""
        parts = dirname.split('_')
        if parts and parts[0].isdigit():
            return parts[0].zfill(3)
        return None
    
    def _update_stats(self, problem_data: Dict) -> None:
        """Actualizar estadísticas con datos del problema"""
        difficulty = problem_data['difficulty']
        source = problem_data['source']
        problem_id = problem_data['id']
        
        # Estadísticas por dificultad
        self.stats[f"difficulty_{difficulty}"]["total"] += 1
        if problem_id in self.solved_problems:
            self.stats[f"difficulty_{difficulty}"]["solved"] += 1
        
        # Estadísticas por plataforma
        self.stats[f"platform_{source}"]["total"] += 1
        if problem_id in self.solved_problems:
            self.stats[f"platform_{source}"]["solved"] += 1
    
    def show_summary(self) -> None:
        """Mostrar resumen general de progreso"""
        print(f"{Colors.CYAN}{Colors.BOLD}🏆 Competitive Programming Practice - Progress Tracker{Colors.END}")
        print(f"{Colors.CYAN}{'='*60}{Colors.END}")
        print()
        
        # Estadísticas generales
        total_problems = len(self.problems_data)
        total_solved = len(self.solved_problems)
        overall_percentage = (total_solved / total_problems * 100) if total_problems > 0 else 0
        
        print(f"{Colors.BOLD}📊 RESUMEN GENERAL:{Colors.END}")
        print(f"  🎯 Progreso Total: {Colors.GREEN}{total_solved}{Colors.END}/{Colors.BLUE}{total_problems}{Colors.END} problemas ({Colors.YELLOW}{overall_percentage:.1f}%{Colors.END})")
        print()
        
        # Estadísticas por dificultad
        print(f"{Colors.BOLD}📈 ESTADÍSTICAS POR DIFICULTAD:{Colors.END}")
        difficulties = ["basic", "intermediate", "advanced"]
        colors = [Colors.GREEN, Colors.YELLOW, Colors.RED]
        
        for difficulty, color in zip(difficulties, colors):
            stats = self.stats[f"difficulty_{difficulty}"]
            if stats["total"] > 0:
                percentage = (stats["solved"] / stats["total"] * 100)
                print(f"  {color}● {difficulty.capitalize():<12}{Colors.END}: {Colors.GREEN}{stats['solved']:2d}{Colors.END}/{Colors.BLUE}{stats['total']:2d}{Colors.END} ({Colors.YELLOW}{percentage:5.1f}%{Colors.END})")
        
        print()
        
        # Estadísticas por plataforma
        print(f"{Colors.BOLD}🌐 ESTADÍSTICAS POR PLATAFORMA:{Colors.END}")
        platform_stats = [(k.replace("platform_", ""), v) for k, v in self.stats.items() if k.startswith("platform_") and v["total"] > 0]
        platform_stats.sort(key=lambda x: x[1]["total"], reverse=True)
        
        for platform, stats in platform_stats:
            if stats["total"] > 0:
                percentage = (stats["solved"] / stats["total"] * 100)
                print(f"  {Colors.PURPLE}● {platform.capitalize():<12}{Colors.END}: {Colors.GREEN}{stats['solved']:2d}{Colors.END}/{Colors.BLUE}{stats['total']:2d}{Colors.END} ({Colors.YELLOW}{percentage:5.1f}%{Colors.END})")
        
        print()
    
    def show_detailed_progress(self, platform_filter: str = None, difficulty_filter: str = None) -> None:
        """Mostrar progreso detallado por problema"""
        print(f"{Colors.BOLD}📋 PROGRESO DETALLADO POR PROBLEMA:{Colors.END}")
        print(f"{Colors.CYAN}{'='*80}{Colors.END}")
        
        # Filtrar problemas si es necesario
        filtered_problems = self.problems_data
        if platform_filter:
            filtered_problems = [p for p in filtered_problems if p['source'].lower() == platform_filter.lower()]
        if difficulty_filter:
            filtered_problems = [p for p in filtered_problems if p['difficulty'].lower() == difficulty_filter.lower()]
        
        # Agrupar por dificultad
        problems_by_difficulty = defaultdict(list)
        for problem in filtered_problems:
            problems_by_difficulty[problem['difficulty']].append(problem)
        
        # Mostrar por cada dificultad
        for difficulty in ["basic", "intermediate", "advanced", "contest"]:
            if difficulty not in problems_by_difficulty:
                continue
            
            problems = problems_by_difficulty[difficulty]
            if not problems:
                continue
            
            # Color por dificultad
            if difficulty == "basic":
                color = Colors.GREEN
            elif difficulty == "intermediate":
                color = Colors.YELLOW
            elif difficulty == "advanced":
                color = Colors.RED
            else:
                color = Colors.PURPLE
            
            print(f"\n{color}{Colors.BOLD}{difficulty.upper()}:{Colors.END}")
            problems.sort(key=lambda x: x['id'])
            
            for problem in problems:
                status = "✅" if problem['id'] in self.solved_problems else "⭕"
                
                # Información adicional
                extras = []
                if not problem.get('has_test', False):
                    extras.append("❌test")
                if not problem.get('has_solution', False):
                    extras.append("❌sol")
                if not problem.get('has_meta', False):
                    extras.append("❌meta")
                
                extra_info = f" [{', '.join(extras)}]" if extras else ""
                
                print(f"  {status} {Colors.BLUE}{problem['id']}{Colors.END} - {problem['title']} "
                      f"({Colors.CYAN}{problem['source']}{Colors.END}){extra_info}")
        
        print()
    
    def show_tag_analysis(self) -> None:
        """Mostrar análisis por tags"""
        print(f"{Colors.BOLD}🏷️  ANÁLISIS POR TAGS:{Colors.END}")
        print(f"{Colors.CYAN}{'='*50}{Colors.END}")
        
        # Contar tags
        tag_counts = Counter()
        tag_solved = Counter()
        
        for problem in self.problems_data:
            for tag in problem.get('tags', []):
                tag_counts[tag] += 1
                if problem['id'] in self.solved_problems:
                    tag_solved[tag] += 1
        
        # Mostrar top tags
        print(f"\n{Colors.BOLD}Top 10 Tags más frecuentes:{Colors.END}")
        for tag, count in tag_counts.most_common(10):
            solved = tag_solved[tag]
            percentage = (solved / count * 100) if count > 0 else 0
            print(f"  {Colors.YELLOW}#{tag:<20}{Colors.END}: {Colors.GREEN}{solved:2d}{Colors.END}/{Colors.BLUE}{count:2d}{Colors.END} ({percentage:5.1f}%)")
        
        print()
    
    def show_missing_components(self) -> None:
        """Mostrar problemas con componentes faltantes"""
        print(f"{Colors.BOLD}🔍 COMPONENTES FALTANTES:{Colors.END}")
        print(f"{Colors.CYAN}{'='*50}{Colors.END}")
        
        missing_meta = [p for p in self.problems_data if not p.get('has_meta', False)]
        missing_test = [p for p in self.problems_data if not p.get('has_test', False)]
        missing_solution = [p for p in self.problems_data if not p.get('has_solution', False)]
        
        if missing_meta:
            print(f"\n{Colors.RED}❌ Problemas sin meta.yaml ({len(missing_meta)}):{Colors.END}")
            for problem in missing_meta[:5]:  # Mostrar solo los primeros 5
                print(f"  • {problem['id']} - {problem['title']}")
            if len(missing_meta) > 5:
                print(f"  ... y {len(missing_meta) - 5} más")
        
        if missing_test:
            print(f"\n{Colors.YELLOW}⚠️  Problemas sin test.py ({len(missing_test)}):{Colors.END}")
            for problem in missing_test[:5]:
                print(f"  • {problem['id']} - {problem['title']}")
            if len(missing_test) > 5:
                print(f"  ... y {len(missing_test) - 5} más")
        
        if missing_solution:
            print(f"\n{Colors.BLUE}💡 Problemas sin solution.py ({len(missing_solution)}):{Colors.END}")
            for problem in missing_solution[:5]:
                print(f"  • {problem['id']} - {problem['title']}")
            if len(missing_solution) > 5:
                print(f"  ... y {len(missing_solution) - 5} más")
        
        if not any([missing_meta, missing_test, missing_solution]):
            print(f"{Colors.GREEN}✅ ¡Todos los problemas tienen componentes completos!{Colors.END}")
        
        print()
    
    def export_to_csv(self, filename: str = None) -> None:
        """Exportar datos a archivo CSV"""
        if filename is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"progress_report_{timestamp}.csv"
        
        try:
            with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
                fieldnames = ['id', 'title', 'difficulty', 'source', 'solved', 'tags', 'time_minutes', 'has_test', 'has_solution', 'path']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                
                writer.writeheader()
                for problem in sorted(self.problems_data, key=lambda x: x['id']):
                    writer.writerow({
                        'id': problem['id'],
                        'title': problem['title'],
                        'difficulty': problem['difficulty'],
                        'source': problem['source'],
                        'solved': 'YES' if problem['id'] in self.solved_problems else 'NO',
                        'tags': ', '.join(problem.get('tags', [])),
                        'time_minutes': problem.get('time_minutes', 0),
                        'has_test': 'YES' if problem.get('has_test', False) else 'NO',
                        'has_solution': 'YES' if problem.get('has_solution', False) else 'NO',
                        'path': problem['path']
                    })
            
            print(f"{Colors.GREEN}✅ Reporte exportado a: {filename}{Colors.END}")
            
        except Exception as e:
            print(f"{Colors.RED}❌ Error exportando a CSV: {e}{Colors.END}")

def main():
    """Función principal"""
    parser = argparse.ArgumentParser(
        description="Sistema de seguimiento de progreso para Competitive Programming Practice",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Ejemplos de uso:
  python tools/tracker.py                       # Progreso completo
  python tools/tracker.py --detailed            # Detalles por problema  
  python tools/tracker.py --platform leetcode   # Solo problemas de LeetCode
  python tools/tracker.py --difficulty basic    # Solo problemas básicos
  python tools/tracker.py --export              # Exportar a CSV
  python tools/tracker.py --tags                # Análisis por tags
  python tools/tracker.py --missing             # Componentes faltantes
        """
    )
    
    parser.add_argument('--detailed', '-d', action='store_true',
                       help='Mostrar progreso detallado por problema')
    parser.add_argument('--platform', '-p', type=str,
                       help='Filtrar por plataforma (leetcode, codeforces, etc.)')
    parser.add_argument('--difficulty', '-f', type=str,
                       help='Filtrar por dificultad (basic, intermediate, advanced)')
    parser.add_argument('--export', '-e', action='store_true',
                       help='Exportar progreso a archivo CSV')
    parser.add_argument('--tags', '-t', action='store_true',
                       help='Mostrar análisis por tags')
    parser.add_argument('--missing', '-m', action='store_true',
                       help='Mostrar componentes faltantes')
    parser.add_argument('--all', '-a', action='store_true',
                       help='Mostrar toda la información disponible')
    
    args = parser.parse_args()
    
    # Verificar que estamos en el directorio correcto
    if not Path("problems").exists():
        print(f"{Colors.RED}❌ Error: Debes ejecutar este script desde el directorio raíz del repositorio{Colors.END}")
        print(f"{Colors.YELLOW}   cd competitive-programming-practice && python tools/tracker.py{Colors.END}")
        sys.exit(1)
    
    # Crear tracker y ejecutar
    tracker = ProgressTracker()
    
    # Mostrar información según argumentos
    if args.all:
        tracker.show_summary()
        tracker.show_detailed_progress(args.platform, args.difficulty)
        tracker.show_tag_analysis()
        tracker.show_missing_components()
    else:
        # Siempre mostrar resumen
        tracker.show_summary()
        
        if args.detailed:
            tracker.show_detailed_progress(args.platform, args.difficulty)
        
        if args.tags:
            tracker.show_tag_analysis()
        
        if args.missing:
            tracker.show_missing_components()
    
    if args.export:
        tracker.export_to_csv()

if __name__ == "__main__":
    main()

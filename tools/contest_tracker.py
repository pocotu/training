#!/usr/bin/env python3
"""
Competitive Programming Practice - Contest Tracker

Tracker específico para contests con estadísticas detalladas.
Analiza progreso en contests de LeetCode y Codeforces.

Uso:
    python tools/contest_tracker.py                    # Ver todos los contests
    python tools/contest_tracker.py --platform leetcode # Solo LeetCode
    python tools/contest_tracker.py --type weekly      # Solo contests semanales
    python tools/contest_tracker.py --detailed         # Información detallada
    python tools/contest_tracker.py --export           # Exportar a CSV
"""

import os
import sys
import yaml
import argparse
import csv
from pathlib import Path
from collections import defaultdict, Counter
from datetime import datetime
from typing import Dict, List, Set, Optional, Tuple

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

class ContestTracker:
    """Tracker específico para contests de programación competitiva"""
    
    def __init__(self, repo_path: str = "."):
        self.repo_path = Path(repo_path)
        self.contests_path = self.repo_path / "problems" / "contests"
        self.solved_file = self.repo_path / "solved.txt"
        
        # Datos de contests
        self.solved_problems: Set[str] = set()
        self.contests_data: List[Dict] = []
        self.contest_stats = defaultdict(lambda: {"total": 0, "solved": 0, "problems": []})
        
        # Cargar datos
        self._load_solved_problems()
        self._scan_contests()
    
    def _load_solved_problems(self) -> None:
        """Cargar problemas resueltos desde solved.txt"""
        if not self.solved_file.exists():
            print(f"{Colors.YELLOW}⚠️  Archivo solved.txt no encontrado{Colors.END}")
            return
        
        try:
            with open(self.solved_file, 'r', encoding='utf-8') as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith('#'):
                        self.solved_problems.add(line)
        except Exception as e:
            print(f"{Colors.RED}❌ Error leyendo solved.txt: {e}{Colors.END}")
    
    def _scan_contests(self) -> None:
        """Escanear todos los contests recursivamente"""
        if not self.contests_path.exists():
            print(f"{Colors.YELLOW}⚠️  Directorio contests/ no encontrado{Colors.END}")
            return
        
        # Escanear por plataforma
        for platform_dir in self.contests_path.iterdir():
            if platform_dir.is_dir():
                platform_name = platform_dir.name
                self._scan_platform_contests(platform_dir, platform_name)
    
    def _scan_platform_contests(self, platform_dir: Path, platform_name: str) -> None:
        """Escanear contests de una plataforma específica"""
        for contest_type_dir in platform_dir.iterdir():
            if contest_type_dir.is_dir():
                contest_type = contest_type_dir.name
                self._scan_contest_type(contest_type_dir, platform_name, contest_type)
    
    def _scan_contest_type(self, contest_type_dir: Path, platform: str, contest_type: str) -> None:
        """Escanear tipo específico de contest (weekly, div2, etc.)"""
        for contest_dir in contest_type_dir.iterdir():
            if contest_dir.is_dir():
                contest_number = contest_dir.name
                self._scan_individual_contest(contest_dir, platform, contest_type, contest_number)
    
    def _scan_individual_contest(self, contest_dir: Path, platform: str, contest_type: str, contest_number: str) -> None:
        """Escanear contest individual y sus problemas"""
        contest_problems = []
        
        # Buscar problemas en el contest
        for problem_dir in contest_dir.iterdir():
            if problem_dir.is_dir():
                problem_data = self._process_contest_problem(problem_dir, platform, contest_type, contest_number)
                if problem_data:
                    contest_problems.append(problem_data)
                    self.contests_data.append(problem_data)
        
        # Agregar estadísticas del contest
        if contest_problems:
            contest_key = f"{platform}_{contest_type}_{contest_number}"
            self.contest_stats[contest_key]["total"] = len(contest_problems)
            self.contest_stats[contest_key]["problems"] = contest_problems
            self.contest_stats[contest_key]["platform"] = platform
            self.contest_stats[contest_key]["type"] = contest_type
            self.contest_stats[contest_key]["number"] = contest_number
            
            # Contar problemas resueltos
            solved_in_contest = sum(1 for p in contest_problems if p['id'] in self.solved_problems)
            self.contest_stats[contest_key]["solved"] = solved_in_contest
    
    def _process_contest_problem(self, problem_dir: Path, platform: str, contest_type: str, contest_number: str) -> Optional[Dict]:
        """Procesar problema individual de contest"""
        meta_file = problem_dir / "meta.yaml"
        
        # Datos básicos del problema
        problem_data = {
            'path': str(problem_dir),
            'platform': platform,
            'contest_type': contest_type,
            'contest_number': contest_number,
            'has_meta': meta_file.exists(),
            'has_test': (problem_dir / "test.py").exists(),
            'has_solution': (problem_dir / "solution.py").exists()
        }
        
        if meta_file.exists():
            try:
                with open(meta_file, 'r', encoding='utf-8') as f:
                    meta_data = yaml.safe_load(f) or {}
                
                problem_data.update({
                    'id': meta_data.get('id', ''),
                    'title': meta_data.get('title', problem_dir.name),
                    'tags': meta_data.get('tags', []),
                    'difficulty': meta_data.get('difficulty', 'unknown'),
                    'time_minutes': meta_data.get('time_minutes', 0),
                    'contest_info': meta_data.get('contest_info', {})
                })
                
                # Información específica del contest
                contest_info = problem_data['contest_info']
                if contest_info:
                    problem_data['position'] = contest_info.get('position', '')
                    problem_data['contest_date'] = contest_info.get('date', '')
                
            except Exception as e:
                print(f"{Colors.YELLOW}⚠️  Error procesando {meta_file}: {e}{Colors.END}")
                problem_data.update({
                    'id': self._extract_id_from_dirname(problem_dir.name),
                    'title': problem_dir.name,
                    'tags': [],
                    'difficulty': 'unknown'
                })
        else:
            # Sin metadata, usar información básica
            problem_data.update({
                'id': self._extract_id_from_dirname(problem_dir.name),
                'title': problem_dir.name,
                'tags': [],
                'difficulty': 'unknown'
            })
        
        return problem_data
    
    def _extract_id_from_dirname(self, dirname: str) -> str:
        """Extraer ID del nombre de directorio"""
        parts = dirname.split('_')
        if parts and parts[0].isdigit():
            return parts[0].zfill(3)
        return dirname[:10]  # Fallback
    
    def show_contest_summary(self, platform_filter: str = None, type_filter: str = None) -> None:
        """Mostrar resumen de contests"""
        print(f"{Colors.CYAN}{Colors.BOLD}🏆 Contest Tracker - Resumen de Contests{Colors.END}")
        print(f"{Colors.CYAN}{'='*60}{Colors.END}")
        print()
        
        # Filtrar contests
        filtered_contests = {}
        for contest_key, contest_data in self.contest_stats.items():
            platform = contest_data['platform']
            contest_type = contest_data['type']
            
            if platform_filter and platform.lower() != platform_filter.lower():
                continue
            if type_filter and contest_type.lower() != type_filter.lower():
                continue
            
            filtered_contests[contest_key] = contest_data
        
        if not filtered_contests:
            print(f"{Colors.YELLOW}⚠️  No se encontraron contests con los filtros aplicados{Colors.END}")
            return
        
        # Estadísticas generales
        total_contests = len(filtered_contests)
        total_problems = sum(c["total"] for c in filtered_contests.values())
        total_solved = sum(c["solved"] for c in filtered_contests.values())
        
        print(f"{Colors.BOLD}📊 ESTADÍSTICAS GENERALES:{Colors.END}")
        print(f"  🏆 Total de contests: {Colors.BLUE}{total_contests}{Colors.END}")
        print(f"  📝 Total de problemas: {Colors.BLUE}{total_problems}{Colors.END}")
        print(f"  ✅ Problemas resueltos: {Colors.GREEN}{total_solved}{Colors.END}")
        if total_problems > 0:
            percentage = (total_solved / total_problems * 100)
            print(f"  📈 Porcentaje general: {Colors.YELLOW}{percentage:.1f}%{Colors.END}")
        print()
        
        # Estadísticas por plataforma
        platform_stats = defaultdict(lambda: {"contests": 0, "problems": 0, "solved": 0})
        for contest_data in filtered_contests.values():
            platform = contest_data['platform']
            platform_stats[platform]["contests"] += 1
            platform_stats[platform]["problems"] += contest_data["total"]
            platform_stats[platform]["solved"] += contest_data["solved"]
        
        print(f"{Colors.BOLD}🌐 ESTADÍSTICAS POR PLATAFORMA:{Colors.END}")
        for platform, stats in platform_stats.items():
            percentage = (stats["solved"] / stats["problems"] * 100) if stats["problems"] > 0 else 0
            print(f"  {Colors.PURPLE}● {platform.capitalize():<12}{Colors.END}: "
                  f"{Colors.GREEN}{stats['solved']:2d}{Colors.END}/"
                  f"{Colors.BLUE}{stats['problems']:2d}{Colors.END} problemas "
                  f"({Colors.YELLOW}{percentage:5.1f}%{Colors.END}) - "
                  f"{Colors.CYAN}{stats['contests']}{Colors.END} contests")
        print()
        
        # Estadísticas por tipo de contest
        type_stats = defaultdict(lambda: {"contests": 0, "problems": 0, "solved": 0})
        for contest_data in filtered_contests.values():
            contest_type = contest_data['type']
            type_stats[contest_type]["contests"] += 1
            type_stats[contest_type]["problems"] += contest_data["total"]
            type_stats[contest_type]["solved"] += contest_data["solved"]
        
        print(f"{Colors.BOLD}🎯 ESTADÍSTICAS POR TIPO:{Colors.END}")
        for contest_type, stats in type_stats.items():
            percentage = (stats["solved"] / stats["problems"] * 100) if stats["problems"] > 0 else 0
            print(f"  {Colors.CYAN}● {contest_type.capitalize():<12}{Colors.END}: "
                  f"{Colors.GREEN}{stats['solved']:2d}{Colors.END}/"
                  f"{Colors.BLUE}{stats['problems']:2d}{Colors.END} problemas "
                  f"({Colors.YELLOW}{percentage:5.1f}%{Colors.END}) - "
                  f"{Colors.CYAN}{stats['contests']}{Colors.END} contests")
        print()
    
    def show_detailed_contests(self, platform_filter: str = None, type_filter: str = None) -> None:
        """Mostrar información detallada de contests"""
        print(f"{Colors.BOLD}📋 CONTESTS DETALLADOS:{Colors.END}")
        print(f"{Colors.CYAN}{'='*80}{Colors.END}")
        
        # Filtrar y agrupar contests
        contests_by_platform = defaultdict(lambda: defaultdict(list))
        
        for contest_key, contest_data in self.contest_stats.items():
            platform = contest_data['platform']
            contest_type = contest_data['type']
            
            if platform_filter and platform.lower() != platform_filter.lower():
                continue
            if type_filter and contest_type.lower() != type_filter.lower():
                continue
            
            contests_by_platform[platform][contest_type].append((contest_key, contest_data))
        
        # Mostrar por plataforma y tipo
        for platform, types_data in contests_by_platform.items():
            print(f"\n{Colors.PURPLE}{Colors.BOLD}{platform.upper()}:{Colors.END}")
            
            for contest_type, contests in types_data.items():
                print(f"\n  {Colors.CYAN}{contest_type.capitalize()}:{Colors.END}")
                
                # Ordenar contests por número
                contests.sort(key=lambda x: x[1]['number'])
                
                for contest_key, contest_data in contests:
                    solved = contest_data['solved']
                    total = contest_data['total']
                    percentage = (solved / total * 100) if total > 0 else 0
                    
                    # Indicador de progreso
                    if percentage == 100:
                        status = f"{Colors.GREEN}✅{Colors.END}"
                    elif percentage >= 50:
                        status = f"{Colors.YELLOW}🔄{Colors.END}"
                    else:
                        status = f"{Colors.RED}⭕{Colors.END}"
                    
                    print(f"    {status} {Colors.BLUE}{contest_data['number']:<15}{Colors.END}: "
                          f"{Colors.GREEN}{solved:2d}{Colors.END}/"
                          f"{Colors.BLUE}{total:2d}{Colors.END} "
                          f"({Colors.YELLOW}{percentage:5.1f}%{Colors.END})")
                    
                    # Mostrar problemas si hay pocos
                    if total <= 4:
                        for problem in contest_data['problems']:
                            problem_status = "✅" if problem['id'] in self.solved_problems else "⭕"
                            position = problem.get('position', '?')
                            print(f"      {problem_status} {position}: {problem['title']}")
        
        print()
    
    def show_performance_analysis(self) -> None:
        """Mostrar análisis de rendimiento en contests"""
        print(f"{Colors.BOLD}📊 ANÁLISIS DE RENDIMIENTO:{Colors.END}")
        print(f"{Colors.CYAN}{'='*50}{Colors.END}")
        
        if not self.contest_stats:
            print(f"{Colors.YELLOW}⚠️  No hay datos de contests para analizar{Colors.END}")
            return
        
        # Análisis por tipo de contest
        type_performance = defaultdict(list)
        for contest_data in self.contest_stats.values():
            contest_type = contest_data['type']
            total = contest_data['total']
            solved = contest_data['solved']
            percentage = (solved / total * 100) if total > 0 else 0
            type_performance[contest_type].append(percentage)
        
        print(f"\n{Colors.BOLD}Rendimiento promedio por tipo:{Colors.END}")
        for contest_type, percentages in type_performance.items():
            if percentages:
                avg_percentage = sum(percentages) / len(percentages)
                max_percentage = max(percentages)
                min_percentage = min(percentages)
                
                print(f"  {Colors.CYAN}● {contest_type.capitalize():<12}{Colors.END}: "
                      f"Promedio {Colors.YELLOW}{avg_percentage:5.1f}%{Colors.END} "
                      f"(Mejor: {Colors.GREEN}{max_percentage:5.1f}%{Colors.END}, "
                      f"Peor: {Colors.RED}{min_percentage:5.1f}%{Colors.END})")
        
        # Contests completados vs incompletos
        completed_contests = sum(1 for c in self.contest_stats.values() if c['solved'] == c['total'] and c['total'] > 0)
        partial_contests = sum(1 for c in self.contest_stats.values() if 0 < c['solved'] < c['total'])
        untouched_contests = sum(1 for c in self.contest_stats.values() if c['solved'] == 0)
        
        print(f"\n{Colors.BOLD}Estado de contests:{Colors.END}")
        print(f"  {Colors.GREEN}✅ Completados: {completed_contests}{Colors.END}")
        print(f"  {Colors.YELLOW}🔄 Parciales: {partial_contests}{Colors.END}")  
        print(f"  {Colors.RED}⭕ Sin empezar: {untouched_contests}{Colors.END}")
        
        # Análisis de tags más frecuentes en contests
        tag_counts = Counter()
        for contest_data in self.contest_stats.values():
            for problem in contest_data['problems']:
                for tag in problem.get('tags', []):
                    tag_counts[tag] += 1
        
        if tag_counts:
            print(f"\n{Colors.BOLD}Tags más frecuentes en contests:{Colors.END}")
            for tag, count in tag_counts.most_common(5):
                print(f"  {Colors.PURPLE}#{tag:<15}{Colors.END}: {count} problemas")
        
        print()
    
    def export_contest_data(self, filename: str = None) -> None:
        """Exportar datos de contests a CSV"""
        if filename is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"contest_report_{timestamp}.csv"
        
        try:
            with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
                fieldnames = [
                    'platform', 'contest_type', 'contest_number', 'problem_id', 
                    'problem_title', 'position', 'solved', 'tags', 'difficulty',
                    'has_test', 'has_solution', 'path'
                ]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                
                writer.writeheader()
                for problem in sorted(self.contests_data, key=lambda x: (x['platform'], x['contest_type'], x['contest_number'])):
                    writer.writerow({
                        'platform': problem['platform'],
                        'contest_type': problem['contest_type'],
                        'contest_number': problem['contest_number'],
                        'problem_id': problem.get('id', ''),
                        'problem_title': problem.get('title', ''),
                        'position': problem.get('position', ''),
                        'solved': 'YES' if problem.get('id', '') in self.solved_problems else 'NO',
                        'tags': ', '.join(problem.get('tags', [])),
                        'difficulty': problem.get('difficulty', ''),
                        'has_test': 'YES' if problem.get('has_test', False) else 'NO',
                        'has_solution': 'YES' if problem.get('has_solution', False) else 'NO',
                        'path': problem['path']
                    })
            
            print(f"{Colors.GREEN}✅ Reporte de contests exportado a: {filename}{Colors.END}")
            
        except Exception as e:
            print(f"{Colors.RED}❌ Error exportando a CSV: {e}{Colors.END}")

def main():
    """Función principal"""
    parser = argparse.ArgumentParser(
        description="Tracker específico para contests de programación competitiva",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Ejemplos de uso:
  python tools/contest_tracker.py                     # Ver todos los contests
  python tools/contest_tracker.py --platform leetcode # Solo LeetCode
  python tools/contest_tracker.py --type weekly       # Solo contests semanales
  python tools/contest_tracker.py --detailed          # Información detallada
  python tools/contest_tracker.py --performance       # Análisis de rendimiento
  python tools/contest_tracker.py --export            # Exportar a CSV
        """
    )
    
    parser.add_argument('--platform', '-p', type=str,
                       help='Filtrar por plataforma (leetcode, codeforces)')
    parser.add_argument('--type', '-t', type=str,
                       help='Filtrar por tipo (weekly, biweekly, div2, div3, educational)')
    parser.add_argument('--detailed', '-d', action='store_true',
                       help='Mostrar información detallada de contests')
    parser.add_argument('--performance', '-r', action='store_true',
                       help='Mostrar análisis de rendimiento')
    parser.add_argument('--export', '-e', action='store_true',
                       help='Exportar datos a CSV')
    parser.add_argument('--all', '-a', action='store_true',
                       help='Mostrar toda la información disponible')
    
    args = parser.parse_args()
    
    # Verificar directorio
    if not Path("problems").exists():
        print(f"{Colors.RED}❌ Error: Debes ejecutar desde el directorio raíz del repositorio{Colors.END}")
        print(f"{Colors.YELLOW}   cd competitive-programming-practice && python tools/contest_tracker.py{Colors.END}")
        sys.exit(1)
    
    # Crear tracker
    tracker = ContestTracker()
    
    # Mostrar información según argumentos
    if args.all:
        tracker.show_contest_summary(args.platform, args.type)
        tracker.show_detailed_contests(args.platform, args.type)
        tracker.show_performance_analysis()
    else:
        # Siempre mostrar resumen
        tracker.show_contest_summary(args.platform, args.type)
        
        if args.detailed:
            tracker.show_detailed_contests(args.platform, args.type)
        
        if args.performance:
            tracker.show_performance_analysis()
    
    if args.export:
        tracker.export_contest_data()

if __name__ == "__main__":
    main()

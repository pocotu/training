#!/usr/bin/env python3
"""
Contest Structure Validator (Simplified)

Validates the complete contest directory structure for Phase 7 implementation.
Does not require external dependencies.

Usage:
    python phase7-validator.py
"""

import os
import re
from pathlib import Path
from collections import defaultdict

class Phase7Validator:
    """Simplified validator for Phase 7 contest structure."""
    
    def __init__(self):
        """Initialize validator."""
        # Assume we're in contest-templates/tools/
        self.base_path = Path(__file__).parent.parent.parent
        self.errors = []
        self.warnings = []
        self.stats = defaultdict(int)
    
    def validate_phase7(self):
        """Validate complete Phase 7 implementation."""
        print("🔍 Phase 7 Contest Structure Validation")
        print("=" * 50)
        
        # Check basic directory structure
        self._check_directory_structure()
        
        # Validate LeetCode implementation
        self._validate_leetcode_implementation()
        
        # Validate Codeforces implementation  
        self._validate_codeforces_implementation()
        
        # Check templates and tools
        self._validate_templates_tools()
        
        # Generate final report
        self._generate_phase7_report()
        
        return len(self.errors) == 0
    
    def _check_directory_structure(self):
        """Check basic directory structure."""
        print("📁 Checking directory structure...")
        
        required_dirs = [
            "leetcode",
            "leetcode/weekly", 
            "leetcode/biweekly",
            "leetcode/daily",
            "codeforces",
            "codeforces/div2",
            "codeforces/div3", 
            "codeforces/educational",
            "contest-templates"
        ]
        
        for dir_path in required_dirs:
            full_path = self.base_path / dir_path
            if full_path.exists() and full_path.is_dir():
                self.stats['directories_ok'] += 1
                print(f"  ✅ {dir_path}")
            else:
                self.errors.append(f"Missing directory: {dir_path}")
                print(f"  ❌ {dir_path}")
        
        print(f"Directories: {self.stats['directories_ok']}/{len(required_dirs)}")
    
    def _validate_leetcode_implementation(self):
        """Validate LeetCode contest implementation."""
        print("\n🏆 Checking LeetCode contests...")
        
        leetcode_path = self.base_path / "leetcode"
        if not leetcode_path.exists():
            self.errors.append("LeetCode directory missing")
            return
        
        # Check contest types and specific contests
        contest_types = {
            'weekly': ['contest_380', 'contest_381', 'contest_382'],
            'biweekly': ['contest_120', 'contest_121', 'contest_122'],
            'daily': ['contest_2024_01', 'contest_2024_02', 'contest_2024_03']
        }
        
        for contest_type, expected_contests in contest_types.items():
            type_path = leetcode_path / contest_type
            print(f"  Checking {contest_type}...")
            
            if not type_path.exists():
                self.errors.append(f"Missing {contest_type} directory")
                continue
            
            for contest in expected_contests:
                contest_path = type_path / contest
                if contest_path.exists():
                    self._check_leetcode_contest(contest_path, contest)
                    self.stats['leetcode_contests'] += 1
                    print(f"    ✅ {contest}")
                else:
                    self.warnings.append(f"Missing {contest_type}/{contest}")
                    print(f"    ⚠️  {contest}")
    
    def _check_leetcode_contest(self, contest_path, contest_name):
        """Check individual LeetCode contest."""
        # Check README
        readme_path = contest_path / "README.md"
        if readme_path.exists():
            self.stats['readmes'] += 1
        
        # Check problems (expect 4 problems)
        problem_dirs = [d for d in contest_path.iterdir() 
                       if d.is_dir() and d.name.startswith('problem_')]
        
        for problem_dir in problem_dirs:
            if self._check_problem_files(problem_dir):
                self.stats['complete_problems'] += 1
    
    def _validate_codeforces_implementation(self):
        """Validate Codeforces contest implementation."""
        print("\n🎯 Checking Codeforces contests...")
        
        codeforces_path = self.base_path / "codeforces"
        if not codeforces_path.exists():
            self.errors.append("Codeforces directory missing")
            return
        
        contest_types = {
            'div2': ['round_915', 'round_916', 'round_917'],
            'div3': ['round_900', 'round_901'],
            'educational': ['round_160', 'round_161']
        }
        
        for contest_type, expected_contests in contest_types.items():
            type_path = codeforces_path / contest_type
            print(f"  Checking {contest_type}...")
            
            if not type_path.exists():
                self.errors.append(f"Missing {contest_type} directory")
                continue
            
            for contest in expected_contests:
                contest_path = type_path / contest
                if contest_path.exists():
                    self._check_codeforces_contest(contest_path, contest)
                    self.stats['codeforces_contests'] += 1
                    print(f"    ✅ {contest}")
                else:
                    self.warnings.append(f"Missing {contest_type}/{contest}")
                    print(f"    ⚠️  {contest}")
    
    def _check_codeforces_contest(self, contest_path, contest_name):
        """Check individual Codeforces contest."""
        # Check README
        readme_path = contest_path / "README.md"
        if readme_path.exists():
            self.stats['readmes'] += 1
        
        # Check problems
        problem_dirs = [d for d in contest_path.iterdir() 
                       if d.is_dir() and d.name.startswith('problem_')]
        
        for problem_dir in problem_dirs:
            if self._check_problem_files(problem_dir):
                self.stats['complete_problems'] += 1
    
    def _check_problem_files(self, problem_path):
        """Check if problem has all required files."""
        required_files = ['problem.md', 'solution.py', 'meta.yaml']
        found_files = 0
        
        for file_name in required_files:
            file_path = problem_path / file_name
            if file_path.exists():
                found_files += 1
                self.stats['problem_files'] += 1
        
        return found_files == len(required_files)
    
    def _validate_templates_tools(self):
        """Validate templates and management tools."""
        print("\n🛠️  Checking templates and tools...")
        
        templates_path = self.base_path / "contest-templates"
        if not templates_path.exists():
            self.errors.append("Contest templates directory missing")
            return
        
        # Check for tools
        tools_path = templates_path / "tools"
        if tools_path.exists():
            tool_files = list(tools_path.glob("*.py"))
            self.stats['tools'] = len(tool_files)
            print(f"  ✅ Found {len(tool_files)} Python tools")
            
            # Check for specific important tools
            important_tools = [
                'contest-creator.py',
                'contest-tracker.py', 
                'contest-validator.py'
            ]
            
            for tool in important_tools:
                tool_path = tools_path / tool
                if tool_path.exists():
                    print(f"    ✅ {tool}")
                else:
                    self.warnings.append(f"Missing tool: {tool}")
                    print(f"    ⚠️  {tool}")
        else:
            self.errors.append("Tools directory missing")
        
        # Check for README
        readme_path = templates_path / "README.md"
        if readme_path.exists():
            self.stats['documentation'] += 1
            print(f"  ✅ Templates documentation found")
        else:
            self.warnings.append("Templates README missing")
    
    def _generate_phase7_report(self):
        """Generate comprehensive Phase 7 validation report."""
        print("\n" + "=" * 50)
        print("📋 PHASE 7 VALIDATION REPORT")
        print("=" * 50)
        
        # Statistics summary
        print("📊 IMPLEMENTATION STATISTICS:")
        print(f"   • Directory Structure: {self.stats['directories_ok']}/9 ({'✅' if self.stats['directories_ok'] >= 8 else '❌'})")
        print(f"   • LeetCode Contests: {self.stats.get('leetcode_contests', 0)}")
        print(f"   • Codeforces Contests: {self.stats.get('codeforces_contests', 0)}")
        print(f"   • Complete Problems: {self.stats.get('complete_problems', 0)}")
        print(f"   • Problem Files: {self.stats.get('problem_files', 0)}")
        print(f"   • Contest READMEs: {self.stats.get('readmes', 0)}")
        print(f"   • Management Tools: {self.stats.get('tools', 0)}")
        print(f"   • Documentation: {self.stats.get('documentation', 0)}")
        
        # Error summary
        if self.errors:
            print(f"\n❌ CRITICAL ISSUES ({len(self.errors)}):")
            for i, error in enumerate(self.errors, 1):
                print(f"   {i}. {error}")
        
        # Warning summary  
        if self.warnings:
            print(f"\n⚠️  WARNINGS ({len(self.warnings)}):")
            for i, warning in enumerate(self.warnings, 1):
                print(f"   {i}. {warning}")
        
        # Phase 7 completion assessment
        self._assess_phase7_completion()
    
    def _assess_phase7_completion(self):
        """Assess Phase 7 completion status."""
        print(f"\n🎯 PHASE 7 COMPLETION ASSESSMENT:")
        
        # Define success criteria
        criteria = [
            ("Basic directory structure", self.stats['directories_ok'] >= 8),
            ("LeetCode contests implemented", self.stats.get('leetcode_contests', 0) >= 1),
            ("Codeforces contests implemented", self.stats.get('codeforces_contests', 0) >= 1), 
            ("Problems with complete files", self.stats.get('complete_problems', 0) >= 5),
            ("Management tools available", self.stats.get('tools', 0) >= 2),
            ("Documentation provided", self.stats.get('documentation', 0) >= 1),
            ("No critical errors", len(self.errors) == 0)
        ]
        
        passed = 0
        total = len(criteria)
        
        print("   Success Criteria:")
        for criterion, success in criteria:
            status = "✅" if success else "❌"
            if success:
                passed += 1
            print(f"   {status} {criterion}")
        
        completion_rate = (passed / total) * 100
        print(f"\n   📈 Completion Rate: {passed}/{total} ({completion_rate:.1f}%)")
        
        # Overall assessment
        if completion_rate >= 85:
            print("\n🎉 FASE 7 COMPLETADA EXITOSAMENTE!")
            print("   La estructura de contests está bien implementada")
            print("   con funcionalidad completa para práctica competitiva.")
            return True
        elif completion_rate >= 70:
            print("\n📈 FASE 7 MAYORMENTE COMPLETA")
            print("   La implementación es sólida con algunas áreas menores")
            print("   que podrían mejorarse.")
            return True
        else:
            print("\n🚧 FASE 7 NECESITA MÁS TRABAJO")
            print("   Se requieren mejoras adicionales para completar")
            print("   exitosamente la fase.")
            return False
    
    def get_implementation_summary(self):
        """Get summary of what has been implemented."""
        summary = []
        summary.append("📋 RESUMEN DE IMPLEMENTACIÓN FASE 7:")
        summary.append("")
        
        # What's working well
        summary.append("✅ COMPONENTES EXITOSOS:")
        if self.stats['directories_ok'] >= 8:
            summary.append("   • Estructura de directorios completa")
        if self.stats.get('leetcode_contests', 0) > 0:
            summary.append(f"   • {self.stats['leetcode_contests']} contests de LeetCode implementados")
        if self.stats.get('codeforces_contests', 0) > 0:
            summary.append(f"   • {self.stats['codeforces_contests']} contests de Codeforces implementados")
        if self.stats.get('complete_problems', 0) > 0:
            summary.append(f"   • {self.stats['complete_problems']} problemas completamente implementados")
        if self.stats.get('tools', 0) > 0:
            summary.append(f"   • {self.stats['tools']} herramientas de gestión disponibles")
        
        # Areas needing work
        if self.errors or self.warnings:
            summary.append("")
            summary.append("🎯 ÁREAS DE MEJORA:")
            if self.errors:
                summary.append("   • Resolver errores críticos identificados")
            if self.warnings:
                summary.append("   • Atender advertencias para completar implementación")
        
        return "\n".join(summary)

def main():
    """Main validation function."""
    validator = Phase7Validator()
    
    print("🚀 Iniciando validación completa de la Fase 7")
    print("   Estructura de contests para programación competitiva")
    print()
    
    success = validator.validate_phase7()
    
    print("\n" + "=" * 50)
    print(validator.get_implementation_summary())
    
    if success:
        print(f"\n🌟 ¡Fase 7 implementada exitosamente!")
        return 0
    else:
        print(f"\n⚡ Fase 7 requiere trabajo adicional")
        return 1

if __name__ == "__main__":
    exit(main())

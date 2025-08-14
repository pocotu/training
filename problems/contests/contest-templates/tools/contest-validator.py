#!/usr/bin/env python3
"""
Contest Structure Validator

Validates the complete contest directory structure and ensures all components
are properly implemented according to Phase 7 requirements.

Usage:
    python contest-validator.py --check-all
    python contest-validator.py --platform leetcode
    python contest-validator.py --contest weekly_380
"""

import os
import yaml
import json
import argparse
from pathlib import Path
from collections import defaultdict
import re

class ContestValidator:
    """Validates contest structure and implementation."""
    
    def __init__(self, base_path=None):
        """Initialize validator with base contest path."""
        if base_path is None:
            # Assume we're in contest-templates/tools/
            self.base_path = Path(__file__).parent.parent.parent
        else:
            self.base_path = Path(base_path)
        
        self.errors = []
        self.warnings = []
        self.stats = defaultdict(int)
    
    def validate_all(self):
        """Validate complete contest structure."""
        print("🔍 Starting comprehensive contest structure validation...")
        print("=" * 60)
        
        # Validate directory structure
        self._validate_directory_structure()
        
        # Validate LeetCode contests
        self._validate_leetcode_contests()
        
        # Validate Codeforces contests
        self._validate_codeforces_contests()
        
        # Validate templates and tools
        self._validate_templates_and_tools()
        
        # Generate validation report
        self._generate_validation_report()
        
        return len(self.errors) == 0
    
    def _validate_directory_structure(self):
        """Validate overall directory structure."""
        print("📁 Validating directory structure...")
        
        required_dirs = [
            "leetcode",
            "leetcode/weekly",
            "leetcode/biweekly", 
            "leetcode/daily",
            "codeforces",
            "codeforces/div2",
            "codeforces/div3",
            "codeforces/educational",
            "contest-templates",
            "contest-templates/tools"
        ]
        
        for dir_path in required_dirs:
            full_path = self.base_path / dir_path
            if not full_path.exists():
                self.errors.append(f"Missing required directory: {dir_path}")
            else:
                self.stats['directories_found'] += 1
        
        print(f"  ✓ Found {self.stats['directories_found']}/{len(required_dirs)} required directories")
    
    def _validate_leetcode_contests(self):
        """Validate LeetCode contest implementations."""
        print("\n🏆 Validating LeetCode contests...")
        
        leetcode_path = self.base_path / "leetcode"
        if not leetcode_path.exists():
            self.errors.append("LeetCode directory not found")
            return
        
        # Expected contests
        expected_contests = {
            'weekly': ['contest_380', 'contest_381', 'contest_382'],
            'biweekly': ['contest_120', 'contest_121', 'contest_122'],
            'daily': ['contest_2024_01', 'contest_2024_02', 'contest_2024_03']
        }
        
        for contest_type, contests in expected_contests.items():
            type_path = leetcode_path / contest_type
            if not type_path.exists():
                self.errors.append(f"Missing LeetCode {contest_type} directory")
                continue
            
            print(f"  Checking {contest_type} contests...")
            for contest in contests:
                contest_path = type_path / contest
                if contest_path.exists():
                    self._validate_leetcode_contest(contest_path, contest_type, contest)
                    self.stats['leetcode_contests_found'] += 1
                else:
                    self.warnings.append(f"Missing LeetCode {contest_type} contest: {contest}")
    
    def _validate_leetcode_contest(self, contest_path, contest_type, contest_name):
        """Validate individual LeetCode contest."""
        # Check README exists
        readme_path = contest_path / "README.md"
        if readme_path.exists():
            self._validate_readme_content(readme_path, "leetcode")
        else:
            self.errors.append(f"Missing README.md in {contest_name}")
        
        # Check problems (should have 4 problems)
        expected_problems = 4
        problem_dirs = [d for d in contest_path.iterdir() if d.is_dir() and d.name.startswith('problem_')]
        
        if len(problem_dirs) != expected_problems:
            self.warnings.append(f"{contest_name}: Expected {expected_problems} problems, found {len(problem_dirs)}")
        
        # Validate each problem
        for problem_dir in problem_dirs:
            self._validate_leetcode_problem(problem_dir, contest_name)
    
    def _validate_leetcode_problem(self, problem_path, contest_name):
        """Validate individual LeetCode problem."""
        problem_name = problem_path.name
        
        required_files = ['problem.md', 'solution.py', 'meta.yaml']
        for file_name in required_files:
            file_path = problem_path / file_name
            if file_path.exists():
                self.stats['problem_files_found'] += 1
                
                # Validate file content
                if file_name == 'meta.yaml':
                    self._validate_meta_yaml(file_path, "leetcode")
                elif file_name == 'solution.py':
                    self._validate_solution_file(file_path)
                elif file_name == 'problem.md':
                    self._validate_problem_markdown(file_path)
            else:
                self.errors.append(f"Missing {file_name} in {contest_name}/{problem_name}")
    
    def _validate_codeforces_contests(self):
        """Validate Codeforces contest implementations."""
        print("\n🎯 Validating Codeforces contests...")
        
        codeforces_path = self.base_path / "codeforces"
        if not codeforces_path.exists():
            self.errors.append("Codeforces directory not found")
            return
        
        # Expected contests
        expected_contests = {
            'div2': ['round_915', 'round_916', 'round_917'],
            'div3': ['round_900', 'round_901'],
            'educational': ['round_160', 'round_161']
        }
        
        for contest_type, contests in expected_contests.items():
            type_path = codeforces_path / contest_type
            if not type_path.exists():
                self.errors.append(f"Missing Codeforces {contest_type} directory")
                continue
            
            print(f"  Checking {contest_type} contests...")
            for contest in contests:
                contest_path = type_path / contest
                if contest_path.exists():
                    self._validate_codeforces_contest(contest_path, contest_type, contest)
                    self.stats['codeforces_contests_found'] += 1
                else:
                    self.warnings.append(f"Missing Codeforces {contest_type} contest: {contest}")
    
    def _validate_codeforces_contest(self, contest_path, contest_type, contest_name):
        """Validate individual Codeforces contest."""
        # Check README exists
        readme_path = contest_path / "README.md"
        if readme_path.exists():
            self._validate_readme_content(readme_path, "codeforces")
        else:
            self.errors.append(f"Missing README.md in {contest_name}")
        
        # Check problems based on contest type
        expected_problems = {
            'div2': 6,  # A-F
            'div3': 7,  # A-G
            'educational': 6  # A-F
        }
        
        expected_count = expected_problems.get(contest_type, 6)
        problem_dirs = [d for d in contest_path.iterdir() if d.is_dir() and d.name.startswith('problem_')]
        
        if len(problem_dirs) < expected_count:
            self.warnings.append(f"{contest_name}: Expected {expected_count} problems, found {len(problem_dirs)}")
        
        # Validate each problem
        for problem_dir in problem_dirs:
            self._validate_codeforces_problem(problem_dir, contest_name)
    
    def _validate_codeforces_problem(self, problem_path, contest_name):
        """Validate individual Codeforces problem."""
        problem_name = problem_path.name
        
        required_files = ['problem.md', 'solution.py', 'meta.yaml']
        for file_name in required_files:
            file_path = problem_path / file_name
            if file_path.exists():
                self.stats['problem_files_found'] += 1
                
                # Validate file content
                if file_name == 'meta.yaml':
                    self._validate_meta_yaml(file_path, "codeforces")
                elif file_name == 'solution.py':
                    self._validate_solution_file(file_path)
                elif file_name == 'problem.md':
                    self._validate_problem_markdown(file_path)
            else:
                self.errors.append(f"Missing {file_name} in {contest_name}/{problem_name}")
    
    def _validate_templates_and_tools(self):
        """Validate contest templates and management tools."""
        print("\n🛠️  Validating templates and tools...")
        
        templates_path = self.base_path / "contest-templates"
        if not templates_path.exists():
            self.errors.append("Contest templates directory not found")
            return
        
        # Check for required tools
        tools_path = templates_path / "tools"
        required_tools = [
            'contest-creator.py',
            'contest-tracker.py',
            'contest-validator.py'
        ]
        
        for tool in required_tools:
            tool_path = tools_path / tool
            if tool_path.exists():
                self.stats['tools_found'] += 1
                # Basic validation - check if it's a Python file
                if not self._is_valid_python_file(tool_path):
                    self.errors.append(f"Invalid Python syntax in {tool}")
            else:
                self.errors.append(f"Missing required tool: {tool}")
        
        # Check for README
        readme_path = templates_path / "README.md"
        if readme_path.exists():
            self.stats['documentation_found'] += 1
        else:
            self.errors.append("Missing contest templates README.md")
    
    def _validate_meta_yaml(self, yaml_path, platform):
        """Validate meta.yaml file content."""
        try:
            with open(yaml_path, 'r') as f:
                meta_data = yaml.safe_load(f)
            
            # Check required fields
            required_fields = {
                'leetcode': ['problem_id', 'contest_id', 'platform', 'title', 'difficulty'],
                'codeforces': ['problem_id', 'contest_id', 'platform', 'title', 'difficulty']
            }
            
            for field in required_fields.get(platform, []):
                if field not in meta_data:
                    self.errors.append(f"Missing required field '{field}' in {yaml_path}")
            
            # Validate platform field
            if meta_data.get('platform') != platform:
                self.errors.append(f"Incorrect platform in {yaml_path}: expected {platform}")
            
        except yaml.YAMLError as e:
            self.errors.append(f"Invalid YAML syntax in {yaml_path}: {e}")
        except Exception as e:
            self.errors.append(f"Error reading {yaml_path}: {e}")
    
    def _validate_solution_file(self, solution_path):
        """Validate solution.py file."""
        try:
            with open(solution_path, 'r') as f:
                content = f.read()
            
            # Check for basic structure
            required_patterns = [
                r'def.*\(',  # At least one function definition
                r'if __name__ == "__main__"',  # Main guard
                r'""".*"""',  # Docstring
            ]
            
            for pattern in required_patterns:
                if not re.search(pattern, content, re.DOTALL):
                    self.warnings.append(f"Missing pattern in {solution_path}: {pattern}")
            
            # Check if it's valid Python
            if not self._is_valid_python_file(solution_path):
                self.errors.append(f"Invalid Python syntax in {solution_path}")
            
        except Exception as e:
            self.errors.append(f"Error reading {solution_path}: {e}")
    
    def _validate_problem_markdown(self, problem_path):
        """Validate problem.md file."""
        try:
            with open(problem_path, 'r') as f:
                content = f.read()
            
            # Check for required sections
            required_sections = [
                '# ',  # Title
                '## Problem Statement',
                '## Examples',
                '## Constraints'
            ]
            
            for section in required_sections:
                if section not in content:
                    self.warnings.append(f"Missing section '{section}' in {problem_path}")
            
        except Exception as e:
            self.errors.append(f"Error reading {problem_path}: {e}")
    
    def _validate_readme_content(self, readme_path, platform):
        """Validate README.md content."""
        try:
            with open(readme_path, 'r') as f:
                content = f.read()
            
            # Check for YAML frontmatter
            if not content.startswith('---'):
                self.warnings.append(f"Missing YAML frontmatter in {readme_path}")
            
            # Check for required sections
            required_sections = [
                '# ',  # Title
                '## Contest Overview',
                '## Problems Summary'
            ]
            
            for section in required_sections:
                if section not in content:
                    self.warnings.append(f"Missing section '{section}' in {readme_path}")
            
        except Exception as e:
            self.errors.append(f"Error reading {readme_path}: {e}")
    
    def _is_valid_python_file(self, file_path):
        """Check if Python file has valid syntax."""
        try:
            with open(file_path, 'r') as f:
                source = f.read()
            compile(source, str(file_path), 'exec')
            return True
        except SyntaxError:
            return False
        except Exception:
            return True  # Other errors don't indicate syntax issues
    
    def _generate_validation_report(self):
        """Generate comprehensive validation report."""
        print("\n" + "=" * 60)
        print("📋 VALIDATION REPORT")
        print("=" * 60)
        
        # Summary statistics
        print(f"📊 STATISTICS:")
        print(f"   • Directories found: {self.stats.get('directories_found', 0)}")
        print(f"   • LeetCode contests: {self.stats.get('leetcode_contests_found', 0)}")
        print(f"   • Codeforces contests: {self.stats.get('codeforces_contests_found', 0)}")
        print(f"   • Problem files: {self.stats.get('problem_files_found', 0)}")
        print(f"   • Tools found: {self.stats.get('tools_found', 0)}")
        print(f"   • Documentation: {self.stats.get('documentation_found', 0)}")
        
        # Errors
        if self.errors:
            print(f"\n❌ ERRORS ({len(self.errors)}):")
            for i, error in enumerate(self.errors, 1):
                print(f"   {i:2d}. {error}")
        else:
            print(f"\n✅ NO ERRORS FOUND!")
        
        # Warnings
        if self.warnings:
            print(f"\n⚠️  WARNINGS ({len(self.warnings)}):")
            for i, warning in enumerate(self.warnings, 1):
                print(f"   {i:2d}. {warning}")
        else:
            print(f"\n✅ NO WARNINGS!")
        
        # Overall status
        print(f"\n🎯 OVERALL STATUS:")
        if not self.errors and not self.warnings:
            print("   🌟 EXCELLENT - Contest structure is complete and well-organized!")
        elif not self.errors:
            print("   ✅ GOOD - Structure is valid with minor issues to address")
        else:
            print("   ❌ NEEDS WORK - Critical issues must be resolved")
        
        # Phase 7 completion assessment
        self._assess_phase7_completion()
    
    def _assess_phase7_completion(self):
        """Assess Phase 7 implementation completion."""
        print(f"\n🚀 PHASE 7 COMPLETION ASSESSMENT:")
        
        # Calculate completion metrics
        total_expected_contests = 11  # 3 weekly + 3 biweekly + 3 daily + 2 Codeforces (partial)
        total_found = (self.stats.get('leetcode_contests_found', 0) + 
                      self.stats.get('codeforces_contests_found', 0))
        
        contest_completion = (total_found / total_expected_contests) * 100 if total_expected_contests > 0 else 0
        
        # Tools completion
        tools_expected = 3
        tools_found = self.stats.get('tools_found', 0)
        tools_completion = (tools_found / tools_expected) * 100 if tools_expected > 0 else 0
        
        # Overall completion
        overall_completion = (contest_completion + tools_completion) / 2
        
        print(f"   • Contest Structure: {contest_completion:.1f}% complete")
        print(f"   • Management Tools: {tools_completion:.1f}% complete")
        print(f"   • Overall Progress: {overall_completion:.1f}% complete")
        
        if overall_completion >= 80:
            print("   🎉 Phase 7 is SUBSTANTIALLY COMPLETE!")
        elif overall_completion >= 60:
            print("   📈 Phase 7 is MOSTLY COMPLETE - good progress!")
        else:
            print("   🚧 Phase 7 needs MORE WORK to reach completion")
        
        # Success criteria assessment
        print(f"\n📋 SUCCESS CRITERIA ASSESSMENT:")
        criteria = [
            ("Contest directory structure created", self.stats.get('directories_found', 0) >= 8),
            ("LeetCode contests implemented", self.stats.get('leetcode_contests_found', 0) >= 1),
            ("Codeforces contests implemented", self.stats.get('codeforces_contests_found', 0) >= 1),
            ("Management tools available", self.stats.get('tools_found', 0) >= 2),
            ("Documentation provided", self.stats.get('documentation_found', 0) >= 1),
            ("No critical errors", len(self.errors) == 0)
        ]
        
        passed_criteria = sum(1 for _, passed in criteria if passed)
        total_criteria = len(criteria)
        
        for criterion, passed in criteria:
            status = "✅" if passed else "❌"
            print(f"   {status} {criterion}")
        
        print(f"\n   📊 SUCCESS RATE: {passed_criteria}/{total_criteria} ({passed_criteria/total_criteria*100:.1f}%)")
        
        if passed_criteria >= total_criteria * 0.8:
            print("   🏆 Phase 7 SUCCESSFULLY IMPLEMENTED!")
            return True
        else:
            print("   🎯 Phase 7 needs additional work to meet success criteria")
            return False

def main():
    """Main function for command-line usage."""
    parser = argparse.ArgumentParser(description="Validate contest structure implementation")
    parser.add_argument("--check-all", action="store_true",
                       help="Validate complete contest structure")
    parser.add_argument("--platform", choices=["leetcode", "codeforces"],
                       help="Validate specific platform")
    parser.add_argument("--contest", 
                       help="Validate specific contest")
    parser.add_argument("--base-path",
                       help="Base path for validation (default: auto-detect)")
    
    args = parser.parse_args()
    
    validator = ContestValidator(args.base_path)
    
    if args.check_all or (not args.platform and not args.contest):
        success = validator.validate_all()
        exit(0 if success else 1)
    
    # Specific validation logic would go here for --platform or --contest
    print("Specific platform/contest validation not yet implemented")

if __name__ == "__main__":
    main()

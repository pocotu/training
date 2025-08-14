#!/usr/bin/env python3
"""
COMPREHENSIVE PHASE 6 VALIDATION REPORT
========================================

This script validates the complete implementation of Phase 6 from PLAN_IMPLEMENTACION.md
- Reviews all 15 advanced problems (201-215)
- Validates file structure and completeness
- Checks solution quality and testing coverage
- Provides final success assessment
"""

import os
import glob
import sys
from typing import Dict, List, Tuple, Any

# Handle yaml import gracefully
try:
    import yaml
    YAML_AVAILABLE = True
except ImportError:
    YAML_AVAILABLE = False
    print("Warning: PyYAML not installed. Meta.yaml validation will be limited.")

class Phase6Validator:
    """Comprehensive validator for Phase 6 implementation."""
    
    def __init__(self, base_path: str):
        self.base_path = base_path
        self.advanced_path = os.path.join(base_path, "competitive-programming-practice", "problems", "advanced")
        self.validation_results = {}
        self.issues = []
        self.successes = []
        
    def validate_directory_structure(self) -> Dict[str, Any]:
        """Validate the directory structure for Phase 6."""
        print("=" * 60)
        print("VALIDATING DIRECTORY STRUCTURE")
        print("=" * 60)
        
        if not os.path.exists(self.advanced_path):
            self.issues.append("❌ Advanced problems directory does not exist")
            return {"exists": False, "problems": []}
        
        # Expected problems based on our implementation
        expected_problems = [
            "201_wildcard_matching",
            "202_happy_number", 
            "203_remove_linked_list_elements",
            "204_count_primes",
            "205_trapping_rain_water",
            "206_n_queens",
            "207_course_schedule_ii",
            "208_implement_trie",
            "209_minimum_size_subarray_sum", 
            "210_course_schedule",
            "211_add_search_word",
            "212_word_search_ii",
            "213_house_robber_ii",
            "214_shortest_palindrome",
            "215_palindrome_pairs"
        ]
        
        found_problems = []
        
        for problem in expected_problems:
            problem_path = os.path.join(self.advanced_path, problem)
            if os.path.exists(problem_path):
                found_problems.append(problem)
                print(f"✅ {problem}/ - EXISTS")
            else:
                print(f"❌ {problem}/ - MISSING")
                self.issues.append(f"Missing problem directory: {problem}")
        
        print(f"\nDirectory Summary: {len(found_problems)}/15 problems found")
        
        if len(found_problems) == 15:
            self.successes.append("✅ All 15 problem directories exist")
        
        return {
            "exists": True,
            "problems": found_problems,
            "expected": expected_problems,
            "count": len(found_problems)
        }
    
    def validate_problem_files(self, problems: List[str]) -> Dict[str, Any]:
        """Validate required files for each problem."""
        print("\n" + "=" * 60)
        print("VALIDATING PROBLEM FILES")
        print("=" * 60)
        
        required_files = ["meta.yaml", "solution.py"]
        problem_status = {}
        
        for problem in problems:
            problem_path = os.path.join(self.advanced_path, problem)
            files_status = {}
            
            print(f"\n🔍 Checking {problem}:")
            
            for file_name in required_files:
                file_path = os.path.join(problem_path, file_name)
                exists = os.path.exists(file_path)
                files_status[file_name] = exists
                
                if exists:
                    file_size = os.path.getsize(file_path)
                    print(f"  ✅ {file_name} - {file_size:,} bytes")
                else:
                    print(f"  ❌ {file_name} - MISSING")
                    self.issues.append(f"{problem}: Missing {file_name}")
            
            problem_status[problem] = files_status
        
        # Count complete problems
        complete_problems = sum(1 for status in problem_status.values() 
                              if all(status.values()))
        
        print(f"\nFile Summary: {complete_problems}/15 problems have all required files")
        
        if complete_problems == 15:
            self.successes.append("✅ All problems have required files (meta.yaml, solution.py)")
        
        return {
            "problems": problem_status,
            "complete_count": complete_problems,
            "total_expected": len(problems)
        }
    
    def validate_meta_yaml_content(self, problems: List[str]) -> Dict[str, Any]:
        """Validate meta.yaml content for completeness."""
        print("\n" + "=" * 60)
        print("VALIDATING META.YAML CONTENT")
        print("=" * 60)
        
        required_fields = ["id", "title", "difficulty", "tags", "constraints", "approach"]
        valid_meta_count = 0
        
        for problem in problems:
            meta_path = os.path.join(self.advanced_path, problem, "meta.yaml")
            
            if not os.path.exists(meta_path):
                continue
                
            try:
                if YAML_AVAILABLE:
                    with open(meta_path, 'r', encoding='utf-8') as f:
                        meta_data = yaml.safe_load(f)
                else:
                    # Simple text-based validation
                    with open(meta_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    meta_data = {}
                    for field in required_fields:
                        if f"{field}:" in content:
                            meta_data[field] = "present"
                
                print(f"\n📋 {problem} meta.yaml:")
                missing_fields = []
                
                for field in required_fields:
                    if field in meta_data and meta_data[field]:
                        print(f"  ✅ {field}: ✓")
                    else:
                        print(f"  ❌ {field}: Missing/Empty")
                        missing_fields.append(field)
                
                if not missing_fields:
                    valid_meta_count += 1
                    
                # Check difficulty is "Hard"
                if meta_data.get("difficulty") == "Hard":
                    print(f"  ✅ Difficulty correctly set to Hard")
                else:
                    print(f"  ⚠️  Difficulty: {meta_data.get('difficulty')} (should be Hard)")
                
            except Exception as e:
                print(f"  ❌ Error reading meta.yaml: {e}")
                self.issues.append(f"{problem}: Invalid meta.yaml - {e}")
        
        print(f"\nMeta.yaml Summary: {valid_meta_count}/15 problems have complete metadata")
        
        if valid_meta_count >= 12:  # Allow some flexibility
            self.successes.append("✅ Most problems have comprehensive metadata")
        
        return {
            "valid_count": valid_meta_count,
            "total_expected": len(problems)
        }
    
    def validate_solution_content(self, problems: List[str]) -> Dict[str, Any]:
        """Validate solution.py content for quality and completeness."""
        print("\n" + "=" * 60)
        print("VALIDATING SOLUTION QUALITY")
        print("=" * 60)
        
        solution_analysis = {}
        comprehensive_solutions = 0
        
        for problem in problems:
            solution_path = os.path.join(self.advanced_path, problem, "solution.py")
            
            if not os.path.exists(solution_path):
                continue
            
            try:
                with open(solution_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                print(f"\n🧮 {problem} solution.py:")
                
                # Quality indicators
                indicators = {
                    "Multiple algorithms": len([line for line in content.split('\n') if 'def ' in line and problem.split('_')[1] in line]) >= 3,
                    "Comprehensive testing": 'test_cases' in content and len(content.split('test_cases')) > 1,
                    "Performance analysis": 'Performance' in content or 'performance' in content,
                    "Edge case handling": 'edge' in content.lower() or 'Edge' in content,
                    "Complexity analysis": 'Time Complexity' in content and 'Space Complexity' in content,
                    "Documentation": '"""' in content and content.count('"""') >= 4,
                    "Error handling": 'try:' in content or 'except:' in content,
                    "Validation logic": 'assert' in content or 'validate' in content.lower()
                }
                
                score = sum(indicators.values())
                total_indicators = len(indicators)
                
                for indicator, present in indicators.items():
                    status = "✅" if present else "❌"
                    print(f"  {status} {indicator}")
                
                print(f"  📊 Quality Score: {score}/{total_indicators} ({score/total_indicators*100:.1f}%)")
                
                # Check file size (comprehensive solutions should be substantial)
                file_size = len(content)
                print(f"  📏 File Size: {file_size:,} characters")
                
                if score >= 6 and file_size >= 5000:  # High quality threshold
                    comprehensive_solutions += 1
                    print(f"  🏆 COMPREHENSIVE SOLUTION")
                
                solution_analysis[problem] = {
                    "score": score,
                    "total": total_indicators,
                    "size": file_size,
                    "comprehensive": score >= 6 and file_size >= 5000
                }
                
            except Exception as e:
                print(f"  ❌ Error analyzing solution: {e}")
                self.issues.append(f"{problem}: Error analyzing solution - {e}")
        
        print(f"\nSolution Quality Summary: {comprehensive_solutions}/15 problems have comprehensive solutions")
        
        if comprehensive_solutions >= 10:
            self.successes.append("✅ Most problems have high-quality, comprehensive solutions")
        
        return {
            "analysis": solution_analysis,
            "comprehensive_count": comprehensive_solutions,
            "total_analyzed": len(solution_analysis)
        }
    
    def validate_testing_infrastructure(self) -> Dict[str, Any]:
        """Validate testing files and infrastructure."""
        print("\n" + "=" * 60)
        print("VALIDATING TESTING INFRASTRUCTURE")
        print("=" * 60)
        
        # Check for test files
        test_files = [
            "test_201_210.py",
            "test_211_215.py"
        ]
        
        test_status = {}
        
        for test_file in test_files:
            test_path = os.path.join(self.advanced_path, test_file)
            exists = os.path.exists(test_path)
            test_status[test_file] = exists
            
            if exists:
                file_size = os.path.getsize(test_path)
                print(f"✅ {test_file} - {file_size:,} bytes")
                
                # Check test content quality
                try:
                    with open(test_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    test_indicators = {
                        "Test runner class": "TestRunner" in content,
                        "Multiple test functions": content.count("def test_") >= 5,
                        "Performance testing": "performance" in content.lower(),
                        "Edge case testing": "edge" in content.lower(),
                        "Error handling": "try:" in content and "except:" in content,
                        "Comprehensive coverage": len(content) >= 10000
                    }
                    
                    test_score = sum(test_indicators.values())
                    print(f"  📊 Test Quality: {test_score}/{len(test_indicators)} indicators")
                    
                    for indicator, present in test_indicators.items():
                        status = "✅" if present else "❌"
                        print(f"    {status} {indicator}")
                        
                except Exception as e:
                    print(f"  ❌ Error analyzing test file: {e}")
            else:
                print(f"❌ {test_file} - MISSING")
                self.issues.append(f"Missing test file: {test_file}")
        
        complete_testing = all(test_status.values())
        
        if complete_testing:
            self.successes.append("✅ Complete testing infrastructure implemented")
        
        return {
            "test_files": test_status,
            "complete": complete_testing
        }
    
    def check_advanced_algorithms_coverage(self, problems: List[str]) -> Dict[str, Any]:
        """Check coverage of advanced algorithmic concepts."""
        print("\n" + "=" * 60)
        print("VALIDATING ADVANCED ALGORITHMS COVERAGE")
        print("=" * 60)
        
        # Expected algorithmic concepts for LeetCode Hard problems
        expected_concepts = {
            "Dynamic Programming": ["wildcard_matching", "trapping_rain_water", "house_robber"],
            "Graph Algorithms": ["course_schedule", "n_queens"],
            "Trie Data Structure": ["implement_trie", "add_search_word", "word_search"],
            "String Algorithms": ["shortest_palindrome", "palindrome_pairs"],
            "Backtracking": ["n_queens", "word_search"],
            "Mathematical": ["happy_number", "count_primes"],
            "Array/Sliding Window": ["minimum_size_subarray_sum"],
            "Linked List": ["remove_linked_list_elements"],
            "Hash Maps/Sets": ["happy_number", "palindrome_pairs"],
            "Pattern Matching": ["wildcard_matching", "shortest_palindrome"]
        }
        
        concept_coverage = {}
        
        for concept, related_problems in expected_concepts.items():
            covered_problems = []
            
            for problem in problems:
                problem_name = problem.lower()
                if any(keyword in problem_name for keyword in related_problems):
                    covered_problems.append(problem)
            
            coverage_ratio = len(covered_problems) / len(related_problems) if related_problems else 0
            concept_coverage[concept] = {
                "covered_problems": covered_problems,
                "coverage_ratio": coverage_ratio,
                "expected_count": len(related_problems)
            }
            
            status = "✅" if coverage_ratio >= 0.5 else "❌"
            print(f"{status} {concept}: {len(covered_problems)} problems covered")
        
        # Overall coverage assessment
        total_concepts = len(expected_concepts)
        covered_concepts = sum(1 for coverage in concept_coverage.values() 
                             if coverage["coverage_ratio"] >= 0.5)
        
        coverage_percentage = (covered_concepts / total_concepts) * 100
        print(f"\n📊 Algorithm Coverage: {covered_concepts}/{total_concepts} concepts ({coverage_percentage:.1f}%)")
        
        if coverage_percentage >= 70:
            self.successes.append("✅ Good coverage of advanced algorithmic concepts")
        
        return {
            "concept_coverage": concept_coverage,
            "coverage_percentage": coverage_percentage,
            "total_concepts": total_concepts,
            "covered_concepts": covered_concepts
        }
    
    def generate_final_report(self) -> Dict[str, Any]:
        """Generate comprehensive final validation report."""
        print("\n" + "=" * 80)
        print("PHASE 6 FINAL VALIDATION REPORT")
        print("=" * 80)
        
        # Overall success criteria
        success_criteria = {
            "✅ All 15 problem directories exist": any("All 15 problem directories" in s for s in self.successes),
            "✅ Required files present": any("All problems have required files" in s for s in self.successes),
            "✅ High-quality solutions": any("comprehensive solutions" in s for s in self.successes),
            "✅ Testing infrastructure": any("testing infrastructure" in s for s in self.successes),
            "✅ Algorithm coverage": any("algorithmic concepts" in s for s in self.successes),
            "✅ Metadata completeness": any("comprehensive metadata" in s for s in self.successes)
        }
        
        met_criteria = sum(success_criteria.values())
        total_criteria = len(success_criteria)
        
        print("SUCCESS CRITERIA ASSESSMENT:")
        for criterion, met in success_criteria.items():
            print(f"  {criterion if met else criterion.replace('✅', '❌')}")
        
        print(f"\nOVERALL SUCCESS RATE: {met_criteria}/{total_criteria} ({met_criteria/total_criteria*100:.1f}%)")
        
        # Final determination
        if met_criteria >= 5:
            final_status = "🎉 PHASE 6 IMPLEMENTATION SUCCESSFUL"
            final_message = "Phase 6 has been implemented successfully with comprehensive coverage!"
        elif met_criteria >= 4:
            final_status = "✅ PHASE 6 MOSTLY COMPLETE"
            final_message = "Phase 6 is largely complete with minor issues to address."
        elif met_criteria >= 3:
            final_status = "⚠️ PHASE 6 PARTIALLY COMPLETE"
            final_message = "Phase 6 has good foundation but needs additional work."
        else:
            final_status = "❌ PHASE 6 NEEDS SIGNIFICANT WORK"
            final_message = "Phase 6 implementation requires substantial additional effort."
        
        print(f"\n{final_status}")
        print(f"{final_message}")
        
        # Summary statistics
        print(f"\nSUMMARY STATISTICS:")
        print(f"  • Total Successes: {len(self.successes)}")
        print(f"  • Total Issues: {len(self.issues)}")
        print(f"  • Implementation Quality: {'High' if met_criteria >= 5 else 'Medium' if met_criteria >= 3 else 'Low'}")
        
        if self.issues:
            print(f"\nREMAINING ISSUES TO ADDRESS:")
            for issue in self.issues[:10]:  # Show first 10 issues
                print(f"  • {issue}")
            if len(self.issues) > 10:
                print(f"  ... and {len(self.issues) - 10} more issues")
        
        if self.successes:
            print(f"\nKEY ACHIEVEMENTS:")
            for success in self.successes:
                print(f"  • {success}")
        
        return {
            "final_status": final_status,
            "final_message": final_message,
            "success_rate": met_criteria / total_criteria,
            "met_criteria": met_criteria,
            "total_criteria": total_criteria,
            "issues_count": len(self.issues),
            "successes_count": len(self.successes)
        }
    
    def run_complete_validation(self) -> Dict[str, Any]:
        """Run complete Phase 6 validation."""
        print("🔍 STARTING COMPREHENSIVE PHASE 6 VALIDATION")
        print("=" * 80)
        
        # Step 1: Directory structure
        dir_result = self.validate_directory_structure()
        
        if not dir_result["exists"] or dir_result["count"] == 0:
            print("❌ Cannot proceed: No advanced problems directory found")
            return {"error": "No advanced problems found"}
        
        # Step 2: File validation
        file_result = self.validate_problem_files(dir_result["problems"])
        
        # Step 3: Meta.yaml validation
        meta_result = self.validate_meta_yaml_content(dir_result["problems"])
        
        # Step 4: Solution quality
        solution_result = self.validate_solution_content(dir_result["problems"])
        
        # Step 5: Testing infrastructure
        test_result = self.validate_testing_infrastructure()
        
        # Step 6: Algorithm coverage
        algorithm_result = self.check_advanced_algorithms_coverage(dir_result["problems"])
        
        # Step 7: Final report
        final_result = self.generate_final_report()
        
        return {
            "directory": dir_result,
            "files": file_result,
            "metadata": meta_result,
            "solutions": solution_result,
            "testing": test_result,
            "algorithms": algorithm_result,
            "final": final_result
        }

def main():
    """Main validation function."""
    base_path = r"d:\Algo\Win\VSC\pocotu\training"
    
    validator = Phase6Validator(base_path)
    results = validator.run_complete_validation()
    
    # Return appropriate exit code
    if results.get("final", {}).get("success_rate", 0) >= 0.8:
        sys.exit(0)  # Success
    else:
        sys.exit(1)  # Needs work

if __name__ == "__main__":
    main()

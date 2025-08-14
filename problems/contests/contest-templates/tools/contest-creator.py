#!/usr/bin/env python3
"""
Contest Creator Tool

Creates directory structure and template files for new competitive programming contests.
Supports LeetCode and Codeforces platforms with appropriate templates.

Usage:
    python contest-creator.py --platform leetcode --type weekly --number 383
    python contest-creator.py --platform codeforces --type div2 --number 918
"""

import os
import argparse
import yaml
from pathlib import Path
from datetime import datetime, timedelta

class ContestCreator:
    """Creates contest directory structure and template files."""
    
    def __init__(self, base_path=None):
        """Initialize contest creator with base path."""
        if base_path is None:
            # Assume we're in contest-templates/tools/
            self.base_path = Path(__file__).parent.parent.parent
        else:
            self.base_path = Path(base_path)
        
        self.templates_path = self.base_path / "contest-templates"
    
    def create_leetcode_contest(self, contest_type, number):
        """Create LeetCode contest structure."""
        contest_name = f"contest_{number}"
        if contest_type == "weekly":
            contest_dir = self.base_path / "leetcode" / "weekly" / contest_name
        elif contest_type == "biweekly":
            contest_dir = self.base_path / "leetcode" / "biweekly" / contest_name
        elif contest_type == "daily":
            contest_dir = self.base_path / "leetcode" / "daily" / contest_name
        else:
            raise ValueError(f"Unknown LeetCode contest type: {contest_type}")
        
        # Create contest directory
        contest_dir.mkdir(parents=True, exist_ok=True)
        
        # Create contest README
        self._create_leetcode_contest_readme(contest_dir, contest_type, number)
        
        # Create problem directories
        num_problems = 4  # LeetCode contests typically have 4 problems
        for i in range(1, num_problems + 1):
            problem_dir = contest_dir / f"problem_{i}"
            problem_dir.mkdir(exist_ok=True)
            
            self._create_leetcode_problem_files(problem_dir, contest_type, number, i)
        
        print(f"Created LeetCode {contest_type} contest {number} at {contest_dir}")
        return contest_dir
    
    def create_codeforces_contest(self, contest_type, number):
        """Create Codeforces contest structure."""
        if contest_type == "div2":
            contest_dir = self.base_path / "codeforces" / "div2" / f"round_{number}"
            num_problems = 6  # A-F
        elif contest_type == "div3":
            contest_dir = self.base_path / "codeforces" / "div3" / f"round_{number}"
            num_problems = 7  # A-G
        elif contest_type == "educational":
            contest_dir = self.base_path / "codeforces" / "educational" / f"round_{number}"
            num_problems = 6  # A-F
        else:
            raise ValueError(f"Unknown Codeforces contest type: {contest_type}")
        
        # Create contest directory
        contest_dir.mkdir(parents=True, exist_ok=True)
        
        # Create contest README
        self._create_codeforces_contest_readme(contest_dir, contest_type, number)
        
        # Create problem directories
        for i in range(num_problems):
            problem_letter = chr(ord('A') + i)
            problem_dir = contest_dir / f"problem_{problem_letter.lower()}"
            problem_dir.mkdir(exist_ok=True)
            
            self._create_codeforces_problem_files(problem_dir, contest_type, number, problem_letter)
        
        print(f"Created Codeforces {contest_type} contest {number} at {contest_dir}")
        return contest_dir
    
    def _create_leetcode_contest_readme(self, contest_dir, contest_type, number):
        """Create README for LeetCode contest."""
        content = f"""---
contest_id: "{contest_type}_{number}"
platform: "leetcode"
contest_type: "{contest_type}"
contest_number: {number}
date: "{self._get_contest_date()}"
duration: "90 minutes"
problems_count: 4
difficulty_range: "Easy to Hard"
---

# LeetCode {contest_type.title()} Contest {number}

**Date:** {self._get_contest_date()}  
**Duration:** 90 minutes  
**Problems:** 4  

## Contest Overview
This contest features a typical progression from Easy to Hard problems, designed to test various algorithmic and problem-solving skills.

## Problems Summary

| Problem | Title | Difficulty | Points | Tags |
|---------|-------|------------|--------|------|
| 1 | [Problem Title] | Easy | 3 | [Tags] |
| 2 | [Problem Title] | Medium | 4 | [Tags] |
| 3 | [Problem Title] | Medium | 5 | [Tags] |
| 4 | [Problem Title] | Hard | 7 | [Tags] |

## Contest Strategy
- **0-15 minutes:** Read and solve Problem 1
- **15-35 minutes:** Work on Problem 2
- **35-60 minutes:** Tackle Problem 3
- **60-90 minutes:** Attempt Problem 4 or review solutions

## Learning Objectives
1. **Problem 1:** Basic implementation and edge case handling
2. **Problem 2:** Common algorithmic patterns
3. **Problem 3:** Advanced data structures or algorithms
4. **Problem 4:** Complex problem solving and optimization

## Post-Contest Analysis
[Add analysis after completing the contest]
"""
        
        readme_path = contest_dir / "README.md"
        readme_path.write_text(content)
    
    def _create_codeforces_contest_readme(self, contest_dir, contest_type, number):
        """Create README for Codeforces contest."""
        if contest_type == "div2":
            duration = "120 minutes"
            problems = "6 (A-F)"
        elif contest_type == "div3":
            duration = "135 minutes" 
            problems = "7 (A-G)"
        else:  # educational
            duration = "120 minutes"
            problems = "6 (A-F)"
        
        content = f"""---
contest_id: "{contest_type}_{number}"
platform: "codeforces"
contest_type: "{contest_type}"
round_number: {number}
date: "{self._get_contest_date()}"
duration: "{duration}"
problems_count: {problems.split()[0]}
difficulty_range: "{problems.split()[1]}"
---

# Codeforces Round #{number} ({contest_type.replace('div', 'Div. ').title()})

**Date:** {self._get_contest_date()}  
**Duration:** {duration}  
**Problems:** {problems}  

## Contest Overview
{self._get_codeforces_description(contest_type)}

## Problems Summary

| Problem | Title | Difficulty | Points | Tags |
|---------|-------|------------|--------|------|
{self._generate_problem_table(contest_type)}

## Contest Statistics
- **Participants:** [TBD]
- **Successful Submissions:** [TBD]

## Learning Objectives
{self._get_learning_objectives(contest_type)}

## Contest Strategy
{self._get_contest_strategy(contest_type)}

## Post-Contest Analysis
[Add analysis after completing the contest]
"""
        
        readme_path = contest_dir / "README.md"
        readme_path.write_text(content)
    
    def _create_leetcode_problem_files(self, problem_dir, contest_type, contest_number, problem_number):
        """Create problem files for LeetCode."""
        # Load templates
        templates_dir = self.templates_path / "leetcode"
        
        # Create problem.md
        problem_template = self._load_template(templates_dir / "problem-template.md")
        problem_content = problem_template.format(
            contest_type=contest_type,
            contest_number=contest_number,
            problem_number=problem_number,
            difficulty=self._get_leetcode_difficulty(problem_number),
            points=self._get_leetcode_points(problem_number)
        )
        (problem_dir / "problem.md").write_text(problem_content)
        
        # Create solution.py
        solution_template = self._load_template(templates_dir / "solution-template.py")
        solution_content = solution_template.format(
            contest_type=contest_type,
            contest_number=contest_number,
            problem_number=problem_number
        )
        (problem_dir / "solution.py").write_text(solution_content)
        
        # Create meta.yaml
        meta_data = {
            'problem_id': f"LC_{contest_type[0].upper()}{contest_number}_P{problem_number}",
            'contest_id': f"{contest_type}_{contest_number}",
            'platform': 'leetcode',
            'contest_type': contest_type,
            'problem_number': problem_number,
            'title': '[Problem Title]',
            'difficulty': self._get_leetcode_difficulty(problem_number),
            'points': self._get_leetcode_points(problem_number),
            'tags': ['[tag1]', '[tag2]', '[tag3]']
        }
        
        with open(problem_dir / "meta.yaml", 'w') as f:
            yaml.dump(meta_data, f, default_flow_style=False)
    
    def _create_codeforces_problem_files(self, problem_dir, contest_type, contest_number, problem_letter):
        """Create problem files for Codeforces."""
        # Load templates
        templates_dir = self.templates_path / "codeforces"
        
        # Create problem.md
        problem_template = self._load_template(templates_dir / "problem-template.md")
        problem_content = problem_template.format(
            contest_type=contest_type,
            contest_number=contest_number,
            problem_letter=problem_letter,
            difficulty=self._get_codeforces_difficulty(problem_letter),
            points=self._get_codeforces_points(problem_letter)
        )
        (problem_dir / "problem.md").write_text(problem_content)
        
        # Create solution.py
        solution_template = self._load_template(templates_dir / "solution-template.py")
        solution_content = solution_template.format(
            contest_type=contest_type,
            contest_number=contest_number,
            problem_letter=problem_letter
        )
        (problem_dir / "solution.py").write_text(solution_content)
        
        # Create meta.yaml
        meta_data = {
            'problem_id': f"{contest_number}{problem_letter}",
            'contest_id': f"{contest_type}_{contest_number}",
            'platform': 'codeforces',
            'problem_letter': problem_letter,
            'title': '[Problem Title]',
            'difficulty': self._get_codeforces_difficulty(problem_letter),
            'points': self._get_codeforces_points(problem_letter),
            'tags': ['[tag1]', '[tag2]', '[tag3]']
        }
        
        with open(problem_dir / "meta.yaml", 'w') as f:
            yaml.dump(meta_data, f, default_flow_style=False)
    
    def _load_template(self, template_path):
        """Load template file content."""
        try:
            return template_path.read_text()
        except FileNotFoundError:
            # Return basic template if file doesn't exist
            return "# Template not found\n[Add template content here]"
    
    def _get_contest_date(self):
        """Get formatted contest date."""
        return datetime.now().strftime("%Y-%m-%d")
    
    def _get_leetcode_difficulty(self, problem_number):
        """Get LeetCode problem difficulty based on number."""
        difficulties = {1: "Easy", 2: "Medium", 3: "Medium", 4: "Hard"}
        return difficulties.get(problem_number, "Medium")
    
    def _get_leetcode_points(self, problem_number):
        """Get LeetCode problem points based on number."""
        points = {1: 3, 2: 4, 3: 5, 4: 7}
        return points.get(problem_number, 4)
    
    def _get_codeforces_difficulty(self, problem_letter):
        """Get Codeforces problem difficulty based on letter."""
        difficulties = {
            'A': 800, 'B': 1000, 'C': 1200, 'D': 1600, 'E': 1900, 'F': 2200, 'G': 2500
        }
        return difficulties.get(problem_letter, 1200)
    
    def _get_codeforces_points(self, problem_letter):
        """Get Codeforces problem points based on letter."""
        points = {
            'A': 500, 'B': 1000, 'C': 1500, 'D': 2000, 'E': 2500, 'F': 3000, 'G': 3500
        }
        return points.get(problem_letter, 1500)
    
    def _get_codeforces_description(self, contest_type):
        """Get contest description based on type."""
        descriptions = {
            'div2': "Div. 2 contests are designed for participants with rating below 2100.",
            'div3': "Div. 3 contests are designed for participants with rating below 1600.",
            'educational': "Educational contests focus on learning specific algorithmic techniques."
        }
        return descriptions.get(contest_type, "Contest description")
    
    def _generate_problem_table(self, contest_type):
        """Generate problem table for Codeforces README."""
        if contest_type == "div2":
            problems = ['A', 'B', 'C', 'D', 'E', 'F']
        elif contest_type == "div3":
            problems = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
        else:  # educational
            problems = ['A', 'B', 'C', 'D', 'E', 'F']
        
        table_lines = []
        for letter in problems:
            difficulty = self._get_codeforces_difficulty(letter)
            points = self._get_codeforces_points(letter)
            table_lines.append(f"| {letter} | [Problem Title] | {difficulty} | {points} | [Tags] |")
        
        return "\n".join(table_lines)
    
    def _get_learning_objectives(self, contest_type):
        """Get learning objectives based on contest type."""
        objectives = {
            'div2': """1. **Problem A:** Basic implementation and math
2. **Problem B:** Greedy algorithms and observations
3. **Problem C:** Data structures and algorithms
4. **Problem D:** Advanced algorithms and techniques
5. **Problem E:** Complex problem solving
6. **Problem F:** Expert-level techniques""",
            'div3': """1. **Problem A:** Simple implementation
2. **Problem B:** Basic algorithms
3. **Problem C:** Standard techniques
4. **Problem D:** Intermediate algorithms
5. **Problem E:** Data structures
6. **Problem F:** Advanced techniques
7. **Problem G:** Complex problem solving""",
            'educational': """1. **Focus on specific algorithmic concepts**
2. **Progressive difficulty increase**
3. **Educational problem explanations**
4. **Practice standard techniques**"""
        }
        return objectives.get(contest_type, "Learning objectives")
    
    def _get_contest_strategy(self, contest_type):
        """Get contest strategy based on type."""
        if contest_type == "div2":
            return """- **0-15 minutes:** Solve A quickly
- **15-35 minutes:** Work on B
- **35-65 minutes:** Tackle C
- **65-90 minutes:** Attempt D
- **90-120 minutes:** Try E or review solutions"""
        elif contest_type == "div3":
            return """- **0-10 minutes:** Solve A
- **10-25 minutes:** Work on B  
- **25-45 minutes:** Tackle C
- **45-75 minutes:** Attempt D
- **75-105 minutes:** Try E
- **105-135 minutes:** Work on F/G"""
        else:  # educational
            return """- **Focus on understanding concepts**
- **Take time to learn from each problem**
- **Practice specific techniques**
- **Don't rush through problems**"""

def main():
    """Main function for command-line usage."""
    parser = argparse.ArgumentParser(description="Create competitive programming contest structure")
    parser.add_argument("--platform", choices=["leetcode", "codeforces"], required=True,
                       help="Contest platform")
    parser.add_argument("--type", required=True,
                       help="Contest type (weekly/biweekly/daily for LeetCode, div2/div3/educational for Codeforces)")
    parser.add_argument("--number", type=int, required=True,
                       help="Contest number")
    parser.add_argument("--base-path", 
                       help="Base path for contest creation (default: auto-detect)")
    
    args = parser.parse_args()
    
    creator = ContestCreator(args.base_path)
    
    if args.platform == "leetcode":
        if args.type not in ["weekly", "biweekly", "daily"]:
            print("Error: LeetCode contest type must be weekly, biweekly, or daily")
            return
        creator.create_leetcode_contest(args.type, args.number)
    elif args.platform == "codeforces":
        if args.type not in ["div2", "div3", "educational"]:
            print("Error: Codeforces contest type must be div2, div3, or educational")
            return
        creator.create_codeforces_contest(args.type, args.number)

if __name__ == "__main__":
    main()

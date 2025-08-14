#!/usr/bin/env python3
"""
Contest Tracker Tool

Tracks competitive programming contest participation, results, and progress.
Provides analytics and recommendations for improvement.

Usage:
    python contest-tracker.py --record [contest_data]
    python contest-tracker.py --stats
    python contest-tracker.py --report
"""

import json
import sqlite3
import argparse
from datetime import datetime, timedelta
from pathlib import Path
from collections import defaultdict
import matplotlib.pyplot as plt
import pandas as pd

class ContestTracker:
    """Tracks contest participation and generates analytics."""
    
    def __init__(self, data_dir=None):
        """Initialize contest tracker with database."""
        if data_dir is None:
            self.data_dir = Path(__file__).parent / "data"
        else:
            self.data_dir = Path(data_dir)
        
        self.data_dir.mkdir(exist_ok=True)
        self.db_path = self.data_dir / "contest_tracker.db"
        self._init_database()
    
    def _init_database(self):
        """Initialize SQLite database for contest tracking."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Create contests table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS contests (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                platform TEXT NOT NULL,
                contest_type TEXT NOT NULL,
                contest_id TEXT NOT NULL,
                date TEXT NOT NULL,
                duration INTEGER,
                total_problems INTEGER,
                solved_problems INTEGER,
                rank INTEGER,
                rating_change INTEGER,
                notes TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        # Create problems table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS problems (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                contest_id INTEGER,
                problem_id TEXT NOT NULL,
                problem_title TEXT,
                difficulty TEXT,
                solved BOOLEAN,
                solve_time INTEGER,
                attempts INTEGER,
                tags TEXT,
                notes TEXT,
                FOREIGN KEY (contest_id) REFERENCES contests (id)
            )
        ''')
        
        # Create learning_progress table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS learning_progress (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                topic TEXT NOT NULL,
                difficulty_level INTEGER,
                problems_solved INTEGER,
                success_rate REAL,
                average_time REAL,
                last_practiced TEXT,
                notes TEXT
            )
        ''')
        
        conn.commit()
        conn.close()
    
    def record_contest(self, contest_data):
        """Record contest participation data."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Insert contest data
        cursor.execute('''
            INSERT INTO contests (
                platform, contest_type, contest_id, date, duration,
                total_problems, solved_problems, rank, rating_change, notes
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            contest_data['platform'],
            contest_data['contest_type'],
            contest_data['contest_id'],
            contest_data['date'],
            contest_data.get('duration'),
            contest_data['total_problems'],
            contest_data['solved_problems'],
            contest_data.get('rank'),
            contest_data.get('rating_change'),
            contest_data.get('notes', '')
        ))
        
        contest_db_id = cursor.lastrowid
        
        # Insert problem data
        if 'problems' in contest_data:
            for problem in contest_data['problems']:
                cursor.execute('''
                    INSERT INTO problems (
                        contest_id, problem_id, problem_title, difficulty,
                        solved, solve_time, attempts, tags, notes
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                ''', (
                    contest_db_id,
                    problem['problem_id'],
                    problem.get('title'),
                    problem.get('difficulty'),
                    problem['solved'],
                    problem.get('solve_time'),
                    problem.get('attempts', 1),
                    ','.join(problem.get('tags', [])),
                    problem.get('notes', '')
                ))
        
        conn.commit()
        conn.close()
        
        print(f"Recorded contest: {contest_data['contest_id']}")
    
    def get_contest_stats(self):
        """Get overall contest statistics."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Overall stats
        cursor.execute('''
            SELECT 
                COUNT(*) as total_contests,
                AVG(solved_problems * 1.0 / total_problems) as avg_solve_rate,
                SUM(solved_problems) as total_solved,
                SUM(total_problems) as total_attempted
            FROM contests
        ''')
        overall_stats = cursor.fetchone()
        
        # Platform breakdown
        cursor.execute('''
            SELECT 
                platform,
                COUNT(*) as contests,
                AVG(solved_problems * 1.0 / total_problems) as avg_solve_rate
            FROM contests
            GROUP BY platform
        ''')
        platform_stats = cursor.fetchall()
        
        # Recent performance (last 30 days)
        thirty_days_ago = (datetime.now() - timedelta(days=30)).strftime('%Y-%m-%d')
        cursor.execute('''
            SELECT 
                COUNT(*) as recent_contests,
                AVG(solved_problems * 1.0 / total_problems) as recent_solve_rate
            FROM contests
            WHERE date >= ?
        ''', (thirty_days_ago,))
        recent_stats = cursor.fetchone()
        
        conn.close()
        
        return {
            'overall': overall_stats,
            'platform': platform_stats,
            'recent': recent_stats
        }
    
    def get_problem_analysis(self):
        """Analyze problem-solving patterns."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Difficulty analysis
        cursor.execute('''
            SELECT 
                difficulty,
                COUNT(*) as total,
                SUM(CASE WHEN solved THEN 1 ELSE 0 END) as solved,
                AVG(solve_time) as avg_time
            FROM problems
            WHERE difficulty IS NOT NULL
            GROUP BY difficulty
        ''')
        difficulty_analysis = cursor.fetchall()
        
        # Topic analysis (from tags)
        cursor.execute('''
            SELECT tags, solved FROM problems WHERE tags IS NOT NULL AND tags != ''
        ''')
        problem_tags = cursor.fetchall()
        
        # Process tags
        topic_stats = defaultdict(lambda: {'total': 0, 'solved': 0})
        for tags_str, solved in problem_tags:
            if tags_str:
                for tag in tags_str.split(','):
                    tag = tag.strip()
                    if tag:
                        topic_stats[tag]['total'] += 1
                        if solved:
                            topic_stats[tag]['solved'] += 1
        
        conn.close()
        
        return {
            'difficulty': difficulty_analysis,
            'topics': dict(topic_stats)
        }
    
    def generate_progress_report(self):
        """Generate comprehensive progress report."""
        stats = self.get_contest_stats()
        problem_analysis = self.get_problem_analysis()
        
        report = []
        report.append("=" * 60)
        report.append("COMPETITIVE PROGRAMMING PROGRESS REPORT")
        report.append("=" * 60)
        report.append("")
        
        # Overall Performance
        overall = stats['overall']
        report.append("📊 OVERALL PERFORMANCE")
        report.append("-" * 30)
        report.append(f"Total Contests: {overall[0]}")
        report.append(f"Average Solve Rate: {overall[1]:.1%}")
        report.append(f"Problems Solved: {overall[2]}/{overall[3]}")
        report.append("")
        
        # Platform Performance
        if stats['platform']:
            report.append("🏆 PLATFORM BREAKDOWN")
            report.append("-" * 30)
            for platform, contests, solve_rate in stats['platform']:
                report.append(f"{platform.title()}: {contests} contests, {solve_rate:.1%} solve rate")
            report.append("")
        
        # Recent Performance
        recent = stats['recent']
        if recent[0] > 0:
            report.append("📈 RECENT PERFORMANCE (Last 30 days)")
            report.append("-" * 30)
            report.append(f"Recent Contests: {recent[0]}")
            report.append(f"Recent Solve Rate: {recent[1]:.1%}")
            report.append("")
        
        # Difficulty Analysis
        if problem_analysis['difficulty']:
            report.append("🎯 DIFFICULTY ANALYSIS")
            report.append("-" * 30)
            for difficulty, total, solved, avg_time in problem_analysis['difficulty']:
                solve_rate = solved / total if total > 0 else 0
                time_str = f", {avg_time:.0f}min avg" if avg_time else ""
                report.append(f"{difficulty}: {solved}/{total} ({solve_rate:.1%}){time_str}")
            report.append("")
        
        # Topic Strengths/Weaknesses
        topics = problem_analysis['topics']
        if topics:
            report.append("🧠 TOPIC ANALYSIS")
            report.append("-" * 30)
            
            # Sort topics by solve rate
            topic_rates = []
            for topic, data in topics.items():
                if data['total'] >= 3:  # Only include topics with sufficient data
                    rate = data['solved'] / data['total']
                    topic_rates.append((topic, rate, data['total']))
            
            topic_rates.sort(key=lambda x: x[1], reverse=True)
            
            report.append("Strongest Topics:")
            for topic, rate, total in topic_rates[:5]:
                report.append(f"  • {topic}: {rate:.1%} ({total} problems)")
            
            report.append("")
            report.append("Areas for Improvement:")
            for topic, rate, total in topic_rates[-5:]:
                report.append(f"  • {topic}: {rate:.1%} ({total} problems)")
        
        # Recommendations
        report.append("")
        report.append("💡 RECOMMENDATIONS")
        report.append("-" * 30)
        report.append(self._generate_recommendations(stats, problem_analysis))
        
        return "\n".join(report)
    
    def _generate_recommendations(self, stats, problem_analysis):
        """Generate personalized recommendations."""
        recommendations = []
        
        overall_rate = stats['overall'][1] if stats['overall'][1] else 0
        
        if overall_rate < 0.3:
            recommendations.append("• Focus on easier problems to build confidence")
            recommendations.append("• Practice basic algorithms and data structures")
        elif overall_rate < 0.5:
            recommendations.append("• Work on medium difficulty problems")
            recommendations.append("• Study common contest patterns")
        else:
            recommendations.append("• Challenge yourself with harder problems")
            recommendations.append("• Focus on advanced algorithms and techniques")
        
        # Topic-specific recommendations
        topics = problem_analysis['topics']
        if topics:
            weak_topics = []
            for topic, data in topics.items():
                if data['total'] >= 3:
                    rate = data['solved'] / data['total']
                    if rate < 0.4:
                        weak_topics.append(topic)
            
            if weak_topics:
                recommendations.append(f"• Practice weak topics: {', '.join(weak_topics[:3])}")
        
        if not recommendations:
            recommendations.append("• Keep practicing consistently!")
            recommendations.append("• Try contests on different platforms")
        
        return "\n".join(recommendations)
    
    def export_data(self, format='json'):
        """Export contest data for analysis."""
        conn = sqlite3.connect(self.db_path)
        
        if format == 'json':
            # Export to JSON
            contests_df = pd.read_sql_query("SELECT * FROM contests", conn)
            problems_df = pd.read_sql_query("SELECT * FROM problems", conn)
            
            export_data = {
                'contests': contests_df.to_dict('records'),
                'problems': problems_df.to_dict('records'),
                'export_date': datetime.now().isoformat()
            }
            
            export_path = self.data_dir / f"contest_data_{datetime.now().strftime('%Y%m%d')}.json"
            with open(export_path, 'w') as f:
                json.dump(export_data, f, indent=2)
            
            print(f"Data exported to {export_path}")
        
        elif format == 'csv':
            # Export to CSV
            contests_df = pd.read_sql_query("SELECT * FROM contests", conn)
            problems_df = pd.read_sql_query("SELECT * FROM problems", conn)
            
            date_str = datetime.now().strftime('%Y%m%d')
            contests_df.to_csv(self.data_dir / f"contests_{date_str}.csv", index=False)
            problems_df.to_csv(self.data_dir / f"problems_{date_str}.csv", index=False)
            
            print(f"Data exported to CSV files in {self.data_dir}")
        
        conn.close()
    
    def plot_progress(self):
        """Generate progress visualization."""
        conn = sqlite3.connect(self.db_path)
        
        # Get contest data over time
        df = pd.read_sql_query('''
            SELECT 
                date,
                solved_problems * 1.0 / total_problems as solve_rate,
                solved_problems,
                total_problems
            FROM contests
            ORDER BY date
        ''', conn)
        
        if len(df) == 0:
            print("No data available for plotting")
            return
        
        df['date'] = pd.to_datetime(df['date'])
        
        # Create subplots
        fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 10))
        fig.suptitle('Competitive Programming Progress', fontsize=16)
        
        # Solve rate over time
        ax1.plot(df['date'], df['solve_rate'])
        ax1.set_title('Solve Rate Over Time')
        ax1.set_ylabel('Solve Rate')
        ax1.tick_params(axis='x', rotation=45)
        
        # Problems solved per contest
        ax2.bar(range(len(df)), df['solved_problems'])
        ax2.set_title('Problems Solved Per Contest')
        ax2.set_ylabel('Problems Solved')
        ax2.set_xlabel('Contest Number')
        
        # Difficulty distribution
        difficulty_df = pd.read_sql_query('''
            SELECT difficulty, COUNT(*) as count
            FROM problems
            WHERE difficulty IS NOT NULL
            GROUP BY difficulty
        ''', conn)
        
        if len(difficulty_df) > 0:
            ax3.pie(difficulty_df['count'], labels=difficulty_df['difficulty'], autopct='%1.1f%%')
            ax3.set_title('Problems by Difficulty')
        
        # Success rate by difficulty
        success_df = pd.read_sql_query('''
            SELECT 
                difficulty,
                AVG(CASE WHEN solved THEN 1.0 ELSE 0.0 END) as success_rate
            FROM problems
            WHERE difficulty IS NOT NULL
            GROUP BY difficulty
        ''', conn)
        
        if len(success_df) > 0:
            ax4.bar(success_df['difficulty'], success_df['success_rate'])
            ax4.set_title('Success Rate by Difficulty')
            ax4.set_ylabel('Success Rate')
            ax4.tick_params(axis='x', rotation=45)
        
        plt.tight_layout()
        plot_path = self.data_dir / f"progress_{datetime.now().strftime('%Y%m%d')}.png"
        plt.savefig(plot_path, dpi=300, bbox_inches='tight')
        print(f"Progress chart saved to {plot_path}")
        
        conn.close()

def main():
    """Main function for command-line usage."""
    parser = argparse.ArgumentParser(description="Track competitive programming contest progress")
    parser.add_argument("--record", metavar="JSON_FILE", 
                       help="Record contest data from JSON file")
    parser.add_argument("--stats", action="store_true",
                       help="Show contest statistics")
    parser.add_argument("--report", action="store_true",
                       help="Generate progress report")
    parser.add_argument("--export", choices=["json", "csv"],
                       help="Export data in specified format")
    parser.add_argument("--plot", action="store_true",
                       help="Generate progress visualization")
    parser.add_argument("--data-dir",
                       help="Data directory path (default: auto-detect)")
    
    args = parser.parse_args()
    
    tracker = ContestTracker(args.data_dir)
    
    if args.record:
        with open(args.record, 'r') as f:
            contest_data = json.load(f)
        tracker.record_contest(contest_data)
    
    if args.stats:
        stats = tracker.get_contest_stats()
        print("Contest Statistics:")
        print(f"Total contests: {stats['overall'][0]}")
        print(f"Average solve rate: {stats['overall'][1]:.1%}")
    
    if args.report:
        report = tracker.generate_progress_report()
        print(report)
    
    if args.export:
        tracker.export_data(args.export)
    
    if args.plot:
        tracker.plot_progress()

if __name__ == "__main__":
    main()

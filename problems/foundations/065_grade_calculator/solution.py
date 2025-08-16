"""
Solution for Grade Calculator
Problem ID: F065
"""

def calculate_grade(grades):
    """
    Calculates comprehensive grade statistics.
    Args:
        grades (list): list of numeric grades
    Returns:
        dict: dictionary with grade statistics
    """
    if not grades:
        return {
            'average': 0,
            'letter_grade': 'F',
            'highest': 0,
            'lowest': 0,
            'passing': False
        }
    
    # Calculate statistics
    average = sum(grades) / len(grades)
    highest = max(grades)
    lowest = min(grades)
    passing = average >= 60
    
    # Determine letter grade
    if average >= 90:
        letter_grade = 'A'
    elif average >= 80:
        letter_grade = 'B'
    elif average >= 70:
        letter_grade = 'C'
    elif average >= 60:
        letter_grade = 'D'
    else:
        letter_grade = 'F'
    
    return {
        'average': round(average, 1),
        'letter_grade': letter_grade,
        'highest': highest,
        'lowest': lowest,
        'passing': passing
    }

def main():
    """
    Función principal para 065_grade_calculator
    """
    # Ejemplos de uso
    test_cases = [
        [85, 92, 78, 90, 88],
        [95, 87, 92, 96, 89],
        [65, 70, 68, 72],
        [45, 50, 55, 48],
        []
    ]
    
    for grades in test_cases:
        result = calculate_grade(grades)
        print(f"Grades: {grades}")
        print(f"Results: {result}\n")
    
    return calculate_grade([85, 92, 78, 90, 88])

if __name__ == "__main__":
    result = main()
    print(f"Resultado: {result}")

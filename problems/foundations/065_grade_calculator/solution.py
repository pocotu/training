"""
Solution for Grade Calculator
Problem ID: F065
"""

def calculate_grade(grades):
    # TODO: Implement your solution here
    pass

def main():
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

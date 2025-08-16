"""
Solution for Object-Oriented Programming Basics
Problem ID: F074
"""

class Student:
    """
    A simple Student class to demonstrate OOP concepts.
    """
    
    def __init__(self, name, age):
        """
        Initialize a new student.
        Args:
            name (str): student's name
            age (int): student's age
        """
        self.name = name
        self.age = age
        self.grades = []
    
    def add_grade(self, grade):
        """
        Add a grade to the student's record.
        Args:
            grade (float): grade to add
        """
        if 0 <= grade <= 100:
            self.grades.append(grade)
        else:
            print("Grade must be between 0 and 100")
    
    def get_average(self):
        """
        Calculate the average grade.
        Returns:
            float: average grade or 0 if no grades
        """
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)
    
    def get_info(self):
        """
        Get student information.
        Returns:
            str: formatted student information
        """
        average = self.get_average()
        return f"{self.name} ({self.age} años) - Promedio: {average:.1f}"

def main():
    """
    Función principal para 074_oop_basics
    """
    # Ejemplo de uso
    print("OOP Basics Example:")
    
    # Create student
    student = Student("Alice", 20)
    print(f"Created student: {student.name}, age {student.age}")
    
    # Add grades
    student.add_grade(85)
    student.add_grade(92)
    student.add_grade(78)
    print(f"Added grades: {student.grades}")
    
    # Get average
    avg = student.get_average()
    print(f"Average grade: {avg:.1f}")
    
    # Get full info
    info = student.get_info()
    print(f"Student info: {info}")
    
    return student

if __name__ == "__main__":
    result = main()
    print(f"Resultado: {result}")

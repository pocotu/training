"""
Solution for Object-Oriented Programming Basics
Problem ID: F074
"""

class Student:
    def __init__(self, name, age):
        # TODO: Implement your solution here
        pass
    
    def add_grade(self, grade):
        # TODO: Implement your solution here
        pass
    
    def get_average(self):
        # TODO: Implement your solution here
        pass
    
    def get_info(self):
        # TODO: Implement your solution here
        pass

def main():
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

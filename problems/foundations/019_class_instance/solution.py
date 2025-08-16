"""
Solution for Class Instance
Problem ID: F019
"""

class Person:
    """
    A simple Person class.
    """
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        return f"Hi, I'm {self.name} and I'm {self.age} years old."

def main():
    """
    Función principal para 019_class_instance
    """
    # Ejemplo de uso
    person = Person("Alice", 25)
    result = person.introduce()
    print(f"Persona creada: {result}")
    return result

if __name__ == "__main__":
    result = main()
    print(f"Resultado: {result}")

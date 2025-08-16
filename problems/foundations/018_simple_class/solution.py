"""
Solution for Simple Class
Problem ID: F018
"""

class Dog:
    """
    A simple Dog class.
    """
    def __init__(self, name):
        self.name = name
    
    def bark(self):
        return f"{self.name} says woof!"

def main():
    """
    Función principal para 018_simple_class
    """
    # Ejemplo de uso
    dog = Dog("Buddy")
    result = dog.bark()
    print(f"Perro creado: {result}")
    return result

if __name__ == "__main__":
    result = main()
    print(f"Resultado: {result}")

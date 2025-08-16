"""
Solution for Class Inheritance
Problem ID: F047
"""

class Animal:
    """
    Clase base Animal
    """
    def make_sound(self):
        """
        Método para hacer sonido
        Returns:
            str: sonido genérico del animal
        """
        return "Some generic animal sound"

class Dog(Animal):
    """
    Clase Dog que hereda de Animal
    """
    def make_sound(self):
        """
        Método sobrescrito para hacer sonido de perro
        Returns:
            str: sonido del perro
        """
        return "Woof!"

def main():
    """
    Función principal para 047_class_inheritance
    """
    # Ejemplos de uso
    animal = Animal()
    print(f"Animal sound: {animal.make_sound()}")
    
    dog = Dog()
    print(f"Dog sound: {dog.make_sound()}")
    print(f"Is dog an Animal? {isinstance(dog, Animal)}")
    
    return dog.make_sound()

if __name__ == "__main__":
    result = main()
    print(f"Resultado: {result}")

"""
Solution for Class Inheritance
Problem ID: F047
"""

class Animal:
    def make_sound(self):
        # TODO: Implement your solution here
        pass

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

def main():
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

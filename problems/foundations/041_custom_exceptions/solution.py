"""
Solution for Custom Exceptions and Error Handling
Problem ID: F041
"""

class InvalidAgeError(ValueError):
    def __init__(self, age):
        self.age = age
        super().__init__(f"Invalid age: {age}. Age must be between 0 and 150.")
        # TODO: Implement your solution here (if additional logic needed)
        pass

class InsufficientFundsError(Exception):
    def __init__(self, balance, amount):
        super().__init__(f"Insufficient funds: balance is {balance}, but {amount} required.")
        self.balance = balance
        self.amount = amount

def validate_person(name, age, balance):
    if age < 0 or age > 150:
        raise InvalidAgeError(age)
    
    if balance < 0:
        raise InsufficientFundsError(balance, 0)
    
    return True

def main():
    try:
        # Ejemplo de uso
        result = validate_person("Alice", 30, 100.0)
        print(f"Validación exitosa: {result}")
        
        # Test con edad inválida
        validate_person("Bob", -5, 100.0)
    except InvalidAgeError as e:
        print(f"Error de edad: {e}")
    except InsufficientFundsError as e:
        print(f"Error de fondos: {e}")
    
    return True

if __name__ == "__main__":
    result = main()
    print(f"Resultado: {result}")

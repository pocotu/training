"""
Solution for Custom Exceptions and Error Handling
Problem ID: F041
"""

class InvalidAgeError(ValueError):
    """
    Excepción personalizada para edad inválida
    """
    def __init__(self, age):
        """
        Constructor para InvalidAgeError
        Args:
            age (int): edad inválida
        """
        super().__init__(f"Invalid age: {age}. Age must be between 0 and 150.")
        self.age = age

class InsufficientFundsError(Exception):
    """
    Excepción personalizada para fondos insuficientes
    """
    def __init__(self, balance, amount):
        """
        Constructor para InsufficientFundsError
        Args:
            balance (float): balance actual
            amount (float): cantidad requerida
        """
        super().__init__(f"Insufficient funds: balance is {balance}, but {amount} required.")
        self.balance = balance
        self.amount = amount

def validate_person(name, age, balance):
    """
    Valida datos de una persona
    Args:
        name (str): nombre de la persona
        age (int): edad de la persona
        balance (float): balance de la cuenta
    Raises:
        InvalidAgeError: si edad < 0 o > 150
        InsufficientFundsError: si balance < 0
    Returns:
        bool: True si todos los datos son válidos
    """
    if age < 0 or age > 150:
        raise InvalidAgeError(age)
    
    if balance < 0:
        raise InsufficientFundsError(balance, 0)
    
    return True

def main():
    """
    Función principal para 041_custom_exceptions
    """
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

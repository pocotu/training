"""
Solution for Password Validator
Problem ID: F059
"""

def is_valid_password(password):
    # TODO: Implement your solution here
    pass

def main():
    # Ejemplos de uso
    test_passwords = [
        "password",
        "Password",
        "Password1",
        "Password1!",
        "Pass1!",
        "VeryStrongPassword123!",
        "weak",
        "NOLOWERCASE123!",
        "nouppercase123!"
    ]
    
    for pwd in test_passwords:
        result = is_valid_password(pwd)
        print(f"'{pwd}' es válida: {result}")
    
    return is_valid_password("Password1!")

if __name__ == "__main__":
    result = main()
    print(f"Resultado: {result}")

"""
Solution for Dictionary get() method
Problem ID: F030
"""

def get_value_safely(dictionary, key, default="Not Found"):
    # TODO: Implement your solution here
    pass

def main():
    # Ejemplo de uso
    test_dict = {'name': 'Alice', 'age': 30}
    result = get_value_safely(test_dict, 'city', 'Unknown')
    print(f"Valor para 'city' con default: {result}")
    return result

if __name__ == "__main__":
    result = main()
    print(f"Resultado: {result}")

"""
Solution for Exception Handling Basics
Problem ID: F072
"""

def safe_division(a, b):
    # TODO: Implement your solution here
    pass

def safe_list_access(lst, index):
    # TODO: Implement your solution here
    pass

def safe_int_conversion(value):
    # TODO: Implement your solution here
    pass

def main():
    # Ejemplos de uso
    print("Exception Handling Examples:")
    
    # Division tests
    print(f"10 / 2 = {safe_division(10, 2)}")
    print(f"10 / 0 = {safe_division(10, 0)}")
    
    # List access tests
    lst = [1, 2, 3, 4, 5]
    print(f"List[2] = {safe_list_access(lst, 2)}")
    print(f"List[10] = {safe_list_access(lst, 10)}")
    
    # Int conversion tests
    print(f"Convert '123': {safe_int_conversion('123')}")
    print(f"Convert 'abc': {safe_int_conversion('abc')}")
    
    return safe_division(10, 2)

if __name__ == "__main__":
    result = main()
    print(f"Resultado: {result}")

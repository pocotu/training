"""
Solution for Decorators Fundamentals
Problem ID: F078
"""

import time
import functools

def timing_decorator(func):
    # TODO: Implement your solution here
    pass

def validate_types(*expected_types):
    # TODO: Implement your solution here
    pass

def cache_result(func):
    # TODO: Implement your solution here
    pass

@timing_decorator
def slow_function():
    # TODO: Implement your solution here
    pass

@validate_types(int, int)
def add_numbers(a, b):
    # TODO: Implement your solution here
    pass

@cache_result
def expensive_calculation(n):
    # TODO: Implement your solution here
    pass

def main():
    print("Decorators Examples:")
    
    # Timing decorator
    print("\n1. Timing decorator:")
    result = slow_function()
    print(f"Result: {result}")
    
    # Type validation decorator
    print("\n2. Type validation decorator:")
    try:
        result = add_numbers(5, 3)
        print(f"5 + 3 = {result}")
        
        # This should raise TypeError
        result = add_numbers("5", 3)
    except TypeError as e:
        print(f"Type error: {e}")
    
    # Caching decorator
    print("\n3. Caching decorator:")
    print(f"First call: {expensive_calculation(5)}")
    print(f"Second call: {expensive_calculation(5)}")  # Should use cache
    print(f"Third call: {expensive_calculation(10)}")  # New calculation
    
    return True

if __name__ == "__main__":
    result = main()
    print(f"Resultado: {result}")

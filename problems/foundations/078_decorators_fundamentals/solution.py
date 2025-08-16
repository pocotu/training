"""
Solution for Decorators Fundamentals
Problem ID: F078
"""

import time
import functools

def timing_decorator(func):
    """
    Decorator that measures function execution time.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function '{func.__name__}' took {end_time - start_time:.4f} seconds")
        return result
    return wrapper

def validate_types(*expected_types):
    """
    Decorator that validates argument types.
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for i, (arg, expected_type) in enumerate(zip(args, expected_types)):
                if not isinstance(arg, expected_type):
                    raise TypeError(f"Argument {i} must be of type {expected_type.__name__}")
            return func(*args, **kwargs)
        return wrapper
    return decorator

def cache_result(func):
    """
    Simple caching decorator.
    """
    cache = {}
    
    @functools.wraps(func)
    def wrapper(*args):
        if args in cache:
            print(f"Cache hit for {args}")
            return cache[args]
        
        result = func(*args)
        cache[args] = result
        print(f"Cache miss for {args}, result cached")
        return result
    
    return wrapper

@timing_decorator
def slow_function():
    """Example function that takes some time."""
    time.sleep(0.1)
    return "Done"

@validate_types(int, int)
def add_numbers(a, b):
    """Add two numbers with type validation."""
    return a + b

@cache_result
def expensive_calculation(n):
    """Example of expensive calculation that benefits from caching."""
    time.sleep(0.01)  # Simulate expensive operation
    return n * n

def main():
    """
    Función principal para 078_decorators_fundamentals
    """
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

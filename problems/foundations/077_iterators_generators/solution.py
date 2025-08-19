"""
Solution for Iterator and Generator Basics
Problem ID: F077
"""

def number_generator(start, end):
    # TODO: Implement your solution here
    pass

def fibonacci_generator(n):
    # TODO: Implement your solution here
    pass

class CountdownIterator:    
    def __init__(self, start):
        # TODO: Implement your solution here
        pass
    
    def __iter__(self):
        # TODO: Implement your solution here
        pass
    
    def __next__(self):
        # TODO: Implement your solution here
        pass

def main():
    print("Iterators and Generators Examples:")
    
    # Number generator
    print("Number generator (1 to 5):")
    for num in number_generator(1, 5):
        print(f"  {num}")
    
    # Fibonacci generator
    print("\nFirst 8 Fibonacci numbers:")
    fib_gen = fibonacci_generator(8)
    fib_numbers = list(fib_gen)
    print(f"  {fib_numbers}")
    
    # Countdown iterator
    print("\nCountdown from 5:")
    countdown = CountdownIterator(5)
    for num in countdown:
        print(f"  {num}")
    
    return list(number_generator(1, 5))

if __name__ == "__main__":
    result = main()
    print(f"Resultado: {result}")

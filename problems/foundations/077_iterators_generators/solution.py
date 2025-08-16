"""
Solution for Iterator and Generator Basics
Problem ID: F077
"""

def number_generator(start, end):
    """
    Generator that yields numbers from start to end.
    Args:
        start (int): starting number
        end (int): ending number
    Yields:
        int: numbers from start to end
    """
    current = start
    while current <= end:
        yield current
        current += 1

def fibonacci_generator(n):
    """
    Generator that yields first n Fibonacci numbers.
    Args:
        n (int): number of Fibonacci numbers to generate
    Yields:
        int: Fibonacci numbers
    """
    a, b = 0, 1
    count = 0
    
    while count < n:
        yield a
        a, b = b, a + b
        count += 1

class CountdownIterator:
    """
    Iterator that counts down from a given number.
    """
    
    def __init__(self, start):
        """
        Initialize countdown iterator.
        Args:
            start (int): starting number
        """
        self.start = start
    
    def __iter__(self):
        """Return iterator object."""
        return self
    
    def __next__(self):
        """Return next value in countdown."""
        if self.start <= 0:
            raise StopIteration
        
        current = self.start
        self.start -= 1
        return current

def main():
    """
    Función principal para 077_iterators_generators
    """
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

"""
Solution for Unit Testing Fundamentals
Problem ID: F081
"""

import unittest

def add(a, b):
    """
    Simple addition function for testing.
    Args:
        a (int): first number
        b (int): second number
    Returns:
        int: sum of a and b
    """
    return a + b

def divide(a, b):
    """
    Division function that handles zero division.
    Args:
        a (float): dividend
        b (float): divisor
    Returns:
        float: result of division
    Raises:
        ValueError: if b is zero
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def is_even(number):
    """
    Check if a number is even.
    Args:
        number (int): number to check
    Returns:
        bool: True if even, False if odd
    """
    return number % 2 == 0

class Calculator:
    """
    Simple calculator class for testing.
    """
    
    def __init__(self):
        """Initialize calculator."""
        self.result = 0
    
    def add(self, value):
        """Add value to result."""
        self.result += value
        return self.result
    
    def subtract(self, value):
        """Subtract value from result."""
        self.result -= value
        return self.result
    
    def multiply(self, value):
        """Multiply result by value."""
        self.result *= value
        return self.result
    
    def reset(self):
        """Reset result to zero."""
        self.result = 0
        return self.result
    
    def get_result(self):
        """Get current result."""
        return self.result

def main():
    """
    Función principal para 081_unit_testing_fundamentals
    """
    # Ejemplos de uso
    print("Unit Testing Fundamentals Examples:")
    
    # Test functions
    print(f"add(2, 3) = {add(2, 3)}")
    print(f"divide(10, 2) = {divide(10, 2)}")
    print(f"is_even(4) = {is_even(4)}")
    print(f"is_even(3) = {is_even(3)}")
    
    # Test calculator class
    calc = Calculator()
    calc.add(10)
    calc.multiply(2)
    print(f"Calculator result: {calc.get_result()}")
    
    return True

if __name__ == "__main__":
    result = main()
    print(f"Resultado: {result}")

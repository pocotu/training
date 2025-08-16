"""
Solution for Simple Calculator
Problem ID: F060
"""

def calculate(num1, num2, operation):
    """
    Performs basic mathematical operations.
    Args:
        num1 (float): first number
        num2 (float): second number
        operation (str): operation to perform (+, -, *, /)
    Returns:
        float or str: result of the operation or "Error" for invalid operations
    """
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 == 0:
            return "Error"
        return num1 / num2
    else:
        return "Error"

def main():
    """
    Función principal para 060_simple_calculator
    """
    # Ejemplos de uso
    test_cases = [
        (10, 5, '+'),
        (10, 5, '-'),
        (10, 5, '*'),
        (10, 5, '/'),
        (7, 3, '+'),
        (15.5, 2.5, '*'),
        (10, 0, '/'),  # División por cero
        (5, 3, '%')    # Operación inválida
    ]
    
    for num1, num2, op in test_cases:
        result = calculate(num1, num2, op)
        print(f"{num1} {op} {num2} = {result}")
    
    return calculate(10, 5, '+')

if __name__ == "__main__":
    result = main()
    print(f"Resultado: {result}")

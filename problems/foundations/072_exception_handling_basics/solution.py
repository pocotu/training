"""
Solution for Exception Handling Basics
Problem ID: F072
"""

def safe_division(a, b):
    """
    Safely divides two numbers, handling division by zero.
    Args:
        a (float): dividend
        b (float): divisor
    Returns:
        float or str: result of division or error message
    """
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: División por cero"
    except TypeError:
        return "Error: Tipos inválidos para división"

def safe_list_access(lst, index):
    """
    Safely accesses list element by index.
    Args:
        lst (list): input list
        index (int): index to access
    Returns:
        any or str: element at index or error message
    """
    try:
        return lst[index]
    except IndexError:
        return "Error: Índice fuera de rango"
    except TypeError:
        return "Error: Tipo de índice inválido"

def safe_int_conversion(value):
    """
    Safely converts value to integer.
    Args:
        value: value to convert
    Returns:
        int or str: converted integer or error message
    """
    try:
        return int(value)
    except ValueError:
        return "Error: No se puede convertir a entero"
    except TypeError:
        return "Error: Tipo inválido para conversión"

def main():
    """
    Función principal para 072_exception_handling_basics
    """
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

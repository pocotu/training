"""
Solution for Nested Loops
Problem ID: F052
"""

def multiplication_table(n):
    # TODO: Implement your solution here
    pass

def main():
    # Ejemplo de uso
    result = multiplication_table(3)
    print(f"Tabla de multiplicación 3x3: {result}")
    
    # Mostrar de forma más legible
    for i, row in enumerate(result, 1):
        print(f"Fila {i}: {row}")
    
    return result

if __name__ == "__main__":
    result = main()
    print(f"Resultado: {result}")

"""
Solution for Lambda Functions
Problem ID: F038
"""

# Crear una función lambda que multiplica por 10
multiplier = lambda x: x * 10

def main():
    """
    Función principal para 038_lambda_functions
    """
    # Ejemplo de uso
    result = multiplier(5)
    print(f"Multiplicando 5 por 10: {result}")
    return result

if __name__ == "__main__":
    result = main()
    print(f"Resultado: {result}")

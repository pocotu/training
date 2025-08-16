"""
Solution for While Loop
Problem ID: F014
"""

def count_down(n):
    """
    Counts down from n to 1 using a while loop.
    """
    result = []
    while n > 0:
        result.append(n)
        n -= 1
    return result

def main():
    """
    Función principal para 014_while_loop
    """
    # Ejemplo de uso
    result = count_down(5)
    print(f"Conteo regresivo desde 5: {result}")
    return result

if __name__ == "__main__":
    result = main()
    print(f"Resultado: {result}")

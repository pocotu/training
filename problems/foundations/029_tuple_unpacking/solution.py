"""
Solution for Tuple Unpacking
Problem ID: F029
"""

def unpack_tuple(tup):
    """
    Unpacks a tuple and returns its elements as separate variables.
    Returns a tuple of the unpacked values.
    """
    if len(tup) >= 3:
        a, b, c = tup[0], tup[1], tup[2]
        return (a, b, c)
    else:
        return tup

def main():
    """
    Función principal para 029_tuple_unpacking
    """
    # Ejemplo de uso
    test_tuple = (1, 2, 3)
    result = unpack_tuple(test_tuple)
    print(f"Tupla desempaquetada {test_tuple}: {result}")
    return result

if __name__ == "__main__":
    result = main()
    print(f"Resultado: {result}")

"""
Solution for Variables and Types
Problem ID: F002
"""

def create_variables():
    """
    Creates and returns a tuple with different variable types:
    1. Integer: 10
    2. Float: 3.14
    3. String: "Python"
    4. Boolean: True
    """
    integer_var = 10
    float_var = 3.14
    string_var = "Python"
    boolean_var = True
    
    return (integer_var, float_var, string_var, boolean_var)

def main():
    """
    Función principal para 002_variables_and_types
    """
    result = create_variables()
    print(f"Variables creadas: {result}")
    return result

if __name__ == "__main__":
    result = main()
    print(f"Resultado: {result}")

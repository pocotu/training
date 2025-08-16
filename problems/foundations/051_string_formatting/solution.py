"""
Solution for String Formatting
Problem ID: F051
"""

def format_person_info(name, age, city):
    """
    Formats person information into a readable string.
    Args:
        name (str): person's name
        age (int): person's age
        city (str): person's city
    Returns:
        str: formatted string
    """
    return f"My name is {name}, I am {age} years old, and I live in {city}."

def main():
    """
    Función principal para 051_string_formatting
    """
    # Ejemplo de uso
    result = format_person_info("Alice", 25, "New York")
    print(f"Formatted info: {result}")
    return result

if __name__ == "__main__":
    result = main()
    print(f"Resultado: {result}")

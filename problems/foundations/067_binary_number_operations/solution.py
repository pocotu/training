"""
Solution for Binary Number Operations
Problem ID: F067
"""

def decimal_to_binary(decimal_num):
    """
    Converts decimal number to binary string.
    Args:
        decimal_num (int): decimal number
    Returns:
        str: binary representation
    """
    if decimal_num == 0:
        return "0"
    
    binary = ""
    num = abs(decimal_num)
    
    while num > 0:
        binary = str(num % 2) + binary
        num //= 2
    
    return binary

def binary_to_decimal(binary_str):
    """
    Converts binary string to decimal number.
    Args:
        binary_str (str): binary string
    Returns:
        int: decimal number
    """
    decimal = 0
    power = 0
    
    # Process from right to left
    for i in range(len(binary_str) - 1, -1, -1):
        if binary_str[i] == '1':
            decimal += 2 ** power
        power += 1
    
    return decimal

def binary_add(bin1, bin2):
    """
    Adds two binary numbers.
    Args:
        bin1 (str): first binary number
        bin2 (str): second binary number
    Returns:
        str: sum in binary
    """
    # Convert to decimal, add, then back to binary
    dec1 = binary_to_decimal(bin1)
    dec2 = binary_to_decimal(bin2)
    sum_decimal = dec1 + dec2
    
    return decimal_to_binary(sum_decimal)

def main():
    """
    Función principal para 067_binary_number_operations
    """
    # Ejemplos de uso
    print("Decimal to Binary:")
    for num in [10, 25, 0, 7]:
        binary = decimal_to_binary(num)
        print(f"{num} -> {binary}")
    
    print("\nBinary to Decimal:")
    for binary in ["1010", "11001", "0", "111"]:
        decimal = binary_to_decimal(binary)
        print(f"{binary} -> {decimal}")
    
    print("\nBinary Addition:")
    test_cases = [("1010", "1100"), ("111", "1"), ("0", "1010")]
    for bin1, bin2 in test_cases:
        result = binary_add(bin1, bin2)
        print(f"{bin1} + {bin2} = {result}")
    
    return decimal_to_binary(10)

if __name__ == "__main__":
    result = main()
    print(f"Resultado: {result}")

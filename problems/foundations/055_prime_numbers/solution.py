"""
Solution for Prime Numbers
Problem ID: F055
"""

def is_prime(n):
    """
    Checks if a number is prime.
    Args:
        n (int): number to check
    Returns:
        bool: True if prime, False otherwise
    """
    if n < 2:
        return False
    
    if n == 2:
        return True
    
    if n % 2 == 0:
        return False
    
    # Check odd divisors up to sqrt(n)
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    
    return True

def main():
    """
    Función principal para 055_prime_numbers
    """
    # Ejemplo de uso
    test_numbers = [2, 3, 4, 5, 17, 25, 29, 100]
    
    for num in test_numbers:
        result = is_prime(num)
        print(f"{num} es primo: {result}")
    
    # Encontrar los primeros 10 primos
    primes = []
    num = 2
    while len(primes) < 10:
        if is_prime(num):
            primes.append(num)
        num += 1
    
    print(f"\nPrimeros 10 números primos: {primes}")
    
    return is_prime(17)

if __name__ == "__main__":
    result = main()
    print(f"Resultado: {result}")

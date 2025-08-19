"""
Solution for Prime Numbers
Problem ID: F055
"""

def is_prime(n):
    # TODO: Implement your solution here
    pass

def main():
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

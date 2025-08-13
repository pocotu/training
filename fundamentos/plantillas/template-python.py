# 🐍 Plantilla Python para Programación Competitiva
# Usa esta plantilla como punto de partida para tus soluciones

# ==========================================
# CONFIGURACIÓN BÁSICA
# ==========================================

import sys
import math
from collections import defaultdict, deque, Counter
from itertools import combinations, permutations

# Optimización de entrada para casos con mucha entrada
input = sys.stdin.readline

# ==========================================
# FUNCIONES ÚTILES
# ==========================================

def debug(*args):
    """Imprime variables para debugging (descomenta cuando necesites)"""
    # print("DEBUG:", *args, file=sys.stderr)
    pass

def read_int():
    """Lee un entero"""
    return int(input())

def read_ints():
    """Lee múltiples enteros en una línea"""
    return list(map(int, input().split()))

def read_string():
    """Lee una cadena (sin salto de línea)"""
    return input().strip()

def read_strings():
    """Lee múltiples cadenas en una línea"""
    return input().strip().split()

# ==========================================
# CONSTANTES ÚTILES
# ==========================================

INF = float('inf')          # Infinito
MOD = 10**9 + 7            # Módulo común en problemas
MAX_N = 10**5              # Tamaño máximo común

# ==========================================
# FUNCIÓN PRINCIPAL
# ==========================================

def solve():
    """
    Aquí escribes tu solución al problema
    """
    # Ejemplo: leer dos números y sumarlos
    # a, b = read_ints()
    # print(a + b)
    
    pass  # Reemplaza esto con tu código

# ==========================================
# EJECUCIÓN PRINCIPAL
# ==========================================

def main():
    # Si hay múltiples casos de prueba, descomenta estas líneas:
    # t = read_int()
    # for _ in range(t):
    #     solve()
    
    # Si hay un solo caso, usa esto:
    solve()

if __name__ == "__main__":
    main()

# ==========================================
# NOTAS Y CONSEJOS
# ==========================================

"""
📝 CÓMO USAR ESTA PLANTILLA:

1. Copia este archivo para cada problema nuevo
2. Escribe tu lógica en la función solve()
3. Usa las funciones de lectura (read_int, read_ints, etc.)
4. Prueba con casos de ejemplo antes de enviar

⚡ TRUCOS PARA PYTHON EN COMPETENCIAS:

- Usa 'input = sys.stdin.readline' para entrada rápida
- Prefiere listas en lugar de append() repetidos
- Usa 'print(*lista)' para imprimir lista separada por espacios
- Usa 'sys.exit()' para terminar programa inmediatamente

🐛 DEBUGGING:
- Usa la función debug() para imprimir variables
- Comenta/descomenta según necesites
- También puedes usar: print("DEBUG:", variable, file=sys.stderr)

📊 COMPLEJIDADES TÍPICAS:
- O(n): hasta 10^6 elementos
- O(n log n): hasta 10^5 elementos  
- O(n²): hasta 10^3 elementos
"""

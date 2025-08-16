"""
Solution for Deque and Advanced Collections
Problem ID: F049
"""

from collections import deque, Counter
from typing import List, Any

def sliding_window_max(arr: List[int], window_size: int) -> List[int]:
    """
    Encuentra el máximo en cada ventana deslizante usando deque
    Args:
        arr: lista de números
        window_size: tamaño de la ventana
    Returns:
        lista con el máximo de cada ventana
    """
    if not arr or window_size <= 0 or window_size > len(arr):
        return []
    
    # Deque para almacenar índices
    dq = deque()
    result = []
    
    for i in range(len(arr)):
        # Remover elementos fuera de la ventana actual
        while dq and dq[0] <= i - window_size:
            dq.popleft()
        
        # Remover elementos menores que el actual
        while dq and arr[dq[-1]] <= arr[i]:
            dq.pop()
        
        dq.append(i)
        
        # El frente del deque tiene el índice del máximo actual
        if i >= window_size - 1:
            result.append(arr[dq[0]])
    
    return result

def palindrome_checker_deque(text: str) -> bool:
    """
    Verifica si un texto es palíndromo usando deque
    Args:
        text: texto a verificar
    Returns:
        True si es palíndromo, False caso contrario
    """
    # Limpiar texto: solo letras y números, convertir a minúsculas
    clean_text = ''.join(char.lower() for char in text if char.isalnum())
    
    dq = deque(clean_text)
    
    while len(dq) > 1:
        if dq.popleft() != dq.pop():
            return False
    
    return True

def counter_analysis(data: List[Any]) -> dict:
    """
    Analiza la frecuencia de elementos usando Counter
    Args:
        data: lista de elementos
    Returns:
        diccionario con análisis de frecuencia
    """
    counter = Counter(data)
    
    if not counter:
        return {
            "total_elements": 0,
            "unique_elements": 0,
            "most_common": [],
            "frequency_distribution": {}
        }
    
    return {
        "total_elements": sum(counter.values()),
        "unique_elements": len(counter),
        "most_common": counter.most_common(3),
        "frequency_distribution": dict(counter)
    }

def main():
    """
    Función principal para 049_deque_advanced_collections
    """
    # Ejemplo sliding window max
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    window_max = sliding_window_max(arr, 3)
    print(f"Sliding window max: {window_max}")
    
    # Ejemplo palindrome checker
    text = "A man a plan a canal Panama"
    is_palindrome = palindrome_checker_deque(text)
    print(f"'{text}' es palíndromo: {is_palindrome}")
    
    # Ejemplo counter analysis
    data = ['apple', 'banana', 'apple', 'cherry', 'banana', 'apple']
    analysis = counter_analysis(data)
    print(f"Análisis de frecuencia: {analysis}")
    
    return analysis

if __name__ == "__main__":
    result = main()
    print(f"Resultado: {result}")

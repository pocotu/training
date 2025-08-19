"""
Solution for Graph Theory Basics
Problem ID: F050
"""

from collections import defaultdict, deque
from typing import Dict, List, Set

def create_graph(edges: List[tuple]) -> Dict[int, List[int]]:
    # TODO: Implement your solution here
    pass

def bfs_traversal(graph: Dict[int, List[int]], start_node: int) -> List[int]:
    # TODO: Implement your solution here
    pass

def find_connected_components(graph: Dict[int, List[int]]) -> List[List[int]]:
    # TODO: Implement your solution here
    pass

def main():
    # Ejemplo de uso
    edges = [(1, 2), (2, 3), (4, 5), (1, 3)]
    
    # Crear grafo
    graph = create_graph(edges)
    print(f"Grafo: {graph}")
    
    # BFS traversal
    bfs_result = bfs_traversal(graph, 1)
    print(f"BFS desde nodo 1: {bfs_result}")
    
    # Encontrar componentes conectados
    components = find_connected_components(graph)
    print(f"Componentes conectados: {components}")
    
    return components

if __name__ == "__main__":
    result = main()
    print(f"Resultado: {result}")

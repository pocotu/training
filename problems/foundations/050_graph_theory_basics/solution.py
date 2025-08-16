"""
Solution for Graph Theory Basics
Problem ID: F050
"""

from collections import defaultdict, deque
from typing import Dict, List, Set

def create_graph(edges: List[tuple]) -> Dict[int, List[int]]:
    """
    Crea un grafo a partir de una lista de aristas
    Args:
        edges: lista de tuplas (nodo1, nodo2)
    Returns:
        diccionario representando grafo como lista de adyacencia
    """
    graph = defaultdict(list)
    
    for node1, node2 in edges:
        graph[node1].append(node2)
        graph[node2].append(node1)  # Grafo no dirigido
    
    return dict(graph)

def bfs_traversal(graph: Dict[int, List[int]], start_node: int) -> List[int]:
    """
    Realiza recorrido BFS (Breadth-First Search) desde un nodo inicial
    Args:
        graph: grafo como diccionario de listas de adyacencia
        start_node: nodo inicial
    Returns:
        lista de nodos en orden de recorrido BFS
    """
    if start_node not in graph:
        return []
    
    visited = set()
    queue = deque([start_node])
    result = []
    
    while queue:
        node = queue.popleft()
        
        if node not in visited:
            visited.add(node)
            result.append(node)
            
            # Agregar vecinos no visitados a la cola
            for neighbor in sorted(graph.get(node, [])):
                if neighbor not in visited:
                    queue.append(neighbor)
    
    return result

def find_connected_components(graph: Dict[int, List[int]]) -> List[List[int]]:
    """
    Encuentra todos los componentes conectados en el grafo
    Args:
        graph: grafo como diccionario de listas de adyacencia
    Returns:
        lista de componentes conectados (cada componente es una lista de nodos)
    """
    visited = set()
    components = []
    
    # Obtener todos los nodos del grafo
    all_nodes = set(graph.keys())
    for neighbors in graph.values():
        all_nodes.update(neighbors)
    
    for node in all_nodes:
        if node not in visited:
            # BFS para encontrar componente conectado
            component = []
            queue = deque([node])
            
            while queue:
                current = queue.popleft()
                
                if current not in visited:
                    visited.add(current)
                    component.append(current)
                    
                    # Agregar vecinos no visitados
                    for neighbor in graph.get(current, []):
                        if neighbor not in visited:
                            queue.append(neighbor)
            
            if component:
                components.append(sorted(component))
    
    return components

def main():
    """
    Función principal para 050_graph_theory_basics
    """
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

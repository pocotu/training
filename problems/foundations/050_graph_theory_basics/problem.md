# [F050] Graph Theory Basics

## Problema

Implementa tres funciones para trabajar con grafos básicos:

1. `create_graph(edges)` - crea grafo usando lista de adyacencia
2. `bfs_traversal(graph, start)` - recorrido BFS desde nodo inicial
3. `find_connected_components(graph)` - encuentra componentes conectados

## Ejemplos

### Función create_graph:
```python
edges = [
    ("A", "B"), ("A", "C"), ("B", "D"), 
    ("C", "D"), ("E", "F")
]
graph = create_graph(edges)
print(graph)
# {
#   "A": ["B", "C"], "B": ["A", "D"], "C": ["A", "D"],
#   "D": ["B", "C"], "E": ["F"], "F": ["E"]
# }
```

### Función bfs_traversal:
```python
path = bfs_traversal(graph, "A")
print(path)  # ["A", "B", "C", "D"] (orden BFS)
```

### Función find_connected_components:
```python
components = find_connected_components(graph)
print(components)
# [
#   ["A", "B", "C", "D"],  # Componente 1
#   ["E", "F"]             # Componente 2
# ]
```

## Restricciones
- create_graph debe crear grafo no dirigido (bidireccional)
- bfs_traversal debe usar queue (collections.deque) 
- find_connected_components debe retornar lista de listas
- Manejar grafos desconectados correctamente
- Usar conjunto (set) para evitar revisitar nodos

## Conceptos a Practicar
- Representación de grafos con lista de adyacencia
- Algoritmo BFS (Breadth-First Search)
- Detección de componentes conectados
- Estructuras de datos para grafos

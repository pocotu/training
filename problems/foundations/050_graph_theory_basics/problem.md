# [F050] Graph Theory Basics

## Problema

Implementa una función básica para trabajar con grafos usando diccionarios.

Escribe una función llamada `create_graph` que reciba una lista de aristas (edges) representadas como tuplas de dos nodos, y devuelva un grafo representado como un diccionario donde cada clave es un nodo y su valor es una lista de nodos vecinos.

**Simplificación para Foundations**: Solo se requiere crear la estructura del grafo, sin algoritmos complejos como BFS o componentes conectados.

## Ejemplos

### Ejemplo 1:
```python
edges = [("A", "B"), ("A", "C"), ("B", "D")]
graph = create_graph(edges)
print(graph)
# Output: {
#   "A": ["B", "C"], 
#   "B": ["A", "D"], 
#   "C": ["A"], 
#   "D": ["B"]
# }
```

### Ejemplo 2:
```python
edges = [("1", "2"), ("2", "3")]
graph = create_graph(edges)
print(graph)
# Output: {
#   "1": ["2"], 
#   "2": ["1", "3"], 
#   "3": ["2"]
# }
```

### Ejemplo 3:
```python
edges = []
graph = create_graph(edges)
print(graph)
# Output: {}
```

## Restricciones

- Las aristas serán tuplas de exactamente 2 elementos (nodo1, nodo2)  
- Los nodos pueden ser strings o números
- El grafo será no dirigido (si A conecta con B, B también conecta con A)
- No habrá aristas duplicadas en la entrada

## Tags
graph, dictionary, data-structures, foundations

## Notas Adicionales
- **Complejidad de tiempo**: O(V + E) donde V = vértices, E = aristas
- **Complejidad de espacio**: O(V + E)
- **Conceptos clave**: Grafos, listas de adyacencia, diccionarios

# [F080] Data Structures Implementation

## Problema

Implementa tres estructuras de datos básicas:
1. `LinkedList` - lista enlazada con métodos append, prepend, delete
2. `BinaryTree` - árbol binario con métodos insert, search, inorder_traversal
3. `HashTable` - tabla hash con métodos set, get, delete

## Ejemplos

### LinkedList:
```python
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.prepend(0)
print(ll.to_list())  # [0, 1, 2]
ll.delete(1)
print(ll.to_list())  # [0, 2]
```

### BinaryTree:
```python
bt = BinaryTree()
bt.insert(5)
bt.insert(3)
bt.insert(7)
print(bt.search(3))     # True
print(bt.inorder_traversal())  # [3, 5, 7]
```

### HashTable:
```python
ht = HashTable()
ht.set("clave1", "valor1")
ht.set("clave2", "valor2")
print(ht.get("clave1"))  # "valor1"
ht.delete("clave1")
print(ht.get("clave1"))  # None
```

## Restricciones
- Implementar desde cero (no usar listas de Python para LinkedList)
- LinkedList debe usar nodos con referencias
- BinaryTree debe mantener propiedad de árbol binario de búsqueda
- HashTable debe manejar colisiones con chaining
- Incluir método __str__ para visualización

## Conceptos a Practicar
- Estructuras de datos enlazadas
- Recursión en árboles
- Función hash y manejo de colisiones
- Diseño de clases y métodos

# [128] Sum Root to Leaf Numbers

## Problema
Dado un árbol binario donde cada nodo contiene un dígito (0-9), encuentra la suma total de todos los números root-to-leaf.

Un número root-to-leaf es formado concatenando todos los dígitos en el camino desde la raíz hasta la hoja.

## Input/Output
- **Input**: `root` (TreeNode - raíz del árbol binario)
- **Output**: Entero representando la suma total de todos los números root-to-leaf

## Constraints
- El número de nodos está en el rango [1, 1000]
- 0 ≤ Node.val ≤ 9
- La profundidad del árbol no excederá 10

## Ejemplos

### Ejemplo 1:
```
Input: root = [1,2,3]
    1
   / \
  2   3
Output: 25
Explicación: 
- El camino root-to-leaf 1->2 forma el número 12
- El camino root-to-leaf 1->3 forma el número 13
- Por lo tanto, suma = 12 + 13 = 25
```

### Ejemplo 2:
```
Input: root = [4,9,0,5,1]
    4
   / \
  9   0
 / \
5   1
Output: 1026
Explicación:
- El camino root-to-leaf 4->9->5 forma el número 495
- El camino root-to-leaf 4->9->1 forma el número 491
- El camino root-to-leaf 4->0 forma el número 40
- Por lo tanto, suma = 495 + 491 + 40 = 1026
```

### Ejemplo 3 (Edge Case):
```
Input: root = [1]
Output: 1
```

## Explicación
Para cada camino desde la raíz hasta una hoja, construimos un número concatenando los valores de los nodos. Luego sumamos todos estos números.

## Hints
- Usa DFS para recorrer el árbol
- Pasa el número acumulado hasta el momento como parámetro
- Cuando llegues a una hoja, agrega el número completo a la suma total
- Recuerda que número = número_anterior * 10 + valor_nodo_actual

## Tags
tree, dfs, backtracking

## Notas Adicionales
- **Complejidad de tiempo esperada**: O(n) donde n es el número de nodos
- **Complejidad de espacio esperada**: O(h) donde h es la altura del árbol

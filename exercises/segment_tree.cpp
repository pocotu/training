/*
 * Implementación de Segment Tree para consultas de rango y actualizaciones
 * 
 * Este código muestra una implementación básica de un Segment Tree para:
 * 1. Consultar la suma en un rango [l, r]
 * 2. Actualizar un valor en una posición específica
 */

#include <bits/stdc++.h>
using namespace std;

class SegmentTree {
private:
    vector<int> tree;
    int n;
    
    // Construir el árbol recursivamente
    void build(vector<int>& arr, int node, int start, int end) {
        if (start == end) {
            // Nodo hoja
            tree[node] = arr[start];
        } else {
            int mid = (start + end) / 2;
            
            // Construir hijo izquierdo
            build(arr, 2 * node, start, mid);
            // Construir hijo derecho
            build(arr, 2 * node + 1, mid + 1, end);
            
            // Actualizar nodo padre con la suma de sus hijos
            tree[node] = tree[2 * node] + tree[2 * node + 1];
        }
    }
    
    // Consulta de rango [l, r]
    int query(int node, int start, int end, int l, int r) {
        // Caso 1: [start, end] está completamente fuera de [l, r]
        if (start > r || end < l) {
            return 0; // Elemento neutro para la suma
        }
        
        // Caso 2: [start, end] está completamente dentro de [l, r]
        if (l <= start && end <= r) {
            return tree[node];
        }
        
        // Caso 3: [start, end] está parcialmente en [l, r]
        int mid = (start + end) / 2;
        int p1 = query(2 * node, start, mid, l, r);
        int p2 = query(2 * node + 1, mid + 1, end, l, r);
        
        return p1 + p2;
    }
    
    // Actualizar un valor en una posición
    void update(int node, int start, int end, int idx, int val) {
        if (start == end) {
            // Nodo hoja - actualizar directamente
            tree[node] = val;
        } else {
            int mid = (start + end) / 2;
            
            if (idx <= mid) {
                // Si el índice está en el hijo izquierdo
                update(2 * node, start, mid, idx, val);
            } else {
                // Si el índice está en el hijo derecho
                update(2 * node + 1, mid + 1, end, idx, val);
            }
            
            // Actualizar el nodo padre
            tree[node] = tree[2 * node] + tree[2 * node + 1];
        }
    }
    
public:
    SegmentTree(vector<int>& arr) {
        n = arr.size();
        // Asignar memoria para el árbol (4 * n es suficiente)
        tree.resize(4 * n);
        
        // Construir el árbol
        build(arr, 1, 0, n - 1);
    }
    
    // API para consulta
    int query(int l, int r) {
        return query(1, 0, n - 1, l, r);
    }
    
    // API para actualización
    void update(int idx, int val) {
        update(1, 0, n - 1, idx, val);
    }
};

int main() {
    // Ejemplo de uso
    vector<int> arr = {1, 3, 5, 7, 9, 11};
    SegmentTree st(arr);
    
    // Consulta original para el rango [1, 3]
    cout << "Suma en rango [1, 3]: " << st.query(1, 3) << endl;  // 3 + 5 + 7 = 15
    
    // Actualizar arr[2] = 10
    st.update(2, 10);
    
    // Consulta después de actualizar
    cout << "Suma en rango [1, 3] después de actualizar: " << st.query(1, 3) << endl;  // 3 + 10 + 7 = 20
    
    return 0;
}

/*
 * Salida esperada:
 * Suma en rango [1, 3]: 15
 * Suma en rango [1, 3] después de actualizar: 20
 */ 
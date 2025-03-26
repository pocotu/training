/*
 * Implementaciones básicas de algoritmos de grafos
 * 
 * Este archivo contiene implementaciones de:
 * 1. BFS (Breadth-First Search)
 * 2. DFS (Depth-First Search)
 * 3. Algoritmo de Dijkstra para caminos más cortos
 * 4. Algoritmo de Kruskal para Árbol de Expansión Mínima
 */

#include <bits/stdc++.h>
using namespace std;

typedef pair<int, int> pii;
typedef vector<vector<int>> graph;
typedef vector<vector<pii>> weighted_graph;

// --------- Representación de grafos ---------

// Crear grafo no dirigido con lista de adyacencia
graph createGraph(int n, vector<pair<int, int>>& edges) {
    graph g(n);
    for (auto& edge : edges) {
        int u = edge.first;
        int v = edge.second;
        g[u].push_back(v);
        g[v].push_back(u); // Para grafo no dirigido
    }
    return g;
}

// Crear grafo con pesos con lista de adyacencia
weighted_graph createWeightedGraph(int n, vector<tuple<int, int, int>>& edges) {
    weighted_graph g(n);
    for (auto& [u, v, w] : edges) {
        g[u].push_back({v, w});
        g[v].push_back({u, w}); // Para grafo no dirigido
    }
    return g;
}

// --------- BFS (Breadth-First Search) ---------

vector<int> bfs(const graph& g, int start) {
    int n = g.size();
    vector<bool> visited(n, false);
    vector<int> order; // Orden de visita
    
    queue<int> q;
    q.push(start);
    visited[start] = true;
    
    while (!q.empty()) {
        int u = q.front();
        q.pop();
        order.push_back(u);
        
        for (int v : g[u]) {
            if (!visited[v]) {
                visited[v] = true;
                q.push(v);
            }
        }
    }
    
    return order;
}

// BFS que también obtiene distancias desde el origen
vector<int> bfs_distances(const graph& g, int start) {
    int n = g.size();
    vector<int> dist(n, -1); // -1 indica nodo no alcanzable
    
    queue<int> q;
    q.push(start);
    dist[start] = 0;
    
    while (!q.empty()) {
        int u = q.front();
        q.pop();
        
        for (int v : g[u]) {
            if (dist[v] == -1) {
                dist[v] = dist[u] + 1;
                q.push(v);
            }
        }
    }
    
    return dist;
}

// --------- DFS (Depth-First Search) ---------

void dfs_recursive(const graph& g, int u, vector<bool>& visited, vector<int>& order) {
    visited[u] = true;
    order.push_back(u);
    
    for (int v : g[u]) {
        if (!visited[v]) {
            dfs_recursive(g, v, visited, order);
        }
    }
}

vector<int> dfs(const graph& g, int start) {
    int n = g.size();
    vector<bool> visited(n, false);
    vector<int> order;
    
    dfs_recursive(g, start, visited, order);
    
    return order;
}

// DFS iterativo (usando una pila explícita)
vector<int> dfs_iterative(const graph& g, int start) {
    int n = g.size();
    vector<bool> visited(n, false);
    vector<int> order;
    
    stack<int> s;
    s.push(start);
    
    while (!s.empty()) {
        int u = s.top();
        s.pop();
        
        if (!visited[u]) {
            visited[u] = true;
            order.push_back(u);
            
            // Añadir los vecinos en orden inverso para mantener el mismo orden que el DFS recursivo
            for (int i = g[u].size() - 1; i >= 0; i--) {
                int v = g[u][i];
                if (!visited[v]) {
                    s.push(v);
                }
            }
        }
    }
    
    return order;
}

// --------- Algoritmo de Dijkstra ---------

vector<int> dijkstra(const weighted_graph& g, int start) {
    int n = g.size();
    vector<int> dist(n, INT_MAX);
    dist[start] = 0;
    
    // Usar min-heap para obtener siempre el nodo con menor distancia
    priority_queue<pii, vector<pii>, greater<pii>> pq;
    pq.push({0, start}); // {distancia, nodo}
    
    while (!pq.empty()) {
        auto [d, u] = pq.top(); // C++17 structured binding
        pq.pop();
        
        // Ignorar si ya encontramos un camino mejor
        if (d > dist[u]) continue;
        
        for (auto& [v, w] : g[u]) {
            if (dist[u] + w < dist[v]) {
                dist[v] = dist[u] + w;
                pq.push({dist[v], v});
            }
        }
    }
    
    return dist;
}

// --------- Kruskal para MST ---------

// Implementación de Disjoint Set Union (DSU)
class DSU {
private:
    vector<int> parent, rank;
    
public:
    DSU(int n) {
        parent.resize(n);
        rank.resize(n, 0);
        for (int i = 0; i < n; i++) {
            parent[i] = i; // Cada nodo es su propio padre inicialmente
        }
    }
    
    int find(int x) {
        if (parent[x] != x) {
            parent[x] = find(parent[x]); // Compresión de camino
        }
        return parent[x];
    }
    
    void unite(int x, int y) {
        int rootX = find(x);
        int rootY = find(y);
        
        if (rootX == rootY) return;
        
        // Unión por rango
        if (rank[rootX] < rank[rootY]) {
            parent[rootX] = rootY;
        } else {
            parent[rootY] = rootX;
            if (rank[rootX] == rank[rootY]) {
                rank[rootX]++;
            }
        }
    }
    
    bool connected(int x, int y) {
        return find(x) == find(y);
    }
};

// Algoritmo de Kruskal para encontrar el Árbol de Expansión Mínima
vector<tuple<int, int, int>> kruskal(int n, vector<tuple<int, int, int>>& edges) {
    // Ordenar aristas por peso
    sort(edges.begin(), edges.end(), [](const auto& a, const auto& b) {
        return get<2>(a) < get<2>(b);
    });
    
    DSU dsu(n);
    vector<tuple<int, int, int>> mst;
    
    for (auto& [u, v, w] : edges) {
        if (!dsu.connected(u, v)) {
            dsu.unite(u, v);
            mst.push_back({u, v, w});
        }
    }
    
    return mst;
}

// --------- Ejemplo de uso ---------

int main() {
    // Ejemplo para BFS y DFS
    vector<pair<int, int>> edges = {
        {0, 1}, {0, 2}, {1, 3}, {1, 4}, {2, 5}, {2, 6}
    };
    graph g = createGraph(7, edges);
    
    cout << "BFS desde nodo 0: ";
    vector<int> bfs_order = bfs(g, 0);
    for (int node : bfs_order) {
        cout << node << " ";
    }
    cout << endl;
    
    cout << "DFS desde nodo 0: ";
    vector<int> dfs_order = dfs(g, 0);
    for (int node : dfs_order) {
        cout << node << " ";
    }
    cout << endl;
    
    // Ejemplo para Dijkstra
    vector<tuple<int, int, int>> weighted_edges = {
        {0, 1, 4}, {0, 2, 2}, {1, 2, 5}, {1, 3, 10}, 
        {2, 3, 3}, {2, 4, 2}, {3, 4, 7}
    };
    weighted_graph wg = createWeightedGraph(5, weighted_edges);
    
    cout << "Distancias desde nodo 0 (Dijkstra): ";
    vector<int> distances = dijkstra(wg, 0);
    for (int d : distances) {
        cout << d << " ";
    }
    cout << endl;
    
    // Ejemplo para Kruskal
    cout << "Árbol de expansión mínima (Kruskal): " << endl;
    vector<tuple<int, int, int>> mst = kruskal(5, weighted_edges);
    int total_weight = 0;
    for (auto& [u, v, w] : mst) {
        cout << "Arista: " << u << " - " << v << ", Peso: " << w << endl;
        total_weight += w;
    }
    cout << "Peso total del MST: " << total_weight << endl;
    
    return 0;
}

/*
 * Salida esperada:
 * BFS desde nodo 0: 0 1 2 3 4 5 6
 * DFS desde nodo 0: 0 1 3 4 2 5 6
 * Distancias desde nodo 0 (Dijkstra): 0 4 2 5 4
 * Árbol de expansión mínima (Kruskal):
 * Arista: 0 - 2, Peso: 2
 * Arista: 2 - 4, Peso: 2
 * Arista: 2 - 3, Peso: 3
 * Arista: 0 - 1, Peso: 4
 * Peso total del MST: 11
 */ 
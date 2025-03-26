/*
 * Problema de la Mochila (0/1 Knapsack Problem)
 * 
 * Descripción:
 * Dado un conjunto de n items, donde cada item tiene un peso y un valor,
 * determinar la cantidad máxima de valor que se puede obtener en una mochila
 * con una capacidad máxima W.
 * 
 * Este es un problema clásico de programación dinámica.
 */

#include <bits/stdc++.h>
using namespace std;

// Solución con programación dinámica
int knapsack(vector<int>& weights, vector<int>& values, int capacity) {
    int n = weights.size();
    
    // dp[i][j] representa el valor máximo que se puede obtener
    // considerando los primeros i items y una capacidad j
    vector<vector<int>> dp(n + 1, vector<int>(capacity + 1, 0));
    
    for (int i = 1; i <= n; i++) {
        for (int j = 0; j <= capacity; j++) {
            // Si el peso del item actual es mayor que la capacidad,
            // no podemos incluirlo
            if (weights[i - 1] > j) {
                dp[i][j] = dp[i - 1][j];
            } else {
                // Máximo entre no tomar el item actual o tomarlo
                dp[i][j] = max(dp[i - 1][j], 
                              dp[i - 1][j - weights[i - 1]] + values[i - 1]);
            }
        }
    }
    
    // Valor máximo que se puede obtener con n items y capacidad W
    return dp[n][capacity];
}

// Solución optimizada con espacio O(W) en lugar de O(n*W)
int knapsack_optimized(vector<int>& weights, vector<int>& values, int capacity) {
    int n = weights.size();
    
    // Solo necesitamos dos filas: la actual y la anterior
    // O incluso mejor, podemos usar una sola fila actualizándola correctamente
    vector<int> dp(capacity + 1, 0);
    
    for (int i = 0; i < n; i++) {
        // Iteramos de derecha a izquierda para evitar sobreescribir valores que necesitamos
        for (int j = capacity; j >= weights[i]; j--) {
            dp[j] = max(dp[j], dp[j - weights[i]] + values[i]);
        }
    }
    
    return dp[capacity];
}

// Reconstrucción de la solución: qué objetos fueron seleccionados
vector<int> reconstruct_solution(vector<int>& weights, vector<int>& values, int capacity) {
    int n = weights.size();
    vector<vector<int>> dp(n + 1, vector<int>(capacity + 1, 0));
    
    // Calcular la tabla DP como antes
    for (int i = 1; i <= n; i++) {
        for (int j = 0; j <= capacity; j++) {
            if (weights[i - 1] > j) {
                dp[i][j] = dp[i - 1][j];
            } else {
                dp[i][j] = max(dp[i - 1][j], 
                              dp[i - 1][j - weights[i - 1]] + values[i - 1]);
            }
        }
    }
    
    // Reconstruir la solución
    vector<int> selected_items;
    int w = capacity;
    
    for (int i = n; i > 0; i--) {
        // Si este item fue incluido
        if (dp[i][w] != dp[i - 1][w]) {
            selected_items.push_back(i - 1);  // Índice del item seleccionado
            w -= weights[i - 1];              // Reducir la capacidad restante
        }
    }
    
    // Los items están en orden inverso, así que revertimos
    reverse(selected_items.begin(), selected_items.end());
    
    return selected_items;
}

int main() {
    // Ejemplo: tenemos 4 items
    vector<int> weights = {2, 3, 4, 5};   // Pesos
    vector<int> values = {3, 4, 5, 6};    // Valores
    int capacity = 8;                     // Capacidad de la mochila
    
    // Calcular valor máximo
    int max_value = knapsack(weights, values, capacity);
    cout << "Valor máximo obtenible: " << max_value << endl;
    
    // Valor máximo con implementación optimizada
    int max_value_opt = knapsack_optimized(weights, values, capacity);
    cout << "Valor máximo (optimizado): " << max_value_opt << endl;
    
    // Items seleccionados
    vector<int> selected = reconstruct_solution(weights, values, capacity);
    cout << "Items seleccionados: ";
    for (int idx : selected) {
        cout << idx << " (peso: " << weights[idx] << ", valor: " << values[idx] << ")  ";
    }
    cout << endl;
    
    return 0;
}

/*
 * Salida esperada:
 * Valor máximo obtenible: 7
 * Valor máximo (optimizado): 7
 * Items seleccionados: 0 (peso: 2, valor: 3)  1 (peso: 3, valor: 4)
 */ 
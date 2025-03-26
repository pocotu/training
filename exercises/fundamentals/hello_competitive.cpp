/*
 * Problema: Hello Competitive Programming
 * Descripción: Un problema simple para empezar con programación competitiva.
 * Entrada: Un entero n (1 ≤ n ≤ 100), seguido de n enteros a_i (1 ≤ a_i ≤ 100).
 * Salida: La suma, el máximo y el mínimo de los n enteros.
 */

#include <bits/stdc++.h>
using namespace std;

int main() {
    // Optimización de entrada/salida
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    
    // Lectura de datos
    int n;
    cin >> n;
    
    vector<int> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }
    
    // Procesamiento
    int sum = 0;
    int min_val = a[0];
    int max_val = a[0];
    
    for (int val : a) {
        sum += val;
        min_val = min(min_val, val);
        max_val = max(max_val, val);
    }
    
    // Salida de resultados
    cout << "Sum: " << sum << endl;
    cout << "Min: " << min_val << endl;
    cout << "Max: " << max_val << endl;
    
    return 0;
}

/*
 * Ejemplo de entrada:
 * 5
 * 1 5 3 8 2
 *
 * Ejemplo de salida:
 * Sum: 19
 * Min: 1
 * Max: 8
 */ 
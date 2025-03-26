// Incluye todas las bibliotecas estándar de C++
// bits/stdc++.h es una cabecera que incluye todas las bibliotecas estándar
// Es útil en programación competitiva para no tener que incluir cada biblioteca por separado
#include <bits/stdc++.h>

// Usar el namespace std para no tener que escribir std:: antes de cada función/objeto
using namespace std;

// Definiciones útiles para hacer el código más corto y legible
#define ll long long        // Define 'll' como long long para números grandes
#define ld long double      // Define 'ld' como long double para números decimales con más precisión
#define pb push_back       // Define 'pb' como push_back para agregar elementos a vectores
#define mp make_pair       // Define 'mp' como make_pair para crear pares de elementos
#define all(x) (x).begin(), (x).end()     // Define 'all' para obtener el rango completo de un contenedor
#define rall(x) (x).rbegin(), (x).rend()  // Define 'rall' para obtener el rango inverso de un contenedor
#define F first            // Define 'F' como first para acceder al primer elemento de un par
#define S second           // Define 'S' como second para acceder al segundo elemento de un par

// Constantes útiles para problemas de programación competitiva
const int MOD = 1e9 + 7;   // Módulo común usado en problemas combinatorios
const int INF = 1e9;       // Infinito para problemas de grafos y DP
const ll LLINF = 1e18;     // Infinito para números grandes
const double PI = acos(-1.0);  // Constante PI para problemas geométricos

// Función para optimizar la entrada/salida
// Desactiva la sincronización con C++ streams para mejor rendimiento
void fastIO() {
    ios_base::sync_with_stdio(false);  // Desactiva la sincronización con C++ streams
    cin.tie(nullptr);                  // Desvincula cin de cout para mejor rendimiento
    cout.tie(nullptr);                 // Desvincula cout de cin para mejor rendimiento
}

// Función principal para resolver el problema
void solve() {
    // Aquí irá tu código para resolver el problema específico
    
}

// Función principal del programa
int main() {
    fastIO();  // Optimiza la entrada/salida
    
    int t = 1;  // Número de casos de prueba
    // cin >> t;  // Descomentar si hay múltiples casos de prueba
    
    // Bucle para procesar cada caso de prueba
    while (t--) {
        solve();  // Resuelve cada caso de prueba
    }
    
    return 0;  // Indica que el programa terminó correctamente
} 
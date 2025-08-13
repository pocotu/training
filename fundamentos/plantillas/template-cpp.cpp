// ⚡ Plantilla C++ para Programación Competitiva
// Usa esta plantilla como punto de partida para tus soluciones

// ==========================================
// INCLUDES Y CONFIGURACIÓN
// ==========================================

#include <bits/stdc++.h>
using namespace std;

// ==========================================
// DEFINICIONES Y MACROS ÚTILES
// ==========================================

// Tipos de datos más cortos
#define ll long long
#define ld long double
#define ull unsigned long long

// Operaciones con contenedores
#define pb push_back
#define mp make_pair
#define all(x) (x).begin(), (x).end()
#define rall(x) (x).rbegin(), (x).rend()
#define sz(x) (int)(x).size()

// Acceso a pares
#define F first
#define S second

// Loops más cortos
#define rep(i, a, b) for(int i = a; i < b; i++)
#define per(i, a, b) for(int i = a; i >= b; i--)
#define fore(x, v) for(auto &x : v)

// ==========================================
// CONSTANTES ÚTILES
// ==========================================

const int MOD = 1e9 + 7;      // Módulo común
const int INF = 1e9;          // Infinito para int
const ll LLINF = 1e18;        // Infinito para long long
const double EPS = 1e-9;      // Epsilon para comparaciones de punto flotante
const double PI = acos(-1.0); // Pi

// ==========================================
// FUNCIONES ÚTILES
// ==========================================

// Optimización de entrada/salida
void fastIO() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
}

// Debugging (descomenta cuando necesites)
template<typename T>
void debug(T x) {
    // cerr << "DEBUG: " << x << endl;
}

template<typename T, typename... Args>
void debug(T x, Args... args) {
    // cerr << "DEBUG: " << x << " ";
    // debug(args...);
}

// Máximo común divisor
ll gcd(ll a, ll b) {
    return b == 0 ? a : gcd(b, a % b);
}

// Mínimo común múltiplo
ll lcm(ll a, ll b) {
    return a / gcd(a, b) * b;
}

// Potencia rápida con módulo
ll power(ll base, ll exp, ll mod = MOD) {
    ll result = 1;
    while (exp > 0) {
        if (exp % 2 == 1) result = (result * base) % mod;
        base = (base * base) % mod;
        exp /= 2;
    }
    return result;
}

// ==========================================
// FUNCIÓN PRINCIPAL
// ==========================================

void solve() {
    /*
    Aquí escribes tu solución al problema
    */
    
    // Ejemplo: leer dos números y sumarlos
    // int a, b;
    // cin >> a >> b;
    // cout << a + b << endl;
}

// ==========================================
// EJECUCIÓN PRINCIPAL
// ==========================================

int main() {
    fastIO();  // Optimiza entrada/salida
    
    int t = 1;  // Número de casos de prueba
    // cin >> t;  // Descomenta si hay múltiples casos
    
    while (t--) {
        solve();
    }
    
    return 0;
}

// ==========================================
// NOTAS Y CONSEJOS
// ==========================================

/*
📝 CÓMO USAR ESTA PLANTILLA:

1. Copia este archivo para cada problema nuevo
2. Escribe tu lógica en la función solve()
3. Descomenta 'cin >> t' si hay múltiples casos de prueba
4. Usa las macros y funciones definidas para código más limpio

⚡ TRUCOS PARA C++ EN COMPETENCIAS:

- Siempre usa fastIO() para problemas con mucha entrada
- Prefiere vector<int> sobre arrays cuando el tamaño es variable
- Usa 'auto' para tipos complicados: auto it = mp.begin();
- Usa 'const' cuando sepas que no cambiarás una variable

🔧 MACROS ÚTILES:
- rep(i, 0, n): for(int i = 0; i < n; i++)
- all(v): v.begin(), v.end() (para sort, etc.)
- sz(v): tamaño de contenedor
- pb: push_back más corto

🐛 DEBUGGING:
- Usa debug(variable) para imprimir en stderr
- Comenta/descomenta según necesites
- También: cerr << "DEBUG: " << variable << endl;

⚠️ CUIDADO CON:
- Overflow: usa 'long long' para números grandes
- Índices: arrays empiezan en 0, no en 1
- Comparaciones de punto flotante: usa EPS
- Módulo negativo: ((x % MOD) + MOD) % MOD

📊 COMPLEJIDADES TÍPICAS EN C++:
- O(n): hasta 10^7 elementos
- O(n log n): hasta 10^6 elementos  
- O(n²): hasta 5*10^3 elementos
*/

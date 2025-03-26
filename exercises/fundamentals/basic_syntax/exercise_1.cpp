#include <bits/stdc++.h>
using namespace std;

/*
 * Ejercicio 1: Determinar si un número es par o impar
 * 
 * Este programa solicita al usuario un número y determina si es par o impar.
 * Es un ejercicio básico para practicar:
 * - Entrada/salida básica
 * - Operador módulo (%)
 * - Estructuras condicionales (if-else)
 */

int main() {
    // Desactivar sincronización de I/O para mejor rendimiento
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int numero;
    
    // Solicitar entrada al usuario
    cout << "Ingrese un número: ";
    cin >> numero;
    
    // Determinar si es par o impar usando el operador módulo
    if (numero % 2 == 0) {
        cout << numero << " es un número par.\n";
    } else {
        cout << numero << " es un número impar.\n";
    }
    
    return 0;
} 
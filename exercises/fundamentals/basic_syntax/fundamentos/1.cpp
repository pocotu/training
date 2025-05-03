// 1. Escribe un programa que solicite al usuario un// número y determine si es par o impar.

#include <iostream>

using namespace std;

int main() {
    int num;
    cout <<"Ingrese un numero: ";
    cin >> num;
    if (num % 2 == 0) {
        cout << "El numero es par";
        
    } else {
        cout << "El numero es impar";
    }

    return 0;
}


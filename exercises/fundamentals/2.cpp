// Crea un programa que pida al usuario tres 
// números y muestre el mayor de ellos usando 
// estructuras condicionales.

#include <iostream>

using namespace std;

int main() {
    int a, b, c;

    cout << "Primer numero";
    cin >> a;

    cout << "Segundo numero";
    cin >> b;

    cout << "Tercer numero";
    cin >> c;

    if (a > b && a > c ) {
        cout << "a es el mayor";
    } else if (b > a && b > c) {
        cout << "b es el mayor";
    } else {
        cout << "c es el mayor";
    }

    return 0;
}



# Estructura de Ejercicios

Este directorio contiene todos los ejercicios y soluciones organizados según el plan de estudio en `learning.md`.

## Estructura de Directorios

```
exercises/
├── fundamentals/           # Fundamentos de C++
│   ├── basic_syntax/      # Sintaxis básica y estructuras de control
│   ├── functions/         # Funciones y modularización
│   ├── stl/              # Estructuras de datos básicas y STL
│   ├── oop/              # Programación Orientada a Objetos
│   └── optimization/      # Técnicas de optimización
├── algorithms/           # Algoritmos y estructuras de datos básicos
│   ├── recursion/        # Recursión y backtracking
│   ├── sorting/          # Ordenamiento y búsqueda
│   ├── data_structures/  # Estructuras de datos adicionales
│   └── complexity/       # Análisis de complejidad
├── mathematics/          # Matemáticas para programación competitiva
│   ├── number_theory/    # Teoría de números
│   ├── combinatorics/    # Combinatoria y probabilidad
│   ├── linear_algebra/   # Álgebra lineal y matrices
│   └── game_theory/      # Teoría de juegos
├── competitive/          # Introducción a la programación competitiva
│   ├── contest_format/   # Formato y estrategias de concursos
│   ├── basic_problems/   # Problemas iniciales
│   ├── problem_types/    # Formatos específicos de problemas
│   └── debugging/        # Debugging y estrategias de prueba
├── advanced/             # Algoritmos y técnicas comunes
│   ├── dp/              # Programación dinámica
│   ├── greedy/          # Algoritmos voraces
│   ├── data_structures/ # Estructuras de datos avanzadas
│   ├── graphs/          # Grafos y algoritmos de grafos
│   ├── specialized/     # Estructuras y algoritmos especializados
│   └── strings/         # Procesamiento de cadenas
└── contests/            # Soluciones de concursos
    ├── codeforces/      # Problemas de Codeforces
    ├── atcoder/         # Problemas de AtCoder
    └── cses/            # Problemas del CSES Problem Set
```

## Cómo Resolver los Ejercicios

1. **Organización**: Cada ejercicio debe estar en su directorio correspondiente según el tema y subtema.

2. **Nombrado de Archivos**: 
   - Usa nombres descriptivos en minúsculas con guiones bajos
   - Incluye el número del ejercicio si está especificado en learning.md
   - Ejemplo: `exercise_1.cpp`, `palindrome_checker.cpp`

3. **Estructura de Archivos**:
   ```cpp
   // exercise_name.cpp
   #include <bits/stdc++.h>
   using namespace std;

   // Tu solución aquí
   int main() {
       // Código principal
       return 0;
   }
   ```

4. **Testing**:
   - Crea casos de prueba para cada ejercicio
   - Usa el directorio `tests/` para archivos de prueba
   - Incluye casos de prueba en el mismo archivo cuando sea apropiado

5. **Documentación**:
   - Incluye comentarios explicando el algoritmo
   - Documenta la complejidad temporal y espacial
   - Menciona cualquier consideración especial o casos edge

## Plataformas de Práctica

Para resolver los ejercicios, puedes usar las siguientes plataformas:

1. **Plataformas Principales**:
   - [Codeforces](https://codeforces.com/)
   - [AtCoder](https://atcoder.jp/)
   - [CSES Problem Set](https://cses.fi/problemset/)
   - [SPOJ](https://www.spoj.com/)

2. **Plataformas Adicionales**:
   - [UVa Online Judge](https://onlinejudge.org/)
   - [LeetCode](https://leetcode.com/)
   - [HackerRank](https://www.hackerrank.com/)

## Recursos Adicionales

- Usa el directorio `templates/` para plantillas de código
- Consulta `resources/` para materiales de estudio adicionales
- Revisa las editoriales de problemas en las plataformas mencionadas
- Participa en la comunidad para recibir feedback y aprender de otros

## Seguimiento de Progreso

1. Marca los ejercicios completados en `learning.md`
2. Documenta las soluciones en tu repositorio
3. Mantén un registro de los problemas resueltos por tema
4. Revisa periódicamente los conceptos aprendidos 
#!/bin/bash

# Competitive Programming Practice - Test Runner
# Script para ejecutar todos los tests del repositorio
# 
# Uso:
#   ./tools/run_tests.sh              # Ejecutar todos los tests
#   ./tools/run_tests.sh basic        # Solo tests básicos
#   ./tools/run_tests.sh intermediate # Solo tests intermedios  
#   ./tools/run_tests.sh advanced     # Solo tests avanzados
#   ./tools/run_tests.sh contests     # Solo tests de contests
#   ./tools/run_tests.sh 001          # Test específico por ID

set -e  # Salir si algún comando falla

# Colores para output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# Banner
echo -e "${CYAN}🏆 Competitive Programming Practice - Test Runner${NC}"
echo -e "${CYAN}=================================================${NC}"
echo ""

# Verificar si pytest está instalado
if ! command -v pytest &> /dev/null; then
    echo -e "${RED}❌ pytest no está instalado. Instálalo con:${NC}"
    echo -e "${YELLOW}   pip install pytest${NC}"
    exit 1
fi

# Verificar si estamos en el directorio correcto
if [ ! -d "problems" ]; then
    echo -e "${RED}❌ Error: Debes ejecutar este script desde el directorio raíz del repositorio${NC}"
    echo -e "${YELLOW}   cd competitive-programming-practice && ./tools/run_tests.sh${NC}"
    exit 1
fi

# Función para mostrar estadísticas
show_stats() {
    echo ""
    echo -e "${BLUE}📊 Estadísticas de Tests:${NC}"
    echo -e "${BLUE}========================${NC}"
    
    # Contar archivos de test
    total_tests=$(find problems -name "test.py" | wc -l)
    basic_tests=$(find problems/basic -name "test.py" 2>/dev/null | wc -l || echo "0")
    intermediate_tests=$(find problems/intermediate -name "test.py" 2>/dev/null | wc -l || echo "0")
    advanced_tests=$(find problems/advanced -name "test.py" 2>/dev/null | wc -l || echo "0")
    contest_tests=$(find problems/contests -name "test.py" 2>/dev/null | wc -l || echo "0")
    
    echo -e "  📁 Total de archivos de test: ${GREEN}$total_tests${NC}"
    echo -e "  🟢 Básicos: ${GREEN}$basic_tests${NC}"
    echo -e "  🟡 Intermedios: ${YELLOW}$intermediate_tests${NC}"
    echo -e "  🔴 Avanzados: ${RED}$advanced_tests${NC}"
    echo -e "  🏆 Contests: ${PURPLE}$contest_tests${NC}"
    echo ""
}

# Función para ejecutar tests con pytest
run_pytest() {
    local path=$1
    local description=$2
    
    echo -e "${BLUE}🔍 Ejecutando tests: $description${NC}"
    echo -e "${BLUE}===========================${NC}"
    
    if [ -z "$(find $path -name "test.py" 2>/dev/null)" ]; then
        echo -e "${YELLOW}⚠️  No se encontraron archivos test.py en $path${NC}"
        return 0
    fi
    
    # Ejecutar pytest con opciones detalladas
    if pytest "$path" -v --tb=short --color=yes; then
        echo -e "${GREEN}✅ Tests en $path: EXITOSOS${NC}"
        return 0
    else
        echo -e "${RED}❌ Tests en $path: FALLARON${NC}"
        return 1
    fi
}

# Función para ejecutar test específico por ID
run_specific_test() {
    local test_id=$1
    echo -e "${BLUE}🎯 Buscando test para problema ID: $test_id${NC}"
    
    # Buscar el problema por ID
    test_file=""
    for dir in problems/basic problems/intermediate problems/advanced problems/contests; do
        if [ -d "$dir" ]; then
            for problem_dir in "$dir"/*; do
                if [ -d "$problem_dir" ] && [[ "$(basename "$problem_dir")" == *"$test_id"* ]]; then
                    if [ -f "$problem_dir/test.py" ]; then
                        test_file="$problem_dir/test.py"
                        break 2
                    fi
                fi
            done
        fi
    done
    
    if [ -z "$test_file" ]; then
        echo -e "${RED}❌ No se encontró test para el problema ID: $test_id${NC}"
        return 1
    fi
    
    echo -e "${GREEN}📁 Encontrado: $test_file${NC}"
    echo ""
    
    if pytest "$test_file" -v --tb=short --color=yes; then
        echo -e "${GREEN}✅ Test para $test_id: EXITOSO${NC}"
        return 0
    else
        echo -e "${RED}❌ Test para $test_id: FALLÓ${NC}"
        return 1
    fi
}

# Función para mostrar ayuda
show_help() {
    echo -e "${CYAN}📖 Uso del script run_tests.sh${NC}"
    echo ""
    echo -e "${YELLOW}Comandos disponibles:${NC}"
    echo -e "  ./tools/run_tests.sh              ${GREEN}# Ejecutar todos los tests${NC}"
    echo -e "  ./tools/run_tests.sh basic        ${GREEN}# Solo tests básicos (001-015)${NC}"
    echo -e "  ./tools/run_tests.sh intermediate ${GREEN}# Solo tests intermedios (101-120)${NC}"
    echo -e "  ./tools/run_tests.sh advanced     ${GREEN}# Solo tests avanzados (201-215)${NC}"
    echo -e "  ./tools/run_tests.sh contests     ${GREEN}# Solo tests de contests${NC}"
    echo -e "  ./tools/run_tests.sh 001          ${GREEN}# Test específico por ID${NC}"
    echo -e "  ./tools/run_tests.sh --help       ${GREEN}# Mostrar esta ayuda${NC}"
    echo -e "  ./tools/run_tests.sh --stats      ${GREEN}# Solo mostrar estadísticas${NC}"
    echo ""
    echo -e "${YELLOW}Ejemplos:${NC}"
    echo -e "  ./tools/run_tests.sh 001          ${GREEN}# Ejecutar test del problema Two Sum${NC}"
    echo -e "  ./tools/run_tests.sh 101          ${GREEN}# Ejecutar test del problema Add Two Numbers${NC}"
    echo -e "  ./tools/run_tests.sh basic        ${GREEN}# Todos los problemas básicos${NC}"
    echo ""
}

# Variable para contar errores
errors=0

# Procesar argumentos
case "${1:-all}" in
    "--help"|"-h"|"help")
        show_help
        exit 0
        ;;
        
    "--stats"|"-s"|"stats")
        show_stats
        exit 0
        ;;
        
    "basic")
        show_stats
        run_pytest "problems/basic" "Problemas Básicos (001-015)" || ((errors++))
        ;;
        
    "intermediate")
        show_stats
        run_pytest "problems/intermediate" "Problemas Intermedios (101-120)" || ((errors++))
        ;;
        
    "advanced")
        show_stats
        run_pytest "problems/advanced" "Problemas Avanzados (201-215)" || ((errors++))
        ;;
        
    "contests")
        show_stats
        run_pytest "problems/contests" "Problemas de Contests" || ((errors++))
        ;;
        
    [0-9][0-9][0-9])
        # Test específico por ID (formato: 001, 101, 201, etc.)
        run_specific_test "$1" || ((errors++))
        ;;
        
    "all"|"")
        # Ejecutar todos los tests
        show_stats
        
        echo -e "${PURPLE}🚀 Ejecutando TODOS los tests...${NC}"
        echo ""
        
        # Tests básicos
        if [ -d "problems/basic" ]; then
            run_pytest "problems/basic" "Problemas Básicos" || ((errors++))
            echo ""
        fi
        
        # Tests intermedios
        if [ -d "problems/intermediate" ]; then
            run_pytest "problems/intermediate" "Problemas Intermedios" || ((errors++))
            echo ""
        fi
        
        # Tests avanzados
        if [ -d "problems/advanced" ]; then
            run_pytest "problems/advanced" "Problemas Avanzados" || ((errors++))
            echo ""
        fi
        
        # Tests de contests
        if [ -d "problems/contests" ]; then
            run_pytest "problems/contests" "Problemas de Contests" || ((errors++))
            echo ""
        fi
        ;;
        
    *)
        echo -e "${RED}❌ Argumento no reconocido: $1${NC}"
        echo ""
        show_help
        exit 1
        ;;
esac

# Resumen final
echo ""
echo -e "${CYAN}🏁 Resumen de Ejecución${NC}"
echo -e "${CYAN}======================${NC}"

if [ $errors -eq 0 ]; then
    echo -e "${GREEN}✅ ¡Todos los tests pasaron exitosamente!${NC}"
    echo -e "${GREEN}🎉 Tu código está funcionando correctamente.${NC}"
    exit 0
else
    echo -e "${RED}❌ $errors grupo(s) de tests fallaron.${NC}"
    echo -e "${YELLOW}💡 Revisa los errores mostrados arriba para identificar los problemas.${NC}"
    echo ""
    echo -e "${YELLOW}Consejos para debugging:${NC}"
    echo -e "  • Ejecuta un test específico: ${CYAN}./tools/run_tests.sh 001${NC}"
    echo -e "  • Revisa la implementación en el archivo solution.py${NC}"
    echo -e "  • Verifica que los imports sean correctos${NC}"
    echo -e "  • Asegúrate de que la función tenga el nombre correcto${NC}"
    exit 1
fi

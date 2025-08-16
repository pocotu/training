# [F094] Command Line Interface Tools

## Problema

Crea una herramienta CLI completa usando argparse:

1. `TaskCLI` - clase principal para la interfaz CLI
2. Comandos: `create`, `list`, `update`, `delete`, `config`
3. Soporte para argumentos, opciones y subcomandos

## Ejemplos

### Uso básico:
```bash
python task_cli.py create "Nueva tarea" --priority high --due "2025-08-20"
python task_cli.py list --status pending --priority high
python task_cli.py update 1 --status completed
python task_cli.py delete 2
python task_cli.py config --set email user@example.com
```

### Función TaskCLI:
```python
cli = TaskCLI()
cli.run()  # Procesa argumentos de línea de comandos
```

### Subcomandos soportados:
- `create <title>` - Crear nueva tarea
- `list` - Listar tareas con filtros opcionales
- `update <id>` - Actualizar tarea existente
- `delete <id>` - Eliminar tarea
- `config` - Gestión de configuración

## Restricciones
- Usar argparse para parsing de argumentos
- TaskCLI debe soportar todos los subcomandos
- Incluir help text descriptivo para cada comando
- Validar argumentos requeridos
- Manejar errores de entrada graciosamente
- Soportar tanto argumentos posicionales como opcionales

## Conceptos a Practicar
- argparse module avanzado
- Subparsers para subcomandos
- Validación de entrada de usuario
- Diseño de interfaces CLI intuitivas

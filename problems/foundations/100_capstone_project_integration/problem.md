# [F100] Foundations Review Integration

## Problema

Crea funciones que integren múltiples conceptos básicos aprendidos en foundations:

1. `process_student_data(students_list)` - procesa datos de estudiantes usando diccionarios y listas
2. `create_grade_report(student_data)` - genera reporte usando strings y formateo
3. `validate_and_store(data, storage)` - valida datos y los almacena en estructura

**Foundations**: Integra conceptos fundamentales: listas, diccionarios, strings, validación, funciones.

## Funcionalidades:

### Función process_student_data:
- Recibe lista de diccionarios con datos de estudiantes
- Calcula promedios, encuentra mejor/peor estudiante  
- Retorna estadísticas resumidas

### Función create_grade_report:
- Genera reporte de calificaciones en formato texto
- Usa formateo de strings para presentación limpia
- Incluye estadísticas calculadas

### Función validate_and_store:  
- Valida formato de datos de entrada
- Almacena datos válidos en estructura de diccionarios
- Maneja errores de validación apropiadamente

### API Endpoints:
```
POST /api/tasks - Create task
GET /api/tasks - List tasks
PUT /api/tasks/{id} - Update task
DELETE /api/tasks/{id} - Delete task
POST /api/auth/login - Authentication
```

### CLI Interface:
```bash
python task_manager.py create "New task" --priority high
python task_manager.py list --status pending
python task_manager.py config --email user@example.com
```

## Restricciones Técnicas:
- Usar FastAPI o Flask para API web
- SQLite para base de datos con SQLAlchemy ORM
- JWT para autenticación
- SMTP para notificaciones email
- argparse para CLI
- YAML para configuración
- logging module para logs
- pytest para testing
- setup.py para packaging

## Arquitectura del Proyecto:
```
task_manager/
├── __init__.py
├── models.py          # Database models
├── api.py            # Web API endpoints  
├── cli.py            # Command line interface
├── auth.py           # Authentication system
├── notifications.py  # Email notifications
├── config.py         # Configuration management
├── utils.py          # Utility functions
├── tests/            # Unit tests
└── setup.py          # Package configuration
```

## Conceptos Integrados:
- OOP avanzado con herencia y polimorfismo
- API REST design patterns
- Database design y ORM
- Authentication y autorización
- Async/await para operaciones I/O
- Error handling y logging
- Configuration management
- Testing strategies
- Package distribution
- CLI design
- Email automation
- Security best practices

## Entregables:
1. Código fuente completo y funcional
2. Tests con >80% cobertura
3. Documentación API (OpenAPI/Swagger)
4. README con instrucciones de instalación
5. Archivo de configuración ejemplo
6. Script de setup para deployment

Este proyecto capstone demuestra la integración de todos los conceptos foundations aprendidos en un sistema real y funcional.

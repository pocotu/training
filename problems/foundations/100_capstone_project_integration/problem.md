# [F100] Capstone Project Integration

## Problema

Crea una aplicación completa que integre múltiples conceptos de foundations:

**Proyecto**: Sistema de Gestión de Tareas con API Web

### Componentes Requeridos:

1. **TaskManager Class** - gestión completa de tareas
2. **RESTful API** - endpoints para CRUD operations  
3. **Database Integration** - persistencia con SQLite
4. **Authentication System** - login básico con JWT
5. **Email Notifications** - notificaciones automáticas
6. **CLI Interface** - herramienta de línea de comandos
7. **Configuration Management** - settings centralizados
8. **Logging System** - registro de actividades
9. **Unit Tests** - cobertura de testing completa
10. **Package Structure** - distribución como paquete Python

## Funcionalidades Principales:

### TaskManager Class:
```python
manager = TaskManager(config_file="config.yaml")
task_id = manager.create_task("Complete project", "high", "2025-08-20")
manager.update_task(task_id, status="in_progress")
tasks = manager.get_tasks(filter_by="high")
```

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

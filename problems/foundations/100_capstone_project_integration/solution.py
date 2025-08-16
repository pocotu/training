"""
F100 - Capstone Project Integration
Sistema de Gestión de Tareas Completo

Este es el proyecto capstone que integra todos los conceptos foundations
"""

from typing import Dict, List, Optional, Any
import sqlite3
import json
import logging
import yaml
from datetime import datetime, date
import hashlib
import os

class TaskManager:
    """
    Gestor principal de tareas que integra múltiples conceptos
    """
    
    def __init__(self, config_file: str = "config.yaml"):
        """
        Inicializa el gestor de tareas
        Args:
            config_file: archivo de configuración
        """
        self.config_file = config_file
        self.db_path = "tasks.db"
        self.logger = logging.getLogger(__name__)
        
        # Configurar logging
        setup_logging()
        
        # Configurar base de datos
        setup_database()
        
        # Cargar configuración
        self.config_manager = ConfigManager(config_file)
        self.config = self.config_manager.load_config()
        
        self.logger.info("TaskManager inicializado correctamente")
    
    def create_task(self, title: str, priority: str, due_date: str) -> int:
        """
        Crea una nueva tarea
        Args:
            title: título de la tarea
            priority: prioridad (low, medium, high)
            due_date: fecha límite en formato YYYY-MM-DD
        Returns:
            int: ID de la tarea creada
        """
        if priority not in ['low', 'medium', 'high']:
            raise ValueError("Priority must be 'low', 'medium', or 'high'")
        
        try:
            datetime.strptime(due_date, '%Y-%m-%d')
        except ValueError:
            raise ValueError("Due date must be in YYYY-MM-DD format")
        
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute("""
            INSERT INTO tasks (title, priority, due_date, status, created_at)
            VALUES (?, ?, ?, 'pending', ?)
        """, (title, priority, due_date, datetime.now().isoformat()))
        
        task_id = cursor.lastrowid
        conn.commit()
        conn.close()
        
        self.logger.info(f"Tarea creada: ID {task_id}, título '{title}'")
        return task_id
    
    def update_task(self, task_id: int, **kwargs) -> bool:
        """
        Actualiza una tarea existente
        Args:
            task_id: ID de la tarea
            **kwargs: campos a actualizar
        Returns:
            bool: True si actualización exitosa
        """
        if not kwargs:
            return False
        
        allowed_fields = ['title', 'priority', 'due_date', 'status']
        valid_kwargs = {k: v for k, v in kwargs.items() if k in allowed_fields}
        
        if not valid_kwargs:
            return False
        
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Verificar que la tarea existe
        cursor.execute("SELECT id FROM tasks WHERE id = ?", (task_id,))
        if not cursor.fetchone():
            conn.close()
            return False
        
        # Construir query de actualización
        set_clause = ", ".join([f"{k} = ?" for k in valid_kwargs.keys()])
        query = f"UPDATE tasks SET {set_clause}, updated_at = ? WHERE id = ?"
        
        values = list(valid_kwargs.values()) + [datetime.now().isoformat(), task_id]
        
        cursor.execute(query, values)
        conn.commit()
        conn.close()
        
        self.logger.info(f"Tarea {task_id} actualizada: {valid_kwargs}")
        return True
    
    def get_tasks(self, filter_by: str = None) -> List[Dict]:
        """
        Obtiene lista de tareas con filtros opcionales
        Args:
            filter_by: filtro a aplicar (priority, status, etc.)
        Returns:
            List[Dict]: lista de tareas
        """
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        if filter_by:
            # Simple filtro por status o priority
            if filter_by in ['pending', 'completed', 'cancelled']:
                cursor.execute("SELECT * FROM tasks WHERE status = ?", (filter_by,))
            elif filter_by in ['low', 'medium', 'high']:
                cursor.execute("SELECT * FROM tasks WHERE priority = ?", (filter_by,))
            else:
                cursor.execute("SELECT * FROM tasks")
        else:
            cursor.execute("SELECT * FROM tasks ORDER BY created_at DESC")
        
        rows = cursor.fetchall()
        conn.close()
        
        tasks = [dict(row) for row in rows]
        self.logger.info(f"Recuperadas {len(tasks)} tareas")
        return tasks
    
    def delete_task(self, task_id: int) -> bool:
        """
        Elimina una tarea
        Args:
            task_id: ID de la tarea a eliminar
        Returns:
            bool: True si eliminación exitosa
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
        deleted_count = cursor.rowcount
        
        conn.commit()
        conn.close()
        
        if deleted_count > 0:
            self.logger.info(f"Tarea {task_id} eliminada")
            return True
        else:
            self.logger.warning(f"No se encontró tarea con ID {task_id}")
            return False

class AuthSystem:
    """
    Sistema de autenticación con JWT (simulado)
    """
    
    def __init__(self, secret_key: str):
        self.secret_key = secret_key
        self.users = {}  # En producción sería una base de datos
    
    def create_user(self, username: str, password: str) -> bool:
        """Crea nuevo usuario con contraseña hasheada"""
        if username in self.users:
            return False
        
        # Hash de la contraseña
        password_hash = hashlib.sha256(password.encode()).hexdigest()
        
        self.users[username] = {
            'password_hash': password_hash,
            'created_at': datetime.now().isoformat()
        }
        
        return True
    
    def authenticate(self, username: str, password: str) -> Optional[str]:
        """Autentica usuario y retorna JWT token (simulado)"""
        if username not in self.users:
            return None
        
        password_hash = hashlib.sha256(password.encode()).hexdigest()
        
        if self.users[username]['password_hash'] == password_hash:
            # Token JWT simulado (en producción usar PyJWT)
            token_data = {
                'username': username,
                'issued_at': datetime.now().isoformat()
            }
            token = f"mock_jwt_token_{username}_{datetime.now().timestamp()}"
            return token
        
        return None
    
    def verify_token(self, token: str) -> Optional[Dict]:
        """Verifica token JWT y retorna payload (simulado)"""
        if token.startswith("mock_jwt_token_"):
            parts = token.split("_")
            if len(parts) >= 4:
                username = parts[3]
                return {'username': username, 'valid': True}
        
        return None

class EmailNotifier:
    """
    Sistema de notificaciones por email (simulado)
    """
    
    def __init__(self, smtp_config: Dict):
        self.smtp_config = smtp_config
        self.logger = logging.getLogger(__name__)
    
    def send_task_reminder(self, email: str, task: Dict) -> bool:
        """Envía recordatorio de tarea por email (simulado)"""
        message = f"""
        Recordatorio de Tarea
        
        Título: {task.get('title', 'N/A')}
        Prioridad: {task.get('priority', 'N/A')}
        Fecha límite: {task.get('due_date', 'N/A')}
        Estado: {task.get('status', 'N/A')}
        
        ¡No olvides completar esta tarea!
        """
        
        self.logger.info(f"Email de recordatorio enviado a {email} para tarea {task.get('id')}")
        print(f"📧 Email enviado a {email}: Recordatorio de tarea '{task.get('title')}'")
        return True
    
    def send_daily_summary(self, email: str, tasks: List[Dict]) -> bool:
        """Envía resumen diario de tareas (simulado)"""
        pending_tasks = [t for t in tasks if t.get('status') == 'pending']
        completed_tasks = [t for t in tasks if t.get('status') == 'completed']
        
        message = f"""
        Resumen Diario de Tareas
        
        Tareas Pendientes: {len(pending_tasks)}
        Tareas Completadas: {len(completed_tasks)}
        Total de Tareas: {len(tasks)}
        
        ¡Sigue así!
        """
        
        self.logger.info(f"Resumen diario enviado a {email}")
        print(f"📊 Resumen diario enviado a {email}: {len(pending_tasks)} pendientes, {len(completed_tasks)} completadas")
        return True

class ConfigManager:
    """
    Gestor de configuración centralizado
    """
    
    def __init__(self, config_file: str):
        self.config_file = config_file
        self.config = {}
    
    def load_config(self) -> Dict:
        """Carga configuración desde archivo"""
        try:
            if os.path.exists(self.config_file):
                with open(self.config_file, 'r', encoding='utf-8') as f:
                    self.config = yaml.safe_load(f) or {}
            else:
                # Configuración por defecto
                self.config = {
                    'database': {'name': 'tasks.db'},
                    'logging': {'level': 'INFO', 'file': 'app.log'},
                    'email': {'smtp_server': 'smtp.example.com', 'port': 587},
                    'auth': {'secret_key': 'default_secret_key'}
                }
                self.save_config(self.config)
        except Exception as e:
            print(f"Error cargando configuración: {e}")
            self.config = {}
        
        return self.config
    
    def save_config(self, config: Dict) -> bool:
        """Guarda configuración a archivo"""
        try:
            with open(self.config_file, 'w', encoding='utf-8') as f:
                yaml.dump(config, f, default_flow_style=False)
            self.config = config
            return True
        except Exception as e:
            print(f"Error guardando configuración: {e}")
            return False
    
    def get(self, key: str, default: Any = None) -> Any:
        """Obtiene valor de configuración"""
        keys = key.split('.')
        value = self.config
        
        try:
            for k in keys:
                value = value[k]
            return value
        except (KeyError, TypeError):
            return default

def setup_database():
    """
    Configura la base de datos inicial
    """
    conn = sqlite3.connect("tasks.db")
    cursor = conn.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            priority TEXT NOT NULL CHECK (priority IN ('low', 'medium', 'high')),
            due_date TEXT NOT NULL,
            status TEXT NOT NULL DEFAULT 'pending' CHECK (status IN ('pending', 'completed', 'cancelled')),
            created_at TEXT NOT NULL,
            updated_at TEXT
        )
    """)
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            created_at TEXT NOT NULL
        )
    """)
    
    conn.commit()
    conn.close()
    
    print("✅ Base de datos configurada")

def setup_logging():
    """
    Configura el sistema de logging
    """
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler('capstone.log'),
            logging.StreamHandler()
        ]
    )
    
    print("✅ Sistema de logging configurado")

def main():
    """
    Función principal del capstone project
    """
    print("🏆 Capstone Project - Sistema de Gestión de Tareas")
    print("Iniciando componentes...")
    
    # Configuración inicial
    setup_logging()
    setup_database()
    
    # Inicializar componentes principales
    task_manager = TaskManager()
    
    # Crear algunas tareas de ejemplo
    task1_id = task_manager.create_task("Completar proyecto capstone", "high", "2024-12-31")
    task2_id = task_manager.create_task("Revisar documentación", "medium", "2024-12-15")
    
    # Obtener tareas
    all_tasks = task_manager.get_tasks()
    print(f"📋 Total de tareas: {len(all_tasks)}")
    
    # Actualizar una tarea
    task_manager.update_task(task1_id, status="completed")
    
    # Sistema de autenticación
    auth = AuthSystem("secret_key_123")
    auth.create_user("admin", "password123")
    token = auth.authenticate("admin", "password123")
    
    if token:
        print("🔐 Autenticación exitosa")
    
    # Sistema de notificaciones
    email_notifier = EmailNotifier({'smtp_server': 'smtp.example.com'})
    if all_tasks:
        email_notifier.send_task_reminder("user@example.com", all_tasks[0])
    
    print("✅ Sistema inicializado exitosamente")
    return True

if __name__ == "__main__":
    result = main()
    print(f"Resultado: {result}")

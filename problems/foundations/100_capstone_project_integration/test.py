import unittest
from unittest.mock import patch, MagicMock
from solution import TaskManager, AuthSystem, EmailNotifier, ConfigManager, main

class TestCapstoneProjectIntegration(unittest.TestCase):
    
    def setUp(self):
        """Configuración inicial para tests"""
        self.task_manager = TaskManager("test_config.yaml")
        self.auth_system = AuthSystem("test_secret_key")
        self.config_manager = ConfigManager("test_config.yaml")
    
    def test_task_manager_initialization(self):
        """Test inicialización del TaskManager"""
        self.assertIsInstance(self.task_manager, TaskManager)
    
    def test_create_task_basic(self):
        """Test creación básica de tarea"""
        task_id = self.task_manager.create_task(
            "Test Task", 
            "high", 
            "2025-08-20"
        )
        # TODO: Uncomment when implementation is complete
        # self.assertIsInstance(task_id, int)
        # self.assertGreater(task_id, 0)
    
    def test_auth_system_initialization(self):
        """Test inicialización del sistema de autenticación"""
        self.assertIsInstance(self.auth_system, AuthSystem)
        self.assertEqual(self.auth_system.secret_key, "test_secret_key")
    
    def test_user_creation(self):
        """Test creación de usuario"""
        result = self.auth_system.create_user("testuser", "password123")
        # TODO: Uncomment when implementation is complete
        # self.assertIsInstance(result, bool)
    
    def test_config_manager_initialization(self):
        """Test inicialización del gestor de configuración"""
        self.assertIsInstance(self.config_manager, ConfigManager)
        self.assertEqual(self.config_manager.config_file, "test_config.yaml")
    
    @patch('smtplib.SMTP')
    def test_email_notifier_initialization(self, mock_smtp):
        """Test inicialización del notificador de email"""
        smtp_config = {
            "server": "smtp.test.com",
            "port": 587,
            "username": "test@test.com",
            "password": "testpass"
        }
        notifier = EmailNotifier(smtp_config)
        self.assertIsInstance(notifier, EmailNotifier)
        self.assertEqual(notifier.smtp_config, smtp_config)
    
    def test_integration_workflow(self):
        """Test workflow integrado básico"""
        # 1. Crear usuario
        user_created = self.auth_system.create_user("john", "password123")
        
        # 2. Autenticar usuario  
        token = self.auth_system.authenticate("john", "password123")
        
        # 3. Crear tarea
        task_id = self.task_manager.create_task(
            "Integration Test Task",
            "medium", 
            "2025-08-25"
        )
        
        # 4. Obtener tareas
        tasks = self.task_manager.get_tasks()
        
        # TODO: Uncomment when implementations are complete
        # self.assertTrue(user_created)
        # self.assertIsNotNone(token)
        # self.assertIsInstance(task_id, int)
        # self.assertIsInstance(tasks, list)
    
    def test_main_function_execution(self):
        """Test que la función main se ejecuta sin errores"""
        try:
            main()
            # Si llega aquí, no hubo excepciones
            self.assertTrue(True)
        except Exception as e:
            self.fail(f"main() raised an exception: {e}")
    
    def test_component_integration(self):
        """Test integración entre componentes"""
        # Verificar que los componentes pueden trabajar juntos
        components = [
            TaskManager("test.yaml"),
            AuthSystem("secret"),
            ConfigManager("test.yaml")
        ]
        
        for component in components:
            self.assertIsNotNone(component)
    
    def test_error_handling(self):
        """Test manejo de errores básico"""
        task_manager = TaskManager()
        
        # Test con prioridad inválida
        with self.assertRaises(ValueError):
            task_manager.create_task("Test Task", "invalid_priority", "2024-12-31")
        
        # Test con fecha inválida
        with self.assertRaises(ValueError):
            task_manager.create_task("Test Task", "high", "invalid_date")

if __name__ == '__main__':
    unittest.main()

"""
Solution for Project Integration and Best Practices
Problem ID: F085
"""

import os
import sys
import logging
from pathlib import Path
import configparser

class ProjectManager:
    """
    Project management and best practices implementation.
    """
    
    def __init__(self, project_name="sample_project"):
        """
        Initialize project manager.
        Args:
            project_name (str): name of the project
        """
        self.project_name = project_name
        self.project_root = Path.cwd() / project_name
        self.config = configparser.ConfigParser()
        self.logger = self._setup_logging()
    
    def _setup_logging(self):
        """Set up logging configuration."""
        logger = logging.getLogger(self.project_name)
        logger.setLevel(logging.INFO)
        
        # Create console handler
        handler = logging.StreamHandler()
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        
        return logger
    
    def create_project_structure(self):
        """
        Create standard project directory structure.
        Returns:
            bool: True if successful
        """
        try:
            directories = [
                self.project_root,
                self.project_root / "src",
                self.project_root / "tests",
                self.project_root / "docs",
                self.project_root / "config",
                self.project_root / "logs"
            ]
            
            for directory in directories:
                directory.mkdir(parents=True, exist_ok=True)
            
            self.logger.info(f"Created project structure for {self.project_name}")
            return True
        except Exception as e:
            self.logger.error(f"Failed to create project structure: {e}")
            return False
    
    def create_config_file(self, config_data):
        """
        Create configuration file.
        Args:
            config_data (dict): configuration data
        Returns:
            bool: True if successful
        """
        try:
            for section, options in config_data.items():
                self.config.add_section(section)
                for key, value in options.items():
                    self.config.set(section, key, str(value))
            
            config_path = self.project_root / "config" / "settings.ini"
            with open(config_path, 'w') as f:
                self.config.write(f)
            
            self.logger.info("Configuration file created")
            return True
        except Exception as e:
            self.logger.error(f"Failed to create config file: {e}")
            return False
    
    def read_config_file(self, config_path=None):
        """
        Read configuration file.
        Args:
            config_path (str): path to config file
        Returns:
            dict: configuration data
        """
        try:
            if config_path is None:
                config_path = self.project_root / "config" / "settings.ini"
            
            self.config.read(config_path)
            
            config_dict = {}
            for section in self.config.sections():
                config_dict[section] = dict(self.config.items(section))
            
            return config_dict
        except Exception as e:
            self.logger.error(f"Failed to read config file: {e}")
            return {}
    
    def validate_dependencies(self, required_modules):
        """
        Validate that required modules are available.
        Args:
            required_modules (list): list of required module names
        Returns:
            dict: validation results
        """
        results = {
            "all_available": True,
            "missing_modules": [],
            "available_modules": []
        }
        
        for module_name in required_modules:
            try:
                __import__(module_name)
                results["available_modules"].append(module_name)
            except ImportError:
                results["missing_modules"].append(module_name)
                results["all_available"] = False
        
        return results
    
    def create_readme(self):
        """
        Create README.md file with project template.
        Returns:
            bool: True if successful
        """
        try:
            readme_content = f"""# {self.project_name}

## Description
Brief description of the project.

## Installation
```bash
pip install -r requirements.txt
```

## Usage
```python
python src/main.py
```

## Project Structure
```
{self.project_name}/
├── src/           # Source code
├── tests/         # Test files
├── docs/          # Documentation
├── config/        # Configuration files
├── logs/          # Log files
└── README.md      # This file
```

## Testing
```bash
python -m pytest tests/
```

## Contributing
1. Fork the repository
2. Create a feature branch
3. Make changes
4. Run tests
5. Submit pull request
"""
            
            readme_path = self.project_root / "README.md"
            with open(readme_path, 'w', encoding='utf-8') as f:
                f.write(readme_content)
            
            self.logger.info("README.md created")
            return True
        except Exception as e:
            self.logger.error(f"Failed to create README: {e}")
            return False
    
    def cleanup_project(self):
        """
        Clean up temporary project files.
        Returns:
            bool: True if successful
        """
        try:
            import shutil
            if self.project_root.exists():
                shutil.rmtree(self.project_root)
            self.logger.info("Project cleaned up")
            return True
        except Exception as e:
            self.logger.error(f"Failed to cleanup project: {e}")
            return False

def setup_virtual_environment():
    """
    Mock function to demonstrate virtual environment setup.
    Returns:
        dict: setup information
    """
    return {
        "virtual_env": "recommended",
        "python_version": sys.version,
        "pip_available": True,
        "setup_command": "python -m venv venv"
    }

def code_quality_check():
    """
    Mock function for code quality checks.
    Returns:
        dict: quality check results
    """
    return {
        "style_check": "passed",
        "complexity_check": "passed",
        "documentation_coverage": "85%",
        "test_coverage": "90%"
    }

def main():
    """
    Función principal para 085_project_integration
    """
    print("Project Integration Examples:")
    
    # Create project manager
    pm = ProjectManager("demo_project")
    
    # Create project structure
    if pm.create_project_structure():
        print("✅ Project structure created")
        
        # Create configuration
        config_data = {
            "database": {
                "host": "localhost",
                "port": "5432",
                "name": "demo_db"
            },
            "logging": {
                "level": "INFO",
                "format": "%(asctime)s - %(levelname)s - %(message)s"
            }
        }
        
        pm.create_config_file(config_data)
        pm.create_readme()
        
        # Check dependencies
        deps = pm.validate_dependencies(["json", "os", "sys"])
        print(f"✅ Dependencies check: {deps['all_available']}")
        
        # Virtual environment info
        venv_info = setup_virtual_environment()
        print(f"✅ Virtual env setup: {venv_info['setup_command']}")
        
        # Quality check
        quality = code_quality_check()
        print(f"✅ Code quality: {quality['style_check']}")
        
        # Cleanup
        pm.cleanup_project()
        print("✅ Project cleaned up")
    
    return True

if __name__ == "__main__":
    result = main()
    print(f"Resultado: {result}")

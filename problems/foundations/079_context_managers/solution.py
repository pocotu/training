"""
Solution for Context Managers
Problem ID: F079
"""

import os
import tempfile
from contextlib import contextmanager

class FileManager:
    """
    Context manager for file operations.
    """
    
    def __init__(self, filename, mode='r'):
        """
        Initialize file manager.
        Args:
            filename (str): file to manage
            mode (str): file mode
        """
        self.filename = filename
        self.mode = mode
        self.file = None
    
    def __enter__(self):
        """Enter context - open file."""
        print(f"Opening file: {self.filename}")
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_value, traceback):
        """Exit context - close file."""
        if self.file:
            print(f"Closing file: {self.filename}")
            self.file.close()
        
        # Handle exceptions
        if exc_type is not None:
            print(f"Exception occurred: {exc_value}")
            return False  # Don't suppress the exception
        
        return True

@contextmanager
def temporary_directory():
    """
    Context manager that creates and cleans up a temporary directory.
    """
    temp_dir = tempfile.mkdtemp()
    print(f"Created temporary directory: {temp_dir}")
    
    try:
        yield temp_dir
    finally:
        # Cleanup
        import shutil
        shutil.rmtree(temp_dir, ignore_errors=True)
        print(f"Cleaned up temporary directory: {temp_dir}")

class Timer:
    """
    Context manager for timing code execution.
    """
    
    def __enter__(self):
        """Enter context - start timer."""
        import time
        self.start_time = time.time()
        print("Timer started")
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        """Exit context - stop timer and report."""
        import time
        elapsed = time.time() - self.start_time
        print(f"Timer stopped. Elapsed time: {elapsed:.4f} seconds")
        return False

def main():
    """
    Función principal para 079_context_managers
    """
    print("Context Managers Examples:")
    
    # File manager example
    print("\n1. Custom File Manager:")
    temp_file = "temp_test.txt"
    try:
        with FileManager(temp_file, 'w') as f:
            f.write("Hello, Context Manager!")
        
        with FileManager(temp_file, 'r') as f:
            content = f.read()
            print(f"File content: {content}")
    
    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Cleanup
        if os.path.exists(temp_file):
            os.remove(temp_file)
    
    # Temporary directory example
    print("\n2. Temporary Directory Manager:")
    with temporary_directory() as temp_dir:
        print(f"Working in: {temp_dir}")
        # Create a test file in temp directory
        test_file = os.path.join(temp_dir, "test.txt")
        with open(test_file, 'w') as f:
            f.write("Test content")
        print(f"Created file: {test_file}")
    
    # Timer example
    print("\n3. Timer Context Manager:")
    with Timer():
        # Simulate some work
        import time
        time.sleep(0.1)
        print("Doing some work...")
    
    return True

if __name__ == "__main__":
    result = main()
    print(f"Resultado: {result}")

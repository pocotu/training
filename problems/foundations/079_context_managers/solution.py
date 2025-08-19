"""
Solution for Context Managers
Problem ID: F079
"""

import os
import tempfile
from contextlib import contextmanager

class FileManager:    
    def __init__(self, filename, mode='r'):
        # TODO: Implement your solution here
        pass
    
    def __enter__(self):
        # TODO: Implement your solution here
        pass
    
    def __exit__(self, exc_type, exc_value, traceback):
        # TODO: Implement your solution here
        pass

@contextmanager
def temporary_directory():
    # TODO: Implement your solution here
    pass

class Timer:
    def __enter__(self):
        import time
        self.start_time = time.time()
        print("Timer started")
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        import time
        elapsed = time.time() - self.start_time
        print(f"Timer stopped. Elapsed time: {elapsed:.4f} seconds")
        return False

def main():
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

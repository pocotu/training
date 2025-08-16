"""
Solution for File Operations Basics
Problem ID: F073
"""

def write_lines_to_file(filename, lines):
    """
    Writes lines to a file.
    Args:
        filename (str): name of the file
        lines (list): list of strings to write
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            for line in lines:
                f.write(line + '\n')
        return True
    except Exception:
        return False

def read_lines_from_file(filename):
    """
    Reads lines from a file.
    Args:
        filename (str): name of the file
    Returns:
        list: list of lines or empty list if error
    """
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return [line.strip() for line in f.readlines()]
    except Exception:
        return []

def count_words_in_file(filename):
    """
    Counts words in a file.
    Args:
        filename (str): name of the file
    Returns:
        int: number of words or 0 if error
    """
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
            words = content.split()
            return len(words)
    except Exception:
        return 0

def main():
    """
    Función principal para 073_file_operations_basics
    """
    # Ejemplos de uso (usando archivos temporales)
    test_filename = "test_file.txt"
    test_lines = ["Hello World", "Python Programming", "File Operations"]
    
    print("File Operations Examples:")
    
    # Write to file
    write_success = write_lines_to_file(test_filename, test_lines)
    print(f"Write success: {write_success}")
    
    if write_success:
        # Read from file
        read_lines = read_lines_from_file(test_filename)
        print(f"Read lines: {read_lines}")
        
        # Count words
        word_count = count_words_in_file(test_filename)
        print(f"Word count: {word_count}")
        
        # Cleanup
        try:
            import os
            os.remove(test_filename)
        except:
            pass
    
    return write_success

if __name__ == "__main__":
    result = main()
    print(f"Resultado: {result}")

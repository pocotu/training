"""
Solution for Regular Expressions Basics
Problem ID: F076
"""

import re

def validate_email(email):
    """
    Validates email format using regex.
    Args:
        email (str): email to validate
    Returns:
        bool: True if valid email, False otherwise
    """
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

def extract_phone_numbers(text):
    """
    Extracts phone numbers from text.
    Args:
        text (str): text to search
    Returns:
        list: list of phone numbers found
    """
    # Pattern for phone numbers (various formats)
    pattern = r'\b(?:\+?1[-.]?)?\(?([0-9]{3})\)?[-.]?([0-9]{3})[-.]?([0-9]{4})\b'
    matches = re.findall(pattern, text)
    
    # Format the phone numbers
    phone_numbers = []
    for match in matches:
        formatted = f"({match[0]}) {match[1]}-{match[2]}"
        phone_numbers.append(formatted)
    
    return phone_numbers

def clean_text(text):
    """
    Cleans text by removing extra whitespaces and special characters.
    Args:
        text (str): text to clean
    Returns:
        str: cleaned text
    """
    # Remove extra whitespaces
    text = re.sub(r'\s+', ' ', text)
    
    # Remove special characters (keep only letters, numbers, spaces)
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    
    # Strip leading/trailing whitespace
    return text.strip()

def main():
    """
    Función principal para 076_regex_basics
    """
    # Ejemplos de uso
    print("Regular Expressions Examples:")
    
    # Email validation
    emails = ["test@example.com", "invalid-email", "user@domain.org"]
    for email in emails:
        is_valid = validate_email(email)
        print(f"Email '{email}': {'Valid' if is_valid else 'Invalid'}")
    
    # Phone number extraction
    text_with_phones = "Call me at (555) 123-4567 or 555.987.6543 for more info"
    phones = extract_phone_numbers(text_with_phones)
    print(f"Found phone numbers: {phones}")
    
    # Text cleaning
    dirty_text = "  Hello!!!   World???   Python@@@   "
    clean = clean_text(dirty_text)
    print(f"Original: '{dirty_text}'")
    print(f"Cleaned: '{clean}'")
    
    return validate_email("test@example.com")

if __name__ == "__main__":
    result = main()
    print(f"Resultado: {result}")

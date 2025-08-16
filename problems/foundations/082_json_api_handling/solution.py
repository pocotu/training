"""
Solution for JSON and API Handling
Problem ID: F082
"""

import json
import urllib.request
import urllib.error

def parse_json(json_string):
    """
    Parse JSON string and return Python object.
    Args:
        json_string (str): JSON string to parse
    Returns:
        dict or list: parsed JSON data
    """
    try:
        return json.loads(json_string)
    except json.JSONDecodeError:
        return None

def create_json(data):
    """
    Convert Python object to JSON string.
    Args:
        data: Python object to convert
    Returns:
        str: JSON string
    """
    try:
        return json.dumps(data, indent=2)
    except TypeError:
        return None

def fetch_url(url, timeout=10):
    """
    Fetch data from URL (mock implementation for testing).
    Args:
        url (str): URL to fetch
        timeout (int): timeout in seconds
    Returns:
        dict: response data with status and content
    """
    # Mock implementation for testing
    if "jsonplaceholder" in url:
        return {
            "status": 200,
            "data": {
                "userId": 1,
                "id": 1,
                "title": "Sample Post",
                "body": "This is a sample post for testing."
            }
        }
    elif "httpbin.org" in url:
        return {
            "status": 200,
            "data": {
                "args": {},
                "headers": {
                    "User-Agent": "Python/urllib"
                },
                "origin": "127.0.0.1",
                "url": url
            }
        }
    else:
        return {
            "status": 404,
            "data": None
        }

def process_api_response(response):
    """
    Process API response and extract relevant data.
    Args:
        response (dict): API response with status and data
    Returns:
        dict: processed response data
    """
    if not response or response.get("status") != 200:
        return {
            "success": False,
            "error": "API request failed"
        }
    
    data = response.get("data", {})
    return {
        "success": True,
        "data": data,
        "summary": f"Processed {len(data)} fields" if isinstance(data, dict) else "Processed response"
    }

def save_json_to_file(data, filename):
    """
    Save data to JSON file.
    Args:
        data: data to save
        filename (str): filename to save to
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        return True
    except Exception:
        return False

def load_json_from_file(filename):
    """
    Load data from JSON file.
    Args:
        filename (str): filename to load from
    Returns:
        dict or None: loaded data or None if error
    """
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception:
        return None

def main():
    """
    Función principal para 082_json_api_handling
    """
    print("JSON and API Handling Examples:")
    
    # JSON parsing
    sample_json = '{"name": "John", "age": 30, "city": "New York"}'
    parsed = parse_json(sample_json)
    print(f"Parsed JSON: {parsed}")
    
    # JSON creation
    data = {"message": "Hello", "status": "success"}
    json_str = create_json(data)
    print(f"Created JSON: {json_str}")
    
    # Mock API call
    response = fetch_url("https://jsonplaceholder.typicode.com/posts/1")
    processed = process_api_response(response)
    print(f"API Response: {processed}")
    
    return True

if __name__ == "__main__":
    result = main()
    print(f"Resultado: {result}")

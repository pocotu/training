"""
Solution for Web Scraping Basics
Problem ID: F089
"""

import re
import json
from urllib.parse import urljoin, urlparse

def parse_html_content(html_content):
    """
    Parse HTML content and extract basic information (mock implementation).
    Args:
        html_content (str): HTML content to parse
    Returns:
        dict: parsed information
    """
    # Mock HTML parsing without external dependencies
    title_match = re.search(r'<title[^>]*>([^<]+)</title>', html_content, re.IGNORECASE)
    title = title_match.group(1) if title_match else "No title found"
    
    # Extract links
    link_pattern = r'<a[^>]*href=["\']([^"\']+)["\'][^>]*>([^<]*)</a>'
    links = re.findall(link_pattern, html_content, re.IGNORECASE)
    
    # Extract images
    img_pattern = r'<img[^>]*src=["\']([^"\']+)["\'][^>]*>'
    images = re.findall(img_pattern, html_content, re.IGNORECASE)
    
    # Extract paragraphs
    p_pattern = r'<p[^>]*>([^<]+)</p>'
    paragraphs = re.findall(p_pattern, html_content, re.IGNORECASE)
    
    return {
        "title": title.strip(),
        "links": links[:10],  # First 10 links
        "images": images[:5],  # First 5 images
        "paragraphs": paragraphs[:3],  # First 3 paragraphs
        "total_links": len(links),
        "total_images": len(images)
    }

def extract_emails_from_text(text):
    """
    Extract email addresses from text.
    Args:
        text (str): text to search for emails
    Returns:
        list: list of email addresses found
    """
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    emails = re.findall(email_pattern, text)
    return list(set(emails))  # Remove duplicates

def extract_phone_numbers(text):
    """
    Extract phone numbers from text.
    Args:
        text (str): text to search for phone numbers
    Returns:
        list: list of phone numbers found
    """
    # Pattern for various phone number formats
    phone_patterns = [
        r'\b\d{3}-\d{3}-\d{4}\b',  # 123-456-7890
        r'\b\(\d{3}\)\s*\d{3}-\d{4}\b',  # (123) 456-7890
        r'\b\d{3}\.\d{3}\.\d{4}\b',  # 123.456.7890
        r'\b\d{10}\b'  # 1234567890
    ]
    
    phone_numbers = []
    for pattern in phone_patterns:
        matches = re.findall(pattern, text)
        phone_numbers.extend(matches)
    
    return list(set(phone_numbers))

def clean_scraped_text(text):
    """
    Clean scraped text by removing extra whitespace and HTML entities.
    Args:
        text (str): text to clean
    Returns:
        str: cleaned text
    """
    # Remove HTML tags
    text = re.sub(r'<[^>]+>', '', text)
    
    # Replace HTML entities
    html_entities = {
        '&amp;': '&',
        '&lt;': '<',
        '&gt;': '>',
        '&quot;': '"',
        '&apos;': "'",
        '&nbsp;': ' '
    }
    
    for entity, replacement in html_entities.items():
        text = text.replace(entity, replacement)
    
    # Clean extra whitespace
    text = re.sub(r'\s+', ' ', text)
    text = text.strip()
    
    return text

def validate_url(url):
    """
    Validate if a URL is properly formed.
    Args:
        url (str): URL to validate
    Returns:
        bool: True if valid URL
    """
    try:
        parsed = urlparse(url)
        return all([parsed.scheme, parsed.netloc])
    except Exception:
        return False

def extract_domain_from_url(url):
    """
    Extract domain from URL.
    Args:
        url (str): URL to extract domain from
    Returns:
        str: domain name or None if invalid
    """
    try:
        parsed = urlparse(url)
        return parsed.netloc
    except Exception:
        return None

def mock_scrape_website(url):
    """
    Mock website scraping function (for testing without actual requests).
    Args:
        url (str): URL to scrape
    Returns:
        dict: mock scraped data
    """
    # Mock HTML content
    mock_html = f"""
    <html>
    <head>
        <title>Sample Website - {extract_domain_from_url(url)}</title>
    </head>
    <body>
        <h1>Welcome to Sample Website</h1>
        <p>This is a sample paragraph with some content.</p>
        <p>Contact us at info@example.com or call (555) 123-4567</p>
        <a href="/about">About Us</a>
        <a href="/contact">Contact</a>
        <img src="/images/logo.png" alt="Logo">
        <div>More content here with email: support@test.com</div>
    </body>
    </html>
    """
    
    # Parse the mock HTML
    parsed_data = parse_html_content(mock_html)
    
    # Extract additional information
    emails = extract_emails_from_text(mock_html)
    phones = extract_phone_numbers(mock_html)
    
    return {
        "url": url,
        "title": parsed_data["title"],
        "content": parsed_data,
        "emails": emails,
        "phone_numbers": phones,
        "scraped_at": "2024-01-01 12:00:00",
        "success": True
    }

def scraping_session_manager():
    """
    Mock scraping session manager.
    Returns:
        dict: session configuration
    """
    return {
        "user_agent": "Mozilla/5.0 (Web Scraper Bot)",
        "timeout": 30,
        "max_retries": 3,
        "delay_between_requests": 1,
        "respect_robots_txt": True
    }

def main():
    """
    Función principal para 089_web_scraping_basics
    """
    print("Web Scraping Basics Examples:")
    
    # Test URL validation
    test_urls = ["https://example.com", "invalid-url", "http://test.org"]
    for url in test_urls:
        is_valid = validate_url(url)
        print(f"URL '{url}': {'Valid' if is_valid else 'Invalid'}")
    
    # Test mock scraping
    scrape_result = mock_scrape_website("https://example.com")
    print(f"\nScraping result:")
    print(f"- Title: {scrape_result['title']}")
    print(f"- Emails found: {scrape_result['emails']}")
    print(f"- Phone numbers: {scrape_result['phone_numbers']}")
    print(f"- Links: {scrape_result['content']['total_links']}")
    
    # Test text cleaning
    dirty_html = "<p>Hello &amp; welcome to our &quot;site&quot;!</p>   "
    clean_text = clean_scraped_text(dirty_html)
    print(f"\nCleaned text: '{clean_text}'")
    
    # Session manager
    session = scraping_session_manager()
    print(f"\nSession configured with {session['max_retries']} max retries")
    
    return True

if __name__ == "__main__":
    result = main()
    print(f"Resultado: {result}")

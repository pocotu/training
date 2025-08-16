# [F089] Web Scraping Basics

## Problema

Implementa tres funciones para web scraping básico:

1. `scrape_webpage(url)` - extrae título, headers y links de una página
2. `scrape_table_data(url, table_selector)` - extrae datos de tabla HTML
3. `scrape_with_session(urls)` - scraping con sesión persistente

## Ejemplos

### Función scrape_webpage:
```python
url = "https://example.com"
data = scrape_webpage(url)
print(data)
# {
#   "title": "Example Domain",
#   "headers": ["h1", "h2", "h3"],
#   "links": ["https://link1.com", "https://link2.com"]
# }
```

### Función scrape_table_data:
```python
url = "https://example.com/table"
table_data = scrape_table_data(url, "table.data")
print(table_data)
# [
#   {"col1": "value1", "col2": "value2"},
#   {"col1": "value3", "col2": "value4"}
# ]
```

### Función scrape_with_session:
```python
urls = ["https://site1.com", "https://site2.com"]
results = scrape_with_session(urls)
print(results)  # Datos scrapeados manteniendo cookies/sesión
```

## Restricciones
- Usar requests para HTTP requests
- Usar BeautifulSoup para parsing HTML
- scrape_webpage debe manejar errores HTTP
- scrape_table_data debe convertir tabla a lista de diccionarios
- scrape_with_session debe usar requests.Session()
- Incluir headers apropiados (User-Agent)
- Respetar robots.txt y rate limiting básico

## Conceptos a Practicar
- HTTP requests con requests library
- HTML parsing con BeautifulSoup
- CSS selectors básicos
- Session management

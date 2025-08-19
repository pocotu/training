"""
Solution for CSV Data Processing
Problem ID: F048
"""

import csv
import io
from pathlib import Path

def create_csv(data, filename=None):
    if not data:
        return ""
    
    # Crear contenido CSV
    output = io.StringIO()
    fieldnames = data[0].keys()
    writer = csv.DictWriter(output, fieldnames=fieldnames)
    
    writer.writeheader()
    writer.writerows(data)
    
    csv_content = output.getvalue()
    output.close()
    
    # Si se proporciona filename, escribir archivo
    if filename:
        with open(filename, 'w', newline='', encoding='utf-8') as f:
            f.write(csv_content)
    
    return csv_content

def read_csv_to_dict(csv_content):
    if not csv_content.strip():
        return []
    
    input_stream = io.StringIO(csv_content)
    reader = csv.DictReader(input_stream)
    return list(reader)

def analyze_csv_data(csv_content):
    data = read_csv_to_dict(csv_content)
    
    if not data:
        return {"total_rows": 0, "columns": []}
    
    return {
        "total_rows": len(data),
        "columns": list(data[0].keys()),
        "sample_row": data[0] if data else None
    }

def main():
    # Ejemplo de uso
    sample_data = [
        {"name": "Alice", "age": "30", "city": "New York"},
        {"name": "Bob", "age": "25", "city": "Los Angeles"},
        {"name": "Charlie", "age": "35", "city": "Chicago"}
    ]
    
    # Crear CSV
    csv_content = create_csv(sample_data)
    print("CSV creado:")
    print(csv_content)
    
    # Leer CSV
    data = read_csv_to_dict(csv_content)
    print(f"Datos leídos: {data}")
    
    # Analizar CSV
    analysis = analyze_csv_data(csv_content)
    print(f"Análisis: {analysis}")
    
    return analysis

if __name__ == "__main__":
    result = main()
    print(f"Resultado: {result}")

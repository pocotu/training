# [F076] Regular Expressions Basics

## Problema

Implementa tres funciones usando expresiones regulares:
1. `validate_email(email)` - valida formato de email
2. `extract_phone_numbers(text)` - extrae números de teléfono
3. `clean_text(text)` - limpia caracteres especiales, deja solo letras y espacios

## Ejemplos

### Función validate_email:
```
Input: validate_email("usuario@dominio.com")
Output: True

Input: validate_email("email-invalido")
Output: False
```

### Función extract_phone_numbers:
```
Input: extract_phone_numbers("Llama al 123-456-7890 o al (555) 123-4567")
Output: ["123-456-7890", "(555) 123-4567"]
```

### Función clean_text:
```
Input: clean_text("Hola! ¿Cómo estás? Bien, gracias.")
Output: "Hola Cómo estás Bien gracias"
```

## Restricciones
- Usar módulo re de Python
- validate_email debe aceptar formato básico: name@domain.extension
- extract_phone_numbers debe encontrar formatos: XXX-XXX-XXXX y (XXX) XXX-XXXX
- clean_text debe preservar espacios únicos entre palabras

## Conceptos a Practicar
- Expresiones regulares básicas
- Validación de patrones
- Extracción de texto
- Limpieza de datos

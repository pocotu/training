# [F076] Regular Expressions Basics

## Problema

Escribe una función llamada `validate_email` que reciba un string `email` y devuelva `True` si tiene un formato de email básicamente válido, `False` en caso contrario.

**Criterios básicos para email válido**:
- Contiene exactamente un símbolo @
- Tiene al menos un carácter antes del @
- Tiene al menos un carácter después del @
- Después del @ contiene al menos un punto
- Tiene al menos un carácter después del último punto

**Simplificado para Foundations**: Validación básica sin regex compleja.

## Ejemplos

### Ejemplo 1:
```
Input: validate_email("usuario@dominio.com")
Output: True
```

### Ejemplo 2:
```
Input: validate_email("email-invalido")
Output: False
```

### Ejemplo 3:
```
Input: validate_email("test@gmail.org")
Output: True
```

## Restricciones

- No usar expresiones regulares complejas (usar métodos básicos de string)
- El email será un string válido
- Considerar solo formato básico (no todas las especificaciones RFC)

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

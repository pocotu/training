# [F090] Email and SMTP Handling

## Problema

Implementa tres funciones para manejo de correo electrónico:

1. `send_simple_email(smtp_config, to, subject, body)` - envía email básico
2. `send_email_with_attachment(smtp_config, to, subject, body, file_path)` - email con adjunto
3. `email_template_system(template, data, recipients)` - sistema de templates

## Ejemplos

### Función send_simple_email:
```python
smtp_config = {
    "server": "smtp.gmail.com",
    "port": 587,
    "username": "user@gmail.com",
    "password": "app_password"
}
result = send_simple_email(smtp_config, "dest@example.com", 
                          "Test Subject", "Hello World!")
print(result)  # True si enviado exitosamente
```

### Función send_email_with_attachment:
```python
result = send_email_with_attachment(smtp_config, "dest@example.com",
                                   "Report", "See attachment", 
                                   "report.pdf")
print(result)  # True si enviado con adjunto
```

### Función email_template_system:
```python
template = "Hello {name}, your order #{order_id} is ready!"
data = [
    {"name": "Ana", "order_id": "123"},
    {"name": "Luis", "order_id": "124"}
]
recipients = ["ana@example.com", "luis@example.com"]
results = email_template_system(template, data, recipients)
print(results)  # Lista de resultados de envío
```

## Restricciones
- Usar smtplib para envío de emails
- Usar email.mime modules para composición
- send_simple_email debe manejar autenticación TLS/SSL
- send_email_with_attachment debe validar que archivo existe
- email_template_system debe hacer template substitution
- Manejar excepciones SMTP apropiadamente
- Validar formato de email básico

## Conceptos a Practicar
- SMTP protocol básico
- Email composition con MIME
- File attachments
- Template systems básicos

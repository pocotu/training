"""
Solution for Email and SMTP Handling
Problem ID: F090
"""

import smtplib
import email
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os
from datetime import datetime

class EmailManager:
    """
    Email management class for sending and composing emails.
    """
    
    def __init__(self, smtp_server="smtp.gmail.com", smtp_port=587):
        """
        Initialize email manager.
        Args:
            smtp_server (str): SMTP server address
            smtp_port (int): SMTP server port
        """
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.connection = None
    
    def create_text_email(self, sender, recipient, subject, body):
        """
        Create a plain text email.
        Args:
            sender (str): sender email address
            recipient (str): recipient email address
            subject (str): email subject
            body (str): email body
        Returns:
            MIMEText: email message object
        """
        msg = MIMEText(body)
        msg['From'] = sender
        msg['To'] = recipient
        msg['Subject'] = subject
        msg['Date'] = email.utils.formatdate(localtime=True)
        
        return msg
    
    def create_html_email(self, sender, recipient, subject, html_body, text_body=None):
        """
        Create an HTML email.
        Args:
            sender (str): sender email address
            recipient (str): recipient email address
            subject (str): email subject
            html_body (str): HTML email body
            text_body (str): plain text alternative
        Returns:
            MIMEMultipart: email message object
        """
        msg = MIMEMultipart('alternative')
        msg['From'] = sender
        msg['To'] = recipient
        msg['Subject'] = subject
        msg['Date'] = email.utils.formatdate(localtime=True)
        
        # Add plain text part if provided
        if text_body:
            text_part = MIMEText(text_body, 'plain')
            msg.attach(text_part)
        
        # Add HTML part
        html_part = MIMEText(html_body, 'html')
        msg.attach(html_part)
        
        return msg
    
    def create_email_with_attachment(self, sender, recipient, subject, body, attachment_path):
        """
        Create email with attachment.
        Args:
            sender (str): sender email address
            recipient (str): recipient email address
            subject (str): email subject
            body (str): email body
            attachment_path (str): path to attachment file
        Returns:
            MIMEMultipart: email message object
        """
        msg = MIMEMultipart()
        msg['From'] = sender
        msg['To'] = recipient
        msg['Subject'] = subject
        msg['Date'] = email.utils.formatdate(localtime=True)
        
        # Add body
        msg.attach(MIMEText(body))
        
        # Add attachment (mock - for testing we don't need actual file)
        if attachment_path:
            filename = os.path.basename(attachment_path)
            attachment = MIMEBase('application', 'octet-stream')
            attachment.set_payload(b'Mock attachment content')  # Mock content
            encoders.encode_base64(attachment)
            attachment.add_header(
                'Content-Disposition',
                f'attachment; filename= {filename}'
            )
            msg.attach(attachment)
        
        return msg
    
    def validate_email_address(self, email_address):
        """
        Validate email address format.
        Args:
            email_address (str): email address to validate
        Returns:
            bool: True if valid format
        """
        import re
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return bool(re.match(pattern, email_address))
    
    def mock_send_email(self, message, username=None, password=None):
        """
        Mock email sending function (for testing without actual SMTP).
        Args:
            message: email message object
            username (str): SMTP username
            password (str): SMTP password
        Returns:
            dict: sending result
        """
        # Mock successful sending
        return {
            "success": True,
            "message_id": f"mock_id_{datetime.now().timestamp()}",
            "recipient": message['To'],
            "subject": message['Subject'],
            "sent_at": datetime.now().isoformat(),
            "server_used": f"{self.smtp_server}:{self.smtp_port}"
        }
    
    def parse_email_headers(self, message):
        """
        Parse email headers and extract information.
        Args:
            message: email message object
        Returns:
            dict: parsed header information
        """
        headers = {}
        
        # Standard headers
        standard_headers = ['From', 'To', 'Subject', 'Date', 'Message-ID']
        
        for header in standard_headers:
            headers[header.lower()] = message.get(header, 'Not found')
        
        # Additional headers
        headers['content_type'] = message.get_content_type()
        headers['is_multipart'] = message.is_multipart()
        
        return headers

def create_email_template(template_type="welcome"):
    """
    Create email templates for common scenarios.
    Args:
        template_type (str): type of template
    Returns:
        dict: email template
    """
    templates = {
        "welcome": {
            "subject": "Welcome to Our Service!",
            "text_body": "Welcome! Thank you for joining our service.",
            "html_body": "<h1>Welcome!</h1><p>Thank you for joining our service.</p>"
        },
        "notification": {
            "subject": "Important Notification",
            "text_body": "This is an important notification for you.",
            "html_body": "<h2>Important Notification</h2><p>This is an important notification.</p>"
        },
        "newsletter": {
            "subject": "Monthly Newsletter",
            "text_body": "Here's your monthly newsletter with updates.",
            "html_body": "<h1>Monthly Newsletter</h1><p>Updates and news here.</p>"
        }
    }
    
    return templates.get(template_type, templates["welcome"])

def bulk_email_validator(email_list):
    """
    Validate multiple email addresses.
    Args:
        email_list (list): list of email addresses
    Returns:
        dict: validation results
    """
    email_manager = EmailManager()
    
    valid_emails = []
    invalid_emails = []
    
    for email_addr in email_list:
        if email_manager.validate_email_address(email_addr):
            valid_emails.append(email_addr)
        else:
            invalid_emails.append(email_addr)
    
    return {
        "total_emails": len(email_list),
        "valid_emails": valid_emails,
        "invalid_emails": invalid_emails,
        "valid_count": len(valid_emails),
        "invalid_count": len(invalid_emails)
    }

def main():
    """
    Función principal para 090_email_smtp_handling
    """
    print("Email and SMTP Handling Examples:")
    
    # Create email manager
    email_manager = EmailManager()
    
    # Test email validation
    test_emails = ["user@example.com", "invalid-email", "test@domain.org"]
    validation_result = bulk_email_validator(test_emails)
    print(f"Email validation: {validation_result['valid_count']}/{validation_result['total_emails']} valid")
    
    # Create different types of emails
    print("\nCreating emails:")
    
    # Text email
    text_email = email_manager.create_text_email(
        "sender@example.com",
        "recipient@example.com", 
        "Test Subject",
        "This is a test email body."
    )
    print("✅ Text email created")
    
    # HTML email
    html_email = email_manager.create_html_email(
        "sender@example.com",
        "recipient@example.com",
        "HTML Test",
        "<h1>HTML Email</h1><p>This is HTML content.</p>",
        "HTML Email\n\nThis is HTML content."
    )
    print("✅ HTML email created")
    
    # Email with attachment
    attachment_email = email_manager.create_email_with_attachment(
        "sender@example.com",
        "recipient@example.com",
        "Email with Attachment",
        "Please find the attachment.",
        "document.pdf"
    )
    print("✅ Email with attachment created")
    
    # Mock send emails
    print("\nSending emails (mock):")
    for i, msg in enumerate([text_email, html_email, attachment_email], 1):
        result = email_manager.mock_send_email(msg)
        if result["success"]:
            print(f"✅ Email {i} sent successfully")
    
    # Test email templates
    template = create_email_template("welcome")
    print(f"\n📧 Template created: {template['subject']}")
    
    # Parse headers
    headers = email_manager.parse_email_headers(text_email)
    print(f"📋 Email headers parsed: {headers['subject']}")
    
    return True

if __name__ == "__main__":
    result = main()
    print(f"Resultado: {result}")

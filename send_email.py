import smtplib
import click
from email.mime.text import MIMEText

@click.command()
@click.argument('to', type=str)
@click.argument('subject', type=str)
@click.argument('body', type=str)
def send_email(to, subject, body):
    """Send an email."""
    # Email configuration
    # sender_email = 'aimo.woima@gmail.com' 
    sender_email = 'your_email@example.com'  # Update with your email
    password = 'your_password'  # Update with your password

    # Create the email content
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = to

    # Send the email
    try:
        with smtplib.SMTP_SSL('smtp.example.com', 465) as server:  # Update with your SMTP server
            server.login(sender_email, password)
            server.send_message(msg)
        click.echo("Email sent successfully!")
    except Exception as e:
        click.echo(f"Failed to send email: {e}")

if __name__ == '__main__':
    send_email()

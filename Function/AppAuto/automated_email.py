"""
Axio Email Module
-----------------
Secure email sender using SMTP.

Features
--------
• Environment variable credentials
• Automatic SMTP connection cleanup
• Email address validation
• Contact lookup
• Voice feedback
• Error handling
• Type hints
"""

import os
import smtplib
from email.message import EmailMessage
from email.utils import parseaddr

from Arms.Speak import speak
from Arms.Listen import mic


# ==========================
# Configuration
# ==========================

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

# Get your email credentials from environment variable
SENDER_EMAIL = os.getenv("AXIO_EMAIL")
SENDER_PASSWORD = os.getenv("AXIO_EMAIL_PASSWORD")


# ==========================
# Contacts
# ==========================

EMAIL_CONTACTS = {
    "person1": "person1@xyz.com",
    "person2": "person2@xyz.com",
}


# ==========================
# Validation
# ==========================

def validate_email(email: str) -> bool:
    """
    Validate an email address.
    """

    return "@" in parseaddr(email)[1]


# ==========================
# Send Email
# ==========================

def send_email(receiver: str, subject: str, message: str) -> bool:
    """
    Send an email.

    Returns
    -------
    bool
        True if sent successfully.
    """

    if not validate_email(receiver):
        speak("The receiver email address is invalid.")
        return False

    if not SENDER_EMAIL or not SENDER_PASSWORD:
        speak("Email credentials are not configured.")
        return False

    try:

        email = EmailMessage()

        email["From"] = SENDER_EMAIL
        email["To"] = receiver
        email["Subject"] = subject

        email.set_content(message)

        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:

            server.starttls()

            server.login(
                SENDER_EMAIL,
                SENDER_PASSWORD
            )

            server.send_message(email)

        return True

    except smtplib.SMTPAuthenticationError:
        speak("Authentication failed.")
        return False

    except smtplib.SMTPException as error:
        print(error)
        speak("Unable to send the email.")
        return False

    except Exception as error:
        print(error)
        speak("An unexpected error occurred.")
        return False


# ==========================
# Voice Interface
# ==========================

def email_info():
    """
    Collect email information using voice input.
    """

    speak("Who would you like to send an email to?")

    name = mic().lower()

    receiver = EMAIL_CONTACTS.get(name)

    if receiver is None:

        speak("I couldn't find that contact.")

        return

    speak("What is the subject?")

    subject = mic()

    speak("What message should I send?")

    message = mic()

    speak(
        f"Sending email to {name}."
    )

    if send_email(receiver, subject, message):

        speak("Email sent successfully.")

    else:

        speak("Failed to send the email.")

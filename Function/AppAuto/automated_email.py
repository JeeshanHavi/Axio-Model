import smtplib
from Arms.Speak import speak
from email.message import EmailMessage
from Arms.Listen import mic

def send_email(receiver, subject, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    # Make sure to give app access in your Google account
    server.login('youremail@gmail.com', 'Sender_Email_password')
    email = EmailMessage()
    email['From'] = 'Sender_Email'
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)

'''store your email contacts here in the list below
in the format shown. First goes receiver's name and receiver's email
address''' 

email_list = {
    'person1': 'person1@xyz.com',
    'person2': 'person2@xyz.com',
}


def email_info():
    str1 = 'To Whom you want to send email''
    print(str1)
    speak(str1)
    name = input()
    receiver = email_list[name]
    print(receiver)
    speak('What is the subject of your email?')
    subject = input()
    speak('Tell me the text in your email')
    message = input()
    send_email(receiver, subject, message)
    speak('Your email is sent')

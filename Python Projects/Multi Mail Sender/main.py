from email.message import EmailMessage
import ssl
import smtplib

mail = "xxxxxxxxx@gmail.com"
password = "xxxxxx"

GREEN = '\033[92m'
RED = '\033[31m'
RESET = '\033[0m'
mailTo = []

print(f"{GREEN}Welcome To Thaw's Email Sender{RESET}")
print(f"{RED}Enter Subject, Message First. Enter the mail if you don't want to add a mail, enter 'X' and continue!{RESET}")
subject = input(f"{GREEN}Enter Subject : {RESET}")
message = input(f"{GREEN}Enter Message : {RESET}")

while True:
    mail_input = input(f"{GREEN}Mail To (enter 'X' to finish): {RESET}")
    if mail_input.strip().upper() == 'X':
        break
    else:
        emails = mail_input.split(",")
        for email in emails:
            stripped_email = email.strip()
            if stripped_email:
                mailTo.append(stripped_email)

if not mailTo:
    print(f"{RED}No valid email addresses entered. Exiting...{RESET}")
else:
    try:
        email_message = EmailMessage()
        email_message['From'] = mail
        email_message['To'] = ', '.join(mailTo)
        email_message['Subject'] = subject
        email_message.set_content(message)

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(mail, password)
            server.send_message(email_message)

        print(f"{GREEN}Email sent successfully to: {', '.join(mailTo)}{RESET}")
    except Exception as e:
        print(f"{RED}An error occurred: {e}{RESET}")

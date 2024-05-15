from email.message import EmailMessage
import ssl
import smtplib

mail_name = "********@gmail.com"
mail_password = "************"

GREEN = '\033[92m'
RESET = '\033[0m'

print("Welcome To Thaw's Email Sender")
mailTo = input(f"{GREEN}Mail To : {RESET}")
subject = input(f"{GREEN}Enter Subject : {RESET}")
message = input(f"{GREEN}Enter Message : {RESET}")


em  = EmailMessage()
em['From'] = mail_name
em['To'] = mailTo
em['subject'] = subject
em.set_content(message)

context = ssl.create_default_context()


with smtplib.SMTP_SSL("smtp.gmail.com",465,context=context) as server:
    server.login(mail_name,mail_password)
    server.send_message(em)
    print(f"{GREEN}Email Sent Success{RESET}")
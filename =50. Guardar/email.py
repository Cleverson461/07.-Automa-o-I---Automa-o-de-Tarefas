from email.message import EmailMessage
import smtplib
import ssl

password = open('senha', 'r').read()
print(password)
from_email = 'cursodepythonguardarmaterial@gmail.com'
to_email = 'cursodepythonguardarmaterial@gmail.com'
subject = 'Curso Python'

body = '''
A melhor forma de prever o futuro é criá-lo
Aprendendo a Linguagem Python.
'''

# 1 - Estruturando a mensagem via e-mail
message = EmailMessage()
message['From'] = from_email
message['To'] = to_email
message['Subject'] = subject

message.set_content(body)
safe = ssl.create_default_context()

# 2 - Envio de e-mail
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=safe) as smtp:
    smtp.login(from_email, password)
    smtp.sendmail(
        from_email,
        to_email,
        message.as_string()
    )

# from email.message import EmailMessage

# # Criar uma nova mensagem de e-mail
# msg = EmailMessage()
# msg['Subject'] = "Curso Python"
# msg['From'] = "cursodepythonguardarmaterial@gmail.com"
# msg['To'] = "cursodepythonguardarmaterial@gmail.com"
# msg.set_content("A melhor forma de prever o futuri é criá-lo, Aprendendo a Linguagem Python")

# # Exibir o conteúdo do e-mail
# print(msg)


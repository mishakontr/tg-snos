import smtplib
from email.mime.text import MIMEText
from message import message
from messages import messages
#uyjdeqfzrqkqipgd

print("Единственный разработчик: @fratess")
print("Исходный код: @bogoslavniy")
print("Примечание. Открой instruction.txt")
input("Нажми Enter для продолжения...") 

def send_email(subject, message, sender, recipients, password, num_emails):
    for i in range(1, num_emails + 1):
        msg = MIMEText(message)
        msg['Subject'] = subject
        msg['From'] = sender
        msg['To'] = ', '.join(recipients)
        with smtplib.SMTP_SSL('smtp.gmail.com') as smtp_server:
            smtp_server.login(sender, password)
            smtp_server.sendmail(sender, recipients, msg.as_string())
        print(f'Круг {num_round}: отправлено сообщений {i}')

subject = input('Введи тему сообщения: ')
user = input('Введи юзер: ')
link = input('Введи ссылку на сообщения: ')
sender = input('Введи gmail почту с которой хотите отправить сообщение: ')
password = input('Введи пароль от вашей почты: ')
recipients = ["dmca@telegram.org", "recover@telegram.org", "abuse@telegram.orgssss"]
num_rounds = int(input('Введи кол-во кругов: '))
num_emails_per_round = int(input('Введи кол-во сообщений за 1 круг (макс. 100): '))

for num_round in range(1, num_rounds + 1):
    print(f'Начат круг {num_round}')
    result = message + user + messages + link
    send_email(subject, result, sender, recipients, password, num_emails_per_round)

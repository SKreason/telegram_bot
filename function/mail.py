import configparser

import smtplib

from email.mime.text import MIMEText

from email.header    import Header

from email.mime.multipart import MIMEMultipart

from email.utils import formatdate

from text.zoo_text import text_subject


#Конфигурация для отправки сообщения по почте
config = configparser.ConfigParser()
config.add_section('Settings')
config.read('config/config.ini')
bot_mail = config['Settings']['bot_mail']
password_mail = config['Settings']['password_mail']
address_employee = config.get('Settings', 'address_employee')
server = config.get('Settings', 'server_adr')


#Отправка сообщения по почте
async def send_mail(info):
    msg = MIMEMultipart()
    msg['From'] = bot_mail
    msg['To'] = address_employee
    msg['Subject'] = Header(text_subject, 'utf-8')
    msg["Date"] = formatdate(localtime=True)
    msg.attach(MIMEText(info, 'html', 'utf-8'))
    smtp = smtplib.SMTP(server, 25)
    smtp.starttls()
    smtp.ehlo()
    smtp.login(bot_mail, password_mail)
    smtp.sendmail(bot_mail, address_employee, msg.as_string())
    smtp.quit()

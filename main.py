import smtplib
from urllib.request import urlopen

import request
import sys
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import socket
import requests as requests
import requests

response = requests.get('https://api.collectapi.com/health/dutyPharmacy?ilce=%C3%87ankaya&il=Ankara', headers={'Authorization': 'apikey 6MWK3Amkt3GjrKo8xqdjuZ:0ZuvWmd2ejiz8bcGA67COW'})

factor=response.text

mail = smtplib.SMTP("smtp.gmail.com",587)
mail.ehlo()
mail.starttls()

# gmail kullanıcı adımı ve şifremi giriyorum.
mail.login("kullanıcı_adı", "password")

message=MIMEMultipart()

message["From"]="********@gmail.com"  # gönderen kişi

message["To"]="**********@gmail.com"  #alıcı

message["Subject"]="api"

body= factor
body_text=MIMEText(body,"plain")
message.attach(body_text)

mail.sendmail(message["From"],message["To"],message.as_string())

print("mail başarılı bir şekilde gönderildi")
print(response.status_code)
mail.close()

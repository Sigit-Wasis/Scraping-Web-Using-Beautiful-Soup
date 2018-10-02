import requests 
from bs4 import BeautifulSoup
import scrapper
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

url = "http://lpse.bnn.go.id"

soup = scrapper.get(url)
find_title = soup.find('title').text
title = find_title.split(":")
tags = soup.find_all('a')

href = []

for t in tags:

    if "pemenang" in t.text.lower():
		href.append(url + "".join(t.attrs['href']))
    else:
        False

if len(href) > 0 :
    fromaddr = "sigitghoticmetal2001@gmail.com" # email pengirim
    toaddr = "sigitwasisqodr2018@gmail.com" # email tujuan
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = title[0] 
    
    for link in href:
    	body = link+"\n"
    	msg.attach(MIMEText(body, 'plain'))
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, "123jajalo") # password pengirim
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()

else:

    False

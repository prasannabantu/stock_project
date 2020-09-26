import bs4
import requests
from bs4 import BeautifulSoup
import time
import smtplib, ssl
smtp_server = "smtp.gmail.com"
sender_email = "sairohith.guntupally1@gmail.com"
receiver_email = "sairohith.guntupally1@gmail.com"
password = "trashfound404"
i=1
def parsePrice():
  r= requests.get('https://finance.yahoo.com/quote/BCH-USD/')
  soup = BeautifulSoup(r.text,'lxml')
  price=soup.find_all('div',{'class':'D(ib) Va(m) Maw(65%) Ov(h)'})[0].find('span').text
  price=float(price)
  return price
while True:
  time.sleep(10)
  price=parsePrice()
  print(price)
  if price >= 306 and i==1:
    print("sell  ",i)
    i=0
    port = 587  # For starttls
    message="price above 306 sell stock"
    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
      server.ehlo()  # Can be omitted
      server.starttls(context=context)
      server.ehlo()  # Can be omitted
      server.login(sender_email, password)
      server.sendmail(sender_email, receiver_email, message)

  if price <= 294 and i==0:
    print("buy  ",i)
    i=1
    port = 587  # For starttls
    message = "price below 294 buy stock"
    print("buy")
    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
      server.ehlo()  # Can be omitted
      server.starttls(context=context)
      server.ehlo()  # Can be omitted
      server.login(sender_email, password)
      server.sendmail(sender_email, receiver_email, message)

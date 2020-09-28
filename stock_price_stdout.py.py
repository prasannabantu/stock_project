# All the necessary libraries
import bs4  
import requests
from bs4 import BeautifulSoup #web scrapping lib
import time #time lib
import smtplib, ssl #mail transfer lib


# Setting up the server,mail and password connections
smtp_server = "smtp.gmail.com"
sender_email = "sairohith.guntupally1@gmail.com"
receiver_email = "sairohith.guntupally1@gmail.com"
password = "trashfound404"


# Parsing the price details from the website
i=1
def parsePrice():
  r= requests.get('https://finance.yahoo.com/quote/BCH-USD/')
  soup = BeautifulSoup(r.text,'lxml')
  price=soup.find_all('div',{'class':'D(ib) Va(m) Maw(65%) Ov(h)'})[0].find('span').text
  price=float(price)
  return price

# Global variables for the control of time and pricing of messages
smsSleepTime=10
sellingPrice=306
buyingPrice=294


# Function for continuous checking of price variations and deployement of messages
while True:
  time.sleep(smsSleepTime)
  price=parsePrice()
  print(price)
  if price >= sellingPrice and i==1:
    print("sell  ",i)
    i=0
    port = 587  
    message="price above " +sellingPrice+ " sell stock"
    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
      server.ehlo()  # Can be omitted
      server.starttls(context=context)
      server.ehlo()  # Can be omitted
      server.login(sender_email, password)
      server.sendmail(sender_email, receiver_email, message)

  if price <= buyingPrice and i==0:
    print("buy  ",i)
    i=1
    port = 587  # For starttls
    message = "price below "+buyingPrice+" buy stock"
    print("buy")
    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
      server.ehlo()  # Can be omitted
      server.starttls(context=context)
      server.ehlo()  # Can be omitted
      server.login(sender_email, password)
      server.sendmail(sender_email, receiver_email, message)

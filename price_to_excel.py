import bs4  
import requests
from bs4 import BeautifulSoup #web scrapping lib
import time #time lib
def parsePrice():
  r= requests.get('https://finance.yahoo.com/quote/BCH-USD/')
  soup = BeautifulSoup(r.text,'lxml')
  price=soup.find_all('div',{'class':'D(ib) Va(m) Maw(65%) Ov(h)'})[0].find('span').text
  price=float(price)
  return price
while True:
  time.sleep(60)  
  price=parsePrice()
  price1=str(price)
  f=open("StockPrice1.csv","a+")
  f.write(price1+'\n')
  f.close()
  

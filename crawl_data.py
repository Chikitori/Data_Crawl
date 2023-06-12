from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
options = webdriver.EdgeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Edge(options=options) 
names=[]
# area=[]
# floors=[]
# bedrooms=[]
prices=[]
# address=[]
driver.get("https://alonhadat.com.vn/can-ban-nha-ho-chi-minh-t2.htm")

content = driver.page_source
soup = BeautifulSoup(content,features="html.parser")
for a in soup.findAll('div', attrs={'class':'content-item'}):
  name=a.find('a', attrs={'class':'vip'})
  price=a.find('div', attrs={'class':'ct_price'})
  print(name)
  names.append(name.text)
  price.append(price.text)
# ratings.append(rating.text) 

df = pd.DataFrame({'Name': names,'Price':prices}) 
df.to_csv('products.csv', index=False, encoding='utf-8')
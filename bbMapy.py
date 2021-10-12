# Benzín Brno - Mapy.cz - https://bit.ly/3izRnLE

# pip install selenium

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import os


# extract - stahne stranku
def extract(url, Key):
  # selenium - How to bypass the message-“your connection is not private” on non-secure page using Selenium? - https://is.gd/7NDpuF
  options = webdriver.ChromeOptions()
  options.add_argument('--ignore-ssl-errors=yes')
  options.add_argument('--ignore-certificate-errors')
  driver = webdriver.Chrome('d:/Utils/chromedriver/chromedriver.exe', options=options)

  # Load the HTML page
  driver.get(url)
  # Parse processed webpage with BeautifulSoup
  soup = BeautifulSoup(driver.page_source, features="lxml")
  item = soup.find(itemprop="price").get_text()
  # 34,40 Kč => 34.40
  item = item.replace(" Kč", "")
  item = item.replace(",", ".")
  # item
  item = float(item)
  # print("item:", item, '|| type:', type(item))
  # Cena
  Cena = '{:.2f}'.format(item)
  # print("Cena:", Cena, '|| type:', type(Cena))
  # Closes the current window
  driver.close()
  return Cena

# globus - vrati cenu za natual - https://www.globus.cz/brno/cerpaci-stanice-a-myci-linka.html
def Mapy(url):
  Key = 'Benzín'
  Cena = extract(url, Key)
  # print('Cena paliva -', Key, '- je:', Cena)
  return Cena

# main
def main():
  url = r'https://bit.ly/3izRnLE'
  print("def Mapy(r'https://bit.ly/3izRnLE'): ", Mapy(url))
  print('OkDone.')

# name__
if __name__ == '__main__':
  main()

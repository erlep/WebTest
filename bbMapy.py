# Benzín Brno - Mapy.cz - https://bit.ly/3izRnLE
# Pro JavaScript pouziva: selenium <-> playwright
from bbCFG import *
from bbGetPage import GetPage
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

# extract - stahne stranku
def extract(url, Key):
  page_source = GetPage(url)
  # Parse processed webpage with BeautifulSoup
  soup = BeautifulSoup(page_source, features="lxml")
  item = soup.find(itemprop="price").get_text()
  # 34,40 Kč => 34.40
  item = item.replace(" Kč", "")
  item = item.replace(",", ".")
  # item
  item = float(item)
  # print("item:", item, '|| type:', type(item))
  # Cena
  # Cena = bbCenaMsk.format(item)
  Cena = item
  # print("Cena:", Cena, '|| type:', type(Cena))
  # Closes the current window
  return Cena

# test function
def tMappy(url=''):
  bbprint('tMappy:', 'url', url)
  if bbProduct and (url != bbNoUrl):
    return Mappy(url)
  else:
    return 39.9
  # s = '39.9' + '   url: ' + url
  # return s

# globus - vrati cenu za natual - https://www.globus.cz/brno/cerpaci-stanice-a-myci-linka.html
def Mappy(url):
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

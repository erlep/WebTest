# Benzín Brno - Globus - Natural- https://www.globus.cz/brno/cerpaci-stanice-a-myci-linka.html
import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from unicodedata import normalize

# extract - stahne stranku
def extract(url, Key):
  headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'}
  r = requests.get(url, headers)
  # r.content
# BeautifulSoup - ted nepotrebuji neni JavaScript
  # soup = BeautifulSoup(r.content, 'html.parser')

  # pd najde tabulky
  table = pd.read_html(r.content)
  # print(f'Total tables: {len(table)}')

  # tabulek je 6, zajima me c. 2.
  df = table[1]  # pandas.core.frame.DataFrame
  # adding column name to the respective columns - https://bit.ly/3oxfuhN
  df.columns = ['Name', 'smazat', 'Cena']
  # smazani sloupce - https://bit.ly/3oBNYjk
  del df['smazat']
  # Cena zmena typu na float - https://bit.ly/3Bi79SL
  df['Cena'] = df['Cena'].astype('float64')
  # Prepocitani df tj. / 100
  df['Cena'] = (df['Cena'] / 100)
  # How to add a trailing zeros to a pandas dataframe column? - https://bit.ly/3D5zwUO
  df['Cena'] = df['Cena'].map('{:.2f}'.format)
  # LookUp - nalezeni hodnoty Key - https://bit.ly/3DuT59p
  Radek = df.loc[df['Name'] == Key]
  # How to get a value from a Pandas DataFrame and not the index and object type - https://bit.ly/3BhmuDc
  Cena = Radek['Cena'].values[0]
  return Cena

# globus - vrati cenu za natual - https://www.globus.cz/brno/cerpaci-stanice-a-myci-linka.html
def Globus():
  url = r'https://www.globus.cz/brno/cerpaci-stanice-a-myci-linka.html'
  Key = 'Drive 95'
  Cena = extract(url, Key)
  # print('Cena paliva -', Key, '- je:', Cena)
  return Cena

# main
def main():
  print('def Globus(): ', Globus())
  print('OkDone.')

# name__
if __name__ == '__main__':
  main()

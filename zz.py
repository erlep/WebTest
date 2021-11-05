# Benzín Brno - bbSaveXls.py - vypise ceny jednotlivych benzinek
# Ulozi ceny benzinek do Xls souboru
from bbCFG import *
from bbLST import *
from bbTankONO import *
from bbMapy import *
from bbGlobus import *
from bbMakro import *
from bbmBenzin import *
from bbCena import *

import pandas as pd
import time

def SaveXls(Dump=False):
  """ Ulozi ceny benzinu do Xls

  Args:
      Dump: Vypisuj ceny
  """
  # Benzinky
  # Hlavicka tabulky - ['Název', 'Cena', 'Old Cena', 'Delta Cena', 'Old Datum', 'Url']
  df = pd.read_excel(bbXlsFlNm, sheet_name=bbXlsShNm)
  print(df)
  # Pandas select specific cell
  hNazev = bbHLAVICKA[0]  # 'Název'
  hCena = bbHLAVICKA[1]  # 'Cena'
  rGlobus = bbBenzinky[2][0]  # 'Globus                 '

  # Sloupec  Cena
  cGlobus = df[[hCena]]

  # Sloupce Nazev a Cena
  cGlobus = df[[hNazev, hCena]]

  # Radek Globus
  cGlobus = df[df[hNazev] == rGlobus]

  # Cena Globus
  cGlobus = df.loc[df[hNazev] == rGlobus, hCena]

  # Cena Globus - pomoci indexu
  cGlobus = df.iloc[2, 1]

  print('>>', rGlobus, '<<', cGlobus)

  return None

# main
def main():
  print()
  print("SaveXls():    ", SaveXls())
  print('OkDone.')

# __name__
if __name__ == '__main__':
  main()

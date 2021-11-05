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
  # Xls file
  dfXls = pd.read_excel(bbXlsFlNm, sheet_name=bbXlsShNm)
  # print(dfXls)

  # Benzinky
  # Hlavicka tabulky - ['Název', 'Cena', 'Old Cena', 'Delta Cena', 'Old Datum', 'Url']
  df = pd.DataFrame(columns=bbHLAVICKA)
  # pole benzinek: Nazev, Fce, Url
  for i, n in enumerate(bbBenzinky):
    # Zjisti cenu
    s = n[3]  # Url
    Cena = eval(n[1])  # nazev promenne v promenne
    bbprint('  su tu n[1]:', n[1], 'Cena', Cena)
    # Nazev: cena
    bbprint('#', i, ': Nazev:', n[0], ' Fce:', n[1], ' Cena:', Cena, ' 2:', n[2], ' Url:', n[3])
    # Udaje Old, Cena - 2. sloupec
    OldCena = dfXls.iloc[i, bbHlavCena]
    OldDelt = dfXls.iloc[i, bbHlavDlta]
    OldDate = dfXls.iloc[i, bbHlavDate]
    # zmena ceny string
    zc = ''
    # Je Zmena Ceny
    if Cena != OldCena:
      # Zmena ceny
      OldDelt = F2f(Cena - OldCena)
      OldDate = time.strftime(bbDateMsk)
      zc = ' ' + str(float(OldDelt)) + ' Cena:' + str(float(Cena)) + ' Old:' + str(float(OldCena)) + ' ' + str(OldDate) + ' - zmena ceny '
      #  Vypis zmenu kdyz neni dump
      print(n[0], ':', Cena, zc) if not(Dump) else None
      # import time - strftime - https://bit.ly/3Edt2np
    else:
      OldCena = dfXls.iloc[i, bbHlavOldC]

    # DataSet
    df.loc[i] = [n[0], Cena, OldCena, OldDelt, OldDate, n[3]]
    # Vypisuj?
    if Dump:
      # Zjisti cenu
      print(n[0], ':', Cena, zc)
  # Save Xls
  # print('df', type(df))
  # df.style.set_precision(2).background_gradient().hide_index().to_excel('styled.xlsx', engine='openpyxl')
  df.to_excel(bbXlsFlNm, index=False, sheet_name=bbXlsShNm)
  return None

# main
def main():
  print()
  print("SaveXls():    ", SaveXls())
  print('OkDone.')

# __name__
if __name__ == '__main__':
  main()

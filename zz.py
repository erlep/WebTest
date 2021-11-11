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
  """
# Benzinky
  # Now date
  NowDate = ' - Staus On: ' + str(time.strftime(bbDateMsk))
  EmpDate = ''
  # Hlavicka tabulky - ['Název', 'Cena', 'Old Cena', 'Delta Cena', 'Old Datum', 'Url']
  Hlava = bbHLAVICKA[:]
  Hlava[bbHlavaUrl] = Hlava[bbHlavaUrl] + NowDate
  print('NowDate', NowDate, type(NowDate))
  print('EmpDate', NowDate, type(NowDate))
  print('bbHLAVICKA', bbHLAVICKA, type(bbHLAVICKA))
  print('Hlava', Hlava, type(Hlava))

  a = [1, 2, 3]
  b = [4]
  a = a + b
  print(a)

  return None

# main
def main():
  print()
  print("SaveXls():    ", SaveXls())
  print('OkDone.')

# __name__
if __name__ == '__main__':
  main()

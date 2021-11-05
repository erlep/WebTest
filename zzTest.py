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
  OldDate = time.strftime(bbDateMsk)
  print(Dump, type(Dump))
  print(OldDate, type(OldDate))
  zc = 'pokus'
  print(zc) if not(Dump) else None
  return None

# main
def main():
  print()
  print("SaveXls():    ", SaveXls(True))
  print("SaveXls():    ", SaveXls())
  print()
  print('Nazvy benzinek')
  print((list(zip(*bbBenzinky)))[0])
  print()
  print('OkDone.')

# __name__
if __name__ == '__main__':
  main()

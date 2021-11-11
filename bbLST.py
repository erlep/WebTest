# Benzín Brno - bbLST.py - LIST tj. seznam benzinek
# v2 - pokus

from bbCFG import *
from bbCena import *
# neVirtual zeber v - vbbTankONO bbTankONO
from vbbTankONO import *
from vbbMapy import *
from vbbGlobus import *
from vbbMakro import *
from vbbmBenzin import *

# s - budouci promenna url
s = bbNoUrl  # '--url--'

# Hlavicka tabulky - 'Název', 'Cena', 'Url'
bbHLAVICKA = ['Název', 'Cena', 'Old Cena', 'Delta Cena', 'Old Datum', 'Url']
bbHlavNazv = 0  # pozice 'Název' v bbHlavicka
bbHlavCena = 1  # pozice 'Cena' v bbHlavicka
bbHlavOldC = 2  # pozice 'Old Cena' v bbHlavicka
bbHlavDlta = 3  # pozice 'Delta Cena' v bbHlavicka
bbHlavDate = 4  # pozice 'Old Datum' v bbHlavicka
bbHlavaUrl = 5  # pozice 'Url' v bbHlavicka

# Konfigurace benzinek - Nazev, Fce, Url
bbBenzinky = [
    ['TankONO                ', 'tF(tTankO(s))', tF(tTankO(s)), r'http://www.tank-ono.cz/cz/index.php?page=cenik'],
    ['Tesco - Mapy           ', 'tF(tMappy(s))', tF(tMappy(s)), r'https://bit.ly/3izRnLE'],
    ['Globus                 ', 'tF(tGlobu(s))', tF(tGlobu(s)), r'https://www.globus.cz/brno/cerpaci-stanice-a-myci-linka.html'],
    ['Makro                  ', 'tF(tMakro(s))', tF(tMakro(s)), r'https://www.makro.cz/prodejny/brno'],
    ['Shell Olomoucká - Mapy ', 'tF(tMappy(s))', tF(tMappy(s)), r'https://mapy.cz/s/megolelafe'],
    ['MOL Olomoucká - Mapy   ', 'tF(tMappy(s))', tF(tMappy(s)), r'https://mapy.cz/s/kepegubeve'],
    ['Benzina Albert Modřice ', 'tF(tmBenz(s))', tF(tmBenz(s)), r'https://bit.ly/3ltfpd1'],
    ['OMV IKEA - Mapy        ', 'tF(tMappy(s))', tF(tMappy(s)), r'https://mapy.cz/s/jatejehoda'],
    ['EuroOil Opuštěná-Mapy  ', 'tF(tMappy(s))', tF(tMappy(s)), r'https://mapy.cz/s/cutobofugo'],
]

# main
def main():
  print("bbTtest:    ", bbTtest)
  print("bbRender:   ", bbRender)
  bbFce = tF(tTankO(s))
  print("bbFce:    ", bbFce)
  print('Nazvy benzinek')
  print((list(zip(*bbBenzinky)))[0])
  print()
  print('OkDone.')

# name__
if __name__ == '__main__':
  main()

# Benzín Brno - TankONO - Natural "95" - pumpa: 'ČS Brno-Hviezdoslavova' - http://www.tank-ono.cz/cz/index.php?page=cenik
# v2 - pokus
from bbCFG import *

# test function
def tTankO(url=''):
  bbprint('tTankO:', 'url', url)
  return 19.9

# main
def main():
  print('def TankO(): ', tTankO('zz'))
  print('OkDone.')

# name__
if __name__ == '__main__':
  main()

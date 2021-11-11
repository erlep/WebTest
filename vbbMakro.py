# Benzín Brno - Makro - "Natural 95" - https://www.makro.cz/prodejny/brno
from bbCFG import *

# test function
def tMakro(url=''):
  bbprint('tMakro:', 'url', url)
  return 29.9

# main
def main():
  print('def Makro(): ', tMakro())
  print('OkDone.')

# name__
if __name__ == '__main__':
  main()

# Benzín Brno - Globus - Natural- https://www.globus.cz/brno/cerpaci-stanice-a-myci-linka.html
from bbCFG import *

# test function
def tGlobu(url=''):
  bbprint('tGlobu:', 'url', url)
  return 29.9


# main
def main():
  print('def Globu(): ', tGlobu())
  print('OkDone.')

# name__
if __name__ == '__main__':
  main()

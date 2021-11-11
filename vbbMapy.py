# Benzín Brno - Mapy.cz - https://bit.ly/3izRnLE
# Pro JavaScript pouziva: selenium <-> playwright
from bbCFG import *

# test function
def tMappy(url=''):
  bbprint('tMappy:', 'url', url)
  return 39.9

# main
def main():
  url = r'https://bit.ly/3izRnLE'
  print("def Mapy(r'https://bit.ly/3izRnLE'): ", tMappy(url))
  print('OkDone.')

# name__
if __name__ == '__main__':
  main()

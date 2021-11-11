# Benzín Brno - mBenzin.cz - https://www.mbenzin.cz/Nejlevnejsi-benzin/brno
# Benzina Albert Modřice - https://bit.ly/3ltfpd1
from bbCFG import *

# test function
def tmBenz(url=''):
  bbprint('tmBenz:', 'url', url)
  return bbNmVR

# main
def main():
  url = r'https://bit.ly/3ltfpd1'
  print("mBenzin Benzina Albert Modřice - https://bit.ly/3ltfpd1:", tmBenz(url))
  print('OkDone.')

# name__
if __name__ == '__main__':
  main()

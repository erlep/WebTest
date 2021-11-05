# Benzín Brno - bbCFG.py - config file
#  BenzinBrno v0.00 - Natural 95 prices in Brno - Python Version
import inspect

# Globalni promenne
bbNmBB = 'BenzinBrno '
bbNmVR = 0.083
bbNmVE = 'v' + str(bbNmVR)
bbNmDE = ' - Natural 95 prices in Brno - Python Version'
bbName = 'BenzinBrno v0.00 - Natural 95 prices in Brno - Python Version'
bbName = bbNmBB + bbNmVE + bbNmDE
bbNadpis = 'Ceny Benzínu v Brně:'
bbTtest = r'C:\peg\z1drv\OneDrive\aaEgp_P2E2\1Drv\qqq_Prj\ppBB\bbCFG.py'
bbRender = 'requests_html'  # selenium | playwright | requests_html
bbXlsFlNm = 'bbCeny.xlsx'  # nazev xls souboru
bbXlsShNm = bbNmBB.strip()  # strip = trim
bbNoUrl = '--url--'

# Configurace App
bbProduct = True  # True / False  - ostra / ladici verze
bbNoBBprn = True  # True / False  - ladeni tj. vypisovani dodatecnych informaci  ano / ne
bbCenaNoF = True  # True / False  - NEformatovat cenu real na string: # 34.4  => 34,40 Kč
# import time - strftime - https://bit.ly/3Edt2np
bbDateMsk = "%Y/%m/%d %H:%M"  # format casu - time.strftime("%Y/%m/%e %H:%M:%S")
bbDateDMY = "%d.%m.%Y %H:%M"  # format casu - time.strftime("%Y/%m/%e %H:%M:%S")

# Formatovani Ceny (float) - Cena = '{:.2f}'.format(item)
bbCenaMsk = '{:.2f}'  # format na 2 desetinna mista

# bbPrintDebug
# bbPrintDebug('Loc:', 'FceName','Var', Var )
def bbprint(s1='', s2='', s3='', s4='', s5='', s6='', s7='', s8='', s9='', s10='', s11='', s12='',):
  if not(bbNoBBprn):
    # akt fce
    # print(inspect.stack()[0][0].f_code.co_name)
    # predchozi funkce - stack[1]
    s0 = inspect.stack()[1][0].f_code.co_name + '/' + inspect.stack()[2][0].f_code.co_name + ': '
    print(s0, s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12)

# main
def main():
  print("bbTtest:    ", bbTtest)
  print("bbRender:    ", bbRender)
  print("bbName:      ", bbName)
  print("bbNmNM:      ", bbXlsShNm)
  bbprint(' bbPrintDebug Test', 'je OK')
  print('OkDone.')

# name__
if __name__ == '__main__':
  main()

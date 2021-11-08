# Benzín Brno - hlavni soubor
# Pro JavaScript pouziva: selenium <-> playwright

# Soubory
# Tento file: bb__.py
# Chk Log:    DoChk.Log
# Notes:      Notes.Txt

from bbCFG import *
from bbLST import *
from bbLog import *
from bbSaveXls import SaveXls
import bbDoChk

# Check
bbDoChk

# # Benzinky zjisti ceny a uloz do Xls
# SaveXls(True)
# print('OkDone.')

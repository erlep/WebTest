# Benzín Brno - bbDoChk.py - Kontrola cen na benzinkach
# Pro JavaScript pouziva: selenium <-> playwright
from bbCFG import *
from bbLST import *
from bbSaveXls import SaveXls
# CFG
print()
print(bbName)
# Benzinky zjisti ceny a uloz do Xls
SaveXls(True)
# Nahod web

# Done
print('OkDone.')

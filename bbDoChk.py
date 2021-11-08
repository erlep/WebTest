# Benzín Brno - bbDoChk.py - Kontrola cen na benzinkach
# Pro JavaScript pouziva: selenium <-> playwright

from bbCFG import *
from bbLST import *
from bbLog import *
from bbSaveXls import SaveXls

# Open
LogOpen()
# Tiulek
print(bbName)
# Benzinky zjisti ceny a uloz do Xls
SaveXls(True)
# Close
LogClose()
# Done
print('OkDone.')

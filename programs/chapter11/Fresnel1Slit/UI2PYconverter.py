# -*- coding: utf-8 -*-
# PyQt5 uic module convert ui file (XML code) into py file (Python code)'''
import sys
if __name__ == '__main__':
    try:
        # Use PyQt5 if present
        from PyQt5.QtCore import QT_VERSION_STR
        print("Qt version:", QT_VERSION_STR)
    except:
        # Else, use PyQt4
        from PyQt4.QtCore import QT_VERSION_STR
        print("Qt version:", QT_VERSION_STR)
if "PyQt5" in sys.modules:
    from PyQt5 import uic
elif "PyQt4" in sys.modules:
    from PyQt4 import uic
else:
    raise SystemError("PyQt4 or PyQt5 need to be installed first")

import glob
for fname in glob.glob("*.ui"):
    print("converting", fname)
    fin = open(fname, 'r')
    fout = open(fname.replace(".ui", ".py"), 'w')
    uic.compileUi(fin, fout, execute=False)
    fin.close()
    fout.close()

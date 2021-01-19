# -*- coding: utf-8 -*-
''' PyQt5 uic module convert ui file (XML code) into py file (Python code)'''

from PyQt5 import uic
fin = open('UiMainApp.ui', 'r')
fout = open('UiMainApp2.py', 'w')
uic.compileUi(fin, fout, execute=True)
fin.close()
fout.close()

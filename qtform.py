import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import *




app = QtWidgets.QApplication(sys.argv)
window = uic.loadUi("form.ui")
window.setFixedSize(994,712)

window.show()
app.exec_()
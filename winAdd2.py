import sys
from PyQt5 import QtWidgets, uic

app = QtWidgets.QApplication(sys.argv)

def sum():
    num1 = float(window.num1Text.text())
    num2 = float(window.num2Text.text())
    ans = num1 + num2
    window.resultLabel.setText("Sum = " + str(ans))

window = uic.loadUi("mainwin.ui")

window.btnAdd.clicked.connect(sum)
window.addMenu.triggered.connect(sum)

window.show()
app.exec()
import sys
from PyQt5 import QtWidgets, uic

class Win(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("mainwin.ui",self)
        self.ui.setStyleSheet("background-color: rgb(255,35,255)")
        self.ui.btnAdd.clicked.connect(self.sum)
        self.ui.addMenu.triggered.connect(self.sum)

    def sum(self):
        num1 = float(self.ui.num1Text.text())
        num2 = float(self.ui.num2Text.text())
        ans = num1 + num2
        self.ui.resultLabel.setText("Total = " + str(ans))

app = QtWidgets.QApplication(sys.argv)
w = Win()
w.show()
app.exec_()
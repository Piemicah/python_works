import sys
from PyQt5 import QtWidgets, uic

class Win(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setMouseTracking(True)
        self.ui = uic.loadUi("pointDemo.ui",self)
        

    def mouseMoveEvent(self,e):
        x = e.x()
        y= e.y()
        text = "x  : " + str(x) + "\n y : " + str(y)
        self.ui.displayLabel.setText(text)



app = QtWidgets.QApplication(sys.argv)
w = Win()
w.show()
app.exec_()
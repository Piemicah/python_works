import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from mymain import Ui_MainWindow

class MyAdd(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btnAdd.clicked.connect(self.sum)
       

    def sum(self):
        num1 = float(self.ui.num1Text.text())
        num2 = float(self.ui.num2Text.text())
        ans = num1 + num2
        self.ui.resultLabel.setText('Sum = ' + str(ans))


app = QApplication(sys.argv)
w = MyAdd()
w.show()
sys.exit(app.exec_())
   
    
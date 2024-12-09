import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from winAddUic import Win

class Add(QMainWindow):
    def __init__(self):
        super().__init__()
        self.window = Win()
       

        


app = QApplication(sys.argv)
w = Add()
#w.show()
app.exec_()
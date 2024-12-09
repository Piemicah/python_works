import sys
from PyQt5.QtWidgets import QApplication, QWidget,QLabel, QMainWindow

class Win(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100,100,400,500)
        self.setWindowTitle("Baba Titi")
        label = QLabel(self)
        label.move(200,250)
        label.setText("Hello")
        self.show()

app = QApplication(sys.argv)
w = Win()
sys.exit(app.exec_())
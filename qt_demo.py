from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton
import sys


class Win(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(200, 200, 400, 300)
        btn = QPushButton("Click me")
        self.setCentralWidget(btn)


app = QApplication(sys.argv)

window = Win()
window.show()

if __name__ == "__main__":
    app.exec()

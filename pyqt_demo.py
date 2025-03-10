from PyQt6.QtWidgets import (
    QMainWindow,
    QApplication,
    QPushButton,
    QLabel,
    QLineEdit,
    QHBoxLayout,
    QVBoxLayout,
    QWidget,
    QGridLayout,
    QMessageBox,
    QFileDialog,
)
import sys
from pyqt_demo_style import style

app = QApplication([])
# app.setStyleSheet(style)


class MyWin(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Window")
        label1 = QLabel("Enter number1")
        self.textField1 = QLineEdit()
        layout1 = QHBoxLayout()
        layout1.addWidget(label1)
        layout1.addWidget(self.textField1)

        label2 = QLabel("Enter number2")
        self.textField2 = QLineEdit()
        layout2 = QHBoxLayout()
        layout2.addWidget(label2)
        layout2.addWidget(self.textField2)

        self.btn = QPushButton("Click Me")

        layout3 = QVBoxLayout()
        layout3.addLayout(layout1)
        layout3.addLayout(layout2)

        self.header_label = QLabel("GUI DEMO")
        self.header_label.setObjectName("hlabel")

        mainGrid = QGridLayout()
        mainGrid.addWidget(self.header_label, 0, 2)
        mainGrid.addLayout(layout3, 1, 1, 2, 3)
        mainGrid.addWidget(self.btn, 3, 2)
        # layout3.addWidget(self.btn)

        container = QWidget()
        container.setLayout(mainGrid)
        container.setContentsMargins(80, 0, 80, 20)
        container.setStyleSheet(style)

        self.setCentralWidget(container)
        self.btn.clicked.connect(self.btn_handler)
        self.setFixedSize(400, 200)

    def btn_handler(self):
        # d = QMessageBox.warning(self, "afff", "hello to the world")
        f = QFileDialog.getExistingDirectoryUrl(
            self, "gggg"
        ).path()  # (self, "select Directory")

        print("Clicked!")
        print("dir=", f.lstrip("/"))


win = MyWin()

win.show()

app.exec()

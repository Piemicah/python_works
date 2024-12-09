import sys
from PyQt5 import QtWidgets, uic

app = QtWidgets.QApplication(sys.argv)

def message():
    name = "name"
    if window.radio1.isChecked()==True:
        name = "King Messi"
    elif window.radio2.isChecked()==True:
        name = "King Ronaldo"
    else:
        name = "King Henry"

    window.label.setText("You selected " + name)


window = uic.loadUi("radioDemo.ui")

window.radio1.toggled.connect(message)
window.radio2.toggled.connect(message)
window.radio3.toggled.connect(message)

window.show()
app.exec()
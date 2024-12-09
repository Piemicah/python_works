import joblib
import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import *


model = joblib.load('hotel.joblib')

def reviewHandler():

    while window.reviewField.text()=="":
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Error")
        msg.setText("Can't process empty review")
        msg.exec_()
        return
    sentiment = window.reviewField.text()
    result = str(model.predict([sentiment]))
    result = result.replace(']','')
    result = result.replace('[','')
    result = result.replace("'",'')
    
    window.resultLabel.setText("This is a "+result.upper()+" review")


app = QtWidgets.QApplication(sys.argv)
window = uic.loadUi("hotel.ui")
window.setFixedSize(994,712)
window.btnStatus.clicked.connect(reviewHandler)

window.show()
app.exec_()
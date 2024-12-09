import joblib
import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import *

model = joblib.load('liver_predictor.joblib')


def predict(a):
    r=model.predict(a)
    if r[0]==1: return 'Have Liver Problem'
    else: return 'No Liver Problem'


def predictHandler():
    tb=window.tbField.text()
    db=window.dbField.text()
    alkphos=window.alkphosField.text()
    sgpt=window.sgptField.text()
    sgot=window.sgotField.text()
    protein=window.proteinField.text()
    albumin=window.albuminField.text()
    ratio=window.ratioField.text()
    try:
        p=predict([[tb,db,alkphos,sgpt,sgot,protein,albumin,ratio]])
        result=window.resultLabel.setText(p)
    except:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText("Wrong value has been entered")
        msg.setWindowTitle("Error")
        msg.exec_()



def aboutHandler():
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Information)
    msg.setWindowTitle("Liver Disease Prediction")
    msg.setText("Piemicah Institutes. nuges1.62@gmail.com")
    msg.exec_()


app = QtWidgets.QApplication(sys.argv)
window = uic.loadUi("liver.ui")
window.setFixedSize(820,650)
window.btnPredict.clicked.connect(predictHandler)
window.actionAbout.triggered.connect(aboutHandler)

window.show()
app.exec_()
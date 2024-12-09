import joblib
import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import *

model = joblib.load('diabetes_predictor.joblib')

def predict(a):
    r=model.predict(a)
    if r[0]==1: return 'Diabetic'
    else: return 'Non Diabetic'

def predictHandler():
    preg=window.pregEdit.text()
    glu=window.glucoseEdit.text()
    blood=window.bloodEdit.text()
    skin=window.skinEdit.text()
    pfunc=window.pfuncEdit.text()
    bmi=window.bmiEdit.text()
    insulin=window.insulinEdit.text()
    age=window.ageEdit.text()
    try:
        p=predict([[preg,glu,blood,skin,insulin,bmi,pfunc,age]])
        result=window.resultLabel.setText(p)
    except:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText("Wrong value has been entered")
        msg.setWindowTitle("Error")
        msg.exec_()

app = QtWidgets.QApplication(sys.argv)
window = uic.loadUi("diabetes.ui")
window.setFixedSize(820,650)
window.btnPredict.clicked.connect(predictHandler)

window.show()
app.exec_()
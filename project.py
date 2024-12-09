import joblib
import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import *

interest = 0
study = 0
family = 0
social = 0
model = joblib.load('student.joblib')
def predictHandler():
    interest = window.interestCombo.currentIndex()
    study = window.studyCombo.currentIndex()
    family = window.familyCombo.currentIndex()
    social = window.socialCombo.currentIndex()
    result = str(model.predict([[interest,study,family,social]]))
    result = result.replace(']','')
    result = result.replace('[','')
    result = result.replace("'",'')
    window.resultLabel.setText(result)

def aboutHandler():
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Information)
    msg.setWindowTitle("Student Performance Prediction")
    msg.setText("Piemicah Institutes. nuges1.62@gmail.com")
    msg.exec_()


app = QtWidgets.QApplication(sys.argv)
window = uic.loadUi("project.ui")
window.setFixedSize(800,600)
window.btnPredict.clicked.connect(predictHandler)
window.actionAbout.triggered.connect(aboutHandler)

window.show()
app.exec_()
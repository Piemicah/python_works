import sys
from PyQt6 import QtWidgets, uic
from PyQt6.QtCore import Qt
import requests, json
from datetime import datetime, timezone
import uuid


baseUrl = "http://127.0.0.1:8000"
headers = {"content-type": "application/json"}
# from PyQt6.QtWidgets import *


def addKey(key):
    url = f"{baseUrl}/api/add/"
    payload = {"activation_key": key}
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    data = json.loads(response.content.decode("utf-8"))
    return data


def generate_key():
    n = window.keyNumEdit.text()
    if not n.isdigit() or n == None:
        m = QtWidgets.QMessageBox()
        m.setWindowTitle("Input Error")
        m.setText("Numeric digits only")
        m.exec()
        return
    n = int(n)
    with open("activation_keys.txt", "a") as f:
        f.write(60 * "#" + "\n")
        for i in range(n):
            key = str(uuid.uuid4())
            addKey(key)
            f.write(f"{key}\n")

    msg = QtWidgets.QMessageBox()
    msg.setWindowTitle("Activation Key")
    msg.setText(f"{n} keys generated successfully")
    msg.exec()


app = QtWidgets.QApplication(sys.argv)
window = uic.loadUi("keygen.ui")
window.setFixedSize(679, 483)
window.btnGenerate.clicked.connect(generate_key)


window.show()
app.exec()

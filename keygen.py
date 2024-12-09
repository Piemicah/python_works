import sys
from PyQt6 import QtWidgets, uic
from PyQt6.QtCore import Qt
import requests, json
from datetime import datetime, timezone
import uuid

headers = {"content-type": "application/json"}
# from PyQt6.QtWidgets import *


def addKey(key):
    url = "http://127.0.0.1:5000/api/add"
    payload = {"key": key}
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    data = json.loads(response.content.decode("utf-8"))
    return data


def generate_key():
    n = int(window.keyNumEdit.text())
    with open("activation_keys.txt", "a") as f:
        for i in range(n):
            key = str(uuid.uuid4())
            addKey(key)
            f.write(f"({i+1}): {key}\n")

    msg = QtWidgets.QMessageBox()
    msg.setWindowTitle("Activation Key")
    msg.setText(f"{n} keys generated successfully")
    msg.exec()


app = QtWidgets.QApplication(sys.argv)
window = uic.loadUi("keygen.ui")
window.setFixedSize(700, 500)
window.btnGenerate.clicked.connect(generate_key)


window.show()
app.exec()

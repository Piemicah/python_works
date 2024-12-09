import sys, sqlite3
from PyQt5 import QtWidgets, uic
from PyQt5.QtGui import QIntValidator


class DataBase:
    def __init__(self):
        self.sql = ""
        self.conn = sqlite3.connect("colors.db")
        self.cur = self.conn.cursor()

    def selectAll(self):
        self.sql = "select * from kolors order by colorName"
        self.cur.execute(self.sql)
        return self.cur.fetchall()

    def selectSingle(self,name):
        self.sql = "select * from kolors where colorName='"+name+"'"
        self.cur.execute(self.sql)
        row=self.cur.fetchone()
        return row

    def insert(self,name,red,green,blue):
        self.sql = "insert into kolors values('"+ name + "','" + str(red) +"','"+str(green)+"','"+str(blue)+"')"
        self.cur.execute(self.sql)
        self.conn.commit()
        
    def delete(self,name):
        self.sql = "delete from kolors where colorName='"+name+"'"
        self.cur.execute(self.sql)
        self.conn.commit()


    def disconnect(self):
        self.conn.close()

    
        


class Win(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.red = 0
        self.green = 0
        self.blue = 0
        self.ui = uic.loadUi("colorManager.ui",self)
        self.ui.colorFrame.setStyleSheet("background-color: rgb(0,0,0)")
        self.setTextValue()
        self.setUi()
        self.loadColor()
        
        

    def textEvent(self):
        red = int(self.ui.redText.text())
        green = int(self.ui.greenText.text())
        blue = int(self.ui.blueText.text())
        self.ui.redSlider.setValue(red)
        self.ui.greenSlider.setValue(green)
        self.ui.blueSlider.setValue(blue)
        hexValue = self.ui.hexText.text()
        hexv = [hexValue[i:i+2] for i in range(0, len(hexValue),2)]

        self.ui.redSlider.setValue(int(hexv[0],16))
        self.ui.greenSlider.setValue(int(hexv[1],16))
        self.ui.blueSlider.setValue(int(hexv[2],16))


    def sliderEvent(self):
        self.red = self.ui.redSlider.value()
        self.green = self.ui.greenSlider.value()
        self.blue = self.ui.blueSlider.value()
        self.setTextValue()
        self.setColor()

    def setUi(self):
        self.ui.redSlider.valueChanged.connect(self.sliderEvent)
        self.ui.greenSlider.valueChanged.connect(self.sliderEvent)
        self.ui.blueSlider.valueChanged.connect(self.sliderEvent)
        self.ui.redText.editingFinished.connect(self.textEvent)
        self.ui.greenText.editingFinished.connect(self.textEvent)
        self.ui.blueText.editingFinished.connect(self.textEvent)
        self.ui.hexText.editingFinished.connect(self.textEvent)
        self.ui.redText.setValidator(QIntValidator(self).setRange(0,255))
        self.ui.greenText.setValidator(QIntValidator(self).setRange(0,255))
        self.ui.blueText.setValidator(QIntValidator(self).setRange(0,255))
        self.ui.hexText.setInputMask("HHHHHH")
        self.ui.colorCombo.currentIndexChanged.connect(self.selectColor)
        self.ui.btnSave.clicked.connect(self.save)
        self.ui.btnDelete.clicked.connect(self.remove)
        

    
    def save(self):
        name,ok = QtWidgets.QInputDialog.getText(self, "Save Color","Enter Color name:")
        if ok:
            db = DataBase()
            db.insert(name,self.red,self.green,self.blue)
        else:
            return
        self.loadColor()

    def remove(self):
        name = self.ui.colorCombo.currentText()
        db = DataBase()
        db.delete(name)
        self.loadColor()

    def setTextValue(self):
        self.ui.redText.setText(str(self.red))
        self.ui.greenText.setText(str(self.green))
        self.ui.blueText.setText(str(self.blue))
        hred =hex(self.red).replace("0x","")
        hgreen =hex(self.green).replace("0x","")
        hblue =hex(self.blue).replace("0x","")
        if len(hred)==1:
            hred="0"+hred
        if len(hgreen)==1:
            hgreen="0"+hgreen
        if len(hblue)==1:
            hblue="0"+hblue
        hexValue = hred+hgreen+hblue
        self.ui.hexText.setText(hexValue)

    def setColor(self):
        color = "background-color: rgb("+str(self.red)+","+str(self.green)+","+str(self.blue)+")"
        self.ui.colorFrame.setStyleSheet(color)
     
    def loadColor(self):
        db = DataBase()
        self.ui.colorCombo.clear()
        for row in db.selectAll():
                self.ui.colorCombo.addItem(row[0])
        
        db.disconnect()
    def selectColor(self):
        name = self.ui.colorCombo.currentText()
        db = DataBase()
        row = db.selectSingle(name)
        if row is not None:
            self.ui.redSlider.setValue(row[1])
            self.ui.greenSlider.setValue(row[2])
            self.ui.blueSlider.setValue(row[3])
            db.disconnect()
        else:
            pass
        


app = QtWidgets.QApplication(sys.argv)
w = Win()
w.show()
app.exec_()
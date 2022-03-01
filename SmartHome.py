from pickle import TRUE
import random
from PyQt5 import QtCore, QtGui, QtWidgets
#prozor w->BOOL jedinica nula jedinica otvaranje jako brzo se mijenja
#       l-> Ako je mračna govori 1 da se pali svijetlo
#       T->temp (float)
#       t->temp(bool grijalica)
#       H->Float za vlagu
#       h->(bool) pali humidifier
import serial
import time
arduino = serial.Serial(port='COM8', baudrate=9600, timeout=.1)
start=0
svijetlo=False
#čitanje iz arduina
def write_read():
    data = arduino.readline()
    return data
from random import random
class Ui_MainWindow(object):
    #pripremanje prozora i etiketiranje prozora
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 1, 1, 1)
        self.Grijanjestatus = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.Grijanjestatus.setObjectName("Grijanjestatus")
        self.gridLayout.addWidget(self.Grijanjestatus, 3, 1, 1, 1)
        self.odvlazivacstatus = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.odvlazivacstatus.setObjectName("odvlazivacstatus")
        self.gridLayout.addWidget(self.odvlazivacstatus, 5, 1, 1, 1)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tempLbl = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tempLbl.setFont(font)
        self.tempLbl.setObjectName("tempLbl")
        self.gridLayout.addWidget(self.tempLbl, 2, 0, 1, 1)
        self.TemperaturaTB = QtWidgets.QTextBrowser(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.TemperaturaTB.setFont(font)
        self.TemperaturaTB.setObjectName("TemperaturaTB")
        self.gridLayout.addWidget(self.TemperaturaTB, 3, 0, 1, 1)

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 4, 0, 1, 1)
        self.vlagaTB = QtWidgets.QTextBrowser(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.vlagaTB.setFont(font)
        self.vlagaTB.setObjectName("vlagaTB")
        self.gridLayout.addWidget(self.vlagaTB, 5, 0, 1, 1)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 7, 1, 1, 1)
        self.vratastatus = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.vratastatus.setObjectName("vratastatus")
        self.gridLayout.addWidget(self.vratastatus, 1, 1, 1, 1)
        self.svijetlostatus = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.svijetlostatus.setObjectName("svijetlostatus")
        self.gridLayout.addWidget(self.svijetlostatus, 8, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 4, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 7, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    #
    def change(self):
        print()
        start=0
        global svijetlo
        vrata=False
        value = write_read() # printing the value
        if value:
            if(chr(value[1])=='w'and chr(value[2])=='1'):
                vrata=True
                start=time.time()
            elif(start-time.time()>5):#radi 5 sekundi otvorena vrata nakon što nađe jednom promjenu u barometru
                vrata=False
            if(chr(value[4])=='l'and chr(value[5])=='1'):#ako dobim l1 onda svijetlo je uključeno
                svijetlo=False
            elif(chr(value[4])=='l'and chr(value[5])=='0'):
                svijetlo=True
        if(vrata==True):
            self.vratastatus.setPlainText("Otvorena")
        else:
            self.vratastatus.setPlainText("Zatvorena")
        if(svijetlo):
            self.svijetlostatus.setPlainText("upaljen")
        else:
            self.svijetlostatus.setPlainText("Ugašen")
    #pronađemo t i parsamo po njemu znamo da pozicija ta određuje temperaturu i samo pronađemo vlagu preko toga da je njen indeks nakon t
    
        value=str(value)
        temp=value.find('T')
        temperature=0
        hum=0
        if temp != -1:
            temperature = value[temp+1:temp+5]
            hum =value[temp+9:temp+13]
            if(value[temp+15]):# opet ako dobim flag samo upalim odvlaživać
                self.odvlazivacstatus.setPlainText("upaljen")
            else:
                self.odvlazivacstatus.setPlainText("Ugašen")
            if(value[temp+2]):#isto sa grijačem
                self.Grijanjestatus.setPlainText("upaljen")
            else:
                self.Grijanjestatus.setPlainText("Ugašen")

            print(self.blu(50))
        if(hum):
            print(self.blu(50))
            self.vlagaTB.setHtml('<p style="color:rgb'+str(self.blu(1/(float(hum)/100*50)))+'";>'+str(hum)+"%</p>"  )
            self.TemperaturaTB.setHtml('<p style="color:rgb'+str(self.rgb(float(temperature)))+'";>'+str(temperature)+"°c</p>"  )
    #računanje plave boje da vise vlage bude vise plavo i manje manje plavo
    def blu(self, value):
        minimum, maximum = float(0), float(100)
        ratio = 2 * (value-minimum) / (maximum - minimum)
        b = int(max(0, 255*(1 - ratio)))
        r = 0
        g = 0
        return r, g, b
    #racunanje boje za temperaturu zeleno idealna crveno topla i plavo hladna
    def rgb(self, value):
        if(value>40):
            value=40
        if(value<0):
            value=0
        minimum, maximum = float(0), float(40)
        ratio = 2 * (value-minimum) / (maximum - minimum)
        b = int(max(0, 255*(1 - ratio)))
        r = int(max(0, 255*(ratio - 1)))
        g = 255 - b - r
        return r, g, b
    def retranslateUi(self, MainWindow):
        #postavljanje HTMLA i stil kako će se gui prikazati
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_4.setText(_translate("MainWindow", "Grijanje"))
        self.label_3.setText(_translate("MainWindow", "Vrata status"))
        self.tempLbl.setText(_translate("MainWindow", "Temp"))
        self.TemperaturaTB.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:30pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p></body></html>"))

        self.label_2.setText(_translate("MainWindow", "Vlaga"))
        self.vlagaTB.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:30pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "Odvlaživać"))
        self.Grijanjestatus.setReadOnly(1)
        self.vratastatus.setReadOnly(1)
        self.svijetlostatus.setReadOnly(1)
        self.odvlazivacstatus.setReadOnly(1)
        self.label_5.setText(_translate("MainWindow", "Svijetlo"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    timer=QtCore.QTimer()
    timer.timeout.connect(ui.change)
    timer.start(1000)
    MainWindow.show()
    sys.exit(app.exec_())

from pickle import TRUE
import random
import threading 
from PyQt5 import QtCore, QtGui, QtWidgets
#prozor w->BOOL jedinica nula jedinica otvaranje jako brzo se mijenja
#       l-> Ako je mračna govori 1 da se pali svijetlo
#       T->temp (float)
#       t->temp(bool grijalica)
#       H->Float za vlagu
#       h->(bool) pali humidifier
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QInputDialog, QLineEdit
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import serial
import time
arduino = serial.Serial(port='COM8', baudrate=9600, timeout=.1)
temparr=[0,0,0,0,0,0,0,0,0,0]
humarr=[0,0,0,0,0,0,0,0,0,0]
svijetlo=False
vrata=False
dtemp=20.0
dvlaga=51.5
dbar=300
dlu=1000
sec=[0,0,0,0,0,0,0,0,0,0]
import timeit
start=0
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
        self.button = QPushButton("promjeni LUX",self.centralwidget)
        self.button.clicked.connect(self.takelu)
        self.button.setToolTip('promjeni LUX')
        self.gridLayout.addWidget(self.button, 10, 1, 1, 1)

        self.gridLayout.addWidget(self.label_4, 2, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.Grijanjestatus = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.Grijanjestatus.setObjectName("Grijanjestatus")

        
        self.gridLayout.addWidget(self.Grijanjestatus, 3, 1, 1, 1)
        self.odvlazivacstatus = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.odvlazivacstatus.setObjectName("odvlazivacstatus")
        self.gridLayout.addWidget(self.odvlazivacstatus, 5, 1, 1, 1)

        self.buttonvl = QPushButton("promjeni vlaga",self.centralwidget)
        self.buttonvl.clicked.connect(self.takevlaga)
        self.buttonvl.setToolTip('promjeni vlaga')
        self.gridLayout.addWidget(self.buttonvl, 6, 1, 1, 1)
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

        self.tg = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tg.setFont(font)
        self.tg.setObjectName("tg")
        self.gridLayout.addWidget(self.tg, 0, 0, 1, 1)

        self.tv = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tv.setFont(font)
        self.tv.setObjectName("tg")
        self.gridLayout.addWidget(self.tg, 6, 0, 1, 1)
        
        self.graft = pg.PlotWidget(self.centralwidget)
        self.graft.setObjectName("graft")
        self.graft.setBackground('w')
        self.gridLayout.addWidget(self.graft, 1, 0, 1, 1)
        self.grafv = pg.PlotWidget(self.centralwidget)
        self.grafv.setBackground('w')
        self.grafv.setObjectName("grafv")
        self.gridLayout.addWidget(self.grafv, 7, 0, 1, 1)


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
        self.vratastatus = QtWidgets.QTextBrowser(self.centralwidget)
        self.vratastatus.setObjectName("vratastatus")
        self.gridLayout.addWidget(self.vratastatus, 1, 1, 1, 1)
        self.svijetlostatus = QtWidgets.QTextBrowser(self.centralwidget)
        self.svijetlostatus.setObjectName("svijetlostatus")
        self.gridLayout.addWidget(self.svijetlostatus, 7, 1, 1, 1)
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
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.buttonbar = QPushButton("promjeni BAR",self.centralwidget)
        self.buttonbar.clicked.connect(self.takebar)
        self.buttonbar.setToolTip('promjeni BAR')
        self.gridLayout.addWidget(self.buttonbar, 2, 1, 1, 1)

        self.buttontemp = QPushButton("promjeni temp",self.centralwidget)
        self.buttontemp.clicked.connect(self.takeinputs)
        self.buttontemp.setToolTip('promjeni temp')
        self.gridLayout.addWidget(self.buttontemp, 4, 1, 1, 1)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def takeinputs(self):
        global dtemp
        d, okPressed = QInputDialog.getDouble(None, "temperatura","Value:", dtemp, 0, 100, -10)
        if okPressed:
            dtemp=d
    def takevlaga(self):
        global dvlaga
        d, okPressed = QInputDialog.getDouble(None, "vlaga","Value:",dvlaga , 0, 100, 10)
        if okPressed:
            dvlaga=d
    def takelu(self):
        global dlu
        d, okPressed = QInputDialog.getDouble(None, "LUX","Value:",dlu , 0, 10000, 10)
        if okPressed:
            dlu=d
    def takebar(self):
        global dbar
        print(dbar)
        d, okPressed = QInputDialog.getDouble(None, "bar","Value:",dbar , 0, 1000, 10)
        if okPressed:
            dbar=d
    def change(self):
        global svijetlo
        global vrata
        global start
        global temparr
        global humarr
        global dtemp
        global dvlaga
        global dlu
        self.svijetlostatus.setHtml(str(svijetlo))
        value = write_read() #pokusaj komunikacije sa arduino
        if value:
            if "B" in str(value):
                bar=find(str(value),"B")
                bara =value[bar+9:bar+13]
                if(float(bara)>dbar):
                    vrata=True
                    start=time.time()
                elif(time.time()-start>3.5):#radi 5 sekundi otvorena vrata nakon što nađe jednom promjenu u barometru
                    vrata=False
                    start=0
            if "L" in str(value):
                ligh=find(str(value),"L")
                lightt =value[ligh+9:ligh+13]
                if(float(ligh)>dlu):
                    svijetlo=True
                else:#radi 5 sekundi otvorena vrata nakon što nađe jednom promjenu u barometru
                    svijetlo=False
                    start=0
        if(vrata==True):
            self.vratastatus.setPlainText("VRATA:Otvorena")
        else:
            self.vratastatus.setPlainText("VRATA:Zatvorena")
        if(svijetlo):
            self.svijetlostatus.setPlainText("SVIJETLO:upaljeno")
        else:
            self.svijetlostatus.setPlainText("SVIJETLO:Ugašeno")

    #pronađemo t i parsamo po njemu znamo da pozicija ta određuje temperaturu i samo pronađemo vlagu preko toga da je njen indeks nakon t
    
        value=str(value)
        temp=value.find('T')
        temperature=0
        hum=0
        if temp != -1:
            temperature = value[temp+1:temp+5]
            hum =value[temp+9:temp+13]
            self.vlagaTB.setHtml('<p style="color:rgb'+str(self.blu(1/(float(hum)/100*50)))+'";>'+str(hum)+"%</p>"  )
            self.TemperaturaTB.setHtml('<p style="color:rgb'+str(self.rgb(float(temperature)))+'";>'+str(temperature)+"°c</p>"  )

            temparr.append(float(temperature))
            humarr.append(float(hum))
            humarr.pop(0)
            temparr.pop(0)
            global sec
            pen = pg.mkPen(self.rgb(float(temperature)))
            sec = sec[1:]  # Remove the first
            sec.append(sec[-1] + 10)  # Add a new random value.
            self.data_line = self.graft.plot(sec, temparr, pen=pen)
            pen1 = pg.mkPen(self.blu(1/(float(hum)/100*50)))
            self.data_line = self.grafv.plot(sec, humarr, pen=pen1)
            if(float(hum)>dvlaga):# opet ako dobim flag samo upalim odvlaživać
                self.odvlazivacstatus.setPlainText("ODVLAŽIVAĆ:upaljen")
            else:
                self.odvlazivacstatus.setPlainText("ODVLAŽIVAĆ:Ugašen")
            if(float(temperature)<dtemp):#isto sa grijačem
                self.Grijanjestatus.setPlainText("GRIJANJE:upaljen")
            else:
                self.Grijanjestatus.setPlainText("GRIJANJE:Ugašen")
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
    #find t in a string and check if the two next characters are larger than given value
    def find_b(self, value, b):
        temp=value.find('B')
        if temp != -1:
            if(int(value[temp+1]+value[temp+2])>b):
                return True
            else:
                return False
    #find L in a string and check if the four next characters are larger than given value
    
    def find_l(self, value, l):
        temp=value.find('L')
        if temp != -1:
            if(int(value[temp+1]+value[temp+2]+value[temp+3]+value[temp+4])>l):
                return True
            else:
                return False
    #find G in a string and check if the 2 next characters are larger than given value
    def find_g(self, value, g):
        temp=value.find('G')
        if temp != -1:
            if(int(value[temp+1]+value[temp+2])>g):
                return True
            else:
                return False
    def retranslateUi(self, MainWindow):

        #postavljanje HTMLA i stil kako će se gui prikazati
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.TemperaturaTB.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:30pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p></body></html>"))

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

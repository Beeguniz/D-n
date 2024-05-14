from PyQt5 import QtGui,QtWidgets,QtCore
import sys
import home, grammar11, grammar12, grammar13, grammar14, exercises,exercises12, exercises13,exercises14

ui = ''
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
def homeUi():
    global ui
    ui = home.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.b_topic11.clicked.connect(grammar11Ui)
    ui.b_topic12.clicked.connect(grammar12Ui)
    ui.b_topic13.clicked.connect(grammar13Ui)
    ui.b_topic14.clicked.connect(grammar14Ui)
    MainWindow.show()

def grammar11Ui():
    global ui
    ui = grammar11.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.ex11.clicked.connect(exercises11Ui)
    ui.back_home11.clicked.connect(homeUi)
    MainWindow.show()

def grammar12Ui():
    global ui
    ui = grammar12.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.ex12.clicked.connect(exercises12Ui)
    ui.back_home12.clicked.connect(homeUi)
    MainWindow.show()

def grammar13Ui():
    global ui
    ui = grammar13.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.ex13.clicked.connect(exercises13Ui)
    ui.back_home13.clicked.connect(homeUi)
    MainWindow.show()

def grammar14Ui():
    global ui
    ui = grammar14.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.ex14.clicked.connect(exercises14Ui)
    ui.back_home14.clicked.connect(homeUi)
    MainWindow.show()

def exercises11Ui():
    global ui
    ui = exercises.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.back_gr11.clicked.connect(grammar11Ui)
    MainWindow.show()

def exercises12Ui():
    global ui
    ui = exercises12.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.back_gr12.clicked.connect(grammar12Ui)
    MainWindow.show()

def exercises13Ui():
    global ui
    ui = exercises13.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.back_gr13.clicked.connect(grammar13Ui)
    MainWindow.show()

def exercises14Ui():
    global ui
    ui = exercises14.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.back_gr14.clicked.connect(grammar14Ui)
    MainWindow.show()

homeUi()
sys.exit(app.exec())
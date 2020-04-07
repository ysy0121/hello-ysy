import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic
from PyQt5 import QtWidgets, QtWebEngineWidgets

#from_class = uic.loadUiType("UiTest.ui")[0]
from_class = uic.loadUiType("MainWindow.ui")[0]

class WindowClass(QMainWindow, from_class):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        #self.pushButton2.clicked.connect(self.slot2)
        self.btn_new.clicked.connect(self.newWindow)

    def slot1(self):
        #self.label.setText("11111111")
        reply = QMessageBox.question(self,'Messagre','Quit?',QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        #if reply == QMessageBox.Yes:


    def slot2(self):
        self.label.setText("2222222222222")

    def newWindow(self):
        DialogClass(self)


class DialogClass(QDialog):
    def __init__(self, parent):
        super(DialogClass, self).__init__(parent)
        dialog_ui = 'UiDialog.ui'
        uic.loadUi(dialog_ui, self)
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    myWindow = WindowClass()
    myWindow.show()
    app.exec_()

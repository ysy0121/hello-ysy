#-*-coding: utf-8 -*-
import os
import sys
from PyQt5 import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtWidgets

#https://www.crocus.co.kr/927
CWD = str(os.getcwd())+'/python/pyqt'
#print(CWD)

"""
def showMessageBox():
    msgbox = QtWidgets.QMessageBox)
    msgbox.question()
"""

class MyWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.formUI()
        self.buttonUI()
        self.initUI()

    def formUI(self):
        QToolTip.setFont(QFont('SansSerif',12))
        self.setToolTip('<b>F</b>orm basics')
        self.statusBar().showMessage('Ready...')

    def buttonUI(self):
        btn = QPushButton('Quit',self)
        btn.setToolTip('<b>*</b>Click<b>*</b>')

        btn.move(50,50)
        btn.resize(btn.sizeHint())
        btn.clicked.connect(QCoreApplication.instance().quit)
    
    def initUI(self):        
        self.setWindowTitle('My first App')
        self.setWindowIcon(QIcon('/web.png'))
        self.setGeometry(300,300,300,200)
        self.move(300,300)
        self.resize(800,600)
        self.show()


class MyDialog(QDialog):

    def __init__(self):
        super().__init__()



class MyWindow(QMainWindow):
    """ 
        레이아웃 참고
        https://freeprog.tistory.com/326
    """   

    def __init__(self):
        super().__init__()
        self.menuUI()
        self.formUI()
        self.buttonUI()
        self.initUI()

    def showMessageBox(self,title,message):
        msgbox = QtWidgets.QMessageBox(self)
        msgbox.question(self, title, message, QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)

    def menuUI(self):
        exit = QAction(QIcon(CWD+'/exit.png'),'Exit',self)
        exit.setShortcut('Ctrl+Q')
        exit.setStatusTip('Exit Application')
        exit.triggered.connect(QCoreApplication.instance().quit)

        menu = self.menuBar()
        menu.setNativeMenuBar(False)
        menuFile = menu.addMenu('&File')
        menuFile.addAction(exit)

        save = QAction(QIcon(CWD+'/save.png'),'Save',self)
        save.setShortcut('Ctrl+S')
        save.setStatusTip('Save Application')
        save.triggered.connect(lambda: self.showMessageBox('Save','내용을 저장합니다.'))

        self.tool = self.addToolBar('Save')
        self.tool.addAction(save)

        edit = QAction(QIcon(CWD+'/edit.png'),'Edit',self)
        edit.setShortcut('Ctrl+E')
        edit.setStatusTip('Edit Application')
        edit.triggered.connect(lambda: self.showMessageBox('Edit','내용을 수정합니다.'))

        #self.tool = self.addToolBar('Edit')
        self.tool.addAction(edit)

    def formUI(self):        
        QToolTip.setFont(QFont('SansSerif',12))
        self.setToolTip('<b>F</b>orm basics')
        
        #날짜참고: https://wikidocs.net/22074
        date = QDate.currentDate()
        self.statusBar().showMessage('Ready... '+ date.toString(Qt.DefaultLocaleLongDate))

    def buttonUI(self):
        btn = QPushButton('Quit',self)
        btn.setToolTip('<b>*</b>Click<b>*</b>')

        btn.move(50,500)
        btn.resize(btn.sizeHint())
        btn.clicked.connect(QCoreApplication.instance().quit)
    
    def moveCenter(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def initUI(self):        
        self.setWindowTitle('My first App')
        self.setWindowIcon(QIcon(CWD+'/web.png'))
        self.setGeometry(300,300,300,200)
        self.move(300,300)
        self.resize(800,600)
        self.moveCenter()
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWindow()
    sys.exit( app.exec_() )
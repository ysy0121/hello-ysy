# -*- coding:utf-8 -*-
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic
from PyQt5 import QtWidgets
from FindText import Ftext

form = uic.loadUiType("Mainfind.ui")[0]


class WindowFind(QDialog, form):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton2.clicked.connect(self.viewText)

    def viewText(self):
        sword = self.lineEdit2.text()
        if sword != '':
            FT = Ftext();
            sarr = FT.exeCore(sword,'dir')
            txt = '\n'.join(sarr)
            self.plainTextEdit.setPlainText(txt)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    myWin = WindowFind()
    myWin.show()
    app.exec_()

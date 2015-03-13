# -*- coding: utf-8 -*-

from PyQt4 import QtCore
from PyQt4 import QtGui
import sys

class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.initMW()

    def initMW(self):
        self.setWindowTitle(u'Мастер кампании')
        self.show()

app = QtGui.QApplication(sys.argv)
MW = MainWindow()
print "Hey!"
sys.exit(app.exec_())
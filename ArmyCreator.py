# -*- coding: utf-8 -*-
from PyQt4 import QtCore
from PyQt4 import QtGui
import sys

class MainWindow(QtGui.QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.initMW()

    def initMW(self):
        self.setWindowTitle(u'Создание армии')
        self.MainLayout = QtGui.QVBoxLayout()

        self.AddArmyButton = QtGui.QPushButton(u"Создать армию")
        self.AddDivisionButton = QtGui.QPushButton(u"Создать дивизию")
        self.AddUnitButton = QtGui.QPushButton(u"Создать отряд")
        self.AddGeneralButton = QtGui.QPushButton(u"Создать генерала")
        self.DeleteSelectedButton = QtGui.QPushButton(u"Удалить выбранное")
        self.TopHLayout = QtGui.QHBoxLayout()
        self.TopHLayout.addWidget(self.AddArmyButton)
        self.TopHLayout.addWidget(self.AddDivisionButton)
        self.TopHLayout.addWidget(self.AddUnitButton)
        self.TopHLayout.addWidget(self.AddArmyButton)
        self.TopHLayout.addWidget(self.AddGeneralButton)
        self.TopHLayout.addWidget(self.DeleteSelectedButton)
        self.MainLayout.addLayout(self.TopHLayout)

        self.BotHLayout = QtGui.QHBoxLayout()
        self.TreeView = QtGui.QTreeWidget()
        self.BotHLayout.addWidget(self.TreeView)

        self.MainLayout.addLayout(self.BotHLayout)
        self.setLayout(self.MainLayout)
        self.TreeView.setHeaderLabel(u"Армии")


        QtCore.QObject.connect(self.DeleteSelectedButton, QtCore.SIGNAL('clicked()'), self.deleteSelected)
        QtCore.QObject.connect(self.AddArmyButton, QtCore.SIGNAL('clicked()'), self.addArmy)
        QtCore.QObject.connect(self.AddDivisionButton, QtCore.SIGNAL('clicked()'), self.addDivision)
        QtCore.QObject.connect(self.AddUnitButton, QtCore.SIGNAL('clicked()'), self.addUnit)
        QtCore.QObject.connect(self.AddGeneralButton, QtCore.SIGNAL('clicked()'), self.addGeneral)
        self.show()

    def addArmy(self):
        self.ArmyCreateWindow = QtGui.QWidget()
        ArmyCreateWindowLayout = QtGui.QGridLayout()
        self.ArmyCreateWindow.setLayout(ArmyCreateWindowLayout)
        NameLabel = QtGui.QLabel(u"Имя армии")
        self.ArmyCreateWindow.NameText = QtGui.QLineEdit()
        ArmyCreateWindowLayout.addWidget(NameLabel, 0, 0)
        ArmyCreateWindowLayout.addWidget(self.ArmyCreateWindow.NameText, 1, 0)
        GeneralLabel = QtGui.QLabel(u"Командир")
        self.ArmyCreateWindow.GeneralPicker = QtGui.QComboBox()
        ArmyCreateWindowLayout.addWidget(GeneralLabel, 2, 0)
        ArmyCreateWindowLayout.addWidget(self.ArmyCreateWindow.GeneralPicker, 3, 0)

        self.ArmyCreateWindow.FinishButton = QtGui.QPushButton(u'Сохранить армию')
        ArmyCreateWindowLayout.addWidget(self.ArmyCreateWindow.FinishButton, 4, 0)
        self.ArmyCreateWindow.show()

        QtCore.QObject.connect(self.ArmyCreateWindow.FinishButton, QtCore.SIGNAL('clicked()'), self.addArmyFinish)

    def addArmyFinish(self):
        NewItem = QtGui.QTreeWidgetItem()
        NewItem.setText(0, self.ArmyCreateWindow.NameText.text())
        self.TreeView.addTopLevelItem(NewItem)
        self.ArmyCreateWindow.close()

    def addDivision(self):

        self.DivisionCreateWindow = QtGui.QWidget()
        DivisionCreateWindowLayout = QtGui.QGridLayout()
        self.DivisionCreateWindow.setLayout(DivisionCreateWindowLayout)
        NameLabel = QtGui.QLabel(u"Имя дивизии")
        self.DivisionCreateWindow.NameText = QtGui.QLineEdit()
        DivisionCreateWindowLayout.addWidget(NameLabel, 0, 0)
        DivisionCreateWindowLayout.addWidget(self.DivisionCreateWindow.NameText, 1, 0)
        GeneralLabel = QtGui.QLabel(u"Командир")
        self.DivisionCreateWindow.GeneralPicker = QtGui.QComboBox()
        DivisionCreateWindowLayout.addWidget(GeneralLabel, 2, 0)
        DivisionCreateWindowLayout.addWidget(self.DivisionCreateWindow.GeneralPicker, 3, 0)

        self.DivisionCreateWindow.FinishButton = QtGui.QPushButton(u"Сохранить дивизию")
        DivisionCreateWindowLayout.addWidget(self.DivisionCreateWindow.FinishButton, 4, 0)
        self.DivisionCreateWindow.show()
        QtCore.QObject.connect(self.DivisionCreateWindow.FinishButton, QtCore.SIGNAL('clicked()'), self.addDivisionFinish)

        print "Division"

    def addDivisionFinish(self):
        Army = self.TreeView.selectedItems()[0]
        NewDivision = QtGui.QTreeWidgetItem()
        NewDivision.setText(0, self.DivisionCreateWindow.NameText.text())
        Army.addChild(NewDivision)
        self.DivisionCreateWindow.close()

    def addUnit(self):
        print "Unit"

    def addGeneral(self):
        print "General"

    def deleteSelected(self):
        root = self.TreeView.invisibleRootItem()
        for item in self.TreeView.selectedItems():
            (item.parent() or root).removeChild(item)

        #ItemToBeDeleted = self.TreeView.currentItem()
        #self.TreeView.removeItemWidget(ItemToBeDeleted, 0)
        print "here"

    def saveArmies(self):
        pass

    def loadArmies(self):
        pass



app = QtGui.QApplication(sys.argv)
MW = MainWindow()
sys.exit(app.exec_())
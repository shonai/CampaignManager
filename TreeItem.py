from PyQt4 import QtCore
from PyQt4 import QtGui

class ArmyItem(QtGui.QTreeWidgetItem):
    Name = ""
    Id = None
    Divisions = []
    supply = None
    Position = None
    Order = None
    Commander = None
    Owner = ""

class DivisionItem(QtGui.QTreeWidgetItem):
    Army = None
    Name = ""
    Id = None
    Units = []
    Commander = None

class UnitItem(QtGui.QTreeWidgetItem):
    Division = None
    Id = None
    Name = ""
    UnitType = None





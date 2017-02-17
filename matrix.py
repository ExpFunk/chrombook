#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Form implementation generated from reading ui file 'matrix.ui'
# Created by: PyQt4 UI code generator 4.11.4
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sys
sys.path.append("/home/vlad/ChromBook")
import DB_manager

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(QtGui.QWidget):
    
    def __init__(self, database, tableName):
        QtGui.QWidget.__init__(self)
        self.dbu = DB_manager.DatabaseUtility(database, tableName)
        self.setupUi(self)
        self.UpdateTree()
        
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(786, 351)
        self.treeWidget = QtGui.QTreeWidget(Dialog)
        self.treeWidget.setGeometry(QtCore.QRect(400, 40, 371, 301))
        self.treeWidget.setMinimumSize(QtCore.QSize(100, 0))
        self.treeWidget.setObjectName(_fromUtf8("treeWidget"))
        self.treeWidget.headerItem().setTextAlignment(0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter|QtCore.Qt.AlignCenter)
        self.widget = QtGui.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(22, 37, 360, 309))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_2 = QtGui.QLabel(self.widget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_3.addWidget(self.label_2)
        self.lineEdit_2 = QtGui.QLineEdit(self.widget)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.horizontalLayout_3.addWidget(self.lineEdit_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label = QtGui.QLabel(self.widget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_4.addWidget(self.label)
        self.dateTimeEdit = QtGui.QDateTimeEdit(self.widget)
        self.dateTimeEdit.setTime(QtCore.QTime(0, 0, 0))
        self.dateTimeEdit.setMinimumDate(QtCore.QDate(1752, 10, 14))
        self.dateTimeEdit.setMaximumTime(QtCore.QTime(23, 59, 59))
        self.dateTimeEdit.setMinimumTime(QtCore.QTime(0, 0, 0))
        self.dateTimeEdit.setObjectName(_fromUtf8("dateTimeEdit"))
        self.horizontalLayout_4.addWidget(self.dateTimeEdit)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_7 = QtGui.QLabel(self.widget)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout.addWidget(self.label_7)
        self.lineEdit = QtGui.QLineEdit(self.widget)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.horizontalLayout.addWidget(self.lineEdit)
        self.label_8 = QtGui.QLabel(self.widget)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.horizontalLayout.addWidget(self.label_8)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_3 = QtGui.QLabel(self.widget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_2.addWidget(self.label_3)
        self.lineEdit_3 = QtGui.QLineEdit(self.widget)
        self.lineEdit_3.setText(_fromUtf8(""))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.horizontalLayout_2.addWidget(self.lineEdit_3)
        self.label_4 = QtGui.QLabel(self.widget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_2.addWidget(self.label_4)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_5 = QtGui.QLabel(self.widget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_2.addWidget(self.label_5, 2, 0, 1, 1)
        self.comboBox_3 = QtGui.QComboBox(self.widget)
        self.comboBox_3.setObjectName(_fromUtf8("comboBox_3"))
        self.gridLayout_2.addWidget(self.comboBox_3, 3, 0, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_2)
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.label_6 = QtGui.QLabel(self.widget)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_3.addWidget(self.label_6, 0, 0, 1, 1)
        self.lineEdit_4 = QtGui.QLineEdit(self.widget)
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.gridLayout_3.addWidget(self.lineEdit_4, 0, 1, 1, 1)
        self.label_9 = QtGui.QLabel(self.widget)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout_3.addWidget(self.label_9, 0, 2, 1, 1)
        self.label_10 = QtGui.QLabel(self.widget)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout_3.addWidget(self.label_10, 1, 0, 1, 1)
        self.comboBox = QtGui.QComboBox(self.widget)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.gridLayout_3.addWidget(self.comboBox, 1, 1, 1, 2)
        self.label_11 = QtGui.QLabel(self.widget)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.gridLayout_3.addWidget(self.label_11, 1, 3, 1, 1)
        self.comboBox_2 = QtGui.QComboBox(self.widget)
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.gridLayout_3.addWidget(self.comboBox_2, 1, 4, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_3)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.buttonBox = QtGui.QDialogButtonBox(self.widget)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Save)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName(_fromUtf8("saveButton"))
        self.horizontalLayout_5.addWidget(self.buttonBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.treeWidget.headerItem().setText(0, _translate("Dialog", "ID", None))
        self.treeWidget.headerItem().setText(1, _translate("Dialog", "Date", None))
        self.treeWidget.headerItem().setText(2, _translate("Dialog", "Flow Rate", None))
        self.treeWidget.headerItem().setText(3, _translate("Dialog", "New Column", None))
        self.treeWidget.headerItem().setText(4, _translate("Dialog", "Electrolyte", None))
        self.treeWidget.headerItem().setText(5, _translate("Dialog", "New Column", None))
        self.treeWidget.headerItem().setText(6, _translate("Dialog", "Temperature", None))
        self.treeWidget.headerItem().setText(7, _translate("Dialog", "Adsorber", None))
        self.label_2.setText(_translate("Dialog", "Column #", None))
        self.label.setText(_translate("Dialog", "Date", None))
        self.dateTimeEdit.setDisplayFormat(_translate("Dialog", "yyyy/MM/dd hh:mm", None))
        self.label_7.setText(_translate("Dialog", "Flow rate", None))
        self.label_8.setText(_translate("Dialog", "ml/min", None))
        self.label_3.setText(_translate("Dialog", "Wave length", None))
        self.label_4.setText(_translate("Dialog", "nm", None))
        self.label_5.setText(_translate("Dialog", "Electrolyte:", None))
        self.label_6.setText(_translate("Dialog", "Volume", None))
        self.label_9.setText(_translate("Dialog", "ml", None))
        self.label_10.setText(_translate("Dialog", "Temperature", None))
        self.label_11.setText(_translate("Dialog", "Adsorber", None))
        self.comboBox_2.setItemText(0, _translate("Dialog", "P-2", None))
        self.comboBox_2.setItemText(1, _translate("Dialog", "P-4", None))

    @QtCore.pyqtSignature("on_saveButton_clicked()")
    def Save(self):
        text = self.lineEdit.text()
        self.dbu.AddEntryToTable(text)
        self.UpdateTree()

if __name__ == "__main__":
    
    db = 'chrombook'
    tableName = 'chromatograms'
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog(db, tableName)
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())


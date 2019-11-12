# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EditWin.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Tabla(object):
    def setupUi(self, Tabla):
        Tabla.setObjectName("Tabla")
        Tabla.resize(595, 388)
        Tabla.setStyleSheet("background-color: rgb(211, 205, 255);")
        self.btnEdit = QtWidgets.QPushButton(Tabla)
        self.btnEdit.setGeometry(QtCore.QRect(230, 300, 140, 60))
        font = QtGui.QFont()
        font.setFamily("Bitstream Vera Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btnEdit.setFont(font)
        self.btnEdit.setStyleSheet("background-color: qlineargradient(spread:reflect, x1:0, y1:0.882, x2:0.851, y2:0, stop:0 rgba(204, 0, 0, 0), stop:0.273632 rgba(255, 255, 255, 255));\n"
"background-color: rgb(147, 125, 255);\n"
"color: rgb(0, 0, 0);\n"
"border-style: solid;\n"
"border-width:2px;\n"
"border-radius:20px;\n"
"border-color: rgb(0, 0, 0);")
        self.btnEdit.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Imagenes/edit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnEdit.setIcon(icon)
        self.btnEdit.setIconSize(QtCore.QSize(40, 40))
        self.btnEdit.setObjectName("btnEdit")
        self.btnDelete = QtWidgets.QPushButton(Tabla)
        self.btnDelete.setEnabled(True)
        self.btnDelete.setGeometry(QtCore.QRect(400, 300, 140, 60))
        font = QtGui.QFont()
        font.setFamily("Bitstream Vera Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btnDelete.setFont(font)
        self.btnDelete.setStyleSheet("background-color: qlineargradient(spread:reflect, x1:0, y1:0.882, x2:0.851, y2:0, stop:0 rgba(204, 0, 0, 0), stop:0.273632 rgba(255, 255, 255, 255));\n"
"background-color: rgb(255, 40, 40);\n"
"color: rgb(0, 0, 0);\n"
"border-style: solid;\n"
"border-width:2px;\n"
"border-radius:20px;\n"
"border-color: rgb(0, 0, 0);")
        self.btnDelete.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Imagenes/121113.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnDelete.setIcon(icon1)
        self.btnDelete.setIconSize(QtCore.QSize(40, 40))
        self.btnDelete.setAutoDefault(False)
        self.btnDelete.setObjectName("btnDelete")
        self.txtNumber = QtWidgets.QTextEdit(Tabla)
        self.txtNumber.setGeometry(QtCore.QRect(100, 310, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Bitstream Vera Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.txtNumber.setFont(font)
        self.txtNumber.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txtNumber.setObjectName("txtNumber")
        self.label = QtWidgets.QLabel(Tabla)
        self.label.setGeometry(QtCore.QRect(60, 320, 41, 17))
        font = QtGui.QFont()
        font.setFamily("Bitstream Vera Sans")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(0, 0, 0);")
        self.label.setObjectName("label")
        self.txtTable = QtWidgets.QTextEdit(Tabla)
        self.txtTable.setEnabled(True)
        self.txtTable.setGeometry(QtCore.QRect(20, 20, 551, 261))
        self.txtTable.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.txtTable.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.txtTable.setReadOnly(True)
        self.txtTable.setObjectName("txtTable")

        self.retranslateUi(Tabla)
        QtCore.QMetaObject.connectSlotsByName(Tabla)

    def retranslateUi(self, Tabla):
        _translate = QtCore.QCoreApplication.translate
        Tabla.setWindowTitle(_translate("Tabla", "Form"))
        self.label.setText(_translate("Tabla", "No."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Tabla = QtWidgets.QWidget()
    ui = Ui_Tabla()
    ui.setupUi(Tabla)
    Tabla.show()
    sys.exit(app.exec_())

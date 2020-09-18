# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TableWindow.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Tabla(object):
    def setupUi(self, Tabla):
        Tabla.setObjectName("Tabla")
        Tabla.resize(425, 495)
        Tabla.setStyleSheet("background-color: rgb(208, 208, 208);")
        self.centralwidget = QtWidgets.QWidget(Tabla)
        self.centralwidget.setObjectName("centralwidget")
        self.TableTextEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.TableTextEdit.setGeometry(QtCore.QRect(0, 0, 521, 481))
        self.TableTextEdit.setInputMethodHints(QtCore.Qt.ImhMultiLine)
        self.TableTextEdit.setReadOnly(True)
        self.TableTextEdit.setObjectName("TableTextEdit")
        Tabla.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Tabla)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 525, 25))
        self.menubar.setObjectName("menubar")
        Tabla.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Tabla)
        self.statusbar.setObjectName("statusbar")
        Tabla.setStatusBar(self.statusbar)

        self.retranslateUi(Tabla)
        QtCore.QMetaObject.connectSlotsByName(Tabla)

    def retranslateUi(self, Tabla):
        _translate = QtCore.QCoreApplication.translate
        Tabla.setWindowTitle(_translate("Tabla", "MainWindow"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Tabla = QtWidgets.QMainWindow()
    ui = Ui_Tabla()
    ui.setupUi(Tabla)
    Tabla.show()
    sys.exit(app.exec_())


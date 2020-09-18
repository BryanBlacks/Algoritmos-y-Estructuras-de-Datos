# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(505, 495)
        font = QtGui.QFont()
        font.setFamily("Laksaman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color: rgb(208, 208, 208);")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.LoadFile = QtWidgets.QPushButton(self.centralwidget)
        self.LoadFile.setGeometry(QtCore.QRect(60, 410, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(9)
        self.LoadFile.setFont(font)
        self.LoadFile.setStyleSheet("QPushButton{\n"
"        border-radius:50px;\n"
"        border: 4px solid #ff5733 ;\n"
"        font: 75 12pt \"Ubuntu Mono\";\n"
"\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    border-radius:30px;\n"
"    background:#fa7659;\n"
"    font: 75 12pt \"Ubuntu Mono\";\n"
"\n"
"}")
        self.LoadFile.setObjectName("LoadFile")
        self.CreateMap = QtWidgets.QPushButton(self.centralwidget)
        self.CreateMap.setGeometry(QtCore.QRect(270, 350, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(9)
        self.CreateMap.setFont(font)
        self.CreateMap.setStyleSheet("QPushButton{\n"
"        border-radius:50px;\n"
"        border: 4px solid #15a26b ;\n"
"        font: 75 12pt \"Ubuntu Mono\";\n"
"\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    border-radius:30px;\n"
"    background:#3cbb89;\n"
"    font: 75 12pt \"Ubuntu Mono\";\n"
"\n"
"}")
        self.CreateMap.setObjectName("CreateMap")
        self.CreateTable = QtWidgets.QPushButton(self.centralwidget)
        self.CreateTable.setGeometry(QtCore.QRect(60, 350, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(9)
        self.CreateTable.setFont(font)
        self.CreateTable.setStyleSheet("QPushButton{\n"
"        border-radius:50px;\n"
"        border: 4px solid #205b9b ;\n"
"        font: 75 12pt \"Ubuntu Mono\";\n"
"\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    border-radius:30px;\n"
"    background:#3a76b7;\n"
"    font: 75 12pt \"Ubuntu Mono\";\n"
"\n"
"}")
        self.CreateTable.setObjectName("CreateTable")
        self.lblOrigin = QtWidgets.QLabel(self.centralwidget)
        self.lblOrigin.setGeometry(QtCore.QRect(90, 240, 111, 17))
        font = QtGui.QFont()
        font.setFamily("Bitstream Vera Sans Mono")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(9)
        self.lblOrigin.setFont(font)
        self.lblOrigin.setStyleSheet("font: 75 12pt \"Bitstream Vera Sans Mono\";")
        self.lblOrigin.setObjectName("lblOrigin")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(310, 240, 111, 17))
        font = QtGui.QFont()
        font.setFamily("Bitstream Vera Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(9)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("font: 75 12pt \"Bitstream Vera Sans\";")
        self.label_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_2.setObjectName("label_2")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(40, 0, 421, 231))
        self.frame.setStyleSheet("QFrame{\n"
"    background-color:rgba(61,61,61,.5);\n"
"    border-radius:7\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.textEdit = QtWidgets.QTextEdit(self.frame)
        self.textEdit.setGeometry(QtCore.QRect(20, 10, 381, 201))
        self.textEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit.setObjectName("textEdit")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(260, 260, 201, 61))
        self.frame_2.setStyleSheet("QFrame{\n"
"    background-color:rgba(61,61,61,.5);\n"
"    border-radius:5\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.DestinyNode = QtWidgets.QTextEdit(self.frame_2)
        self.DestinyNode.setGeometry(QtCore.QRect(10, 10, 181, 41))
        self.DestinyNode.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.DestinyNode.setObjectName("DestinyNode")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(40, 260, 201, 61))
        self.frame_3.setStyleSheet("QFrame{\n"
"    background-color:rgba(61,61,61,.5);\n"
"    border-radius:5\n"
"}")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.OriginNode = QtWidgets.QTextEdit(self.frame_3)
        self.OriginNode.setGeometry(QtCore.QRect(10, 10, 181, 41))
        self.OriginNode.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.OriginNode.setObjectName("OriginNode")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(270, 410, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Laksaman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet("color: rgb(0, 0, 0);")
        self.comboBox.setObjectName("comboBox")
        self.LoadFile.raise_()
        self.CreateMap.raise_()
        self.CreateTable.raise_()
        self.lblOrigin.raise_()
        self.label_2.raise_()
        self.frame.raise_()
        self.frame_2.raise_()
        self.frame_3.raise_()
        self.OriginNode.raise_()
        self.comboBox.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 565, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.LoadFile.setText(_translate("MainWindow", "Cargar Archivo"))
        self.CreateMap.setText(_translate("MainWindow", "Crear Mapa"))
        self.CreateTable.setText(_translate("MainWindow", "Crear Tabla "))
        self.lblOrigin.setText(_translate("MainWindow", "Nodo Origen"))
        self.label_2.setText(_translate("MainWindow", "Nodo Destino"))
        self.DestinyNode.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.OriginNode.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


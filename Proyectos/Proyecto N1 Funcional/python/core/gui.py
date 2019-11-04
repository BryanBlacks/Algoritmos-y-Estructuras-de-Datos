# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1098, 634)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(1098, 634))
        Form.setMaximumSize(QtCore.QSize(1098, 634))
        Form.setStyleSheet("QMainWindow{\n"
"    background:url(:/images/m.jpg);\n"
"}")
        Form.setIconSize(QtCore.QSize(24, 24))
        Form.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.centralwidget = QtWidgets.QWidget(Form)
        self.centralwidget.setObjectName("centralwidget")
        self.explorer1 = QtWidgets.QListWidget(self.centralwidget)
        self.explorer1.setGeometry(QtCore.QRect(160, 100, 211, 391))
        self.explorer1.setStyleSheet("QListWidget{\n"
"    background:transparent;\n"
"    border-radius:60px;\n"
"    font-size: 13px;\n"
"    \n"
"\n"
"}")
        self.explorer1.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.explorer1.setObjectName("explorer1")
        self.explorer2 = QtWidgets.QListWidget(self.centralwidget)
        self.explorer2.setGeometry(QtCore.QRect(730, 100, 211, 391))
        self.explorer2.setStyleSheet("QListWidget{\n"
"    background:transparent;\n"
"    border-radius:60px;\n"
"    font-size: 13px;\n"
"    \n"
"\n"
"}")
        self.explorer2.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.explorer2.setObjectName("explorer2")
        self.delete1 = QtWidgets.QPushButton(self.centralwidget)
        self.delete1.setGeometry(QtCore.QRect(340, 520, 61, 61))
        self.delete1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.delete1.setStyleSheet("QPushButton{\n"
"        border-radius:30px;\n"
"        border:3px solid red;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    border-radius:30px;\n"
"    background:red;\n"
"    border: 2px;\n"
"    border-color:black;\n"
"}")
        self.delete1.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("core/images/d.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.delete1.setIcon(icon)
        self.delete1.setIconSize(QtCore.QSize(40, 40))
        self.delete1.setObjectName("delete1")
        self.NDir1 = QtWidgets.QPushButton(self.centralwidget)
        self.NDir1.setGeometry(QtCore.QRect(130, 520, 61, 61))
        self.NDir1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.NDir1.setStyleSheet("QPushButton{\n"
"        border-radius:30px;\n"
"        border: 3px solid #b3d6ff;\n"
"\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    border-radius:30px;\n"
"    background:#b3d6ff;\n"
"\n"
"}")
        self.NDir1.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("core/images/af.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.NDir1.setIcon(icon1)
        self.NDir1.setIconSize(QtCore.QSize(40, 40))
        self.NDir1.setObjectName("NDir1")
        self.NFile1 = QtWidgets.QPushButton(self.centralwidget)
        self.NFile1.setGeometry(QtCore.QRect(240, 520, 61, 61))
        self.NFile1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.NFile1.setStyleSheet("QPushButton{\n"
"        border-radius:30px;\n"
"        border:3px solid #c97418;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    border-radius:30px;\n"
"    background:#c97418;\n"
"    border: 2px;\n"
"    border-color:black;\n"
"}")
        self.NFile1.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("core/images/afi.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.NFile1.setIcon(icon2)
        self.NFile1.setIconSize(QtCore.QSize(60, 60))
        self.NFile1.setObjectName("NFile1")
        self.NFile2 = QtWidgets.QPushButton(self.centralwidget)
        self.NFile2.setGeometry(QtCore.QRect(810, 520, 61, 61))
        self.NFile2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.NFile2.setMouseTracking(False)
        self.NFile2.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.NFile2.setStatusTip("")
        self.NFile2.setWhatsThis("")
        self.NFile2.setAccessibleDescription("")
        self.NFile2.setAutoFillBackground(False)
        self.NFile2.setStyleSheet("QPushButton{\n"
"        border-radius:30px;\n"
"        border:3px solid #c97418;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    border-radius:30px;\n"
"    background:#c97418;\n"
"    border: 2px;\n"
"    border-color:black;\n"
"}")
        self.NFile2.setText("")
        self.NFile2.setIcon(icon2)
        self.NFile2.setIconSize(QtCore.QSize(60, 60))
        self.NFile2.setObjectName("NFile2")
        self.NDir2 = QtWidgets.QPushButton(self.centralwidget)
        self.NDir2.setGeometry(QtCore.QRect(700, 520, 61, 61))
        self.NDir2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.NDir2.setStyleSheet("QPushButton{\n"
"        border-radius:30px;\n"
"        border: 3px solid #b3d6ff;\n"
"\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    border-radius:30px;\n"
"    background:#b3d6ff;\n"
"\n"
"}")
        self.NDir2.setText("")
        self.NDir2.setIcon(icon1)
        self.NDir2.setIconSize(QtCore.QSize(40, 40))
        self.NDir2.setObjectName("NDir2")
        self.delete2 = QtWidgets.QPushButton(self.centralwidget)
        self.delete2.setGeometry(QtCore.QRect(910, 520, 61, 61))
        self.delete2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.delete2.setStyleSheet("QPushButton{\n"
"        border-radius:30px;\n"
"        border:3px solid red;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    border-radius:30px;\n"
"    background:red;\n"
"    border: 2px;\n"
"    border-color:black;\n"
"}")
        self.delete2.setText("")
        self.delete2.setIcon(icon)
        self.delete2.setIconSize(QtCore.QSize(40, 40))
        self.delete2.setObjectName("delete2")
        self.RightToLeft = QtWidgets.QPushButton(self.centralwidget)
        self.RightToLeft.setGeometry(QtCore.QRect(500, 310, 91, 71))
        self.RightToLeft.setStyleSheet("QPushButton\n"
"{\n"
"    border:3px solid #b3d6ff;\n"
"    border-radius:30px\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    border-radius:30px;\n"
"    background:white;\n"
"}")
        self.RightToLeft.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("core/images/left.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.RightToLeft.setIcon(icon3)
        self.RightToLeft.setIconSize(QtCore.QSize(100, 100))
        self.RightToLeft.setObjectName("RightToLeft")
        self.LeftToRight = QtWidgets.QPushButton(self.centralwidget)
        self.LeftToRight.setGeometry(QtCore.QRect(500, 230, 91, 71))
        self.LeftToRight.setStyleSheet("QPushButton\n"
"{\n"
"    border:3px solid #b3d6ff;\n"
"    border-radius:30px\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"    border-radius:30px;\n"
"    background:white;\n"
"}")
        self.LeftToRight.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("core/images/right.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.LeftToRight.setIcon(icon4)
        self.LeftToRight.setIconSize(QtCore.QSize(100, 100))
        self.LeftToRight.setObjectName("LeftToRight")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(180, 40, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(20)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel\n"
"{\n"
"    color: black;\n"
"}")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(760, 40, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(20)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("QLabel\n"
"{\n"
"    color: black;\n"
"}")
        self.label_2.setObjectName("label_2")
        self.backist1 = QtWidgets.QFrame(self.centralwidget)
        self.backist1.setGeometry(QtCore.QRect(129, 79, 271, 431))
        self.backist1.setStyleSheet("QFrame{\n"
"    background-color:rgba(61,61,61,.5);\n"
"    border-radius:60px;\n"
"}")
        self.backist1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.backist1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.backist1.setObjectName("backist1")
        self.backist2 = QtWidgets.QFrame(self.centralwidget)
        self.backist2.setGeometry(QtCore.QRect(700, 80, 271, 431))
        self.backist2.setStyleSheet("QFrame{\n"
"    background-color:rgba(61,61,61,.5);\n"
"    border-radius:60px;\n"
"}")
        self.backist2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.backist2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.backist2.setObjectName("backist2")
        self.backist2.raise_()
        self.backist1.raise_()
        self.explorer1.raise_()
        self.explorer2.raise_()
        self.delete1.raise_()
        self.NDir1.raise_()
        self.NFile1.raise_()
        self.NFile2.raise_()
        self.NDir2.raise_()
        self.delete2.raise_()
        self.RightToLeft.raise_()
        self.LeftToRight.raise_()
        self.label.raise_()
        self.label_2.raise_()
        Form.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Form)
        self.statusbar.setObjectName("statusbar")
        Form.setStatusBar(self.statusbar)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "MainWindow"))
        self.delete1.setToolTip(_translate("Form", "Delete"))
        self.NDir1.setToolTip(_translate("Form", "Add Folder"))
        self.NFile1.setToolTip(_translate("Form", "Add File"))
        self.NFile2.setToolTip(_translate("Form", "Add File"))
        self.NDir2.setToolTip(_translate("Form", "Add Folder"))
        self.delete2.setToolTip(_translate("Form", "Delete"))
        self.RightToLeft.setToolTip(_translate("Form", "Copy to the left"))
        self.LeftToRight.setToolTip(_translate("Form", "Copy to the right"))
        self.label.setText(_translate("Form", "Directory #1"))
        self.label_2.setText(_translate("Form", "Directory #2"))

from core import images_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QMainWindow()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())


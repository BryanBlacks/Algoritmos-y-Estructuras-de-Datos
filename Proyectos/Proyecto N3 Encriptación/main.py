# *-* coding: utf-8 -*-
import sys

from proyectoAED import *
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from FileDialog import *
from encriptar_archivos import *
from desencriptar_archivos import *
from encriptar_directorio import * 
from desencriptar_directorio import *
from Crypto import Random
from Crypto.Cipher import AES
import os
import time
import os.path
from os import listdir
from os.path import isfile, join


class MainWindow(QtGui.QMainWindow):

	key = b'[EX\xc8\xd5\xbfI{\xa2$\x05(\xd5\x18\xbf\xc0\x85)\x10nc\x94\x02)j\xdf\xcb\xc4\x94\x9d(\x9e'
	def __init__(self, parent=None):
		super(MainWindow, self).__init__(parent=parent)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		#texto en lineedit mostrado como contraseña
		self.ui.contrasenia_enc.setEchoMode(QLineEdit.Password)
		self.ui.contrasenia_des.setEchoMode(QLineEdit.Password)
		#conexion de botones mediante señales.
		QtCore.QObject.connect(self.ui.sel_rutaOrigen, QtCore.SIGNAL('clicked()'), self.abrir)
		QtCore.QObject.connect(self.ui.sel_rutaOrigen, QtCore.SIGNAL('clicked()'), self.mostrar_origen)
		QtCore.QObject.connect(self.ui.encriptar, QtCore.SIGNAL('clicked()'), self.encriptacion)
		QtCore.QObject.connect(self.ui.desencriptar, QtCore.SIGNAL('clicked()'), self.desencriptacion)
		QtCore.QObject.connect(self.ui.sel_rutaDestino, QtCore.SIGNAL('clicked()'), self.abrir)
		QtCore.QObject.connect(self.ui.sel_rutaDestino, QtCore.SIGNAL('clicked()'), self.mostrar_destino)
		QtCore.QObject.connect(self.ui.sel_rutaOrigen, QtCore.SIGNAL('clicked()'), self.tree)
		QtCore.QObject.connect(self.ui.aceptar_contrasenia_enc, QtCore.SIGNAL('clicked()'), self.clave_encriptar)
		QtCore.QObject.connect(self.ui.aceptar_contrasenia_des, QtCore.SIGNAL('clicked()'), self.clave_desencriptar)

#funcion para abrir un dialog box que permite seleccionar tanto archivos como directorio.	
	def abrir(self):
		dialog = FileDialog()
		if dialog.exec_() != QtGui.QDialog.Accepted:
			self.nombre_fichero = dialog.filesSelected()

#funcion que muestra el tree view de una ruta de directorio seleccionada.
	def tree(self):
		self.model = QtGui.QFileSystemModel() 
		index = self.model.setRootPath( str(self.nombre_fichero[0]) )
		self.ui.treeView.setModel(self.model)
		self.ui.treeView.setRootIndex(index)

	def clave_encriptar(self):
		self.contra_enc = self.ui.contrasenia_enc.text()
		self.ui.pass_true_false.clear()

	def clave_desencriptar(self):
		self.contra_des = self.ui.contrasenia_des.text()
		#Comprobando que la contraseña sea la misma para poder desencriptar
		if(self.contra_enc == self.contra_des):
			self.ui.pass_true_false.setText("Correcta")
		else:
 			self.ui.pass_true_false.setText("Incorrecta")

	def mostrar_origen(self):
		#uniendo las rutas en el caso que se selecciones varios archivos/directorios.
		self.archivos = ' '.join(self.nombre_fichero)
		self.ui.ver_rutaOrigen.setText(self.archivos)

	def mostrar_destino(self):
		self.archivos1 = ' '.join(self.nombre_fichero)
		self.ui.ver_rutaDestino.setText(self.archivos1)

	def encriptacion(self):
		#Comprobando por medio de cual algoritmo se realizara la encriptacion/desencriptacion
		if(str(self.ui.sel_algoritmo.currentText()) == "AES-256"):
			self.enc = encriptar_archivos()
			self.enc_d = encriptar_directorio(self.key)
			#separando cada ruta para encriptacion
			self.dirs = self.archivos
			self.dirr = self.dirs.split(' ')
			self.val = len(self.dirr)-1
			for j in self.dirr:
				for i in range(0,len(self.dirr)-self.val):
					self.filename = [j]
					#comprobando si es archivo o directorio
					if os.path.isfile(str(self.filename[i])):
						self.enc.encrypt_file(str(self.filename[i]), str(self.archivos1))

					else:		
						self.enc_d.getAllFiles(str(self.archivos))
						self.enc_d.encrypt_all_files(str(self.archivos), str(self.archivos1))
		else:
			print("NO HAY OTRO ALGORITMO DE ENCRIPTACION/DESENCRIPTACION")

	def desencriptacion(self):
		#Comprobando por medio de cual algoritmo se realizara la encriptacion/desencriptacion
		if(str(self.ui.sel_algoritmo.currentText()) == "AES-256"):
			#Comprobando que la contraseña de encriptacion sea la misma
			if(str(self.ui.pass_true_false.text()) == "Correcta"):
				self.ui.label_error.clear()
				self.des = desencriptar_archivos()
				self.des_d = desencriptar_directorio(self.key)
				#separando cada ruta para encriptacion de archivos/directorios
				self.dirs = self.archivos
				self.dirr = self.dirs.split(' ')
				self.val = len(self.dirr)-1
				for j in self.dirr:
					for i in range(0,len(self.dirr)-self.val):
						self.filename = [j]
						#comprobando si es archivo o directorio.
						if os.path.isfile(str(self.filename[i])):
							self.des.decrypt_file(self.filename[i], str(self.archivos1))

						else:
							self.des_d.getAllFiles(str(self.archivos))
							self.des_d.decrypt_all_files(str(self.archivos), str(self.archivos1))
			else:
				self.ui.label_error.setText("Error")

		else:
			print("NO HAY OTRO ALGORITMO DE ENCRIPTACION/DESENCRIPTACION")

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())




 linea += char(15)
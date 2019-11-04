# *-* coding: utf-8 -*-

from Crypto import Random
from Crypto.Cipher import AES
import os
import os.path
from os import listdir
from os.path import isfile, join
from time import time 


class desencriptar_directorio():
    def __init__(self, key):
        self.key = key

    def pad(self, s):
        return s + b"\0" * (AES.block_size - len(s) % AES.block_size)

    def decrypt(self, ciphertext, key):
        iv = ciphertext[:AES.block_size]
        cipher = AES.new(key, AES.MODE_CBC, iv)
        plaintext = cipher.decrypt(ciphertext[AES.block_size:])
        return plaintext.rstrip(b"\0")

    def decrypt_file(self, file_name, ruta):
        self.dirs = file_name
        self.dirr = self.dirs.split(' ')
        self.val = len(self.dirr)-1
        self.tiempo_inicial = time()
        for j in self.dirr:
            for i in range(0,len(self.dirr)-self.val):
                filename = [j]
                dirname = os.path.dirname(filename[i])
                f = open(filename[i], 'rb')
                f.name
                nombre = os.path.basename(f.name)
                if(nombre.endswith('.enc')):
                    nombre_fichero = os.path.join(os.sep, ruta, nombre)
                    if not os.path.exists(dirname):
                        os.makedirs(dirname)    
                    with f as fo:
                        ciphertext = fo.read()
                    dec = self.decrypt(ciphertext, self.key)
                    with open(nombre_fichero[:-4], 'wb') as fo:
                        fo.write(dec)
                    os.remove(filename[i])
                else:
                    pass
        self.tiempo_final = time()    
        #medir tiempo de desencriptacion de directorio                   
        self.tiempo_ejecucion = str(self.tiempo_final - self.tiempo_inicial)    
        #creando archivo.txt que guarda el tiempo de ejecucion.                    
        t = open("log_decrypt_folder.txt", 'w')
        t.write("El tiempo en desencriptar todos los archivos del directorio fue de: "+self.tiempo_ejecucion+ " segundos")
        t.close()   

    def getAllFiles(self,ruta):
        dir_path = ruta
        dirs = []
        for dirName, subdirList, fileList in os.walk(dir_path):
            for fname in fileList:
                if (fname != 'script.py' and fname != 'data.txt.enc'):
                    dirs.append(dirName + "/" + fname)
        return dirs

    def decrypt_all_files(self,file_name, ruta):
        dirs = self.getAllFiles(file_name)
        for file_name in dirs:
            self.decrypt_file(file_name,ruta)

key = b'[EX\xc8\xd5\xbfI{\xa2$\x05(\xd5\x18\xbf\xc0\x85)\x10nc\x94\x02)j\xdf\xcb\xc4\x94\x9d(\x9e'
enc = desencriptar_directorio(key)
clear = lambda: os.system('cls')
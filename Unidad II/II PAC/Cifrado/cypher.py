#-*- coding:utf8 -*-
#Cifrado
cifrado = (chr(ord("a") ^ ord("b")))
print("Cifrado: %s"  % (cifrado))
print("\n")

#Descifrado
descifrado = (chr(ord(cifrado) ^ ord("b")))
print("Descifrado: '%s'" % (descifrado))

phrase = "Hola Mundo"
print("\n")
print ("Plain Text: '%s'" % (phrase))
#encodePhrase = str.encode(phrase)

#Generar arreglo de Binarios con bytearray
print("Array of Plaint text: %s " % (bytearray(phrase)))

pasword = "z"

encrypted = " ".join(
    list(
        map(
            lambda x:chr(
                x ^ ord(pasword)),(bytearray(phrase)
            )
        )
    )
)

print("Cypher text: '%s'" % (encrypted))

decrypted = " ".join(
    list(
        map(
            lambda x:chr(
                x ^ ord(pasword)),(bytearray(encrypted)
            )
        )
    )
)
print("Decrypted text: %s" % (decrypted))

"""
class Encryptor:
    def __init__(self):
        pass

    def encrypt(self,phrase,password):
        return " ".join(
        list(
            map(
                lambda x:chr(
                    x ^ ord(pasword)),(bytearray(phrase)
                    )
                )
            )
        )

    def decrypt(self,encriptedtext,password):
        return self.encrypt(encriptedtext,password)

e = Encryptor()
print(e.encrypt("Hola mundo","buenos dias"))
print(e.decrypt(e.encrypt("hola mundo","buenos dias"),"buenas tardes"))
"""
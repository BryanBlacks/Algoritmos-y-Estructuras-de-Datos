# -*- coding:utf8 -*-

"""
---------------------------------------------------------------------------------------------------------------------
Node (Nodo)
---------------------------------------------------------------------------------------------------------------------

* Esta clase se usará como modelo para almacenar los vértices, y este a su vez guardarán los archivos y carpetas,
  ingresandolas así a la lista enlazada.

---------------------------------------------------------------------------------------------------------------------
"""

class Node:
    def __init__(self,value,date,parent):
        self.value = value
        self.date = date
        self.parent = parent
        self.next = None
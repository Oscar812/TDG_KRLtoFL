import xml.etree.ElementTree as ET
from Classes import ClassList

class DiccionarioKRL:
    Lista = ClassList.ListaNoOrdenada()

    def crearDiccionario(self,Lista):
        actual = Lista.cabeza
        while actual != None:
            if (actual.obtenerParentName() == "Source"):
                print("___________________")
                print(actual.obtenerTipo())
                print(actual.obtenerNombre())
                print (actual.obtenerId())
                #Lista.SetReglas(actual.obtenerId())
            actual = actual.obtenerSiguiente()

    def crearDiccionarioModelo(self,Lista):
        actual = Lista.cabeza
        while actual != None:
            print("___________________")
            print(actual.obtenerTipo())
            print(actual.obtenerNombre())
            print (actual.obtenerId())
            #Lista.SetReglas(actual.obtenerId())
            actual = actual.obtenerSiguiente()
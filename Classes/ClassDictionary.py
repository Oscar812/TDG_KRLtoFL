import xml.etree.ElementTree as ET
from Classes import ClassList

class ElementosXML:
    Lista = ClassList.ListaNoOrdenada()

    def crearRegla(self,Lista,Diccionario):
        actual = Lista.cabeza
        while actual != None:
            if (actual.obtenerTipo() != ""):
                Lista.AgregarRegla(actual.obtenerId())
                Lista.SetReglas(actual.obtenerId())
            actual = actual.obtenerSiguiente()
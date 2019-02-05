import xml.etree.ElementTree as ET
from operator import is_not
from functools import partial
import zlib
import base64
from Classes import ClassList
from Classes import ClassDictionary
import urllib.parse
def urlencode(str):
    return urllib.parse.quote(str)
def urldecode(str):
    return urllib.parse.unquote(str)
def decode_base64_and_inflate( b64string ):
    decoded_data = base64.b64decode( b64string )
    return zlib.decompress( decoded_data , -15)
def deflate_and_base64_encode( string_val ):
    zlibbed_str = zlib.compress( string_val )
    compressed_string = zlibbed_str[2:-4]
    return base64.b64encode( compressed_string )
from Classes import ClassElement as Elements

Lista = ClassList.ListaNoOrdenada()
file = "TRANSFORMACION.xml"
Elementos = Elements.ElementosXML()
Lista= Elementos.ObtenerElementos(file,Lista)
Elementos.AsigConexion(Lista)
Elementos.AsigRegla(Lista)
DicReg = ClassDictionary.ListaDictionary()
DicMod = ClassDictionary.ListaDictionary()
#Lista.Imprimir()
file2 = "Modelo_prueba.xml"
ListaModelo = ClassList.ListaNoOrdenada()
ListaModelo = Elementos.ObtenerElementos(file2,ListaModelo)
Elementos.AsigConexion(ListaModelo)
Elementos.AsigRegla(ListaModelo)
#print("__________Diccionario Modelo_______________")
#Diccionario.crearDiccionarioModelo(ListaModelo)
#print("__________Modelo_______________")
#ListaModelo.Imprimir()
print("__________Diccionario Reglas_______________")
DicReg=Elementos.LLenarDic(Lista,"Regla")
#Elementos.LLenarDic(Lista,"Regla")
DicReg= Elementos.asignarEtiqueta(Lista, DicReg)
DicReg.Imprimir()

#print("__________Diccionario Modelo_______________")
DicMod=Elementos.LLenarDic(ListaModelo,"Modelo")
#DicMod.Imprimir()
#DicMod.Imprimir()
DicMod=Elementos.buscarReglaModelo(DicReg, DicMod,ListaModelo)
#DicMod.Imprimir()






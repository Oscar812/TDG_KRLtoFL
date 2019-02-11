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


#Declaracion de insumos a utilizar
file = "TRANSFORMACION.xml"
file2 = "Modelo_prueba.xml"
file3 = "PruebaFL.xml"
#Clases LISTA
Lista = ClassList.ListaNoOrdenada()
ListaFL = ClassList.ListaNoOrdenada()
ListaModelo = ClassList.ListaNoOrdenada()
#Obtencion de elemenos de cada XML
Elementos = Elements.ElementosXML()

Lista= Elementos.ObtenerElementos(file,Lista)
Elementos.AsigConexion(Lista)
Elementos.AsigRegla(Lista)
DicReg = ClassDictionary.ListaDictionary()
DicMod = ClassDictionary.ListaDictionary()
DicFL = ClassDictionary.ListaDictionary()
ListaFL= Elementos.ObtenerElementos(file3,ListaFL)
Elementos.AsigConexion(ListaFL)
Elementos.AsigRegla(ListaFL)
ListaModelo = Elementos.ObtenerElementos(file2,ListaModelo)
Elementos.AsigConexion(ListaModelo)
Elementos.AsigRegla(ListaModelo)
DicReg=Elementos.LLenarDic(Lista,"Regla")
Elementos.LLenarDic(Lista,"Regla")
DicReg= Elementos.asignarEtiqueta(Lista, DicReg, "Regla")
DicMod=Elementos.LLenarDic(ListaModelo,"Modelo")
DicFL=Elementos.LLenarDic(ListaFL,"Regla")
DicFL= Elementos.asignarEtiqueta(ListaFL, DicFL, "ReglaFL")
DicMod=Elementos.buscarReglaModelo(DicReg, DicMod, ListaModelo)
#Obtencion de la transformacion al FL
Elementos.ObtenerTrans(DicFL,DicMod)
DicMod.Imprimir()







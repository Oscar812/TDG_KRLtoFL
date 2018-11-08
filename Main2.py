import xml.etree.ElementTree as ET
from operator import is_not
from functools import partial
import zlib
import base64
from Classes import ClassList
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

e = ET.parse('TRANSFORMACION.xml')
root = e.getroot()
#i = 0
k = 0
Rel = []
Hij =[]
info = []
Lista = ClassList.ListaNoOrdenada()

for (ev, el) in ET.iterparse('TRANSFORMACION.xml'):
    inner = []
    if el.tag == 'object':
         Nodo = ClassList.Nodo('', '', '', '')
         for name, value in el.items():
            inner.append([el.tag + '-' + name, str(value).replace('\n', '').replace(' ', '')])
            if (name=='id'):
                Nodo.setId(value)
            if (name == 'label'):
                Nodo.setNombre(value)
            if (name == 'Tipo'):
                Nodo.setTipo(value)
         relacion = []

         for i in el:
            if str(i.text) != 'None':                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
                inner.append([i.tag, str(i.text).replace('\n', '').replace(' ', '')])
            Source = ""
            Targen = ""
            for name, value in i.items():
                 if name == 'parent':
                     Nodo.setParent(value)
                     inner.append([i.tag + '-'+ name, str(value).replace('\n', '').replace(' ', '')])
                 if name == 'source':
                    Source = value
                 if name == 'target':
                    Target = value
            if Source !="" and Target!="":
                Nodo.setRelacion(Source,Target)
         #Nodo.setRelacion(relacion)
         Lista.agregar(Nodo.obtenerNombre(), Nodo.obtenerTipo(), Nodo.obtenerId(), Nodo.obtenerParent(),Nodo.obtenerRelacion())
         info.append(inner)

ListaHijos = ClassList.ListaNoOrdenada()
actual = Lista.cabeza
parent = ''

while actual != None:
    encontrado = False
    #print("Parent: "+actual.obtenerParent())
    #print("Id: " +actual.obtenerId())
    if (actual.obtenerParent() != ' '):
        actual2 = actual.obtenerSiguiente()
        while actual2 != None and not encontrado:
              if actual.obtenerParent() == actual2.obtenerId():
                  actual2.setHijos(actual.obtenerId())
                  #print("Padre Encontrado: "+actual2.obtenerId())
                  encontrado = True
              actual2 = actual2.obtenerSiguiente()
    actual = actual.obtenerSiguiente()

actual = Lista.cabeza
while actual != None:
    print ("Imprimir lista de nodos")
    print("_______________________________")
    print(actual.obtenerNombre())
    print(actual.obtenerTipo())
    print(actual.obtenerParent())
    print(actual.obtenerId())
    print ("Relación")
    print(actual.obtenerRelacion())
    print ("Fin Relación")
    print ("Hijos")
    print(actual.obtenerHijos())
    print ("_______________________________")
    actual=actual.obtenerSiguiente()






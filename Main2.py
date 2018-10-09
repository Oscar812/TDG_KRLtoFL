import xml.etree.ElementTree as ET
from operator import is_not
from functools import partial
import zlib
import base64
#import ejemplo
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


def validar(Tipo,Parent):
    if Tipo == 'Source':
        Parent


'''
tree = ET.parse( 'Matrimonio.xml' )
root = tree.getroot()

xml_codificado= root[0].text
print ( xml_codificado )
result64= base64.b64decode( xml_codificado )
result_data = zlib.decompress( result64 , -15)
print ("Inflate")
print ( result_data )
sin_b = result_data.decode( 'utf-8' )
print ( sin_b )

matrimonio = urldecode( sin_b )

#print (matrimonio)'''

#print( "DESPUES DE LA DECODIFICACIÓN Y CREACIÓN DEL NUEVO XML")
e = ET.parse('TRANSFORMACION.xml')
root = e.getroot()
#i = 0
k = 0
Rel = []
Hij =[]
'''
Nod = ejemplo.Nodo()
Ids = [Nod.Nombre,Nod.Id,Nod.Parent,Nod.Tipo]
Lista = ClassLista.ListaNoOrdenada()
Nodo = ClassLista.Nodo('','','','')
ListaParent = ClassLista.ListaNoOrdenada()
i = 0
data = ' '
Ids.clear()
'''
info = []
Lista = ClassList.ListaNoOrdenada()
Nodo = ClassList.Nodo('','','','','','')



for (ev, el) in ET.iterparse('TRANSFORMACION.xml'):
    inner = []
    if el.tag == 'object':


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


            for name, value in i.items():
                if name == 'parent':
                    Nodo.setParent(value)
                    inner.append([i.tag + '-' + name, str(value).replace('\n', '').replace(' ', '')])
                if name == 'source':
                    if len(relacion) == 0:
                        relacion.append(value)
                    else:
                        relacion.insert(0, value)
                if name == 'target':
                    relacion.append(value)

        print(relacion)
        Nodo.setRelacion(relacion)
        # Lista.agregar(cell.get('label'), cell.get('Tipo'), cell.get('id'), cell.get('parent'))
        Lista.agregar (Nodo.obtenerNombre(), Nodo.obtenerTipo() , Nodo.obtenerId(), Nodo.obtenerParent(), Nodo.obtenerRelacion(), Nodo.obtenerHijos())
        info.append(inner)

#print(info)


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
    print ("_______________________________")

      #validar(actual.obtenerTipo(), actual.obtenerParent)
    actual=actual.obtenerSiguiente()




'''

No borrar Pilas

for atype in e.findall('root'):
    for cell in e.iter('mxCell'):
        print(cell.get('label'))
        ListaParent.agregar(cell.get('label'),cell.get('Tipo'),cell.get('id'),cell.get('parent'))


for atype in e.findall('root'):
    for cell in atype.findall('object'):
        Lista.agregar(cell.get('label'),cell.get('Tipo'),cell.get('id'),cell.get('parent'))
        #Nod.Nombre  cell.get('label')
        #Nod.Id = cell.get('id')
        #Nod.Tipo = cell.get('Tipo')
        #Ids.insert(i,[Nod.Nombre, Nod.Id, Nod.Parent,Nod.Tipo])
        #i += 1

#for object in root.iter('object'):
#print(i)
#print(Ids)
#print(object.attrib.find("': '"))


#for x in range(0,Lista.tamano()):
#   print (Lista.obtener())

#Lista.recorrer()

ListaHijos = ClassLista.ListaNoOrdenada()
actual = Lista.cabeza
parent =''
while actual != None:
    #if (actual.obtenerTipo() == 'Source'):
    parent = actual.obtenerId()
    print("_______________________________")
    print(actual.obtenerNombre())
    print(actual.obtenerTipo())
    print(actual.obtenerParent())
    print(actual.obtenerId())
    print ("_______________________________")

      #validar(actual.obtenerTipo(), actual.obtenerParent)
    actual=actual.obtenerSiguiente()
print ("Parent Source: ")
print (parent)
print ("**************************")
actual = Lista.cabeza
print ("Hijos de Source")




actual= ListaHijos.cabeza
while actual != None:
    print("_______________________________")
    print(actual.obtenerNombre())
    print(actual.obtenerTipo())
    print(actual.obtenerParent())
    print(actual.obtenerId())
    print ("_______________________________")

      #validar(actual.obtenerTipo(), actual.obtenerParent)
    actual=actual.obtenerSiguiente()


'''


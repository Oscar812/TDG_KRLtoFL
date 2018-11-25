'''
Element maintence

'''
import xml.etree.ElementTree as ET
from Classes import ClassList



class ElementosXML:
    Lista = ClassList.ListaNoOrdenada()

    def ObtenerElementos (self, file, Lista):
        #Nodo = ClassList.Nodo('', '', '', '', '', '')
        info = []

        for (ev, el) in ET.iterparse(file):
            inner = []
            if el.tag == 'object':
                Nodo = ClassList.Nodo('', '', '', '')
                for name, value in el.items():
                    inner.append([el.tag + '-' + name, str(value).replace('\n', '').replace(' ', '')])
                    if (name == 'id'):
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
                            inner.append([i.tag + '-' + name, str(value).replace('\n', '').replace(' ', '')])
                        if name == 'source':
                            Source = value
                        if name == 'target':
                            Target = value
                        if name == 'value' and value !="":
                            Nodo.setTag(value)
                    if Source != "" and Target != "":
                        Nodo.setRelacion(Source, Target)
                Lista.agregar(Nodo.obtenerNombre(), Nodo.obtenerTipo(), Nodo.obtenerId(), Nodo.obtenerParent(),
                              Nodo.obtenerRelacion())
                info.append(inner)

        actual = Lista.cabeza
        while actual != None:
            encontrado = False
            if (actual.obtenerParent() != ' '):
                actual2 = actual.obtenerSiguiente()
                while actual2 != None and not encontrado:
                    if actual.obtenerParent() == actual2.obtenerId():
                        actual2.setHijos(actual.obtenerId())
                        encontrado = True
                    actual2 = actual2.obtenerSiguiente()
            actual = actual.obtenerSiguiente()


        for (ev, el) in ET.iterparse(file):
            inner = []
            if el.tag == 'mxCell':
                for name, value in el.items():
                    if (name == "value") and (value is not ""):
                        actual = Lista.cabeza
                        while actual != None:
                            if actual.obtenerId() == el.get('parent'):
                                actual.setTag(value)
                            actual = actual.obtenerSiguiente()
        actual = ClassList.Nodo()
        actual = Lista.cabeza
        while actual != None:
            encontrado = False
            actual2 = ClassList.Nodo()
            actual2 = Lista.cabeza
            while actual2 != None:
                if actual.obtenerId() == actual2.obtenerParent():
                    if actual.obtenerTipo() != "":
                        actual2.setParentName(actual.obtenerTipo())
                actual2 = actual2.obtenerSiguiente()
            actual = actual.obtenerSiguiente()

        return (Lista)

    def ObtenerHijos (self,Lista):
        print("Desde clase")
        actual = Lista.cabeza
        while actual != None:
            print("Imprimir lista de nodos")
            print("_______________________________")
            print(actual.obtenerNombre())
            print(actual.obtenerTipo())
            print(actual.obtenerParent())
            print(actual.obtenerId())
            print("Relación")
            print(actual.obtenerRelacion())
            print("Fin Relación")
            '''
            print("Hijos")
            print(actual.obtenerHijos)
            print("Fin Hijos")
            print("_______________________________")
            '''
            # validar(actual.obtenerTipo(), actual.obtenerParent)
            actual = actual.obtenerSiguiente()

        #Nodo= ClassList.Nodo('', '', '', '', '', '')
        List_hijos = []
        actual = Lista.cabeza
        while actual != None:
            print("Imprimir lista de nodos")
            print("_______________________________")
            print(actual.obtenerId())
            print(actual.obtenerNombre())
            Hijo = Lista.cabeza
            while Hijo != None:
                if Hijo.obtenerParent() == actual.obtenerId():
                   List_hijos.append(Hijo.obtenerId)
                Hijo.obtenerSiguiente()
            Lista.setHijos(List_hijos)
            actual.obtenerSiguiente()
        return (Lista)

    def AsigConexion(self,Lista):
        actual = Lista.cabeza
        while actual != None:
            encontrado = False
            if (actual.obtenerRelacion()):
                Relacion = []
                Relacion = actual.obtenerRelacion()
                Filas =  (len(Relacion)/2).is_integer()
                for i in range(Filas):
                    Lista.AgregarConexion(Relacion[i]  , actual.obtenerNombre(), Relacion[i+1], "Source", actual.obtenerId())
                    Lista.AgregarConexion(Relacion[i+1], actual.obtenerNombre(), Relacion[i]  , "Target", actual.obtenerId())
                    i+1
            actual = actual.obtenerSiguiente()

    def AsigRegla(self,Lista):
        actual = Lista.cabeza
        while actual != None:
            if (actual.obtenerTipo() == "Regla"):
                Lista.AgregarRegla(actual.obtenerId())
                Lista.SetReglas(actual.obtenerId())
            actual = actual.obtenerSiguiente()


    def BuscarPatron(self, ListaRegla, ListaModelo):
            print("Estoy buscando Patron")
            if (ListaRegla.obtenerReglas()):
                print("Hay reglas: ")
                Regla = []
                Regla= ListaRegla.obtenerReglas()
                print("Reglas:",Regla)
                print(len(Regla))
                for i in range(len(Regla)):
                    actual = ClassList.Nodo()
                    actual = ListaRegla.cabeza
                    print("Regla #",i, Regla[i])

                    while actual != None:
                        if actual.obtenerRegla() == Regla[i] and actual.obtenerParentName()== "Source":
                            print("Encontré elemento del source")
                            print("Le mandé Id: "+ actual.obtenerId())
                            self.Patrones(actual, ListaModelo, ListaRegla)
                            print("Voy por aqui: " ,actual.obtenerId())
                        actual = actual.obtenerSiguiente()
                        print("Actual: ",actual)


    def Patrones(self, Objeto, ListaModelo, ListaRegla):
        print("ID: "+Objeto.obtenerId())
        print("Tipo: " + Objeto.obtenerTipo())
        if Objeto.obtenerRelacion():
            print("Tiene Relacion")
            Relacion = []
            Relacion = Objeto.obtenerRelacion()
            actual = ListaRegla.cabeza
            print(Relacion[0])
            while actual != None:
                if actual.obtenerId() == Relacion[0]:
                    print("Aqui voy")
                    self.Patrones(actual, ListaModelo, ListaRegla)
                actual = actual.obtenerSiguiente()
        else:
                self.PatronModelo(ListaModelo, Objeto)



    def PatronModelo(self, ListaModelo, Objeto):
        actual = ListaModelo.SetCabeza
        print("no tiene relacion estoy en el patronmodelo")
        #while actual != None:
            #if actual.obtenerTipo() == Objeto.obtenerTipo():
                #print("Encontré el tipo")
        




'''
Element maintence

'''
import xml.etree.ElementTree as ET
from Classes import ClassList, ClassDictionary


class ElementosXML:
    Lista = ClassList.ListaNoOrdenada()
    DicReglas = ClassDictionary.ListaDictionary()
    DicModelo = ClassDictionary.ListaDictionary()

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
            actual = actual. obtenerSiguiente()

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


    def LLenarDic(self, ListaRegla, DicReg, Tipo):
            if Tipo=="Regla":

                print("Estoy buscando Patron")
                if (ListaRegla.obtenerReglas()):
                    print("Hay reglas: ")
                    Regla = []
                    Regla= ListaRegla.obtenerReglas()
                    for i in range(len(Regla)):
                        #actual = ClassList.Nodo()
                        #actual = ListaRegla.cabeza
                        print("Regla #",i, Regla[i])
                        Sec = 1
                        Sw=0
                        Ind = 'Regla'
                        while True:
                            self.Patrones2(Regla[i],Sec,ListaRegla,DicReg,Sw,Ind)
                            if Sw != 1:
                                break
                            else:
                                Sec += 1
                            #print("Voy por aqui: " ,actual.obtenerId())
                            #actual = actual.obtenerSiguiente()
                            #print("Actual: ",actual)
            else:
                Sec = 1
                Sw = 0
                Ind='Modelo'
                self.Patrones2("",Sec,ListaRegla,DicReg,Sw,Ind)
            return (DicReg)


    def Patrones2(self, Id, Sec, Lista,Dic,Sw, Ind):
        #print("ID: "+Objeto.obtenerId())
        #print("Tipo: " + Objeto.obtenerTipo())
        #Validar si es un tipo conexion
        if Sec == 1:
            if Ind == 'Regla':
                actual = ClassList.Nodo()
                actual = Lista.cabeza
                while actual != None:
                    if actual.obtenerRegla() == Id  and actual.obtenerParentName() == "Source":
                        Dic.agregar(Sec,actual.obtenerTipo(),actual.obtenerId())
                    actual = actual.obtenerSiguiente()
            else:
                actual = ClassList.Nodo()
                actual = Lista.cabeza
                while actual != None:
                    Dic.agregar(Sec, actual.obtenerTipo(), actual.obtenerId())
                    actual = actual.obtenerSiguiente()
            Sw = 1

'''
        if Objeto.obtenerRelacion():
            print("Tiene Relacion")
            Relacion = []
            Relacion = Objeto.obtenerRelacion()
            print(Relacion[0])
            self.patrones(Relacion[0], ListaModelo, ListaRegla)
        else:
            #print("no tiene relacion")
            if Objeto.obtenerConexion():
                print("Tiene Conexion")
                Conexion=[]
                Conexion = Objeto.obtenerConexion()
                if Conexion[3]=="Target":
                    self.patrones(Conexion[1],ListaModelo,ListaRegla)
                else Conexion[3]=="Source":
                    agregardiccionar
                    enciendobandera
            else:
                if Objeto.obtenerHijos() and Objeto.obtenerParentName()=="Source":
                    print("tiene hijos")
                    Hijos = []
                    Hijos = Objeto.obtenerHijos()
                    #self.PatronModelo(ListaModelo, Objeto)

        if Objeto:
            aqui

  
    def Patrones(self, Objeto, ListaModelo, ListaRegla):
        print("ID: "+Objeto.obtenerId())
        print("Tipo: " + Objeto.obtenerTipo())

        if Objeto.obtenerRelacion():
            print("Tiene Relacion")
            Relacion = []
            Relacion = Objeto.obtenerRelacion()
            print(Relacion[0])
            self.patrones(Relacion[0], ListaModelo, ListaRegla)
        else:
            #print("no tiene relacion")
            if Objeto.obtenerConexion():
                print("Tiene Conexion")
                Conexion=[]
                Conexion = Objeto.obtenerConexion()
                if Conexion[3]=="Target":
                    self.patrones(Conexion[1],ListaModelo,ListaRegla)
                else Conexion[3]=="Source":
                    agregardiccionar
                    enciendobandera
            else:
                if Objeto.obtenerHijos() and Objeto.obtenerParentName()=="Source":
                    print("tiene hijos")
                    Hijos = []
                    Hijos = Objeto.obtenerHijos()
                    #self.PatronModelo(ListaModelo, Objeto)

        if Objeto
            


    def PatronModelo(self, ListaModelo, Objeto):
        actual = ListaModelo.SetCabeza
        print("no tiene relacion estoy en el patronmodelo")
        #while actual != None:
            #if actual.obtenerTipo() == Objeto.obtenerTipo():
            #print("Encontré el tipo")
        '''




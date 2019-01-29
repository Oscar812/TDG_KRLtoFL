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


    def LLenarDic(self, Lista, Tipo):
            Sec =1
            Dic = []
            DicDef = ClassDictionary.ListaDictionary()
            if Tipo=="Regla":
                if (Lista.obtenerReglas()):
                    Regla = []
                    Regla= Lista.obtenerReglas()
                    for i in range(len(Regla)):
                        Etiquetas = []
                        Ind = 'Regla'
                        Dic.append(ClassDictionary.ListaDictionary())
                        self.Patrones2(Regla[i], Lista, Dic[i], Ind)
                        while (self.obtenerDatos2(Lista, Dic[i])):
                            Sec += 1
                        Nodo=Dic[i].cabeza
                        Etiquetas= self.asignarEtiqueta(Lista, Regla[i])
                        DicDef.agregar(Nodo.obtenerSec(),Nodo.obtenerPatron(),Nodo.obtenerId(),Regla[i], Etiquetas)
            else:
                print("Entre por el modelo")
                Dic.append(ClassDictionary.ListaDictionary())
                self.Patrones2("", Lista, Dic[0], Tipo)
                while (self.obtenerDatos2(Lista, Dic[0])):
                    Sec += 1
                DicDef=Dic[0]
            return (DicDef)

    def asignarEtiqueta(self, Lista, idRegla):
        actual= Lista.cabeza
        etiqueta=[]
        while(actual != None):
            if actual.obtenerParentName()=="Target" and actual.obtenerRegla == idRegla:
                objetos=[]
                Ids= []
                objetos.append(actual.obtenerTipo())
                Ids.append(actual.obtenerId())
                etiqueta= [objetos,Ids]
            actual = actual.obtenerSiguiente()
        return etiqueta



    def Patrones2(self, Id, Lista, Dic, Ind):
        Sec=1
        if Ind == 'Regla':
            actual = Lista.cabeza
            while actual != None:
                #print("ID regla"+str(actual.obtenerRegla()))
                if actual.obtenerRegla() == Id and actual.obtenerParentName() == "Source":
                    Patron = []
                    Ids= []
                    Patron.append(actual.obtenerTipo())
                    Ids.append(actual.obtenerId())
                    Dic.agregar(Sec,Patron,Ids,Id,"")
                actual = actual.obtenerSiguiente()
        else:
            actual = ClassList.Nodo()
            actual = Lista.cabeza
            while actual != None:
                Patron = []
                Ids = []
                Regla = []
                Patron.append(actual.obtenerTipo())
                Ids.append(actual.obtenerId())
                Dic.agregar(Sec,Patron,Ids,Regla,"")
                actual = actual.obtenerSiguiente()


    def obtenerDatos2(self, Lista, Dic):
        DicNewReg = ClassDictionary.Nodo()
        DicActual = Dic.cabeza
        DicUltimReg = Dic.cabeza
        Sec = DicUltimReg.obtenerSec()
        swp=0
        while DicActual != None:
            if DicActual.obtenerSec()== Sec:
                New = []
                Patron = []
                Ids = []
                actual = Lista.cabeza
                Patron=(DicActual.obtenerPatron().copy())
                Ids=(DicActual.obtenerId().copy())
                long = len(Ids)
                sw = 0
                while actual != None and sw==0:
                    if (actual.obtenerId() == Ids[0]):
                        New=[]
                        New=self.Analizarobjeto(Lista, Ids[0], 'I')
                        if (New):
                            Patron.insert(0,New[0][0])
                            Ids.insert(0,New[0][1])
                            if not(Dic.Buscar(Ids,Sec+1)):
                                Dic.agregar(Sec+1, Patron, Ids,"","")
                            sw = 1
                            break
                    if (actual.obtenerId() == Ids[long-1] and sw==0):
                        New=[]
                        New = self.Analizarobjeto(Lista, Ids[long-1], 'D')
                        if (New):
                            Patron.append(New[0][0])
                            Ids.append(New[0][1])
                            if not(Dic.Buscar(Ids,Sec+1)):
                                Dic.agregar(Sec + 1, Patron, Ids,"","")
                            sw = 1
                            break

                    actual = actual.obtenerSiguiente()
                if sw!=0:
                    swp +=1
            DicActual = DicActual.obtenerSiguiente()
        if swp > 0:
            return Dic
        else:
            return False

    def Analizarobjeto(self, Lista, Id, Orden):
        actual = Lista.cabeza
        RegDic = []
        conexion = []
        relacion = []
        sw=0
        while actual!= None and sw==0:
            if actual.obtenerId()==Id:
                conexion = actual.obtenerConexion()
                hijos = actual.obtenerHijos()
                for i in range (len(conexion)):
                    Conx = conexion[i]
                    RegDic = []
                    if (Conx[3] == "Target" and Orden =='I'):
                        Nodo=Lista.Buscar(Conx[2])
                        RegDic.insert((0),[Nodo.obtenerTipo(),Conx[2]])
                        #print(RegDic)
                        sw=1
                        break
                    else:
                        if (Conx[3] == "Source" and Orden=='D'):
                            Nodo = Lista.Buscar(Conx[2])
                            RegDic.insert(0,[Nodo.obtenerTipo(), Conx[2]])
                            sw=1
                            break
                if sw == 0:
                    RegDic = []
                    if actual.obtenerRelacion():
                        relacion = actual.obtenerRelacion()
                        if Orden == 'I' and relacion[0]!= ' ':
                            Nodo = Lista.Buscar(relacion[0])
                            RegDic.insert(0,[Nodo.obtenerTipo(), relacion[0]])
                            sw=1
                        if Orden == 'D' and relacion[1]!= ' ':
                            Nodo = Lista.Buscar(relacion[1])
                            RegDic.insert(0,[Nodo.obtenerTipo(), relacion[1]])
                            sw=1
                for i in range(len(hijos)):
                    RegDic = []
                    if (hijos):
                        Nodo=Lista.Buscar(hijos[i])
                        RegDic.insert(0, [Nodo.obtenerTipo(), hijos[i]])
                        #print(RegDic)
                sw = 1
                break
            actual=actual.obtenerSiguiente()
        if sw!=0:
            return RegDic
        else:
            return False

    def buscarReglaModelo(self, Dic, Modelo):
        dicActual=Dic.cabeza
        modActual= Modelo.cabeza
        regla=[]
        while(dicActual != None):
            regla.append(dicActual.obtenerPatron())
            dicActual=dicActual.obtenerSiguiente()
        while(modActual != None):
            for i in range(len(regla)):
                if (modActual.obtenerPatron() == regla[i]):
                    print("Cumple")
                    #print(dicActual.obtenerPatron())
                    #print (modActual.obtenerPatron())
            modActual=modActual.obtenerSiguiente()









'''
    def obtenerDatos(self, Lista, Dic, Sec):

        DicActual = Dic.cabeza
        Elementos = []
        ids = []
        while DicActual != None:
            actual = Lista.cabeza
            cont = 1
            Elementos = Dic.obtenerPatron()
            ids = Dic.obtenerId()
            while actual != None:
                for i in len(ids):
                    if (actual.obtenerId() == ids[i]):
                        if (actual.obtenerConexion()):
                            conexion = []
                            for j in len(actual.obtenerConexion()):
                                conexion = actual.obtenerConexion()[i]
                                if (conexion[3] == "Source"):
                                    Elementos.insert(i + 1, conexion[2])
                                    ids.insert(i + 1, conexion[1])
                                    cont += 1
                                if (conexion[3] == "Target"):
                                    Elementos.insert(i - 1, conexion[2])
                                    ids.insert(i - 1, conexion[1])
                                    cont += 1
                        if (actual.obtenerRelacion()):
                            relacion = []
                            relacion = actual.obtenerRelacion()
                            ##source
                            if relacion[0]:
                                ids.insert(i + 1)
                            if relacion[1]:
                                ids.insert(i - 1)
**************************************************************************************************************


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




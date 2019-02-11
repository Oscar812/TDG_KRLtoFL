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
            actual = actual.obtenerSiguiente()
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
            if (actual.obtenerTipo() == "Regla" or actual.obtenerTipo() == "ReglaFL"):
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
                        #Etiquetas= self.asignarEtiqueta(Lista, Regla[i])
                        DicDef.agregar(Nodo.obtenerSec(),Nodo.obtenerPatron(),Nodo.obtenerId(),Regla[i], "","","")
            else:
                Dic.append(ClassDictionary.ListaDictionary())
                self.Patrones2("", Lista, Dic[0], Tipo)
                while (self.obtenerDatos2(Lista, Dic[0])):
                    Sec += 1
                DicDef=Dic[0]
            return (DicDef)

    def asignarEtiqueta(self, Lista, Dic, Tipo):
        DicActual=Dic.cabeza
        DicDef = ClassDictionary.ListaDictionary()
        #dicActual = Dic.cabeza
        idRegla=0
        etiqueta=[]
        while (DicActual !=None):
            idRegla=DicActual.obtenerRegla()
            actual = Lista.cabeza
            while(actual != None):
                if actual.obtenerParentName()=="Target" and actual.obtenerRegla() == idRegla and Tipo=="Regla":
                    objetos2=[]
                    Ids= []
                    IdPatron = []
                    objetos =""
                    objetos=(actual.obtenerNombre())
                    objetos2= objetos.split(" ")
                    Ids.append(actual.obtenerId())
                    etiqueta= [objetos2,Ids]
                    IdPatron = DicActual.obtenerId().copy()
                    Equivalencia = []
                    for i in range(len(IdPatron)):
                        Equivalencia.append(Lista.Buscar(IdPatron[i]).obtenerNombre())
                    LAsoc={"":""}
                    self.AsignarPosDat(etiqueta[0], Equivalencia, LAsoc)
                    DicDef.agregar(DicActual.obtenerSec(), DicActual.obtenerPatron(), DicActual.obtenerId(),
                                   DicActual.obtenerRegla(), etiqueta, Equivalencia, LAsoc)
                if actual.obtenerParentName()=="Source" and actual.obtenerRegla() == idRegla and Tipo=="ReglaFL":
                    objetos2=[]
                    Ids= []
                    IdPatron = []
                    objetos =""
                    objetos=(actual.obtenerNombre())
                    objetos2= objetos.split(" ")
                    Ids.append(actual.obtenerId())
                    etiqueta= [objetos2,Ids]
                    IdPatron = DicActual.obtenerId().copy()
                    Equivalencia = []
                    Equivalencia = self.ObtenerEqReglaFL(idRegla,Lista)
                    #for i in range(len(IdPatron)):
                    #    Equivalencia.append(Lista.Buscar(IdPatron[i]).obtenerNombre())
                    LAsoc={"":""}
                    #LAsoc = self.AsignarPosDat(etiqueta[0], Equivalencia)
                    #LAsoc=self.AsignarPosDat(etiqueta[0], Equivalencia)
                    DicDef.agregar(DicActual.obtenerSec(), DicActual.obtenerPatron(), DicActual.obtenerId(),
                                   DicActual.obtenerRegla(), etiqueta, Equivalencia, LAsoc)
                actual = actual.obtenerSiguiente()
            DicActual= DicActual.obtenerSiguiente()
        return DicDef

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
                    Dic.agregar(Sec,Patron,Ids,Id,"","","")
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
                Dic.agregar(Sec,Patron,Ids,Regla,"","","")
                actual = actual.obtenerSiguiente()


    def obtenerDatos2(self, Lista, Dic):
        DicActual = Dic.cabeza
        DicUltimReg = Dic.cabeza
        Sec = DicUltimReg.obtenerSec()
        swp=0
        while DicActual != None:
            if DicActual.obtenerSec()== Sec:
                Patron = []
                Ids = []
                actual = Lista.cabeza
                sw = 0
                Patron = (DicActual.obtenerPatron().copy())
                Ids = (DicActual.obtenerId().copy())
                long = len(Ids)
                New = []
                New = self.Analizarobjeto(Lista, Ids[0], 'I', Dic, Ids)
                while(New):
                    Patron.insert(0,New[0][0])
                    Ids.insert(0,New[0][1])
                    Dic.agregar(len(Patron), Patron, Ids,"","","","")
                    sw = 1
                    Patron = (DicActual.obtenerPatron().copy())
                    Ids = (DicActual.obtenerId().copy())
                    long = len(Ids)
                    New = []
                    New = self.Analizarobjeto(Lista, Ids[0], 'I', Dic, Ids)
                Patron = (DicActual.obtenerPatron().copy())
                Ids = (DicActual.obtenerId().copy())
                long = len(Ids)
                New = []
                New = self.Analizarobjeto(Lista, Ids[long - 1], 'D', Dic, Ids)
                while (New):
                    Patron.append(New[0][0])
                    Ids.append(New[0][1])
                    Dic.agregar(len(Patron), Patron, Ids,"", "", "","")
                    sw = 1
                    Patron = (DicActual.obtenerPatron().copy())
                    Ids = (DicActual.obtenerId().copy())
                    long = len(Ids)
                    New = []
                    New = self.Analizarobjeto(Lista, Ids[long - 1], 'D', Dic, Ids)
                if sw!=0:
                    swp +=1
            DicActual = DicActual.obtenerSiguiente()
        if swp > 0:
            return True
        else:
            return False

    def Analizarobjeto(self, Lista, Id, Orden, Dic, Ids):
        actual = Lista.cabeza
        RegDic = []
        conexion = []
        relacion = []
        IDs2 = Ids.copy()
        sw=0
        encontrado = False
        while actual!= None and sw==0 and not encontrado:
            if actual.obtenerId()==Id:
                conexion = actual.obtenerConexion().copy()
                i=0
                for i in range (len(conexion)):
                    Conx = conexion[i]
                    RegDic = []
                    IDs2 = Ids.copy()
                    if (Conx[3] == "Target" and Orden =='I'):
                        Nodo=Lista.Buscar(Conx[2])
                        IDs2.insert(0,Conx[2])
                        if not(Dic.Buscar(IDs2)):
                            sw=1
                            RegDic.insert((0),[Nodo.obtenerTipo(),Conx[2]])
                            break
                    else:
                        if (Conx[3] == "Source" and Orden=='D'):
                            Nodo = Lista.Buscar(Conx[2])
                            IDs2 = Ids.copy()
                            IDs2.append(Conx[2])
                            if not (Dic.Buscar(IDs2)):
                                RegDic.insert(0,[Nodo.obtenerTipo(), Conx[2]])
                                sw=1
                                break
                if sw == 0:
                    RegDic = []
                    IDs2 = Ids.copy()
                    if actual.obtenerRelacion():
                        relacion = actual.obtenerRelacion().copy()
                        if Orden == 'I' and relacion[0]!= ' ':
                            Nodo = Lista.Buscar(relacion[0])
                            IDs2.insert(0,relacion[0])
                            if not (Dic.Buscar(IDs2)):
                                RegDic.insert(0,[Nodo.obtenerTipo(), relacion[0]])
                                sw=1
                        if Orden == 'D' and relacion[1]!= ' ':
                            IDs2 = Ids.copy()
                            Nodo = Lista.Buscar(relacion[1])
                            IDs2.append(relacion[1])
                            if not (Dic.Buscar(IDs2)):
                                RegDic.insert(0,[Nodo.obtenerTipo(), relacion[1]])
                                sw=1
                encontrado = True
            actual=actual.obtenerSiguiente()
        if sw!=0:
            return RegDic
        else:
            return False

    def AsignarPosDat(self, Etiq, Patron, LAsoc):

        traduccion = []
        for i in range(len(Etiq)):
            Et = Etiq[i]
            Pos = Et.find("^")
            Et2 = Et[Pos + 1:len(Etiq)]
            Pos2 = Et2.find("^") + Pos+1
            Long = (Pos2+1) - (Pos+1)
            if (Pos != -1):
                Dat = Et[Pos+1:Long]
                sw=0
                j=0
                while(sw==0):
                    if (Patron[j].find(Dat)!= -1):
                        #LAsoc.append({Dat: j})
                        LAsoc[Dat]= j
                        sw=1
                    j+=1

            #return  LAsoc


    def buscarReglaModelo(self, Dic, Modelo, ListaModelo):
        Auxiliar = ClassList.Nodo("", "", "", "")
        traduccion=[]
        DicDef = ClassDictionary.ListaDictionary()
        dicActual=Dic.cabeza
        modActual= Modelo.cabeza
        regla=[]
        etiqueta=[]
        IdReg=[]
        EqMod=[]
        while(dicActual != None):
            regla.append(dicActual.obtenerPatron().copy())
            IdReg.append(dicActual.obtenerId().copy())
            etiqueta.append(dicActual.obtenerEtiqueta())
            EqMod.append(dicActual.obtenerEqMod())
            #Equivalencia.append(dicActual.obtenerEquivalencia().copy())
            dicActual=dicActual.obtenerSiguiente()

        while(modActual != None):
            ptraducido = []
            for i in range(len(regla)):
                if (modActual.obtenerPatron() == regla[i]):
                    #etiqueta2=etiqueta[i][0].copy()
                    k = 0
                    l = 0
                    Equivalencia = []
                    for j in range(len(regla[i])):
                        Equivalencia.append(ListaModelo.Buscar(modActual.obtenerId()[j]).obtenerNombre())
                    DicDef.agregar(modActual.obtenerSec(), modActual.obtenerPatron(), modActual.obtenerId(),
                                   IdReg[i], etiqueta[i], Equivalencia,EqMod[i])
                    #print(ptraducido)
            modActual=modActual.obtenerSiguiente()
        return (DicDef)

    def ObtenerTrans(self, DicReg, DicMod):
        DicDef = ClassDictionary.ListaDictionary()
        dicActual = DicReg.cabeza
        modActual = DicMod.cabeza
        regla = []
        etiqueta = []
        IdReg = []
        EqMod = ""
        Equivalencia=[]
        while (dicActual != None):
            regla.append(dicActual.obtenerPatron().copy())
            IdReg.append(dicActual.obtenerId().copy())
            etiqueta.append(dicActual.obtenerEtiqueta().copy())
            Equivalencia.append(dicActual.obtenerEquivalencia().copy())
            dicActual = dicActual.obtenerSiguiente()

        while (modActual != None):
            #ptraducido = []
            for i in range(len(regla)):
                Etiq =modActual.obtenerEtiqueta()
                ptraducido = []
                if (Etiq[0] == etiqueta[0][i]):
                    result=[]
                    for j in range(len(Equivalencia[i])):
                        cont = Equivalencia[i][j]
                        sw = 0
                        while (sw == 0):
                            Pos = cont.find("^")
                            cont2 = cont[Pos + 1:len(cont)]
                            Pos2 = cont2.find("^") + Pos
                            Long = (Pos2) - (Pos)
                            if (Pos != -1):
                                if (Pos > 0):
                                    Dat = cont[0:Pos]
                                    ptraducido.append(Dat)
                                Dat = cont2[0:Long]
                                EqMod = modActual.obtenerEqMod().copy()
                                # print("Valor: "+ str(EqMod[Dat]))
                                # print("Valor: " + str(modActual.obtenerEquivalencia().copy()[EqMod[Dat]]))
                                ptraducido.append(modActual.obtenerEquivalencia().copy()[EqMod[Dat]])

                            else:
                                sw = 1
                                ptraducido.append(cont)
                            cont = cont2[Long + 1:len(cont2)]
                    if (ptraducido):
                        modActual.setTransf(ptraducido)
                        #print("Encontré una traducción")
            modActual = modActual.obtenerSiguiente()

    def ObtenerEqReglaFL(self, idRegla, Lista):
        objetos=[]
        Actual = Lista.cabeza
        encontrado = False
        while (Actual!=None and not encontrado):
            if Actual.obtenerParentName() == "Target" and Actual.obtenerRegla() == idRegla:
                Data = Actual.obtenerNombre()
                objetos = Data.split(" ")
                encontrado = True
            Actual = Actual.obtenerSiguiente()
        return objetos
import xml.etree.ElementTree as ET
class Nodo:

    def __init__(self, *args):
        if len(args) > 0:
            self.Secuencia = args[0]
            self.Patron = args[1]
            self.Id = args[2]
            self.Regla = args[3]
            self.Etiqueta = args[4]
            self.Equivalencia = args[5]
            self.EqMod = args[6]
            self.Transf = []
        else:
            self.Secuencia = ""
            self.Patron = []
            self.Id = []
            self.Regla = ""
            self.Etiqueta= []
            self.Equivalencia = []
            self.EqMod = []
            self.Transf = []
        self.siguiente = None


    def obtenerSiguiente(self):
        return self.siguiente

    def setSec(self, Sec):
        self.Secuencia.extend([Sec])

    def setPatron(self, Patron):
        self.Patron.extend([Patron])

    def setEtiqueta(self, Etiqueta):
        self.Etiqueta.extend([Etiqueta])

    def setTransf(self, Transf):
        self.Transf.append(Transf)

    def setEqMod(self, EqMod):
        self.EqMod.extend([EqMod])

    def setEquivalencia(self, Equivalencia):
        self.Equivalencia.extend([Equivalencia])

    def setId(self, Id):
        self.Id.extend([Id])

    def obtenerSec(self):
        return self.Secuencia

    def obtenerTransf(self):
        return self.Transf

    def obtenerPatron(self):
        return self.Patron

    def obtenerEtiqueta(self):
        return self.Etiqueta

    def obtenerEqMod(self):
        return self.EqMod

    def obtenerEquivalencia(self):
        return self.Equivalencia

    def obtenerId(self):
        return self.Id

    def obtenerRegla(self):
        return self.Regla

    def asignarDato(self,Sec,Patron,Id,Regla):
        self.Secuencia = Sec
        self.Patron = Patron
        self.Id = Id
        self.Regla=Regla

    def asignarSiguiente(self,nuevosiguiente):
        self.siguiente = nuevosiguiente

    def mostrarNodo(self):
        print("Sec: "+str(self.obtenerSec()))
        print("Patron: " + str(self.obtenerPatron()))
        print("Id: " + str(self.obtenerId()))

class ListaDictionary:

    def __init__(self):
        self.cabeza = None

    def SetCabeza(self):
        return self.cabeza

    def estaVacia(self):
        return self.cabeza == None

    def agregar(self, item1, item2, item3, item4,item5, item6, item7):
        temp = Nodo(item1, item2, item3, item4, item5, item6, item7)
        temp.asignarSiguiente(self.cabeza)
        self.cabeza = temp

    def Imprimir(self):
        actual = self.cabeza
        while actual != None:
            print("Secuencia: "+ str(actual.obtenerSec()))
            #print(actual.obtenerSec())
            print("Patron: " + str(actual.obtenerPatron()))
            #print(actual.obtenerPatron())
            print("Id: " + str(actual.obtenerId()))
            print("Regla: " + str(actual.obtenerRegla()))
            print("Etiqueta: " + str(actual.obtenerEtiqueta()))
            print("Equivalencia: " + str(actual.obtenerEquivalencia()))
            print("Listas Asoc: "+str(actual.obtenerEqMod()))
            print("Transformación "+str(actual.obtenerTransf()))

            #print(actual.obtenerId())
            actual = actual.obtenerSiguiente()

    def ObtenerUltReg(self):
        actual= self.cabeza
        while actual != None:
            ultimo=actual
            actual=actual.obtenerSiguiente()
        return  ultimo

    def Buscar(self, Id):
        #actual = Nodo("", "", "","")
        actual = self.cabeza
        encontrado = False
        #print("Id :" + str(Id))
        while actual != None and not encontrado:
            if actual.obtenerId() == Id:
                #print("Encontre :" +str(Id))
                #print("Secuencia: "+str(Sec))
                encontrado = True
            else:
                actual = actual.obtenerSiguiente()
        return encontrado





import xml.etree.ElementTree as ET
class Nodo:

    def __init__(self, *args):
        if len(args) > 0:
            self.Secuencia = args[0]
            self.Patron = args[1]
            self.Id = args[2]
        else:
            self.Secuencia = ""
            self.Patron = []
            self.Id = []
        self.siguiente = None

    def obtenerSiguiente(self):
        return self.siguiente

    def setSec(self, Sec):
        self.Secuencia.extend([Sec])

    def setPatron(self, Patron):
        self.Patron.extend([Patron])

    def setId(self, Id):
        self.Id.extend([Id])

    def obtenerSec(self):
        return self.Secuencia

    def obtenerPatron(self):
        return self.Patron

    def obtenerId(self):
        return self.Id

    def asignarDato(self,Sec,Patron,Id):
        self.Secuencia = Sec
        self.Patron = Patron
        self.Id = Id

    def asignarSiguiente(self,nuevosiguiente):
        self.siguiente = nuevosiguiente


class ListaDictionary:

    def __init__(self):
        self.cabeza = None

    def SetCabeza(self):
        return self.cabeza

    def estaVacia(self):
        return self.cabeza == None

    def agregar(self, item1, item2, item3):
        temp = Nodo(item1, item2, item3)
        temp.asignarDato(item1, item2, item3)
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
            #print(actual.obtenerId())
            actual = actual.obtenerSiguiente()

    def ObtenerUltReg(self):
        actual= self.cabeza
        while actual != None:
            ultimo=actual
            actual=actual.obtenerSiguiente()
        return  ultimo

    def Buscar(self, Id, Sec):
        actual = Nodo("", "", "")
        actual = self.cabeza
        encontrado = False
        while actual != None and not encontrado:
            if actual.obtenerId() == Id and actual.obtenerSec()==Sec:
                encontrado = True
            else:
                actual = actual.obtenerSiguiente()
        return encontrado


class ListaDiccionario:
    def __init__(self, filas, columnas):
        #self.filas
        #self.columnas
        #self.Matriz = [[i for i in range(self.filas)] for j in range(self.columnas)]
        self.columnas = []
        self.Matriz = [self.columnas]

    def setDato(self, sec, dato, ids, fila):
        i = 0
        self.Matriz[fila][0] = sec
        self.Matriz[fila][1] = dato
        self.Matriz[fila][2] = ids

    def obtenerDato(self):
        return self.Matriz



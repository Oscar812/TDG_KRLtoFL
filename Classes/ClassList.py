class Nodo:
    def __init__(self,Nombre,Tipo,Id,Parent):
        self.Nombre = Nombre
        self.Tipo = Tipo
        self.Id = Id
        self.Parent = Parent
        self.siguiente = None
        self.Relacion = []
        self.Hijos = []
        '''
        NIVEL
        RELACION [SOURCE, TARGET]
        HIJOS []
        PARENT
        '''
    def setNombre(self,Nombre):
        self.Nombre = Nombre
    def setTipo(self, Tipo):
        self.Tipo = Tipo
    def setId(self, Id):
        self.Id = Id
    def setParent(self, Parent):
        self.Parent = Parent
    def setRelacion(self,Source,Target):
        self.Relacion.extend([Source,Target])
    def setHijos(self,Hijo):
        self.Hijos.append(Hijo)
    def obtenerNombre(self):
        return self.Nombre
    def obtenerTipo(self):
        return self.Tipo
    def obtenerId(self):
        return self.Id
    def obtenerParent(self):
        return self.Parent
    def obtenerSiguiente(self):
        return self.siguiente
    def obtenerHijos(self):
        return self.Hijos
    def obtenerRelacion(self):
        return self.Relacion
    def asignarDato(self,Nombre,Tipo,Id,Parent,Relacion):
        self.Nombre = Nombre
        self.Tipo = Tipo
        self.Id = Id
        self.Parent = Parent
        self.Relacion = Relacion
    def asignarSiguiente(self,nuevosiguiente):
        self.siguiente = nuevosiguiente
class ListaNoOrdenada:

     def __init__(self):
        self.cabeza = None

     def SetCabeza(self):
        return self.cabeza

     def estaVacia(self):
        return self.cabeza == None

     def agregar(self, item1, item2, item3, item4, item5):
        temp = Nodo(item1, item2, item3, item4)
        temp.asignarDato(item1, item2, item3, item4, item5)
        temp.asignarSiguiente(self.cabeza)
        self.cabeza = temp

     def tamano(self):
        actual = self.cabeza
        contador = 0
        while actual != None:
            contador = contador + 1
            actual = actual.obtenerSiguiente()
        return contador

     def remover(self,item):
        actual = self.cabeza
        previo = None
        encontrado = False
        while not encontrado:
            if actual.obtenerDato() == item:
                encontrado = True
            else:
                previo = actual
                actual = actual.obtenerSiguiente()
                if previo == None:
                    self.cabeza = actual.obtenerSiguiente()
                else:
                    previo.asignarSiguiente(actual.obtenerSiguiente())

     def recorrer(self):
        actual = self.cabeza
        while actual != None:
            print(actual.obtenerNombre())
            actual=actual.obtenerSiguiente()
     def imprimir(self):
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
             actual = actual.obtenerSiguiente()



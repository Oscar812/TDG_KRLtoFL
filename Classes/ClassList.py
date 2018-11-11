class Nodo:
    def __init__(self,Nombre,Tipo,Id,Parent):
        self.Nombre = Nombre
        self.Tipo = Tipo
        self.Id = Id
        self.Parent = Parent
        self.siguiente = None
        #self.Source = []
        #self.
        #self.Relacion = [self.Source,self.Target]Target = []
        self.Relacion = []
        #matriz = [range(numero_columnas) for i in range(numero_filas)]
        self.Hijos = []
        self.Conexion = []
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
        #self.Source.append(Source)
        #self.Target.append(Target)
        #self.Relacion.extend([self.Source,self.Target])
        self.Relacion.extend([Source,Target])
    def setConexion(self,Tipo,Conexion):
        self.Conexion.extend([Tipo,Conexion])
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
    def obtenerConexion(self):
        return self.Conexion
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

     def AgregarConexion(self, IdBus, Tipo, IdConex):
         actual = self.cabeza
         encontrado = False
         #print("Id a buscar: " +IdBus)
         #print("Tipo que llega: " +Tipo)
         while not encontrado and actual != None:
             #print("Id: " +actual.obtenerId())
             if actual.obtenerId() == IdBus:
                #print("Lo encontré")
                actual.setConexion(Tipo,IdConex)
                encontrado = True
             actual = actual.obtenerSiguiente()


     def Imprimir(self):
         actual = self.cabeza
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
             print("Hijos")
             print(actual.obtenerHijos())
             print("_______________________________")
             print("Conexiones:  ")
             print(actual.obtenerConexion())
             actual = actual.obtenerSiguiente()






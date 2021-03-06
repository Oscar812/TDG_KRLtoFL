class Nodo:
    #def __init__(self,Nombre,Tipo,Id,Parent):
    def __init__(self, *args):
        if len(args)>0:
            Nombre = args[0]
            Tipo = args[1]
            Id = args[2]
            Parent = args[3]
            self.Nombre = Nombre
            self.Tipo = Tipo
            self.Id = Id
            self.Parent = Parent
        else:
            self.Nombre = ""
            self.Tipo = ""
            self.Id = ""
            self.Parent = ""
        self.siguiente = None
        self.Relacion = []
        self.Hijos = []
        self.Conexion = []
        self.Regla = ""
        self.Tag = ""
        self.ParentName = ""

    def setNombre(self,Nombre):
        self.Nombre = Nombre
    def setTipo(self, Tipo):
        self.Tipo = Tipo
    def setId(self, Id):
        self.Id = Id
    def setParent(self, Parent):
        self.Parent = Parent
    def setParentName(self, ParentName):
        self.ParentName = ParentName
    def setRelacion(self,Source,Target):
        self.Relacion.extend([Source,Target])
    #def setConexion(self, Tipo, Conexion, MedioCon, TipoRel):
    def setConexion(self,Conexion):
        self.Conexion.extend([Conexion])
    def setHijos(self,Hijo):
        self.Hijos.append(Hijo)
    def setRegla(self, Regla):
        self.Regla = Regla
    def setTag(self, Tag):
        self.Tag= Tag
    def obtenerNombre(self):
        return self.Nombre
    def obtenerTipo(self):
        return self.Tipo
    def obtenerId(self):
        return self.Id
    def obtenerRegla(self):
        return self.Regla
    def obtenerParent(self):
        return self.Parent
    def obtenerParentName(self):
        return self.ParentName
    def obtenerSiguiente(self):
        return self.siguiente
    def obtenerHijos(self):
        return self.Hijos
    def obtenerRelacion(self):
        return self.Relacion
    def obtenerConexion(self):
        return self.Conexion
    def obtenerTag(self):
        return self.Tag
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
        self.Reglas = []

     def SetReglas(self, Regla):
         self.Reglas.append(Regla)

     def obtenerReglas(self):
         return self.Reglas

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

     def Buscar(self, Id):
        actual = Nodo("","","","")
        actual = self.cabeza
        encontrado = False
        while actual != None and not encontrado:
            if actual.obtenerId() == Id:
                encontrado = True
            else:
                actual=actual.obtenerSiguiente()
        return actual


     def AgregarConexion(self, IdBus, TipoRel, IdConex1, TipoCon, IdConex2):
         actual = self.cabeza
         encontrado = False
         while not encontrado and actual != None:
             #print("Id: " +actual.obtenerId())
             if actual.obtenerId() == IdBus:
                #print("Lo encontré")
                Conexion = []
                Conexion.extend([TipoRel,IdConex1,IdConex2, TipoCon])
                #actual.setConexion(TipoRel, IdConex1, IdConex2, TipoCon)
                actual.setConexion(Conexion)
                encontrado = True
             actual = actual.obtenerSiguiente()


     def AgregarRegla(self, IdRegla):
         actual = self.cabeza
         encontrado = False
         Lista = ListaNoOrdenada()
         while actual != None:
             if actual.obtenerConexion():
                Conexion = []
                Conexion = actual.obtenerConexion()
                #Filas = (len(Conexion) / 4).is_integer()
                #for i in range(Filas):
                for i in range(len(Conexion)):
                    cnx=[]
                    cnx =Conexion[i]
                    if cnx[1] == IdRegla:
                        #print("Encontré Conexion Regla: " + actual.obtenerId())
                        Hijos = []
                        Hijos = actual.obtenerHijos()
                        #print("hijos: ")
                        #print(Hijos)
                        if (actual.obtenerHijos()):
                            for j in range (len(Hijos)):
                                #print("Hijo: "+Hijos[j])
                                actual2 = self.cabeza
                                encontrado = False
                                while actual2 != None and not encontrado :
                                    if actual2.obtenerId() == Hijos[j]:
                                        #print("Encontre Hijo")
                                        actual2.setRegla(IdRegla)
                                        #print("Consulte Regla"+actual2.obtenerRegla())
                                        encontrado = True
                                    actual2 = actual2.obtenerSiguiente()
                    i += 3
             actual = actual.obtenerSiguiente()

     def Imprimir(self):
         actual = self.cabeza
         while actual != None:
             print("Imprimir lista de nodos")
             print("_______________________________")
             print(actual.obtenerNombre())
             print ("TIPO")
             print(actual.obtenerTipo())
             print("--------Parent info--------")
             print(actual.obtenerParent())
             print(actual.obtenerParentName())
             print("--------------------------------")
             print(actual.obtenerId())
             print("Relación")
             print(actual.obtenerRelacion())
             print("Fin Relación")
             print("Hijos")
             print(actual.obtenerHijos())
             print("_______________________________")
             print("Conexiones:  ")
             print(actual.obtenerConexion())
             print("Regla: ")
             print(actual.obtenerRegla())
             print("Tag: ")
             print(actual.obtenerTag())
             actual = actual.obtenerSiguiente()



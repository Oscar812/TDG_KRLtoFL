class Nodo:
    Relacion = []
    Hijos = []
    def __init__(self,Nombre,Tipo,Id,Parent,Relacion, Hijos):
        self.Nombre = Nombre
        self.Tipo = Tipo
        self.Id = Id
        self.Parent = Parent
        self.siguiente = None
        self.Relacion = Relacion
        self.Hijos = Hijos
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

    def setRelacion(self,valor):
        self.Relacion = []
        if (len(self.Relacion) ==0):
            self.Relacion.append(valor)
        else:
            self.Hijos.insert(0,valor)

    def setHijos(self,Hijos):
        self.Hijos = Hijos




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



    def asignarDato(self,Nombre,Tipo,Id,Parent,Relacion,Hijos):
        self.Nombre = Nombre
        self.Tipo = Tipo
        self.Id = Id
        self.Parent = Parent
        self.Relacion = Relacion
        self.Hijos = Hijos

    def asignarSiguiente(self,nuevosiguiente):
        self.siguiente = nuevosiguiente

class ListaNoOrdenada:

    def __init__(self):
        self.cabeza = None

    def SetCabeza(self):
        return self.cabeza

    def estaVacia(self):
        return self.cabeza == None

    def agregar(self, item1, item2, item3, item4, item5, item6):
        temp = Nodo(item1, item2, item3, item4, item5, item6)
        temp.asignarDato(item1, item2, item3, item4, item5, item6)
        temp.asignarSiguiente(self.cabeza)
        self.cabeza = temp

    def tamano(self):
        actual = self.cabeza
        contador = 0
        while actual != None:
            contador = contador + 1
            actual = actual.obtenerSiguiente()

        return contador

    def buscar(self,item):
        actual = self.cabeza
        encontrado = False
        while actual != None and not encontrado:
            if actual.obtenerDato() == item:
                encontrado = True
            else:
                actual = actual.obtenerSiguiente()

        return encontrado

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
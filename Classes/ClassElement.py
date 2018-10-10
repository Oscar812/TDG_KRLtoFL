'''
Element maintence

'''
import xml.etree.ElementTree as ET
from Classes import ClassList


class ElementosXML:

    Lista = ClassList.ListaNoOrdenada()
    Nodo = ClassList.Nodo('', '', '', '', '', '')

    def ObtenerElementos (self, file, Lista):
        Nodo = ClassList.Nodo('', '', '', '', '', '')
        info = []

        for (ev, el) in ET.iterparse(file):
            inner = []
            if el.tag == 'object':

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

                    for name, value in i.items():
                        if name == 'parent':
                            Nodo.setParent(value)
                            inner.append([i.tag + '-' + name, str(value).replace('\n', '').replace(' ', '')])
                        if name == 'source':
                            if len(relacion) == 0:
                                relacion.append(value)
                            else:
                                relacion.insert(0, value)
                        if name == 'target':
                            relacion.append(value)

                print(relacion)
                Nodo.setRelacion(relacion)
                # Lista.agregar(cell.get('label'), cell.get('Tipo'), cell.get('id'), cell.get('parent'))
                Lista.agregar(Nodo.obtenerNombre(), Nodo.obtenerTipo(), Nodo.obtenerId(), Nodo.obtenerParent(),
                              Nodo.obtenerRelacion(), Nodo.obtenerHijos())
                info.append(inner)
        return (Lista)


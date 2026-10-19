from nodo import Nodo

class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
            print("El valor se asignó al nodo raiz :)")
        else:
            self.insertarNodo(self.raiz, valor)

    def insertarNodo(self, nodoActual, valor):
        # Valor a la izquierda
        if nodoActual.valor > valor:
            if nodoActual.izquierdo is None:
                nodoActual.izquierdo = Nodo(valor)
                print("El valor se agregó a la izquierda")
            else:
                self.insertarNodo(nodoActual.izquierdo, valor)

        # Valor a la derecha
        elif nodoActual.valor < valor:
            if nodoActual.derecho is None:
                nodoActual.derecho = Nodo(valor)
                print("El valor se agregó a la derecha")
            else:
                self.insertarNodo(nodoActual.derecho, valor)

        # Valores iguales
        else:
            print("No puede haber 2 numeros iguales, menso >:(")


if __name__ == "__main__":
    arbol = ArbolBinario()
    for n in [16,10,21,7,15,18,26]:
        arbol.insertar(n)
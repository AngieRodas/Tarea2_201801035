
from Nodo import Nodo

class ListaCircularDoble:
    def __init__(self):
        self.primero=None
        self.ultimo=None
    def ingresar(self,valor):
        nuevo= Nodo(valor)
        if (self.primero==None):
            self.primero = nuevo
            self.ultimo = nuevo
            self.primero.anterior= self.ultimo
            self.ultimo.siguiente= self.primero
        else:
            self.ultimo.siguiente= nuevo
            nuevo.anterior = self.ultimo
            nuevo.siguiente = self.primero
            self.primero.anterior= nuevo
            self.ultimo= nuevo


    def imprimir(self):
        pivote = self.primero
        if(self.primero):
            while pivote.siguiente != self.primero:
                print(pivote.dato)
                pivote= pivote.siguiente
            print(pivote.dato)

    def Buscar(self,dato):
        pivote= self.primero
        if(self.primero):
            while pivote.siguiente != self.primero:
                if(pivote.dato == dato):
                    print("anterior  --> "+str(pivote.anterior.dato))
                    print("actual    --> "+str(pivote.dato))
                    print("siguiente --> "+str(self.siguiente.dato))
                    break
                pivote=pivote.siguiente

        if(self.ultimo.dato == dato):
            print("anterior  --> "+str(pivote.anterior.dato))
            print("actual    --> "+str(pivote.dato))
            print("siguiente --> "+str(pivote.siguiente.dato))



lista = ListaCircularDoble()

print("Lista de numeros:")
lista.ingresar(6)
lista.ingresar(20)
lista.ingresar(1)
lista.ingresar(35)
lista.ingresar(3)

lista.imprimir()
print(" Numero seleccionado: " )
lista.Buscar(3)

#lista enlazada----------------------------------
class Nodo:
    def __init__(self, dato=None, siguiente=None):
        self.dato = dato
        self.siguiente = siguiente

class ListaEnlazada:
    def __init__(self):
        self.primero = None

    def agregar_elemento(self, dato):
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.siguiente = self.primero
        self.primero = nuevo_nodo

    def imprimir_lista(self):
        actual = self.primero
        while actual:
            print(actual.dato)
            actual = actual.siguiente

lista = ListaEnlazada()
lista.agregar_elemento(1)
lista.agregar_elemento(2)
lista.agregar_elemento(3)
lista.imprimir_lista()

#Operaciones con listas--------------------------------------
#Creación de una lista vacía
mi_lista = [1, 2, 3, 4]
print(mi_lista)

#acceder a elementos de una lista-------------------------------
primer_elemento = mi_lista[0]
segundo_elemento = mi_lista[1]
tercer_elemento = mi_lista[2]
cuarto_elemento = mi_lista[3]
print(mi_lista)

#Modificación de los elementos de una lista----------------------
mi_lista[2] = 5
print(mi_lista)

#Agregar elementos a una lista-----------------------------------
numeros = [1, 2, 3, 4, 5]
numeros.append(6)
print(numeros)

#Eliminar elementos de una lista--------------------------------
numeros = [1, 2, 3, 4, 5]
del numeros[2]
print(numeros)

#Iterando sobre una lista---------------------------------------
nombres = ["Juan", "Maria", "Luisa", "Pedro"]
for nombre in nombres:
    print(nombre)

#Ordenando una lista--------------------------------------------
numeros = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
numeros.sort()
print(numeros) # salida: [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

#Obtener la longitud de una lista------------------------------
longitud_lista = len(mi_lista)
print(mi_lista)

#Copiar una lista---------------------------------------------
nueva_lista = mi_lista.copy()

#Buscar el índice de un elemento en una lista-----------------
indice_elemento = mi_lista.index(4)
print(indice_elemento)




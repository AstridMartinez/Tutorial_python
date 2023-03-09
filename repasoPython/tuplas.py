#Tuplas anidadas---------------------------------------
mi_tupla = (1, 2, (3, 4), 5, (6, 7, 8))
primer_elemento = mi_tupla[0]
segundo_elemento = mi_tupla[1]
tercer_elemento = mi_tupla[2]
cuarto_elemento = mi_tupla[2][0]
quinto_elemento = mi_tupla[2][1]
sexto_elemento = mi_tupla[4][2]
print(mi_tupla)

#Creación de una tupla-----------------------------------
mi_tupla = (1, 2, 3, 4)
print(mi_tupla)

#Acceso a los elementos de una tupla---------------------
primer_elemento = mi_tupla[0]
segundo_elemento = mi_tupla[1]
tercer_elemento = mi_tupla[2]
cuarto_elemento = mi_tupla[3]
print(mi_tupla)

#Longitud de una tupla------------------------------------
longitud_tupla = len(mi_tupla)
print(longitud_tupla)

#Concatenación de tuplas----------------------------------
tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)
tupla_concatenada = tupla1 + tupla2

print(tupla_concatenada)

#Desempaquetado de una tupla--------------------------------
tupla = (1, 2, 3)
a, b, c = tupla
print(tupla)

#Comparación de tuplas--------------------------------------
tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)
if tupla1 < tupla2:
    print("tupla 1 es menor que tupla 2")
elif tupla1 > tupla2:
    print("tupla 1 es mayor que tupla 2")
else:
    print("tupla 1 y tupla 2 son iguales")

#Conversión de una lista en una tupla--------------------
mi_lista = [1, 2, 3, 4]
mi_tupla = tuple(mi_lista)
print(mi_tupla)

#Obtención de una sub-tupla------------------------------
mi_tupla = (1, 2, 3, 4)
sub_tupla = mi_tupla[1:3]
print(sub_tupla)

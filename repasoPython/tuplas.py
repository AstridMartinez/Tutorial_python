#Tupla vasia---------------------------------------
tupla_vacia = tuple()
print(tupla_vacia)

#Tupla con elementos-------------------------------
# utilizando paréntesis
tupla_numeros = (1, 2, 3, 4, 5)
print(tupla_numeros)

# utilizando la función tuple()
tupla_frutas = tuple(("manzana", "banana", "cereza"))
print(tupla_frutas)

#tupla de un elemento------------------------------------
tupla_un_elemento = ("hola",)
print(tupla_un_elemento)  # Output: ('hola',)

#tupla de rango
tupla_rango = tuple(range(1, 5))
print(tupla_rango)

#Tupla de desempaquetado
tupla_desempaquetada = (1, "hola", True)
a, b, c = tupla_desempaquetada
print(a)
print(b)
print(c)

#Tuplas anidadas---------------------------------------
tupla_anidada = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
print(tupla_anidada)

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

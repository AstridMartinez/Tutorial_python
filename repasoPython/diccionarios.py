#Diccionario estándar---------------
person = {
    "nombre": "Juan",
    "apellido": "Pérez",
    "edad": 30,
    "ciudad": "Buenos Aires"
}
print(person)

#Dicionario ordenado-----------------
from collections import OrderedDict

my_dict = OrderedDict([('uno', 1), ('dos', 2), ('tres', 3)])
print(my_dict)

my_dict['cuatro'] = 4
print(my_dict)

print(my_dict['dos'])

for key, value in my_dict.items():
    print(key, value)

#Diccionario por defecto--------------
from collections import defaultdict

my_dict = defaultdict(int)

# Agregar algunos elementos
my_dict['uno'] = 1
my_dict['dos'] = 2
my_dict['tres'] = 3

print(my_dict['cuatro'])  # toma el valor de 0

for key, value in my_dict.items():
    print(key, value)

#Operaciones con diccionarios--------------------------

#crear diccionario-------------------------------------
valor1 = 2
valor2 = 5
valor3 = 3
nuevo_valor = 8
mi_diccionario = {"clave1": valor1, "clave2": valor2}
mi_diccionario["clave3"] = valor3
print(mi_diccionario)

#eliminar un elemeto del diccionario---------------
mi_diccionario = {"clave1": valor1, "clave2": valor2, "clave3": valor3}
del mi_diccionario["clave2"]
print(mi_diccionario)

#Actualizar un elemento------------------------------
mi_diccionario = {"clave1": valor1, "clave2": valor2, "clave3": valor3}
mi_diccionario["clave1"] = nuevo_valor
print(mi_diccionario)

#Verificar si una clave está en un diccionario--------------
mi_diccionario = {"clave1": valor1, "clave2": valor2, "clave3": valor3}
if "clave2" in mi_diccionario:
    print("La clave 2 está en el diccionario")

#Convinar diccionarios----------------------------------------
diccionario1 = {"clave1": valor1, "clave2": valor2}
diccionario2 = {"clave2": nuevo_valor, "clave3": valor3}
diccionario1.update(diccionario2)
print(diccionario1)

#Copiar un diccionario----------------------------------------
mi_diccionario = {"clave1": valor1, "clave2": valor2, "clave3": valor3}
mi_otro_diccionario = mi_diccionario.copy()
print(mi_otro_diccionario)


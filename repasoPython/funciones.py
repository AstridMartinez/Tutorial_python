#Entradas
base = float(input("Ingrese base: "))
altura = float(input("Ingrese altura: "))

#Proceso

def CalcularAreaTriangulo(b,al):
    area = (b * al)/2
    return area

# Salida
resultado = CalcularAreaTriangulo(base,altura)
print("El area del triangulo es: ", resultado)

#funcion con arguentos por defecto

def mostrarPais(pais = "Colombia"):
    print("Yo soy de: " +pais)

mostrarPais("Suiza")
mostrarPais("Ecuador")
mostrarPais()
mostrarPais("Brazil")
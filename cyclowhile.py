observador = 100
print("menu")
print("0. salir")
print("1. saludar")
print("2. despedir")
while(observador != 0):

    observador=int(input("Digite una opcion: "))

    if(observador == 0):
        break
    elif(observador == 1):
        print("Hola")
    elif(observador == 2):
        print("Adios")
    else: 
        print("Digite por favor una opcion valida")


opc=0

def menu():
    print("=====MENÚ PRINCIPAL=====")
    print("1.Agregar vehículo")
    print("2.Buscar vehículo")
    print("3.Eliminar vehículo")
    print("4.Actualizar disponibilidad")
    print("5.Mostrar vehículos")
    print("6.Salir")
    print("=============================")
    
def opciones():
    while True:
        try:
            opc=int(input("Seleccione una opción (del 1 al 6): "))
            if opc <1 or opc > 6:
                print("Debe elegir una opcion (del 1 al 6). ")
            else:
                return opc
        except ValueError:
            print("Solo se permiten numeros positivos enteros.")

while True:

    menu()
    opc=opciones()

    if opc==1:
        while True:
                modelo=input("Ingrese el modelo de su vehículo: ").strip()
                if len(modelo) ==0:
                    print("El modelo no puede estar vacío ni ser solo espacios en blanco.")
                else:
                    try:
                        año=int(input("Ingresa el año de tu vehículo: "))
                        if año <=1900:
                            print("EL año de su vehículo debe ser mayor a 1990.")
                        else:
                            try:
                                precio=int(input("Ingrese el precio del vehículo"))
                                if precio <=0:
                                    print("El precio debe ser mayor a 0.")
                                else:
                                    break
                            except ValueError:
                                print("Su precio debe ser un decimal mayor a 0")
                    except ValueError:
                        print("El año debe ser un numero entero mayor a 1990")

                    
            

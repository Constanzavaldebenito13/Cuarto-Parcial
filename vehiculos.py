#Sistema de vehículos 

def mostrar_menu():
    print()
    print("________________________MENU PRINCIPAL_________________")
    print("1.- Agregar vehículo")
    print("2.- Buscar vehículo")
    print("3.- Eliminar vehículo")
    print("4.- Actualizar vehículo")
    print("5.- Mostrar vehículo")
    print("6.- Salir")
    print("________________________________________________________")
    
#Funcion para leer 

def leer_opcion():
    try:
        opcion =int(input("Selecciona una opción: "))
        if opcion >=1 and opcion <=6:
            return opcion 
        else:
            print("Error: Debe ingresar una opcion del 1 al 6")
            return 0
    except ValueError:
        print("Ingresa un numero entero positivo")
        return 0 
    
#Funcion modelo

def validacion_modelo(modelo):
    if modelo.strip() != " ":
        return True

    else:
        return False
    
#Funcion año

def validacion_anio(anio):
    if anio > 1900:
        return True
    
    else: 
        return False
    
#Funcion precio

def validacion_precio(precio):
    if precio > 0:
        return True
    else:
        return False

#Funcion vehiculos

def agregar_vehiculo(lista_vehiculos):
    print()
    print("Agregar Vehiculo")

    modelo = input("Ingrese el modelo del vehiculo")

    if not validacion_modelo(modelo):
        print("Error: blablabla")
        return
    
    try:
        anio = int(input("Ingrese el año de su vehiculo"))
        if not validacion_anio(anio):
            print("Error: blablabla")
            return 
    except ValueError:
        print("Error: El año deben ser solo numeros enteros")
        return
    
    try:
        precio=float(input("Ingrese el precio de su vehiculo"))
        if not validacion_precio(precio):
            print("Error: El precio debe ser mayor que cero.")
    except ValueError:
        print("Error: El precio debe ser un numero decimal.")
        return         
    
    vehiculo = {
        "Modelo": modelo.strip(),
        "Año": anio,
        "Precio": precio,
        "Disponible":False
    }

    lista_vehiculos.append(vehiculo)
    print("Vehiculo agregado correctamente")

def buscar_vehiculo(lista_vehiculos, modelo_buscado):
    modelo_buscado = modelo_buscado.strip().lower()

    for i in range(len(lista_vehiculos)):
        modelo_actual = lista_vehiculos[i]["modelo"].strip().lower()

        if modelo_actual == modelo_buscado:
            return i

    return -1

def mostrar_datos_vehiculo(vehiculo):
    print("Modelo:", vehiculo["modelo"])
    print("Año:", vehiculo["anio"])
    print("Precio:", vehiculo["precio"])

    if vehiculo["disponible"] == True:
        print("Estado: DISPONIBLE")
    else:
        print("Estado: NO DISPONIBLE")



def eliminar_vehiculo(lista_vehiculos):
    print()
    print("=== ELIMINAR VEHÍCULO ===")

    modelo = input("Ingrese el modelo del vehículo que desea eliminar: ")

    posicion = buscar_vehiculo(lista_vehiculos, modelo)

    if posicion != -1:
        lista_vehiculos.pop(posicion)
        print("Vehículo eliminado correctamente.")
    else:
        print(f"El vehículo '{modelo}' no se encuentra registrado.")

def actualizar_disponibilidad(lista_vehiculos):
    for vehiculo in lista_vehiculos:
        if vehiculo["anio"] >= 2020:
            vehiculo["disponible"] = True
        else:
            vehiculo["disponible"] = False


# ------------------------------------------------------------
# FUNCIÓN: mostrar_vehiculos
# ------------------------------------------------------------
# Muestra todos los vehículos registrados en la lista.
#
# Antes de mostrar, actualiza la disponibilidad de todos.
# ------------------------------------------------------------

def mostrar_vehiculos(lista_vehiculos):
    print()
    print("=== LISTA DE VEHÍCULOS ===")

    actualizar_disponibilidad(lista_vehiculos)

    if len(lista_vehiculos) == 0:
        print("No hay vehículos registrados.")
        return

    for vehiculo in lista_vehiculos:
        mostrar_datos_vehiculo(vehiculo)
        print("*********************************************")


# ------------------------------------------------------------
# PROGRAMA PRINCIPAL
# ------------------------------------------------------------
# Aquí comienza el programa.
# Se crea la lista principal y se ejecuta el menú.
# ------------------------------------------------------------

vehiculos = []

while True:
    mostrar_menu()
    opcion = leer_opcion()

    # --------------------------------------------------------
    # OPCIÓN 1: Agregar vehículo
    # --------------------------------------------------------
    if opcion == 1:
        agregar_vehiculo(vehiculos)

    # --------------------------------------------------------
    # OPCIÓN 2: Buscar vehículo
    # --------------------------------------------------------
    elif opcion == 2:
        print()
        print("=== BUSCAR VEHÍCULO ===")

        modelo = input("Ingrese el modelo del vehículo a buscar: ")

        posicion = buscar_vehiculo(vehiculos, modelo)

        if posicion != -1:
            print("Vehículo encontrado en la posición:", posicion)

            # Antes de mostrar, actualizamos disponibilidad.
            actualizar_disponibilidad(vehiculos)

            mostrar_datos_vehiculo(vehiculos[posicion])
        else:
            print("Vehículo no encontrado.")

    # --------------------------------------------------------
    # OPCIÓN 3: Eliminar vehículo
    # --------------------------------------------------------
    elif opcion == 3:
        eliminar_vehiculo(vehiculos)

    # --------------------------------------------------------
    # OPCIÓN 4: Actualizar disponibilidad
    # --------------------------------------------------------
    elif opcion == 4:
        actualizar_disponibilidad(vehiculos)
        print("Disponibilidad actualizada correctamente.")

    # --------------------------------------------------------
    # OPCIÓN 5: Mostrar vehículos
    # --------------------------------------------------------
    elif opcion == 5:
        mostrar_vehiculos(vehiculos)

    # --------------------------------------------------------
    # OPCIÓN 6: Salir
    # --------------------------------------------------------
    elif opcion == 6:
        print("Gracias por usar el sistema. Vuelva Pronto")
        break

    # --------------------------------------------------------
    # OPCIÓN INVÁLIDA
    # --------------------------------------------------------
    else:
        print("Intente nuevamente.")
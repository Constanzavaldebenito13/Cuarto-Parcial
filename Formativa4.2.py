

#Funcion del menu

def mostrar_menu():
    print()
    print("============MENÚ PRINCIPAL==========")
    print("1.Agregar paciente")
    print("2.Buscar paciente")
    print("3.Eliminar paciente")
    print("4.Actualizar estado")
    print("5.Mostrar pacientes")
    print("6.Salir")

#Funcion de opcion

def leer_opcion():
    try:
        opc=int(input("Seleccione una opcion: "))
        if opc >=1 and opc <=6:
            return opc
        else:
            print("Error: Seleccione una opcion del 1 al 6")
            return 0
    except ValueError:
        print("Error: el numero debe ser un entero positivo")
        return 0
    
#Funcion alidación nombre

def validacion_nombre(nombre):
    if nombre.strip() !="":
        return True
    else:
        return False
    
#Funcion validación edad

def validacion_edad(edad):
    try:
        if edad >=1:
            return True
        else:
            return False
    except ValueError:
        print("Error: Su edad debe ser un numero entero mayor a 0.")
        return
    
#Funcion validación temperatura

def validacion_temperatura(temperatura):
    try:
        if temperatura >=35.0 and temperatura <=40.2:
            return True
        else:
            return False
    except ValueError:
        print("Error: Su numero debe ser un numero decimal entre 35.0 y 42.0")
        return 
    

#Funcion Agregar paciente

def agregar_paciente(Lista_pacientes):
    print()
    print("=========Agregar paciente=======")

    nombre=input("Ingresa tu nombre: ")

    if not validacion_nombre(nombre):
        print("Error:El nombre no puede estar vacio.")
        return 
    
    try:
        edad=int(input("Ingrese su edad: "))
        if not validacion_edad(edad):
            print("Error: La edad debe ser un numero entero mayor a 0.")
            return
    except ValueError:
        print("Error: La edad debe ser un numero entero mayor a 0.")
        return 
    
    try:
        temperatura=float(input("Ingrese su temperatura: "))
        if not validacion_temperatura(temperatura):
            print("Error: Su temperatura debe ser un numero decimal entre 35.0 y 42.0.")
            return
    except ValueError:
        print("Error: Su temperatura debe ser un numero decimal entre 35.0 y 42.0.")
        return 
    
    paciente = {
        "Nombre": nombre.strip(),
        "Edad": edad,
        "Temperatura": temperatura,
        "Atendido": False
    }
    
    Lista_pacientes.append(paciente)

    print("Paciente Agregado correctamente.")

#Funcion buscar paciente

def buscar_paciente(lista_pacientes, nombre_buscar):
    posicion = 0  
    
    for p in lista_pacientes:
        
        if p["Nombre"] == nombre_buscar.strip():
            return posicion  
        
        posicion = posicion + 1  
            
    return -1

#Funcion eliminar paciente

def eliminar_paciente(lista_pacientes):
    print()
    print("======Eliminar paciente=======")

    nombre = input("Ingrese el paciente que quiera eliminar: ")

    posicion = buscar_paciente(lista_pacientes, nombre)

    if posicion != -1:
        lista_pacientes.pop(posicion)
        print("Paciente eliminado correctamente.")
    else:
        print(f"El paciente '{nombre}' no se encuentra registrado.")

#Funcion actualizar estado

def actualizar_estado(lista_pacientes):
    for paciente in lista_pacientes:
        if paciente ["Temperatura"] <=37.0:
            paciente["Atendido"] = True
        else:
            paciente["Atendido"] = False    

#Funcion mostrar paciente
def impimir_datos_paciente(paciente):
    print("Nombre:", paciente["Nombre"])
    print("Edad:", paciente["Edad"])
    print("Temperatura:", paciente["Temperatura"])

    if paciente["Atendido"] == True:
        print("Estado: ATENDIDO")
    else:
        print("Estado: REQUIERE ATENCIÓN")

def mostrar_paciente(lista_pacientes):
    print()
    print("=======LISTA DE PACIENTES=======")

    actualizar_estado(lista_pacientes)
    
    if len(lista_pacientes) == 0:
        print("No hay pacientes registrados.")
        return
        
    for p in lista_pacientes:
        impimir_datos_paciente(p) 
        print("**************************************")

paciente=[]
#Funcion programa principal 
while True:
    mostrar_menu()
    opc = leer_opcion()

  
    if opc == 1:
        agregar_paciente(paciente)


    elif opc == 2:
        print()
        print("=== BUSCAR PACIENTE ===")

        nombre = input("Ingrese el nombre del paciente a buscar: ")

        posicion = buscar_paciente(paciente,nombre)

        if posicion != -1:
            print("Paciente encontrado en la lista:", posicion)

            actualizar_estado(paciente)

            impimir_datos_paciente(paciente[posicion])
        else:
            print(f"El paciente {nombre} no se encuentra registrado.")

 
    elif opc == 3:
        eliminar_paciente(paciente)

   
    elif opc == 4:
        actualizar_estado(paciente)
        print("Disponibilidad actualizada correctamente.")


    elif opc == 5:
        mostrar_paciente(paciente)

    elif opc == 6:
        print("Gracias por usar el sistema. Vuelva Pronto")
        break

    else:
        print("Intente nuevamente.")